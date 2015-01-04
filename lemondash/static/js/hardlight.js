function HardLightBridge() {
    // State-tracking
    this.rate_limit_timeouts = {}; // List of timeout IDs for any rate-limited actions.
    this.rate_limit = 250;  // Rate-limit on pushing state changes to server.

    // Define event handlers
    var self = this;
    this.event_handlers = {
        onLightToggle: function (e) {
            var $this = $(this),
                light_id = $this.data('lightid'),
                checked = $this.is(':checked');

            // Set the light's on state to on/off depending on the checkbox value.
            self.setLightState(light_id, {on: checked})
        }
    };

    // Link up event handlers
    $('input.light_toggle').change(this.event_handlers.onLightToggle);
};


// Push a new light state up to the server
HardLightBridge.prototype.rateLimitedExecute = function (rate_limit_key, f) {
    if (this.rate_limit_timeouts[HardLightBridge.prototype] !== undefined) {
        console.log("Rate limiting: Clearing timeout " + rate_limit_key);
        clearTimeout(this.rate_limit_timeouts[HardLightBridge.prototype]);
    }

    this.rate_limit_timeouts[HardLightBridge.prototype] = setTimeout(function(){
        console.log("Rate limiting: Executing " + rate_limit_key);
        f()
    }, this.rate_limit)
};

HardLightBridge.prototype.setLightState = function (light_id, data) {
    var self = this,
        light_update_url = LIGHT_UPDATE_URL.replace(LIGHT_UPDATE_PLACEHOLDER_ID, light_id),
        rate_limit_key = 'setLightState_' + light_id;

    this.rateLimitedExecute(rate_limit_key, function () {
        $.post(
            light_update_url, // Defined in the global state by the application
            data,
            null,
            'json'
        ).always(function (response) {
                // Reset our UI to match the response from the server, informing us of the current state of the lights.
                self.setUILightState(response.light_id, response);
            });
    });
};

// Update the UI with the light's current state
HardLightBridge.prototype.setUILightState = function (light_id, state) {
    var $on = $('#light_on_' + light_id),
        $colour = $('#light_colour_' + light_id),
        $name = $('#light_name_' + light_id),
        $brightness = $('#light_brightness_' + light_id);
    $on.prop('checked', state.on);
    $name.text(state.name);
    $brightness.text(state.brightness + "%");

    $colour
        .attr('style', 'color: #' + state.inverted_colour + "; background-color: #" + state.colour)
        .text(state.colour);
};

$(document).ready(function () {
    var hardLightBridge = new HardLightBridge();
});
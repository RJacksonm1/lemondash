$(document).ready(function(){
    // Flick lights on/off
    $('input.light_toggle').change(function(e){
        var $this = $(this),
            light_id = $this.data('lightid'),
            light_update_url = LIGHT_UPDATE_URL.replace(LIGHT_UPDATE_PLACEHOLDER_ID, light_id),
            checked = $this.is(':checked');

        // Tell light to change state to on/off depending on whether our checkbox is checked
        $.post(light_update_url, {
            'on': checked
        }, null, 'json').always(function(response){
            // Reset our UI to match the response from the server, informing us of the current state of the lights.
            $this.prop('checked', response.on);
        });
    });
});
from colour import Color

HUE_MAX_HUE = 65535.0
HUE_MAX_SAT = 254.0
HUE_MAX_BRI = 254.0


def hue_light_to_rgb(light):
    color = Color()
    color.set_hue(light.hue / HUE_MAX_HUE)
    color.set_saturation(light.saturation / HUE_MAX_SAT)
    color.set_luminance(0.5)

    return color.get_hex_l()

import click, json, random, time
from click.core import Context
from kubeleds import console
from kubeleds.constants import COLOR_OFF, COLOR_BAD, COLORS
import board
import adafruit_ws2801

@click.command("set_leds", short_help="Set led colors")
@click.pass_context
@click.argument("data_key", required=True)
@click.argument("status_condition", required=True)
@click.argument("start_led", required=True)
def set_leds(ctx, data_key, status_condition, start_led):
    """ This command will let you set the color of each led

    Examples:

    /b

    """
    odata = board.MOSI
    oclock = board.SCK
    numleds = 50
    bright = 0.25

    leds = adafruit_ws2801.WS2801(
        oclock, odata, numleds, brightness=bright, auto_write=False
    )

    data = {}
    
    if data_key in ctx.obj:
        data = ctx.obj[data_key]

    n_leds = len(leds)
    console.print("Setting " + status_condition + " for " + str(n_leds))

    bad_leds = []
    led_store = [COLOR_OFF] * n_leds

    idx = int(start_led)

    #reset based off of current color?
    if "led_store" in ctx.obj:
        last_leds = ctx.obj["led_store"]
        last_leds_idx = 0
        for last_led_color in last_leds:
            console.print("Current led " + str(last_leds_idx) + " already at " + str(last_led_color))
            leds[last_leds_idx] = last_led_color
            led_store[last_leds_idx] = last_led_color
            last_leds_idx+= 1

    for item in data:
        if idx >= 0 and idx < n_leds:
            color_to_use = COLOR_OFF
            status_conds = item.get_status_conditions()
            if status_condition in status_conds:
                if status_conds[status_condition]:
                    color_to_use = COLORS[status_condition]
                else:
                    color_to_use = COLOR_BAD
                    bad_leds.append(idx)
            else:
                color_to_use = COLOR_OFF

            leds[idx] = color_to_use
            led_store[idx] = color_to_use
            console.print("Set led " + str(idx) + " to " + str(color_to_use))

        idx+= 1

    # while idx < n_leds:
    #     leds[idx] = COLOR_OFF
    #     idx += 1

    leds.show()

    ctx.obj["led_store"] = led_store
    # time.sleep(1)
    # counter+= 1

    #blink bad nodes 5 times
    if len(bad_leds) > 0:
        for bad_led in bad_leds:
            fiveTimes = range(4)
            for blink in fiveTimes:
                if blink % 2 == 0:
                    leds[bad_led] = COLOR_BAD
                else:
                    leds[bad_led] = COLOR_OFF
                leds.show()    
                time.sleep(0.5)

    console.print("set_leds completed")

def random_color():
    return random.randrange(0, 7) * 32
import click, json, random, time
from click.core import Context
from kubeleds import console
from kubeleds import utils
from kubernetes import client
from kubeleds.constants import COLOR_OFF, COLOR_BAD, COLORS

@click.command("set_leds", short_help="Set led colors")
@click.pass_context
@click.argument("data_key", required=True)
@click.argument("status_condition", required=True)
def set_leds(ctx, data_key, status_condition):
    """ This command will let you set the color of each led

    Examples:

    /b

    """
    data = {}
    
    if data_key in ctx.obj:
        data = ctx.obj[data_key]

    n_leds = len(utils.Leds)
    console.print("Setting " + status_condition + " for " + str(n_leds))

    bad_leds = []
    idx = 0

    for item in data:
        if idx >= 0 and idx < n_leds:
            if item.get_status_conditions()[status_condition]:
                color_to_use = COLORS[status_condition]
                utils.Leds[idx] = color_to_use
            else:
                utils.Leds[idx] = COLOR_BAD
                bad_leds.append(idx)
            console.print("Set led " + str(idx) + " to " + str(color_to_use))
        idx+= 1

    while idx < n_leds:
        utils.Leds[idx] = COLOR_OFF
        idx += 1

    utils.Leds.show()

    #blink bad nodes 5 times
    if len(bad_leds) > 0:
        for bad_led in bad_leds:
            fiveTimes = range(4)
            for blink in fiveTimes:
                if blink % 2 == 0:
                    utils.Leds[bad_led] = COLOR_BAD
                else:
                    utils.Leds[bad_led] = COLOR_OFF
                utils.Leds.show()    
                time.sleep(0.5)

    time.sleep(10)

    console.print("set_leds completed")

def random_color():
    return random.randrange(0, 7) * 32
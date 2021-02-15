import click, json, random
from click.core import Context
from kubeleds import console
from kubeleds import utils
from kubernetes import client
from kubeleds.constants import COLOR_OFF, COLOR_BAD, COLOR_GOOD

import board
import adafruit_ws2801

@click.command("set_leds", short_help="Set led colors")
@click.pass_context
@click.argument("contextKey", required=True)
def set_leds(ctx, contextKey):
    """ This command will let you set the color of each led

    Examples:

    /b

    """
    
    console.print("Context Key: " + contextKey)

    data = ctx[contextKey]
    n_leds = len(utils.Leds)
    idx = 0


    for item in enumerate(data):
        #for idx in range(n_leds):
        if idx >= 0 and idx < n_leds:
            if item.get_status_conditions["Ready"]:
                utils.Leds[idx] = COLOR_GOOD
            else:
                utils.Leds[idx] = COLOR_BAD

        idx+= 1

    while idx < n_leds:
        utils.Leds[idx] = COLOR_OFF
        idx += 1


    utils.Leds.show()

    console.print("set_leds completed")

def random_color():
    return random.randrange(0, 7) * 32
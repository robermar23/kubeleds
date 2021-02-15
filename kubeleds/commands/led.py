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
@click.argument("data_key", required=True)
def set_leds(ctx, data_key):
    """ This command will let you set the color of each led

    Examples:

    /b

    """
    
    #console.print("data_key: " + data_key)

    data = ctx.obj[data_key]
    n_leds = len(utils.Leds)
    idx = 0

    for item in data:
        console.print(item)
        if idx >= 0 and idx < n_leds:
            if item.get_status_conditions()["Ready"]:
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
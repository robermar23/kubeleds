"""
Entrypoint for CLI.
"""
import click, atexit

from kubeleds.commands import get_cluster_nodes, get_namespaced_pods, set_leds, init, show, clear_leds

@click.group(chain=True)
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)

def exit_handler():
    click.echo("exit_handler")
    #clear_leds()

cli.add_command(init)
cli.add_command(show)
cli.add_command(get_cluster_nodes)
cli.add_command(get_namespaced_pods)
cli.add_command(set_leds)

atexit.register(exit_handler)

if __name__ == '__main__':
    cli()

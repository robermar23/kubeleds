"""
Entrypoint for CLI.
"""
import click

from kubeleds.commands import get_cluster_nodes, set_leds,  init, show


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


cli.add_command(init)
cli.add_command(show)
cli.add_command(get_cluster_nodes)
cli.add_command(set_leds)

import kubeleds
from click.testing import CliRunner
import unittest
from unittest.mock import patch
from kubeleds import app

def test_cluster(self, ):
    runner = CliRunner()
    #result = runner.invoke(app, ['"get_cluster_nodes", "https://api.c4.us-east-1.dev.aws.ocp.14west.io:6443", "sha256~8e1vZCl7O9lI08ARSyBOmvdNPmVxUqm_ilKwJLDaDWg", "set_leds", "get_cluster_nodes"'])
    result = runner.invoke(app, ["get_cluster_nodes", "https://api.c4.us-east-1.dev.aws.ocp.14west.io:6443", "sha256~8e1vZCl7O9lI08ARSyBOmvdNPmVxUqm_ilKwJLDaDWg"])
    assert result.exit_code == 0
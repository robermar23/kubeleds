## kubeleds
Monitor your kubernetes clusters using NeoPixel LEDS!

## Hardware
### Raspberry PI (any model that supports GPIO)
Currently using a Raspberry PI 4b 2GB.  Preparing a Raspberry PI Zero W

NeoPixel LED Strips, 12mm Diffussed bulbs

![alt text](https://www.dropbox.com/s/nmrmp8nqpghqjc6/2021-02-16%2009.07.11.jpg?dl=0)

![alt text](https://www.dropbox.com/s/v11zt83d14ltddv/2021-02-16%2009.08.32.jpg?dl=0)

![alt text](https://www.dropbox.com/s/vmujbwple1ufjt4/2021-02-16%2009.07.40.jpg?dl=0)


## Usage

1. `cd` into project directory.

2. Create a virtual environment.

```bash
$ make venv
```

3. Activate it.

```bash
$ source venv/bin/activate
```

4. Install development dependencies with editable mode to test the CLI.

```bash
$ make install
```

## Take kubeleds for a spin

This will basic command line functionality

```bash
$ kubeledscli init
```

### This will retrieve node status and set the leds base off of status of each node, testing each status condition (ready, cpu, memory, disk)
```bash
$ kubeledscli get_cluster_nodes '[api fqdn]' \
    '[your token]' 'True' 'get_cluster_nodes' \
    'set_leds' 'get_cluster_nodes' 'Ready' \
    'set_leds' 'get_cluster_nodes' 'MemoryPressure' \
    'set_leds' 'get_cluster_nodes' 'DiskPressure' \
    'set_leds' 'get_cluster_nodes' 'PIDPressure' \
    'set_leds' 'get_cluster_nodes' 'Ready' \
```
The above commands will retrieve cluster node status and set an led frame per status condition, 1 led per node.

GREEN: Node Ready
BLUE: CPU Good
CYAN: Memory good
Purple: Disk Good



### Test with Docker

CLI commands can be tested with Docker.

1. Build an image for the CLI.

    Image is tagged with the same name as the `cli_command`.

```bash
$ make docker-image
```

2. Run the command inside the container.

```bash
$ docker-run --rm kubeledscli init
```

## Documentation

1. Install documentation-related dependencies.

```bash
$ make docs
```

2. Serve the docs locally.

```bash
$ make serve-docs
```

## Distribution

> **NOTE**
>
> Make sure you have account in [PyPI](https://pypi.org/account/register/) before you try this out.

To publish you CLI to PyPI, run:

```bash
$ make distributions
```

`dist` directory will be created inside your project directory. Upload it to PyPI using:

```bash
$ twine dist/*
```

## Help

For help related to make commands.

```bash
$ make help
```

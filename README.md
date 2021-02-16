## kubeleds
Monitor your kubernetes clusters using NeoPixel LEDS!

## Hardware
### Raspberry PI (any model that supports GPIO)
Currently using a Raspberry PI 4b 2GB.  Preparing a Raspberry PI Zero W

NeoPixel LED Strips, 12mm Diffussed bulbs

![alt text](https://previews.dropbox.com/p/thumb/ABEwWReBdyjrxF2X2JoEYMSBMG-gJaBrt6Bks05-n7kAk8k1eDf1KfPaatUn3hd9k0QGfl5mnajx4jsxgdASvNG9FckFYh3a9GF3Okprb9zaCHECOdA0qucx2eXYLYOVZz_Ed3zBuTbU54TspzkNF2WPSFOgqJWyWHRAcCchdw0zEbFS54YHItUWRC4X445-fmS7S6TGnXhdAoutqo649s5o0g5kmmozZMxDBpmwn_ipEXgEIiweepiGm_yXdL4RZ7BRGcPzNfjuzkBwb6mup0BiIey2DnXAPv2v8tIEo6sty0x4MRJn4S3isLNU6KEJkF6gon0RlTmNGGM_TpheWzhza54zy6-JZZcYmzOMSfiOJh6lngsqcL9OTW7MRucOqruEeTFi8nu8DDEXwpk9o_wHB16aMyfbNvwWBaJXivOxMg/p.jpeg?fv_content=true&size_mode=5)

![alt text](https://previews.dropbox.com/p/thumb/ABG8OuWcu-lTl6EFQN2ZvRz22ydm2t7ZJ_OppxSj4Dx0EGtc-UQ3mevj_Fu6aXPv3KCFA9cRNWmBRJUX6mdKC4ZM3CmtE5nKNc_jeQwSI67iIyZSeGU3Xh8CeVWWMe8Y9pl20lEfqB6O8s-pXU77uyf3Yaz3pywhkkQip7kVRYyuNKsz97TBXtcJWkuJdx8191rTDhfl88qql36pIOqq152eEnUmrhT2eT3FBH_yATjPsH9cG2pOhBr0kXZzRGqNjYC76eZONRhZqBCxomGRkSDH00YDpGjAGDEw6gLVQh2QX3-IPIr78VjUp-d0B2ZLL5Z-HYmJs_T1d7Fd6llkbdHZh97eX8UZfHYYsuQveM6gc8b2AgSc20ECDkYcU1z1Ih9-Tqsgwdj26evDPGnTAGtT3aPfCI7uDuGkRrtMw_XLTQ/p.jpeg?fv_content=true&size_mode=5)

![alt text](https://previews.dropbox.com/p/thumb/ABGlyELu19Hj8VVSj7Ac-qgXl-Gb7qbGHh_g2tya-_n058RlCyf3zNSkRakFVpu2qpfLOEqpH4nis9oQSmC_DJv3ND7FmLKsz1pH_pULUC9wdJl75K9H0jslZgbAoYTNZEP81Af1AuOffshBntacr72tSjVA6g_mA94Yv9UT9c4qemBbVUTRVruNPMmV5K8JzbAjcH-r7CcX-5ATPU6bj9o0iJZyQgjdUXhhdD1NSqk6N5eYqVWk2xKncIlyXWrM_RWync0qs4XJBNTPg8gPTFblq-OmJxPEXPEkfkJQ-y5jSHSCs8OF6qau6D3iUi8WsEQDIEolAB4Pzxxun2EK-YgaOS_H_ooMNAqpCMAYJvzooTRmLJ2HaQe4yAxy2wUPo7R4CrPD1cg2xxhh1dwxK37njtu46Qej_idnkfjy3Y68mw/p.jpeg?fv_content=true&size_mode=5)


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

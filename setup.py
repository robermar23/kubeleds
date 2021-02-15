"""Package setup"""
import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

requirements = ["click", "rich<=7.1.0", "simple-term-menu", "requests", "RPI.GPIO", "adafruit-blinka", "adafruit-ws2801", "kubernetes"]


setuptools.setup(
    name="kubeleds",
    version="0.0.1",
    author="Robert Evans",
    description="monitor kubernetes clusters using adafruit neopixels",
    packages=setuptools.find_packages(
        exclude=["dist", "build", "*.egg-info", "tests"]
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "kubeledscli = kubeleds.app:cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
)

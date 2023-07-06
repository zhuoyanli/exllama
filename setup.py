import os

from setuptools import setup, find_packages


_PATH_ROOT = os.path.dirname(__file__)

with open(os.path.join(_PATH_ROOT, "README.md"), encoding="utf-8") as fo:
    readme = fo.read()

setup(
    name='exllama',
    version='0.1.0',
    description='A more memory-efficient rewrite of the HF transformers implementation of Llama for use with quantized weights. ',
    author='turboderp',
    url='https://github.com/turboderp/exllama',
    install_requires=[
        "torch>=2.0.1",
        "safetensors==0.3.1",
        "sentencepiece>=0.1.97",
        "ninja==1.11.1"
    ],
    packages=find_packages("."),
    package_dir={"": "."},
    long_description=readme,
    long_description_content_type="text/markdown",
)
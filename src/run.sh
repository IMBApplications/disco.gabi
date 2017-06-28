#!/bin/bash

source ../discogabi/bin/activate
pip install -r ../requirements.txt

python -m disco.cli  --run-bot --config config.yaml

#!/bin/bash

cd /opt/HandwritingWaterMarker

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python3 -m pip install --upgrade pathlib
python3 -m pip install pywhatkit==4.6
python3 -m pip install --upgrade opencv-python

# make folders
mkdir -p ~/HandwritingWaterMarker
mkdir /opt/HandwritingWaterMarker/images

# run the script
python3 /opt/HandwritingWaterMarker/src/HandwritingWaterMarker.py

sleep 5m

deactivate

rm -r venv

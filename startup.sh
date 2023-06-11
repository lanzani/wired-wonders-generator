#!/bin/bash

# Install and configure X window with virtual screen
sudo apt-get install xserver-xorg libglu1-mesa-dev freeglut3-dev mesa-common-dev libxmu-dev libxi-dev
# Configure the nvidia-x
sudo nvidia-xconfig -a --use-display-device=None --virtual=1280x1024
# Run the virtual screen in the background (:0)
sudo /usr/bin/X :0 &
# We only need to setup the virtual screen once

# Run the program with vitural screen
DISPLAY=:0 <program>

# If you dont want to type `DISPLAY=:0` everytime
export DISPLAY=:0

pip install --upgrade pip
pip install -r requirements.txt

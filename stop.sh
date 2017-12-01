#!/bin/bash

# Stop mopidy.
pkill mopidy*

# Stop all daemons.
pkill python*

# Stop mycroft-core.
echo "Stopping mycroft-core..."
cd mycroft-core
bash mycroft.sh stop
#!/bin/bash

# Stop mopidy.
pkill mopidy*

# Stop all daemons.
pkill python*

# Stop mycroft-core.
echo "Stopping mycroft-core..."
bash mycroft-core/mycroft.sh stop
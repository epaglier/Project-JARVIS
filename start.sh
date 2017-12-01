#!/bin/bash

# Start mopidy music service.
mopidy &
echo "Started mopidy."

# Start the daemon processes in the background.
python jarvis-features/daemons/gpsd.py &
python jarvis-features/daemons/wifid.py &
echo "Started daemons."

# Start mycroft-core.
# Switch into the "core" directory so that the startup script is in the correct working directory.
echo "Starting mycroft-core..."
bash mycroft-core/mycroft.sh start
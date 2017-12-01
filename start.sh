#!/bin/bash

# Start mopidy music service.
start_mopidy() {
  mopidy
  echo "Started mopidy."
}

start_mopidy &

# Start the daemon processes in the background.
start_daemons() {
  python jarvis-features/daemons/gpsd.py
  python jarvis-features/daemons/wifid.py
  echo "Started daemons."
}

start_daemons &

# Start mycroft-core.
# Switch into the "core" directory so that the startup script is in the correct working directory.
echo "Starting mycroft-core..."
bash mycroft-core/mycroft.sh start

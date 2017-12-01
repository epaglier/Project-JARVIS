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
start_mycroft() {
  cd mycroft-core
  bash mycroft.sh start -d
  echo "Starting mycroft-core..."
}

start_mycroft

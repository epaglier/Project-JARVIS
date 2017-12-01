#!/bin/bash

# For consistency, we run everything as root.
if [ "$EUID" -ne 0 ]
  then echo "Please run as root."
  exit
fi

# Start mopidy music service.
start_mopidy() {
  mopidy
  echo "Started mopidy."
}

start_mopidy &

# Start the daemon processes in the background.
start_daemons() {
  cd jarvis-features/daemons
  python gpsd.py
  python wifid.py
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

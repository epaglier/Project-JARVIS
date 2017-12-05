#!/bin/bash

# We need root access to kill some processes.
if [ "$EUID" -ne 0 ]
  then echo "Please run as root."
  exit
fi

# Stop mopidy.
kill_mopidy() {
  echo "Killing mopidy..."
  pkill mopidy*
}

kill_mopidy &

# Stop all daemons.
kill_daemons() {
  echo "Killing daemons..."
  pkill daemon*
}

kill_daemons &

# Stop mycroft-core.
kill_mycroft() {
  echo "Stopping mycroft-core..."
  bash mycroft-core/mycroft.sh stop
}

kill_mycroft

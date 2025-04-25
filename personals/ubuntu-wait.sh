#!/bin/bash
# keep the container running, but allow it to be interruptable
trap : TERM INT
sleep infinity &
wait

#!/bin/bash

log() {
    MESSAGE="$@"
    echo "$(date +'%Y-%m-%d %H:%M:%S') $MACHINE_NAME $USER_NAME system INFO $MESSAGE" >&2
}

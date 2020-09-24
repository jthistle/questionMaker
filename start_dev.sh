#!/usr/bin/env bash

if ! command -v inotifywait > /dev/null; then
    echo "You need to install inotifywait: sudo apt install inotify-tools"
    exit 1
fi

inotifywait -e modify -m main.py index_src.html |
  while read file event; do
    python3 main.py
  done
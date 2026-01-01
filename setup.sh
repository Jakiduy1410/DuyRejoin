#!/data/data/com.termux/files/usr/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

su -c "
export PATH=/data/data/com.termux/files/usr/bin:\$PATH
export TERM=xterm-256color
export HOME=/data/data/com.termux/files/home
cd \"$DIR\"
python manager.py
"

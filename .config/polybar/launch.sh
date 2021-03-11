#!/usr/bin/env bash


# Terminate already running bar instances
# killall polybar

# Wait until the processes have been shut down
# while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar
# # polybar main -c $(dirname $0)/config.ini &
# killall -q polybar

# # Wait until the processes have been shut down
# while pgrep -u $UID -x polybar > /dev/null; do sleep 1; done

# desktop=$(echo $DESKTOP_SESSION)
# count=$(xrandr --query | grep " connected" | cut -d" " -f1 | wc -l)


# if type "xrandr" > /dev/null; then
#   for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#     MONITOR=$m polybar --reload main -c ~/.config/polybar/config.ini&
#   done
# else
# polybar --reload main -c ~/.config/polybar/config.ini &
# fi


killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

for m in $(polybar --list-monitors | cut -d":" -f1); do
	WIRELESS=$(ls /sys/class/net/ | grep ^wl | awk 'NR==1{print $1}') MONITOR=$m polybar --reload main -c ~/.config/polybar/config.ini &
done

echo "Bars launched..."


#!/bin/bash

case "$1" in
  ondemand)
		echo "ondemand governor"
		sudo cpupower frequency-set -g ondemand
        ;;
  performance)
		echo "performance governor"
		sudo cpupower frequency-set -g performance
        ;;
  powersave)
		echo "powersave governor"
		sudo cpupower frequency-set -g powersave
        ;;
  monitor)
        watch -n 1 grep \"cpu MHz\" /proc/cpuinfo
        ;;
  *)
        echo $"Usage: $0 {ondemand|performance|powersave|monitor}"
        exit 1
esac
exit 0

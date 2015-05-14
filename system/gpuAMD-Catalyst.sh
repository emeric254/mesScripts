#!/bin/bash

core=850
vram=1025
		
case "$1" in
  init)
        echo "aticonfig init"
		sudo aticonfig --initial
		;;
  enable)
        echo "Overdrive enable"
		sudo aticonfig --od-enable
        echo "set core @$core & vram @$vram"
		sudo aticonfig --odsc "$core,$vram"
		sudo aticonfig --odcc
        ;;
  disable)
        echo "Overdrive disable"
		sudo aticonfig --od-disable
        ;;
  monitor)
        watch -n 1 `sudo aticonfig --odgc && sudo aticonfig --odgt`
        ;;
  *)
        echo $"Usage: $0 {init|enable|disable|monitor}"
        exit 1
esac
exit 0

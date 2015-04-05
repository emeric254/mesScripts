#!/bin/bash

core=850
vram=1025

sudo aticonfig --odsc "$core,$vram"
sudo aticonfig --odcc

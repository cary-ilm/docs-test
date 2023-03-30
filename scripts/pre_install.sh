#!/usr/bin/bash

echo "pwd:"
pwd

echo "env:"
env

echo pre_install:

echo $READTHEDOCS_OUTPUT
find ${READTHEDOCS_OUTPUT}.. -name index.rst

echo "set JPG"
JPG=${READTHEDOCS_OUTPUT}GammaChart.jpg

wget https://raw.githubusercontent.com/AcademySoftwareFoundation/openexr-images/v1.0/TestImages/GammaChart.exr
convert GammaChart.exr $JPG

ls -l $JPG


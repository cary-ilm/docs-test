#!/usr/bin/bash

JPG=$READTHEDOCS_OUTPUT/GammaChart.jpg
pwd
wget https://raw.githubusercontent.com/AcademySoftwareFoundation/openexr-images/v1.0/TestImages/GammaChart.exr
convert GammaChart.exr $JPG

file $JPG
find $READTHEDOCS_OUTPUT -name index.rst


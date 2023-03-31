#!/usr/bin/env python

import sys, os
from subprocess import PIPE, run

test_images_rst = sys.argv[1]
print(f'test_images.py {sys.argv}')
print(f'cwd: {os.getcwd()}')

directory = os.path.dirname(test_images_rst)
print(f'os.makedirs({directory})')
os.makedirs(directory)
            
print(f'generating rst for test images ...')
with open(test_images_rst, 'w') as outfile:
    outfile.write('Test Images\n')
    outfile.write('###########\n')
    outfile.write('\n')
    outfile.write('.. toctree::\n')
    outfile.write('   :caption: Test Images\n')
    outfile.write('   :maxdepth: 2\n')
    outfile.write('\n')
    outfile.write('   toctree\n')

with open('_test_images/toctree.rst', 'w') as outfile:
    outfile.write('.. toctree::\n')
    outfile.write('   :maxdepth: 0\n')
#    outfile.write('   :hidden:\n')
    outfile.write('\n')
    outfile.write('   TestImages/AllHalfValues\n')

os.makedirs('_test_images/TestImages')

with open('_test_images/TestImages/AllHalfValues.rst', 'w') as outfile:
    outfile.write('All Half Values\n')
    outfile.write('###############\n')
    outfile.write('\n')
    
print(f'generating rst for test images ... done.')

#!/usr/bin/env python

import sys, os
from subprocess import PIPE, run

READTHEDOCS_OUTPUT = os.environ['READTHEDOCS_OUTPUT'] if 'READTHEDOCS_OUTPUT' in os.environ else '_readthedocs'

if len(sys.argv) > 2:
    images_file_path = sys.argv[1]
else:
    images_file_path = '/home/cary/src/cary-ilm/docs-test/docs/test_images.txt'

with open(images_file_path, 'r') as images_file:
    for line in images_file.readlines():
        exr_url = line.rstrip('\n')
        words = exr_url.split('/')
        repo = '/'.join(words[0:4])
        tag = words[5]
        exr_lpath = '/'.join(words[6:])
        exr_filename = words[-1]
        jpg_lpath = exr_lpath.strip('.exr') + '.jpg'
        jpg_path = READTHEDOCS_OUTPUT + '/' + jpg_lpath
        
        print(f'repo: {repo}')
        print(f'tag: {tag}')
        print(f'exr_lpath: {exr_lpath}')
        print(f'exr_filename: {exr_filename}')
        print(f'jpg_lpath: {jpg_lpath}')
        print(f'jpg_path: {jpg_path}')
        
        command = ['wget', exr_url]
        print(command)
        result = run (['wget' , exr_url], 
                      stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if result.returncode != 0:
            print(result.stderr)
#            continue
        
        if not os.path.isfile(jpg_lpath):
            result = run (['convert' , exr_filename, jpg_lpath],
                          stdout=PIPE, stderr=PIPE, universal_newlines=True)
            if result.returncode != 0:
                print(result.stderr)

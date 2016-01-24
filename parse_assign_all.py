#!/bin/env python3

import os
import sys

assign_dir = 'assign_files'
cmd_fmt = 'python3 parse_assign_etree.py assign_files/{} 1'

gen_files = []

has_parsed = False
for f in os.listdir(assign_dir):
  if f.endswith('.xml'):
    gen_files.append(f)

  if f == 'parsed.txt':
    has_parsed = True

gen_files.sort()

# get already parsed files
if has_parsed:
  parsed_fnames = filter(len,map(str.strip,list(open(assign_dir+'/'+'parsed.txt'))))
else:
  parsed_fnames = []
parsed_fid = open(assign_dir+'/'+'parsed.txt','a+')

for f in gen_files:
  print(f)
  if f in parsed_fnames:
    print('Already parsed')
  else:
    cmd = cmd_fmt.format(f)
    ret = os.system(cmd)
    if ret == 0:
      parsed_fid.write(f+'\n')
    elif ret == 2:
      print('ABORTED')
      sys.exit(0)
    else:
      print('PARSE FAILED')

#!/usr/bin/python

import argparse
import string
import re
import sys
import os
from rich import print
from rich.progress import track
from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    # DownloadColumn(),
    #"•",
    # TransferSpeedColumn(),
    # "•",
    TimeRemainingColumn(),
)


def parse_include(includefile,outfh):
    #try:
    #    with open(includefile) as file:
            # print("Found " + includefile + ".  Merging...\n")
    # except IOError as e:
    #    print('Unable to open ' + includefile + ': does not exist or no read permissions')

    fincl = open(includefile, 'r').readlines()
    for line in fincl:
        sec = re.match('\\\\input{(.*?)}', line)
        if sec:
            # if the match is nonempty, then
            fname = re.sub('\\\\input{', '', sec.group(0))
            fname = re.sub('}', '', fname)
            if (fname.find('.tex') == -1):
                fname = fname + '.tex'
                
            print(f'[bold green] Processing file {fname} [/bold green]')
            parse_include(fname,outfh)
            
        # if no \input{},  print the line to the output file
        else:
            outfh.write(line)
    # fincl.close()

def remove_comments(includefile, outfh):
    #try:
    #    with open(includefile) as file:
    #        print("Found " + includefile + ".  Merging...\n")
    #except IOError as e:
    #    print('Unable to open ' + includefile + ': does not exist or no read permissions')

    fincl = open(includefile, 'r').readlines()
    for step in track(fincl):
    # for line in fincl:
        content = re.sub(r"\s%.*|(?<!\\)%.*", '', step, 0)
        if content != "\n" and len(content.strip())>0:
            outfh.write(content)

    # fincl.close()

if __name__ == "__main__":
    inparser = argparse.ArgumentParser(description='Parses argument list')
    inparser.add_argument('texfile', metavar='texfile', help='main .tex file')
    inparser.add_argument('output', metavar='output', help='desired target output file')
    args = inparser.parse_args()


    # INPUT PARSING AND WARNING GENERATION
    try:
        with open(args.texfile) as file:
            pass
    except IOError as e:
        print('Unable to open ' + args.texfile + ': does not exist or no read permissions')

    fin = open(args.texfile, 'r')
    out_file_temp = open(f'{args.output}.bak','w')
    fout = open(args.output, 'w')

    parse_include(args.texfile,out_file_temp)
    
    remove_comments(f'{args.output}.bak', fout)    
    os.remove(f'{args.output}.bak')

    

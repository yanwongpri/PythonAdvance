# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

import os
from argparse import ArgumentParser

# default arguments
PATH = os.getcwdu()
OUTPUT = os.getcwdu() + '/output.mp4'


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--path', dest='path', default=PATH, help='process sources path')
    parser.add_argument('--output', dest='output', default=OUTPUT,  help='output file name')
    return parser


def build_cmd(filename_list, path, output):
    cmd = 'ffmpeg -i \"concat:'
    for filename in filename_list:
        cmd += path + '/' + filename + '|'
    cmd += '\" -acodec copy -vcodec copy -absf aac_adtstoasc %s' % output
    return cmd


def is_int(str):
    str_is_in = True
    try:
        int(str)
    except ValueError:
        str_is_in = False
    return str_is_in


def filter_filename_by_int(filename_list):
    new_filenames_no = []
    new_filenames = []
    for filename in filename_list:
        if filename[-3:] == '.ts':
            if is_int(filename[:-3]):
                new_filenames_no.append(int(filename[:-3]))
    new_filenames_no.sort()
    for sorted_filename in new_filenames_no:
        new_filenames.append('%i.ts' % sorted_filename)
    return new_filenames


if __name__ == '__main__':
    parser = build_parser()
    options = parser.parse_args()

    if not os.path.isabs(options.path):
        options.path = os.path.abspath(options.path)
    if not os.path.isdir(options.path):
        parser.error('path: %s does not exist.' % options.path)

    filenames_raw = os.listdir(options.path)
    filenames = filter_filename_by_int(filenames_raw)

    cmd = build_cmd(filenames, options.path, options.output)

    os.system(cmd)

    print '%s process succeed!' % options.output
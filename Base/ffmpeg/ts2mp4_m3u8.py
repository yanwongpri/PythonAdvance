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


if __name__ == '__main__':
    parser = build_parser()
    options = parser.parse_args()

    if not os.path.isabs(options.path):
        options.path = os.path.abspath(options.path)
    if not os.path.isdir(options.path):
        parser.error('path: %s does not exist.' % options.path)

    filenames = []

    for fn in os.listdir(options.path):
        if not fn.endswith('m3u8'):
            filenames.append(fn)

    cmd = build_cmd(filenames, options.path, options.output)

    os.system(cmd)

    print '%s process succeed!' % options.output
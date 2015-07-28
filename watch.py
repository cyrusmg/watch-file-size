#!/usr/bin/env python
"""Script watching changes in filesize and reporting delta"""

import os, time, math
import logging

SAMPLE_TIMEOUT = 5 # seconds

def convert_size(size):
    if (size <= 0):
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size,1024)))
    p = math.pow(1024,i)
    s = round(size/p,2)
    if (s > 0):
        return '{} {}'.format(s,size_name[i])
    else:
        return '0 B'

def get_speed(file_name):
    size = os.path.getsize(file_name)
    time.sleep(SAMPLE_TIMEOUT)
    speed = (os.path.getsize(file_name) - size) / SAMPLE_TIMEOUT
    return speed

def watch(file_name):
    assert(os.path.isfile(file_name))

    logger = logging.getLogger(__name__)
    
    logger.info("Watching file: {}".format(file_name))
    file_size = os.path.getsize(file_name)
    logger.info("Initial file size is: {}".format(convert_size(file_size)))

    speed = get_speed(file_name) 
    while speed > 0:
        logger.info("Download speed: {}/s".format(convert_size(speed)))
        speed = get_speed(file_name)
    logger.info("It seems download is finished")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Watch a file and report download speed every {} seconds".format(SAMPLE_TIMEOUT))
    parser.add_argument('file_name', type=str, help="watched file")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    if not os.path.isfile(args.file_name):
        logger.error("File not found: {}".format(args.file_name))
        exit(1)
    watch(args.file_name)

#!/usr/bin/env python


import argparse
from gendiff.generate import generate_diff


def parse_arguments():
    text = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    pathes = parse_arguments()
    file_1 = pathes.first_file
    file_2 = pathes.second_file
    return generate_diff(file_1, file_2)


if __name__ == '__main__':
    main()

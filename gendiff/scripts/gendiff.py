#!/usr/bin/env python


import argparse
from gendiff import generate_diff


def parse_arguments():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    pathes = parse_arguments()
    file_path1 = pathes.first_file
    file_path2 = pathes.second_file
    return generate_diff(file_path1, file_path2)


if __name__ == '__main__':
    main()

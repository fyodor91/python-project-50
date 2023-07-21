#!/usr/bin/env python


from gendiff.generate import generate_diff
from gendiff.parse_arguments import parse_arguments


def main():
    pathes = parse_arguments()
    file_1 = pathes.first_file
    file_2 = pathes.second_file
    return generate_diff(file_1, file_2)


if __name__ == '__main__':
    main()

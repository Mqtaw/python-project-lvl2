#!/usr/bin/env python
from gendiff.gendiff import createParser
from gendiff.gendiff import generate_diff


def main():
    parser = createParser()
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    format = args.format
    print(generate_diff(path_to_file1, path_to_file2, format))


if __name__ == '__main__':
    main()

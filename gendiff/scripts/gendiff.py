#!/usr/bin/env python
from gendiff.gendiff import createParser
from gendiff.gendiff import generate_diff


def main():
    parser = createParser()
    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    print(generate_diff(path_to_file1, path_to_file2))


if __name__ == '__main__':
    main()

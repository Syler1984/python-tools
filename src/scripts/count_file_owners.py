"""
This script
Usage:
python count_file_owners.py
"""

import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-recursion', help='Disable folder recursion', action='store_true')
    parser.add_argument('--max-recursion', help='Maximum depth of folder recursion: negative value means infinite, '
                                                '0 disables recursion (same as --no-recursion), positive number '
                                                'indicates actual maximum depth of folder recursion; default: 5',
                        default=5, type=int)
    parser.add_argument('--file-regex', help='Set regular expression for files; default: ".*"',
                        default='.*', type=str)
    parser.add_argument(metavar='file', dest='path', nargs='+', help='Path(s) to a directory for file owners count',
                        type=str)

    args = parser.parse_args()

    print('Arguments:')
    print('\t', f'path: {args.path}')
    print('\t', f'no_recursion: {args.no_recursion}')
    print('\t', f'max_recursion: {args.max_recursion}')
    print('\t', f'file_regex: {args.file_regex}')

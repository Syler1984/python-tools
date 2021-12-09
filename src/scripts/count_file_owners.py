"""
This script
Usage:
python count_file_owners.py
"""

import argparse
import sys


def full_path(path):
    """
    Converts path from local to full. If path is already full, returns path without any changes.
    """
    pass


def sort_paths(paths, duplicates=True):
    """
    Returns list with sorted paths by the depth, from deepest to the shallowest.
    If duplicates set to False, will remove any duplicates.
    Note: This function creates a copy of paths and does not change it.
    """
    pass


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

    paths = [full_path(x) for x in args.path]
    paths = sort_paths(paths, duplicates=False)

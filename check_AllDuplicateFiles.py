"""This module find the dupliate files with content in the given directory or folder.
"""

import os
import sys


def check_filesindir(dirname):
    """Finds the names of all files in dirname.

    dirname: string name of directory
    """
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
    return names


def generate_checksum(filename):
    """Generates the MD5 checksum of the contents of a file.

    filename: string
    """
    cmd = 'md5sum ' + filename
    return content_read(cmd)


def check_diff(file_name1, file_name2):
    """Computes the difference between the contents of two files.

    file_name1, file_name2: string filenames
    """
    cmd = 'diff %s %s' % (file_name1, file_name2)
    return content_read(cmd)


def content_read(cmd):
    """Runs a command in a subprocess.

    cmd: string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    """
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname):
    """Computes checksums for all files with the given suffix.

    dirname: string name of directory to search

    Returns: map from checksum to list of files with that checksum
    """
    names = check_filesindir(dirname)

    d = {}
    for name in names:
        res, stat = generate_checksum(name)
        checksum, _ = res.split()
        if checksum in d:
            d[checksum].append(name)
        else:
            d[checksum] = [name]
    return d


def check_pairs(names):
    """Checks whether any in a list of files differs from the others.

    names: list of string filenames
    """
    for file_name1 in names:
        for file_name2 in names:
            if file_name1 < file_name2:
                res, stat = check_diff(file_name1, file_name2)
                if res:
                    return False
    return True


def print_duplicates(check_dupfiles):
    """Checks for duplicate files.

    check_dupfiles: map from checksum to list of files with that checksum
    """
    for key, names in check_dupfiles.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And the above files are identical.')


if __name__ == '__main__':
    check_dupfiles = compute_checksums(dirname=sys.argv[1])
    print_duplicates(check_dupfiles)


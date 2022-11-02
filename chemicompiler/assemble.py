#!/usr/bin/python3.11
import assembler as asm
import test
from sys import argv

if __name__ == '__main__':
    test.test()
    try:
        print(asm.assemble_file(argv[1], argv[2]))
    except(IndexError):
        print(asm.assemble_file(argv[1]))

#!/usr/bin/python3.11
import assembler as asm

def test() -> bool:
    try:
        print("[...] Disassembly")
        program = "><+-[]{}()'^,$@#.~"
        answer = "INCREF\nDECREF\nADD\nSUB\nLOOP\nEND\nSXSTOR\nSXLOAD\nTXLOAD\nTXSTOR\nAXSTOR\nAXLOAD\nAMOUNT\nHEAT\nMOVE\nISOLAT\nPRINT\nCOMPIL"
        assert asm.disassemble(program) == answer

        print("[...] Assembly")
        program = "><+-[]{}()'^,$@#.~"
        answer = "><+-[]{}()'^,$@#.~"
        assert asm.assemble(asm.disassemble(program)) == answer

        print("[+] Tests passed")
        return True
    except:
        print("[!!!] Tests failed")
        return False
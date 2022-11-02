instruction_to_opcode = {
    ">": 'INCREF',
    "<": 'DECREF',
    "+": 'ADD',
    "-": 'SUB',
    "[": 'LOOP',
    "]": 'END',
    "{": 'SXSTOR',
    "}": 'SXLOAD',
    ")": 'TXSTOR',
    "(": 'TXLOAD',
    "'": 'AXSTOR',
    "^": 'AXLOAD',
    ",": 'AMOUNT',
    "$": 'HEAT',
    "#": 'ISOLAT',
    "@": 'MOVE',
    ".": 'PRINT',
    "~": 'COMPIL'
}
opcode_to_instruction = {v: k for k, v in instruction_to_opcode.items()}

def disassemble(program: str) -> str:
    ret = ""
    for opcode in program:
        ret += instruction_to_opcode[opcode] + "\n"
    return ret[:-1]



def assemble(program: str) -> str:
    ret = ""
    for word in program.split("\n"):
        if '#' not in word:
            if ',' not in word:
                # Translation
                opcode = word
                assert opcode in opcode_to_instruction.keys()
                ret += opcode_to_instruction[opcode]
            else:
                # Extensions
                opcode = word.split(',')
                match opcode[0]:
                    case 'LDCNST':
                        # Load Constant
                        # Loads a 
                        # arguments


    return ret

def assemble_file(filename: str, output_filename: str=None) -> str:
    ret = ""
    with open(filename, 'r') as f:
        ret = assemble(f.read())
    if output_filename != None:
        with open(output_filename, 'w') as f:
            f.write(ret)
    return ret
    



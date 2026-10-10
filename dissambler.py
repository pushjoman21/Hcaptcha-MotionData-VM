import ast
import time

from utils.utils import Utils

OPCODES = {
    49: "MAKE_ARRAY",
    8 : "MEMOIZE",
    20: "PUSH_CONST",
    0 : "MAKE_CLOSURE",
    41: "SET_PROP",
    33: "PUSH_BOOL",
    38: "JUMP_IF_FALSE",
    14: "GET_PROP",
    21: "CALL_DYNAMIC",
    16: "STORE_REGISTER_AND_CACHE",
    30: "POP",
    9 : "SET_AND_SPREAD",
    17: "RESTORE_CONTEXT",
    34: "MUL",
    26: "LOAD_DECRYPTED_STRING",
    10: "GET_PROP_BIND",
    50: "SET_PROP_PUSH",
    11: "NEW_INSTANCE",
    36: "MAKE_OBJECT",
    29: "PUSH_THIS",
    48: "GET_GLOBAL",
    47: "TYPEOF",
    25: "NEQ_STRICT",
    39: "SHIFT_LEFT",
    46: "REPLACE_UNDEFINED",
    40: "NEGATE",
    51: "TRY_CATCH",
    54: "GREATER_THAN",
    44: "PUSH_NULL",
    2 : "GLOBAL_STORE",
    52: "STRICT_EQUAL",
    23: "SET_INDEX",
    43: "DUP",
    19: "LOGICAL_NOT",
    27: "PUSH_GLOBAL_GT",
    24: "LT",
    13: "INCREMENT_PROP",
    35: "SUB",
    4 : "PUSH_CT",
    1 : "SET_HANDLER",
    7 : "ADD",
    32: "GTE",
    37: "PUSH_UNDEFINED",
    22: "EQ",
    3 : "PUSH_ST",
    12: "HAS_PROP",
    18: "ADD_PROP",
    42: "ADD_SET_GLOBAL_PROP",
    45: "PUSH_CT",
    6 : "SET_PROP_OR"
}

with open("input/bytecode.txt", "r") as file:
    bytecode = ast.literal_eval(file.read())

with open("input/stringtable.txt", "r") as file:
    stringtable = file.read()

def disassemble(bytecode):
    start_time = time.time()
    pc = 0
    output = []
    while pc < len(bytecode):
        opcode = bytecode[pc]
        if opcode in OPCODES: 
            if OPCODES[opcode] == "MAKE_ARRAY":
                arg_count = bytecode[pc + 1]
                if pc + 2 + arg_count > len(bytecode):
                    output.append(f"MAKE_ARRAY MISSING_ARGS")
                    break
                args = []
                for i in range(arg_count):
                    args.append(bytecode[pc + 2 + i])
                output.append(f"{OPCODES[opcode]} {args}")
                pc += 2 + arg_count
            elif OPCODES[opcode] == "PUSH_CONST":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "MEMOIZE":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "SET_PROP":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                output.append(f"{OPCODES[opcode]} {arg1} {arg2}")
                pc += 3
            elif OPCODES[opcode] == "PUSH_BOOL":
                arg = bytecode[pc + 1]
                bool_value = Utils().js_bool(arg)
                output.append(f"{OPCODES[opcode]} {bool_value}")
                pc += 2
            elif OPCODES[opcode] == "JUMP_IF_FALSE":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "GET_PROP":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                output.append(f"{OPCODES[opcode]} {arg1} {arg2}")
                pc += 3
            elif OPCODES[opcode] == "STORE_REGISTER_AND_CACHE":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "SET_AND_SPREAD":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                args = []
                for i in range(arg1):
                    args.append(bytecode[pc + 3 + i])
                output.append(f"{OPCODES[opcode]} {arg1} {arg2} {args}")
                pc += 3 + arg1
            elif OPCODES[opcode] == "LOAD_DECRYPTED_STRING":
                start_index = bytecode[pc + 1]
                length = bytecode[pc + 2]
                shift = bytecode[pc + 3]
                decoded_string = Utils().string_decode(stringtable, start_index, length, shift)
                output.append(f"{OPCODES[opcode]} '{decoded_string}'")
                pc += 4
            elif OPCODES[opcode] == "MAKE_OBJECT":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "TRY_CATCH":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "SET_INDEX":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                output.append(f"{OPCODES[opcode]} {arg1} {arg2}")
                pc += 3
            elif OPCODES[opcode] == "INCREMENT_PROP":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                arg3 = bytecode[pc + 3]
                output.append(f"{OPCODES[opcode]} {arg1} {arg2} {arg3}")
                pc += 4
            elif OPCODES[opcode] == "SET_HANDLER":
                arg = bytecode[pc + 1]
                output.append(f"{OPCODES[opcode]} {arg}")
                pc += 2
            elif OPCODES[opcode] == "ADD_SET_GLOBAL_PROP":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                output.append(f"{OPCODES[opcode]} {arg1} {arg2}")
                pc += 3
            elif OPCODES[opcode] == "SET_PROP_OR":
                arg1 = bytecode[pc + 1]
                arg2 = bytecode[pc + 2]
                output.append(f"{OPCODES[opcode]} {arg1} {arg2}")
                pc += 3
            else:
                output.append(f"{OPCODES[opcode]}")
                pc += 1
        else:
            output.append(f"UNKNOWN OPCODE: {opcode}")
            pc += 1

    end_time = time.time()

    print(f"Disassembly completed in {end_time - start_time:.2f} seconds.")
    print(f"Saved to output/disassembled.txt")

    with open("output/disassembled.txt", "w") as file:
        for line in output:
            file.write(line + "\n")



disassemble(bytecode)

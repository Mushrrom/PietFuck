import sys
import imgfunctions


def execute(img, palette = 0):
    if palette == 0: palette = ['#22b14c', '#ed1c24', '#000000', '#a349a4', '#00a2e8', '#3f48cc', '#fff200', '#ff7f27']
    instructions = imgfunctions.readimage(img, palette)
    if instructions == 1: quit()
    loopmap = makeloops(instructions)

    memory = [0, 0, 0, 0]
    ptr = 0
    instructionptr = 0
    while instructionptr < len(instructions):

        if instructions[instructionptr] == 0:
            if memory[ptr] == 255: memory[ptr] = 0
            else: memory[ptr] += 1

        elif instructions[instructionptr] == 1:
            if memory[ptr] == 0: memory[ptr] = 255
            else: memory[ptr] -= 1

        elif instructions[instructionptr] == 2: sys.stdout.write(chr(memory[ptr]))
        elif instructions[instructionptr] == 3: memory[ptr] = ord(input()[0])
        elif instructions[instructionptr] == 4 and memory[ptr] == 0: instructionptr = loopmap[instructionptr]
        elif instructions[instructionptr] == 5 and memory[ptr] != 0: instructionptr = loopmap[instructionptr]

        elif instructions[instructionptr] == 6:
            ptr += 1
            if ptr >= len(memory) -3: memory.append(0)

        elif instructions[instructionptr] == 7 and ptr >= 0: ptr -= 1

        instructionptr += 1

    print("\n\n\u001b[32;1mfinished executing program!\u001b[0m")


def makeloops(program):
    tempopenloops = []
    loopmap = {}
    for count, i in enumerate(program):
        if i == 4: tempopenloops.append(count)
        elif i == 5:
            a = tempopenloops.pop()
            loopmap[count] = a
            loopmap[a] = count
    return loopmap


def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])

    elif len(sys.argv) == 3:
        palette = imgfunctions.importpalette(sys.argv[2])
        if palette == 1: quit()

    else:
        print(f"usage: {sys.argv[0]} [file] optional:[palette]")


if __name__ == "__main__":
    main()
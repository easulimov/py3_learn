import sys
script = sys.argv


def main(language_file, counter=1):
    line = language_file.readline()
    counter += 1


    if line:
        try:
            print_decoded_line(line)
        except:
            return print("Oleyioo!")
        return main(language_file)


def print_decoded_line(line):
    next_line = line.strip()
    print(f"Считанная строка {next_line}")
    print(f"Перекодированная в UTF-8: {next_line.decode('utf-8')}")
    print(f"Срез считанной строки: {next_line[:-1]}")
    print(f"Срез перекодированной строки: {next_line[:-3].decode('utf-8')}")



codes = open("codes.txt", mode="br")

main(codes)

codes.close()

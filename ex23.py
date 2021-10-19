import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)
    def codes_write(raw_bytes):
        codes.write((raw_bytes)+"\n".encode(encoding, errors=errors))
    codes_write(raw_bytes)
### codes.write(cooked_string)


languages = open("languages.txt", encoding="utf-8")
codes = open("codes.txt", mode="bw")

main(languages, encoding, error)

codes.close()
languages.close()
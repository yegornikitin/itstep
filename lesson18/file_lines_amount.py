# Программа также выцепит, если пустая строка в файле состоит не просто из переноса строки (\n)
# Но и если строка состоит из множества пробелов + переноса строки, типа "        \n"

def lines_count(file_name: str):
    with open(file_name, "r") as f:
        count = 0
        for line in f:
            list_symbols = [" ", "\n"]
            for a in line:
                if a not in list_symbols:
                    count += 1
                    break

        print("Count of not-empty lines: ", count)


lines_count("lines.txt")







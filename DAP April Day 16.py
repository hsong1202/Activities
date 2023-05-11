import csv

file = open("C://Users/hsong/Code/SavvyCoders/Activities/Python_LoopPractice.csv", "r")

# print(type(file))

csvreader = csv.reader(file)

# print(type(csvreader))

# print(csvreader)

header = next(csvreader)

# print(type(header))

header.pop()

rows = []

row_num =0

for row in csvreader:
    # row.pop()
    rows.append(row)
        # row_num = row_num + 1
    # print(f"Row {row_num}: {row}")


# print(rows)

pokedex = []

for row in rows:

    row.pop()

    pokedex_entry = dict()

    for index, col in enumerate(header):

        key = col

        value = row[index]

        pokedex_entry[key] = value

        pokedex.append(pokedex_entry)

print(pokedex)

# file.write("C://Users/hsong/Code/SavvyCoders/Activities/Python_LoopPractice.csv", "w")

file.close()


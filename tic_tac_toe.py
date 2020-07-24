
def initial(elements):
    print("---------")
    print(f"| {elements[0]} {elements[1]} {elements[2]} |")
    print(f"| {elements[3]} {elements[4]} {elements[5]} |")
    print(f"| {elements[6]} {elements[7]} {elements[8]} |")
    print("---------")
    return elements


def secondary(elements):
    z = input("Enter the coordinates: ")
    if not z[0].isnumeric():
        print("You should enter numbers!")
        return False, 0
    else:
        x, y = z.split()
        x, y = int(x), int(y)
        if x not in range(1, 4) or y not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            return False, 0
        elif x in range(1, 4) and y in range(1, 4):
            value = (x - 1)  + (9 - (3 * y))
            if elements[value] == " ":
                return True, value
            else:
                print("This cell is occupied! Choose another one!")
                return False, 0


def win(elements):
    countw_x = 0
    countw_o = 0
    for i in range(0, 3):  # columns
        if elements[i] == elements[i + 3] == elements[i + 6] == 'X':
            countw_x += 1
        elif elements[i] == elements[i + 3] == elements[i + 6] == 'O':
            countw_o += 1
    for i in range(0, 8, 3):  # rows
        if elements[i] == elements[i + 1] == elements[i + 2] == 'X':
            countw_x += 1
        elif elements[i] == elements[i + 1] == elements[i + 2] == 'O':
            countw_o += 1
    for i in [6, 8]:  # diagonal
        if i == 6:
            if elements[i] == elements[i - 2] == elements[i - 4] == 'X':
                countw_x += 1
            elif elements[i] == elements[i - 2] == elements[i - 4] == 'O':
                countw_o += 1
        elif i == 8:
            if elements[i] == elements[i - 4] == elements[i - 8] == 'X':
                countw_x += 1
            elif elements[i] == elements[i - 4] == elements[i - 8] == 'O':
                countw_o += 1
    if countw_x > countw_o:
        x = "X wins"
        return True, x
    elif countw_o > countw_x:
        o = "O wins"
        return True, o
    else:
        return False,


spaces = "         "
counter = 1
values = str(initial(spaces))
while True:
    ret, i = secondary(values)
    if counter == 10:
        print("Draw")
        break
    elif counter % 2 != 0 and ret:
        values = values[:i] + 'X' + values[i + 1:]
        initial(values)
        counter += 1
        if win(values)[0]:
            print(win(values)[1])
            break
    elif counter % 2 == 0 and ret:
        values = values[:i] + 'O' + values[i + 1:]
        initial(values)
        counter += 1
        if win(values)[0]:
            print(win(values)[1])
            break

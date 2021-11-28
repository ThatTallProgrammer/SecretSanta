import csv
from random import shuffle

solution = None
current_selection = []


def valid_pick(x):
    return x not in current_selection and \
           (x > len(current_selection) or current_selection[x] != len(current_selection))


def gen_solution(pm):
    global solution
    global current_selection

    if solution is not None:
        return
    if len(pm) == 0:
        solution = current_selection
        return

    for x in pm[0]:
        if valid_pick(x):
            current_selection.append(x)
            gen_solution(pm[1:])
            if solution is None:
                current_selection.pop()


if __name__ == '__main__':
    filename = "name-matrix.csv"
    file = open(filename)
    csv_reader = csv.reader(file)

    names = next(csv_reader)[1:]

    pick_matrix = []
    for row in csv_reader:
        row = row[1:]
        r = []
        for i in range(len(row)):
            if row[i] != '0':
                r.append(i)
        pick_matrix.append(r)

    for i in range(len(pick_matrix)):
        shuffle(pick_matrix[i])

    gen_solution(pick_matrix)

    if solution is not None:
        for i in range(len(solution)):
            print("{} buys for {}".format(names[i], names[solution[i]]))

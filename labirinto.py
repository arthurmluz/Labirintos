# OBSERVAÇÃO: Necessário instalar a biblioteca matplotlib
# (no linux, 'pip install matplotlib')
import matplotlib.pyplot as pyplot
from random import randint

num = 24

scale = 8

pyplot.figure(figsize=(num/scale, num/scale))

pyplot.style.use('dark_background')


Norte = 2
Sul = 3
Leste = 4
Oeste = 5

line_size = num
cells = [[col, lin, False, False, False, False, lin + col + lin * (line_size-1)]
         for lin in range(num) for col in range(num)]

groups = num * num
group_index = 6


def line(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='white')


# Usage: (x1, y1, x2, y2)
def clearLine(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='black')


def drawMazeBorder():
    line(0, 0, num, 0)
    line(0, 0, 0, num)
    line(num, 0, num, num)
    line(0, num, num, num)


def drawClosedCell(x, y):
    line(x, y + 1, x + 1, y + 1)
    line(x, y, x + 1, y)
    line(x + 1, y, x + 1, y + 1)
    line(x, y, x, y + 1)


def derrubaparede(cell, viz, dir):
    cell[dir] = True

    x1 = x2 = cell[0]
    y1 = y2 = cell[1]
    if dir == Norte:
        x2 += 1
        y1 = y2 = y2 + 1
        viz[Sul] = True
    elif dir == Sul:
        x2 += 1
        viz[Norte] = True
    elif dir == Leste:
        y2 += 1
        x1 = x2 = x2 + 1
        viz[Oeste] = True
    else:
        y2 += 1
        viz[Leste] = True

    clearLine(x1, y1, x2, y2)


def change_groups(old, new):
    for cell in cells:
        if cell[group_index] == old:
            cell[group_index] = new


# desenha o labirinto com todas as células fechadas
drawMazeBorder()
for i in range(0, num):
    for j in range(0, num):
        drawClosedCell(i, j)


while groups > 1:
    colviz = colcel = randint(0, num-1)
    linviz = lincel = randint(0, num-1)
    dir = randint(Norte, Oeste)
    if cells[colcel + lincel * line_size][dir]:
        continue
    if dir == Norte:
        linviz += 1
    elif dir == Sul:
        linviz -= 1
    elif dir == Leste:
        colviz += 1
    elif dir == Oeste:
        colviz -= 1
    if colviz < 0 or linviz < 0 or colviz >= num or linviz >= num:
        continue

    cell = cells[colcel + lincel * line_size]
    viz = cells[colviz + linviz * line_size]
    if cell[group_index] == viz[group_index]:
        continue
    else:
        change_groups(cell[group_index], viz[group_index])
        derrubaparede(cell, viz, dir)
        groups -= 1


print("Obs: coordenadas começam com (0,0) no canto inferior esquerdo!")
print("[x, y, Norte, Sul, Leste, Oeste, grupo]")
for lin in range(0, num):
    for col in range(0, num):
        print(cells[lin * line_size + col])
print("Obs: coordenadas começam com (0,0) no canto inferior esquerdo!")

pyplot.show()

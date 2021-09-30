# OBSERVAÇÃO: Necessário instalar a biblioteca matplotlib
# (no linux, 'pip install matplotlib')
import matplotlib.pyplot as pyplot
import sys
from random import randint

#NUM = ex: Matriz[6][6]
lin = 6
col = 4
scale = 6
if len(sys.argv) > 1:
    lin = int(sys.argv[1])
if len(sys.argv) > 2:
    col = int(sys.argv[2])
if len(sys.argv) > 3:
    scale = int(sys.argv[3])

pyplot.figure(figsize=(lin/scale, col/scale))

pyplot.style.use('dark_background')

Norte = 2
Sul = 3
Leste = 4
Oeste = 5

line_size = col
column_size = lin
cells = [[col1, lin1, False, False, False, False, lin1 + col1 + lin1 * (line_size-1)]
         for lin1 in range(lin) for col1 in range(col)]

groups = lin * col
group_index = 6

def line(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='white')


# Usage: (x1, y1, x2, y2)
def clearLine(x1, y1, x2, y2):
    pyplot.plot([x1, x2], [y1, y2], color='black')


def drawMazeBorder():
    line(0, 0, col, 0)
    line(0, 0, 0, lin)
    line(col, 0, col, lin)
    line(0, lin, col, lin)


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
for i in range(0, col):
    for j in range(0, lin):
        drawClosedCell(i, j)

def selectCells(lin,col):
    global line_size, column_size
    indx = col+lin*line_size

    dir = randint(Norte, Oeste)
    if not cells[indx][dir]: return lin, col, dir
    
    if col == line_size-1 and lin == column_size-1:
      return selectCells(0, 0)
       
    if col == line_size-1 and lin < column_size-1:
      return selectCells(lin+1, 0)

    return selectCells(lin, col+1)
  

while groups > 1:
    colcel = randint(0, col-1)
    lincel = randint(0, lin-1)
#    dir = randint(Norte, Oeste)
#    if cells[colcel + lincel * line_size][dir]:
#        continue
    lincel, colcel, dir = selectCells( lincel, colcel )

    linviz = lincel
    colviz = colcel

    if dir == Norte: linviz += 1
    if dir == Sul:   linviz -= 1
    if dir == Leste: colviz += 1
    if dir == Oeste: colviz -= 1


    if colviz < 0 or linviz < 0 or colviz >= col or linviz >= lin:
               continue
    cell = cells[colcel + lincel * line_size]
    viz = cells[colviz + linviz * line_size]
    if cell[group_index] == viz[group_index]:
        continue
    else:
        change_groups(cell[group_index], viz[group_index])
        derrubaparede(cell, viz, dir)
        groups -= 1


#print("Obs: coordenadas começam com (0,0) no canto inferior esquerdo!")
#print("[x, y, Norte, Sul, Leste, Oeste, grupo]")
#for lin1 in range(0, lin):
#    for col1 in range(0, col):
#        print(cells[lin1 * line_size + col1])
#print("Obs: coordenadas começam com (0,0) no canto inferior esquerdo!")

pyplot.show()

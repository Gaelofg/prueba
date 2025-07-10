#pruna
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 0]]
def validar3x3(tablero,numero,pos):
 fila,columna=pos
 #vereficar fila 
 for y in range(9):
  if tablero[fila][y] == numero and y != columna:
   return False
   #vereficar columnas
 for x in range(9):
  if tablero[x][columna] == numero and x != fila:
   return False
 #vereficar el 3x3
  index_fila=(fila//3)*3
 index_columna=(columna//3)*3
 for i in range(index_fila,index_fila+3):
  for j in range(index_columna,index_columna+3):
   if tablero[i][j] == numero and (i,j)!= pos:
    return False
 return True
print(validar3x3(tablero, 4, (4,9)))
import random


def pnt(mtx):
   for row in mtx:
       print(" | ".join(row))
   print()




def done(mtx) :
   for row in mtx :
       for ch in row :
           if ch == '_' :
               return False
   return True


def win(mtx, c) :


   flag = 1
   for i in range(3) :
       flag = 1
       for ch in mtx[i] :
           if ch != c :
               flag = 0
               break
       if(flag) :
           return True


   flag = 1
   for i in range(3):
       flag = 1
       for j in range(3):
           if mtx[j][i] != c:
               flag = 0
               break
       if (flag):
           return True


   flag = 1
   for i in range(3):
       if mtx[i][i] != c :
           flag = 0
           break
   if(flag) :
       return True


   flag = 1
   for i in range(3):
       if mtx[i][2 - i] != c:
           flag = 0
           break
   if (flag):
       return True


   return False


def opMove(mtx):
   while True:
       row = random.randint(0, 2)
       col = random.randint(0, 2)
       if mtx[row][col] == "_":
           return [row, col]


mtx = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
pnt(mtx)
while 1 == 1 :
   r = int(input("enter row : "))
   c = int(input("enter col : "))
   mtx[r][c] = 'X'
   pnt(mtx)
   if win(mtx, 'X') :
       print("X WINS!!")
       break
   if(done(mtx)) :
       print("TIE!!")
       break
   print("opps move : ")
   [op_row, op_col] = opMove(mtx)
   mtx[op_row][op_col] = 'O'
   pnt(mtx)
   if win(mtx, 'O') :
       print("O WINS!!")
       break
   if(done(mtx)) :
       print("TIE!!")
       break

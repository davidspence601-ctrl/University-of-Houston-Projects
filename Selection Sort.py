

from graphics import *
from random import randint


def buildArray(numbers):
   for k in range(52):
      numbers.append(randint(10,640))
   
   
def drawBar(index):
   setColor("red")
   x = index
   y = numbers[index];
   x1 = x * 25 + 3
   x2 = x1 + 18
   y1 = 700 - y
   y2 = 700
   fillRectangle(x1,y1,x2,y2)
   
   
def drawBars(numbers):
   for k in range(52):
      drawBar(k)


def swapBars(numbers,p,q):
   temp = numbers[p]
   numbers[p] = numbers[q]
   numbers[q] = temp
   
      
def sortBars(numbers):
   for p in range(0,len(numbers)):
      smallest = p
      for q in range(p+1,len(numbers)):
         if numbers[q] < numbers[smallest]:
            smallest = q;
      swapBars(numbers,p,smallest)                  



##########
#  MAIN  #
##########

numbers = []
buildArray(numbers)
beginGrfx(1300,700)
drawHeading("John Smith","16")
drawBars(numbers)
sortBars(numbers)


delay(3000)
reset()
drawHeading("John Smith","16")
drawBars(numbers)

endGrfx()

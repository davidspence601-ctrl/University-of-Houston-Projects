from graphics import *
from random import randint
import time

def buildArray(numbers):
    
    for _ in range(52):
        numbers.append(randint(10, 640))

def drawBar(index, numbers):
    
    setColor("red")
    x1 = index * 25 + 3
    x2 = x1 + 18
    y1 = 700 - numbers[index]
    y2 = 700
    fillRectangle(x1, y1, x2, y2)

def drawBars(numbers):
    
    clear()  
    for k in range(52):
        drawBar(k, numbers)

def swapBars(numbers, p, q):
    
    numbers[p], numbers[q] = numbers[q], numbers[p]
    drawBars(numbers)  
    delay(50)  

def sortBars(numbers):
    
    for p in range(len(numbers)):
        smallest = p
        for q in range(p + 1, len(numbers)):
            if numbers[q] < numbers[smallest]:
                smallest = q
        if smallest != p:
            swapBars(numbers, p, smallest)


numbers = []
buildArray(numbers)

beginGrfx(1300, 700)
drawHeading("John Smith", "16")
drawBars(numbers)

sortBars(numbers)  

delay(3000)  
reset()
drawHeading("John Smith", "16")
drawBars(numbers)

endGrfx()

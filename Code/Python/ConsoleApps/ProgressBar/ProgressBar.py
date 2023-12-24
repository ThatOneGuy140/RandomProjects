import os
import time

bars = [
    "[----------]", #0
    "[#---------]", #1
    "[##--------]", #2
    "[###-------]", #3
    "[####------]", #4
    "[#####-----]", #5
    "[######----]", #6
    "[#######---]", #7
    "[########--]", #8
    "[#########-]", #9
    "[##########]" #10

]

def bar(var,wait):
    try:
        print(bars[var])
        time.sleep(wait)
    except:
        print("Error: Inputed variable is higher than 10 or lower than 0")

def clear():
    os.system("clear")

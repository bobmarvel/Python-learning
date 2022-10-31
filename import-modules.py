#!/usr/bin/env python3

# add command chmod +x <file.py>
"""
learning how to import modules
"""

#import - ключевое слово
# есть стандартные модули, а есть кастомные, которые можно ставить через pip

# https://docs.python.org/3.9/library/

import time

currenttime = time.localtime()
print (currenttime)


#pip install rich
import rich
rich.print("[red]DO NOT LOGIN TO THIS DEVICE UNLESS AUTHORIZED")


# Если мы не хотим импортить всю библиотеку, то можно from * import 
# если у нас есть наложение существующей функции и сторонней, имеет смысл ALIAS
# from * import * as *

from rich import print as richprint
richprint("[blue]EleGiggle")

# Можно вызывать функции из других файлов

#import ex3

#how to return several args

def added_and_multiplied(num1,num2):
    added_total = num1 + num2
    mulitplied_total = num1 * num2

    return added_total, mulitplied_total

#richprint(added_and_multiplied(5,6))

x, y = added_and_multiplied(5,6)
richprint(f"Added is equal to {x} and multiplied is equal to {y}")
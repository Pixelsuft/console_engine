if __name__ == '__main__':
    exit()

from os import name as os_type
if not os_type == 'nt':
    exit()

from wav_win_sound import Mixer as sound_mixer_class
from os import get_terminal_size as get_size
from colorama import init as colorama_init
from colorama import Fore as fore
from colorama import Back as back
from colorama import Style as style
from colorama import Cursor as cursor
from time import sleep as time_sleep
from ctypes import windll as windows_dll
from win32con import *
from win32api import GetAsyncKeyState as get_async_key_state
from msvcrt import getch as wait_for_key


mixer = sound_mixer_class()
colorama_init(autoreset = True)


width = 0
height = 0
print_old = print
endl = '\n'
canvas = ''
canvas_mas = []
title = windows_dll.kernel32.SetConsoleTitleW
del windows_dll


def reload_size(fix_width = 0, fix_height = 1):
    global width
    global height
    global canvas_mas
    width, height = get_size()
    width -= fix_width
    height -= fix_height
    for i in range(height):
        canvas_mas.append([])
        for j in range(width):
            canvas_mas[i].append(' ')
    return width, height


def print(*args, **kwargs):
    print_old(*args, **kwargs, end='')


def print_center(string_to_print, auto_endl = False, end = ''):
    result = ''
    for i in str(string_to_print).split(endl):
        result = ' ' * int(width/2 - len(i)/2) + i
        if auto_endl == True:
            result += endl
    print(result + end)


def print_right(string_to_print, auto_endl = False, end = ''):
    result = ''
    for i in str(string_to_print).split(endl):
        result = ' ' * int(width - len(i)) + i
        if auto_endl == True:
            result += endl
    print(result + end)


def tick(fps):
    time_sleep(1/fps)


def clear(fillspace = True):
    global canvas
    canvas = ''
    if fillspace == True:
        canvas = ' ' * width * height


def fill_all(symbol = ' ', color = back.BLACK + fore.GREEN):
    global canvas
    canvas = color + symbol * (width) * (height)


def point(symbol = '@', left_top = (0, 0), color = '', end = ''):
    global canvas_mas
    canvas_mas[left_top[1]][left_top[0]] = symbol


def fill(symbol = '@', left_top = (0, 0), width_height = (5, 5), color = '', end = ''):
    global canvas_mas
    for i in range(height):
        for j in range(width):
            if i >= left_top[1] and i < left_top[1] + width_height[1] and j >= left_top[0] and j < left_top[0] + width_height[0]:
                canvas_mas[i][j] = symbol


def shape(symbol = '@', left_top = (0, 0), width_height = (5, 5), color = '', end = ''):
    global canvas_mas
    for i in range(height):
        for j in range(width):
            if i == left_top[1] and j >= left_top[0] and j < width_height[0] + left_top[0]:
                canvas_mas[i][j] = symbol
            elif i == left_top[1] + width_height[1] and j >= left_top[0] and j < width_height[0] + left_top[0]:
                canvas_mas[i][j] = symbol
            elif j == left_top[0] and i >= left_top[1] and i < width_height[1] + left_top[1]:
                canvas_mas[i][j] = symbol
            elif j == left_top[0] + width_height[0] and i >= left_top[1] and i <= width_height[1] + left_top[1]:
                canvas_mas[i][j] = symbol


def text(string = 'Console Engine', left_top = (0, 0), length = 0, start = '', end = ''):
    if length <= 0:
        length = len(string)
    global canvas_mas
    canvas_mas[left_top[1]][left_top[0]] = start
    for i in range(length):
        if not i == 0:
            canvas_mas[left_top[1]][left_top[0]+i] = ''
        canvas_mas[left_top[1]][left_top[0]+i] += string[i]
        if i == length-1:
            canvas_mas[left_top[1]][left_top[0]+i] += end


def convert():
    global canvas
    result = ''
    for x in canvas_mas:
        for y in x:
            result += y
    canvas = result


def display():
    print(canvas)


def up_screen(fix_count = 1):
    for i in range(width * fix_count):
        print(cursor.BACK())
    for i in range(height * fix_count):
        print(cursor.UP())


reload_size()
up_screen(fix_count = 10)
clear()
up_screen()
display()
title('Pixelsuft Console Engine')

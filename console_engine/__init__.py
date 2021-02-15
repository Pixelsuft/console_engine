if __name__ == '__main__':
    exit()

from os import name as os_type
if not os_type == 'nt':
    exit()

from wav_win_sound import Mixer as wav_mixer
from os import get_terminal_size as get_size
from os import environ as env
from colorama import init as colorama_init
from colorama import Fore as fore
from colorama import Back as back
from colorama import Style as style
from colorama import Cursor as cursor
from time import sleep as time_sleep
from ctypes import windll as windows_dll
from pyautogui import position as get_mouse_pos
from pyautogui import moveTo as move_mouse_to
from win32con import *
from win32api import GetAsyncKeyState as get_async_key_state
from win32api import GetSystemMetrics as get_screen_size
from win32gui import GetWindowRect as get_window_size
from win32gui import GetForegroundWindow as get_current_window
from msvcrt import getch as wait_for_key


colorama_init(autoreset=True)


width = 0
height = 0
print_old = print
endl = '\n'
canvas = ''
canvas_mas = []
title = windows_dll.kernel32.SetConsoleTitleW
del windows_dll
real_mouse_x = 0
real_mouse_y = 0
mouse_x = 0
mouse_y = 0
screen_width = 0
screen_height = 0
window_geometry = (0, 0, 0, 0)


def reload_screen_size():
    global screen_width
    global screen_height
    screen_width = int(get_screen_size(0))
    screen_height = int(get_screen_size(1))


def reload_geometry():
    global window_geometry
    try:
        window_geometry = get_window_size(get_current_window())
    except:
        pass


def reload_mouse_pos():
    global real_mouse_x
    global real_mouse_y
    global mouse_x
    global mouse_y
    real_mouse_x, real_mouse_y = get_mouse_pos()
    mouse_x = real_mouse_x - window_geometry[0]
    mouse_y = real_mouse_y - window_geometry[1]


def center_cursor():
    move_mouse_to(int(screen_width/2), int(screen_height/2))


def reload_size(fix_width=0, fix_height=1):
    global width
    global height
    global canvas_mas
    temp_width, temp_height = get_size()
    if not temp_width == width or not temp_height == height:
        width = temp_width - fix_width
        height = temp_height - fix_height
        canvas_mas = []
        for i in range(height):
            canvas_mas.append([])
            for j in range(width):
                canvas_mas[i].append(' ')


def print(*args, **kwargs):
    print_old(*args, **kwargs, end='')


def print_center(string_to_print, auto_endl=False, end=''):
    result = ''
    for i in str(string_to_print).split(endl):
        result = ' ' * int(width/2 - len(i)/2) + i
        if auto_endl:
            result += endl
    print(result + end)


def print_right(string_to_print, auto_endl=False, end=''):
    result = ''
    for i in str(string_to_print).split(endl):
        result = ' ' * int(width - len(i)) + i
        if auto_endl:
            result += endl
    print(result + end)


def tick(fps):
    time_sleep(1/fps)


def clear(fillspace=True):
    fill_all(symbol=' ')


def fill_all(symbol=' ', color=back.BLACK + fore.GREEN):
    global canvas_mas
    for i in range(len(canvas_mas)):
        for j in range(len(canvas_mas[i])):
            canvas_mas[i][j] = symbol


def point(symbol='@', left_top=(0, 0), color='', end=''):
    global canvas_mas
    canvas_mas[left_top[1]][left_top[0]] = symbol


def fill(symbol='@', left_top=(0, 0), width_height=(5, 5), color='', end=''):
    global canvas_mas
    for i in range(height):
        for j in range(width):
            if i >= left_top[1] and i < left_top[1] + width_height[1] and j >= left_top[0] and j < left_top[0] + width_height[0]:
                canvas_mas[i][j] = symbol


def shape(symbol='@', left_top=(0, 0), width_height=(5, 5), color='', end=''):
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


def text(string='Console Engine', left_top=(0, 0), length=0, start='', end=''):
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


def up_screen(fix_count=1):
    for i in range(width * fix_count):
        print(cursor.BACK())
    for i in range(height * fix_count):
        print(cursor.UP())


if '__CONSOLE_ENGINE_AUTO_HIDE' not in env:
    reload_screen_size()
    reload_size()
    reload_geometry()
    reload_mouse_pos()
    up_screen(fix_count=10)
    clear()
    up_screen()
    display()
    title('Pixelsuft Console Engine')

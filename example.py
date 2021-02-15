import console_engine as engine
from random import choice as pick
from threading import Thread as thread
mixer = engine.wav_mixer()
mixer.load('some_music.wav')
mixer.async_play()
fps = 120
lister = ['@', '0', 'X', 'O', '2', 'E', 'S', '+', '-', '#', '(', '&', '^']
running = True
welcome_text = 'Pixelsuft Console Engine'
engine.center_cursor()


def check_keys():
    global running
    while running:
        if engine.get_async_key_state(engine.VK_ESCAPE):
            running = False
            mixer.stop()
            break


thread(target=check_keys).start()
while running:
    engine.clear()
    engine.reload_size()
    engine.reload_geometry()
    engine.reload_mouse_pos()
    otnosh_x = engine.window_geometry[2] / engine.width
    otnosh_y = engine.window_geometry[3] / engine.height
    engine.shape(engine.fore.GREEN+pick(lister)+engine.style.RESET_ALL, (0, 0), (7, 5))
    engine.shape(engine.fore.GREEN+pick(lister)+engine.style.RESET_ALL, (14, 0), (7, 5))
    engine.shape(engine.back.RED+pick(lister)+engine.style.RESET_ALL, (0, 10), (21, 5))
    engine.text(welcome_text, (int(engine.width/2-len(welcome_text)/2), int(engine.height/2)), start = engine.back.GREEN + engine.fore.BLACK, end = engine.style.RESET_ALL)
    engine.text(str(engine.mouse_x) + 'x' + str(engine.mouse_y), (int(engine.width/2), engine.height - 1))
    try:
        engine.point('X', (int(engine.mouse_x / otnosh_x), int(engine.mouse_y / otnosh_y)))
    except:
        pass
    engine.up_screen()
    engine.convert()
    engine.display()
    engine.tick(fps)
running = False
exit()

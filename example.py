import console_engine as engine
from random import choice as pick
from threading import Thread as thread
engine.mixer.load('some_music.wav')
engine.mixer.async_play()
fps = 10
lister = ['@', '0', 'X', 'O', '2', 'E', 'S', '+', '-', '#', '(', '&', '^']
running = True


def check_keys():
    global running
    while running == True:
        if engine.get_async_key_state(engine.VK_ESCAPE):
            running = False
            engine.mixer.stop()
            break


thread(target = check_keys).start()
while running == True:
    engine.clear()
    engine.shape(engine.fore.GREEN+pick(lister)+engine.style.RESET_ALL, (0, 0), (7, 5))
    engine.shape(engine.fore.GREEN+pick(lister)+engine.style.RESET_ALL, (14, 0), (7, 5))
    engine.shape(engine.back.RED+pick(lister)+engine.style.RESET_ALL, (0, 10), (21, 5))
    engine.up_screen()
    engine.convert()
    engine.display()
    engine.tick(fps)
running = False
exit()

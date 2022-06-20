import pyautogui as pg
import time

pg.hotkey("win","r")
pg.typewrite("https://youtu.be/PHPQbHjWGfs?t=8")
pg.press("enter")
time.sleep(2)
pg.typewrite("k")
pg.hotkey("win","r")
pg.typewrite("notepad\n")
time.sleep(1)
pg.typewrite("Despues de tiempo me la encontre la otra vez\n")
time.sleep(1)
pg.typewrite("Estaba bella como las estrellas\n")


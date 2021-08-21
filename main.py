import cursor
from os import system
import keyboard
from time import sleep
import sys


def print_display(x_size, y_size):

    x_size_real = x_size - 2
    y_size_real = y_size - 2
    top_rigth_coor = (x_size, 2)
    top_left_coor = (2, 2)

    # Imprimimos las esquinas
    print("\033[%d;%dH╔" % (2, 2))
    print("\033[%d;%dH╗" % (2, x_size))
    print("\033[%d;%dH╚" % (y_size+1, 2))
    print("\033[%d;%dH╝" % (y_size+1, x_size))

    #Imprimimos las barras horizontales
    for i in range(3, top_rigth_coor[0]):
        print("\033[%d;%dH═" % (top_left_coor[1], i))
        print("\033[%d;%dH═" % (top_left_coor[1]+y_size-1, i))

    #Imprimimos las barras verticales
    for j in range(3, y_size+1):
        print("\033[%d;%dH║" % (j, 2))
        print("\033[%d;%dH║" % (j, x_size))


#Ocultamos el cursor
cursor.hide()

# Coordenadas iniciales de donde va a aparecer la nave al principio
x = 25
y = 20
system("cls")

#Especificamos las dimenciones del cuadro
dim_x = 50
dim_y = 20
print_display(dim_x, dim_y)
print("\033[%d;%dH═╩═" % (y, x))


def move(x_new, y_new, key):
    if key == "d":
        if x_new is not dim_x-2:
            print("\033[%d;%dH " % (y, x))
            print("\033[%d;%dH═╩═" % (y_new, x_new))
            return y_new, x_new
        return y, x
    elif key == "a":
        if x_new is not 2:
            print("\033[%d;%dH═╩═" % (y_new, x_new))
            print("\033[%d;%dH " % (y, x+2))
            return y_new, x_new
        return y, x
    elif key == "w":
        #Como no queremos que se mueva en el eje y retornamos las coordenadas actuales
        return y, x
    elif key == "s":
        #Como no queremos que se mueva en el eje y retornamos las coordenadas actuales
        return y, x

try:
    while True:
        if keyboard.is_pressed('w'):
            y, x = move(x, y-1, "w")
            sleep(0.15)
        elif keyboard.is_pressed("s"):
            y, x = move(x, y+1, "s")
            sleep(0.15)
        elif keyboard.is_pressed("a"):
            y, x = move(x-1, y, "a")
            sleep(0.1)
        elif keyboard.is_pressed("d"):
            y, x = move(x+1, y, "d")
            sleep(0.1)
        elif keyboard.is_pressed('q'):
            sys.exit()
        sleep(0.1)
except KeyboardInterrupt as e:
    sys.exit()

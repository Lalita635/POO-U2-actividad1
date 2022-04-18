import csv
from menu import Menu
from ClaseEmail import Email
import os

def test () :
    print('------ TEST ------')
    print('datos a probar: \nDatos correctos: \ninformatica.fcefn@gmail.com, sied@unsj-cuim.edu.ar, lali.635@gmail.com \n\nDatos incorrectos: \nlali.635gmail.com, sied@hotmail')
    nuevotest= Email()
    print('\n\n--- DATOS CORRECTOS')
    print('informatica.fcefn@gmail.com')
    nuevotest.crearCuenta('informatica.fcefn@gmail.com','contrasenia1')
    print('sied@unsj-cuim.edu')
    nuevotest.crearCuenta('sied@unsj-cuim.edu','contrasenia2')
    print('lali.635@hotmail.com')
    nuevotest.crearCuenta('lali.635@hotmail.com','contrasenia3')
    print('\n--- DATOS INCORRECTOS')
    print('lali635gmail.com')
    nuevotest.crearCuenta('lali635gmail.com','contrasena4')
    print('sied@hotmail')
    nuevotest.crearCuenta('sied@hotmail','contrasena5')
    os.system('Pause')
    os.system('cls')


if __name__ == '__main__':
    
    op=int (input('Desea ejecutar el test? \n 1 - SI \n 2 - NO\n'))
    if op==1:
        test()
    nuevoMail= Email()
    xmenu=Menu()
    q=False
    while not q:
        print(' --++ Menu ++-- ')
        op= int(input('Seleccione la opcion:\n1- Ingresar el nombre de una persona y su dirección de e-mail\n2- Cambiar la contrasena de la cuenta creada anteriormente\n3- Leer de un archivo\n4- Salir\n'))
        if op != 4:
            xmenu.manejoMenu(op,nuevoMail)
        else:
            q= True

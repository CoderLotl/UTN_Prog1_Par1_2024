from model.services.Utilitarios import Funciones
from model.services.Validaciones import Validaciones
import numpy as np

class App:

    depositos = None
    ocupados = 0
    capacidad = 20
    func = Funciones()

    def __init__(self):
        self.depositos = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],
                          [[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],
                          [[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],
                          [[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
        pass

    def Run(self):        
        end = False
        opt = None

        while(end == False):
            self.func.clear_console()
            self.Menu()
            
            opt = self.Ingresar_Opcion()           

            match opt:
                case 1:
                    self.Ingresar_Celular()                    
                case 2:
                    self.Obtener_Existencia()                    
                case 7:
                    end = True
        pass

    def Menu(self):        
        menu = f""" === [ MENU ] ===

        Depósitos ocupados: {self.ocupados} / {self.capacidad}

        1.- Ingresar Existencia.
        2.- Obtener Existencia.
        7.- Salir.

        """
        print(menu)
        pass

    def Ingresar_Opcion(self):

        valid = False
        val = Validaciones()

        while(valid == False):
            opt = input("Ingrese una opción: ")

            if val.Validar_Num(opt):
                opt = int(opt)
                return opt
            else:
                print("Error: ingrese un número válido.\n")
        pass

    def __Elegir_Marca(self):
        val = Validaciones()
        opt_valid = False
        opt = 0
        marcas = ['Xiaomi', 'Nubia', 'Infinix', 'Samsung']
        mesg = """Escoja la marca:\n\n
        1- Xiaomi\n
        2- Nubia\n
        3- Infinix\n
        4- Samsung\n\n"""

        while(opt_valid == False):
            opt = input(mesg)
            if val.Validar_Num(opt) and (int(opt) - 1) in range(4):
                opt = int(opt)
                return marcas[opt - 1]
            else:
                print("Error: seleccione una de las opciones...")
                input()
        pass

    def Ingresar_Celular(self):
        self.func.clear_console()
        if self.ocupados < (self.capacidad - 1):

            val = Validaciones()
            name = None
            valid_name = False
            price = None
            valid_Price = False
            quan = None
            valid_Quan = False

            name = self.__Elegir_Marca()                
            
            while(valid_Price == False):
                price = input('Ingrese el precio: $')

                if val.Validar_Num(price):
                    valid_Price = True
                else:
                    print('Error: ingrese un precio válido')

            while(valid_Quan == False):
                quan = input('Ingrese la cantidad: ')

                if val.Validar_Num(quan):
                    valid_Quan = True
                else:
                    print('Error: ingrese una cantidad válida.')
            
            self.depositos[self.ocupados][0] = name
            self.depositos[self.ocupados][1] = price
            self.depositos[self.ocupados][2] = quan
            self.ocupados+=1
            print('Existencia agregada al depósito')

        else:
            print('Error: depósitos llenos')
        
        pass

    def Obtener_Existencia(self):
        self.func.clear_console()
        found = False
        void = None

        for dep in range(20):            
            if self.depositos[dep][0] != []:                
                print(f"=== Depósito {dep +1} ===\nMarca: {self.depositos[dep][0]} - Precio: ${self.depositos[dep][1]} - Cantidad: {self.depositos[dep][2]}\n")
                found = True
        
        if found == False:
            print('No se encontraron existencias.')
        void = input("Presione una tecla ...")
        pass
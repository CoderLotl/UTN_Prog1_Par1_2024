import os

class Funciones:
    def __init__(self) :
        pass

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
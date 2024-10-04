class Validaciones:

    def __init__(self) -> None:
        pass

    def Validar_Num(self, entry):
        valid = True

        for char in entry:
            if not char.isdigit():
                valid = False
                break
        return valid
    
    def Validar_Char(self, entry):
        valid = True

        for char in entry:
            if char.isdigit():
                valid = False
                break
        return valid
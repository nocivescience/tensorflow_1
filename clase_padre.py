class Parent:
    def metodo(self):
        print("Soy el padre")
padre=Parent()
padre.metodo()
class MiClaseConInit(Parent):
    def __init__(self):
        print("Soy el hijo")
        
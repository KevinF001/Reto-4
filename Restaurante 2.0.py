class Menu:

    def __init__(self, nombre, precio):
        self.__nombre = nombre        
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio


class Bebida(Menu):

    def __init__(self, nombre, precio, complementos):
        super().__init__(nombre, precio)
        self.complementos = complementos


class Plato(Menu):

    def __init__(self, nombre, precio, momento):
        super().__init__(nombre, precio)
        self.momento = momento


class Postre(Menu):

    def __init__(self, nombre, precio, sabor):
        super().__init__(nombre, precio)
        self.sabor = sabor


class Orden:                                # Para que el usuario ingrese sus platos solo debe poner el número que corresponde a cada uno, luego gracias a la lista nombres_platos
                                            # que contiene la llave de cada uno en el diccionario menu, en orden exacto a como se presentan se puede hacer una relación directa.
    def __init__(self):                                         
        self.orden = [int(pedido) for pedido in input("Ingrese su pedido por el número correspondiente al plato, separe por comas: ").split(',')]
        self.nombres_platos = list(menu.keys())
        self.costo = self.calcular_pedido()   

    def calcular_pedido(self):
        costo = 0
        for items in self.orden:               # Con el atributo precio dado en cada clase hija de Menu simplemente se accede en orden a este en el diccionario Menu y se suma uno a uno.
            costo += menu[self.nombres_platos[items - 1]].get_precio()
        return costo

    def descuentos(self):
        if  1 in self.orden and 5 in self.orden:  # Gracias a a la relación directa entre el tipo de plato y el número de este, se puede saber que tipos particulares hay
          costo_descuento = self.costo * 0.93       # luego se asigna un nuevo valor al costo inicial dado el descuento, sino este se mantiene.
          ahorro = self.costo - costo_descuento
          return f"¡Aplica a 7% de descuento! Su orden ahora cuesta: ${costo_descuento} ahorro: ${ahorro} gracias por comprar"

        elif 2 in self.orden and 7 in self.orden:
          costo_descuento = self.costo * 0.90
          ahorro = self.costo - costo_descuento
          return f"¡Aplica a 10% de descuento! Su orden ahora cuesta: ${costo_descuento} ahorro: ${ahorro} gracias por comprar"
       
        elif 12 in self.orden and  3 in self.orden:
            costo_descuento = self.costo * 0.93
            ahorro = self.costo - costo_descuento
            return f"¡Aplica a 7% de descuento! Su orden ahora cuesta: ${costo_descuento} ahorro: ${ahorro} gracias por comprar"
        else:
            return f"No se aplican descuentos, total a pagar: ${self.costo}"


class MedioPago:

    def __init__(self, costo):
        self.costo = costo

    def pagar(self):
        raise NotImplementedError("Subclases deben implementar pagar()")


class Tarjeta(MedioPago):

    def __init__(self, costo):
        super().__init__(costo)
        self.numero = input("Ingrese su número de tarjeta: ")
        self.cvv = input("Ingrese el CVV de su tarjeta: ")

    def pagar(self):
        print(
            f"Pagando ${self.costo} con tarjeta {self.numero[-4:]}")


class Efectivo(MedioPago):

    def __init__(self, costo):
        super().__init__(costo)
        self.monto_entregado = float(
            input("Ingrese con cuanto desea pagar: "))

    def pagar(self):
        if self.monto_entregado >= self.costo:
            print(
                f"Pago realizado en efectivo. Cambio: ${self.monto_entregado - self.costo}")
        else:
            print(
                f"Fondos insuficientes. Faltan ${self.costo - self.monto_entregado} para completar el pago.")


cáfe = Bebida("Cafe", 2500, "Tamal")
jugo = Bebida("Jugo natural", 3500, "Arroz con pollo")
malteada = Bebida("Malteada", 5000, "Pastel de chocolate")   # Instanciación de cada objeto correspondiente a cada clase hijda de Menu.
vino = Bebida("Vino", 12000, "Pasta")
tamal = Plato("Tamal", 6000, "Desayuno")
huevos = Plato("Huevos pericos", 5000, "Desayuno")
bandeja = Plato("Bandeja paisa", 13000, "Almuerzo")
frijoles = Plato("Frijoles con carne", 10000, "Almuerzo")
arroz = Plato("Arroz paisa", 15000, "Almuerzo")
pasta = Plato("Pasta con albondigas", 12000, "Cena")
ensalada = Postre("Ensalada de frutas", 12000, "dulse")
pastel = Postre("Pastel de chocolate", 8000, "dulse")
mango = Postre("Mango con limon", 4000, "acido")
                                                          # Diccionario que guarda cada objeto con una llave que lleva el nombre de este.
menu = {"Cafe":cáfe, "Jugo natural":jugo, "Malteada":malteada, "Vino":vino, "Tamal":tamal, "Huevos pericos":huevos, "Bandeja paisa":bandeja,
        "Frijoles con carne": frijoles, "Arroz paisa":arroz, "Pasta con albondigas":pasta, "Ensalada de frutas":ensalada, "Pastel de chocolate":pastel, "Mango con limo":mango }

print("Opciones del menu: \n")
n = 1
for opciones in menu:
    if menu[opciones].get_nombre() == "Cafe":   # Esto solo es para que se vea bien la impreción.
        print("|Bebidas: \n")
    elif menu[opciones].get_nombre() == "Tamal":
        print("   \n|Platos:\n")
    elif menu[opciones].get_nombre() == "Ensalada de frutas":
        print("    \n|Postres:\n")

    print(f"{n}. {menu[opciones].get_nombre()}: ${menu[opciones].get_precio()}")  # Gracias al bucle se puede imprimir uno a uno los onjetos como estan guardados en el diccionario
    n += 1                                                                          # n indica el orden simplemente y gracias a esto el usuario puede pedir.
print("\n")

print("Opciones de descuento: \n Si ordena un café y un tamal: 7% de descuento \n Si ordena badeja paisa y jugo: 10% de descuento \n Si ordena una malteada y un pastel: 7% de descuento")

orden = Orden()                                 # Instanciación de la clase orden para permitir mostrar el total a  pagar y descuentos.
print("--Usted ha ordenado lo siguiente: \n")

for items in orden.orden:
    print(
        f"{menu[orden.nombres_platos[items - 1]].get_nombre()}  :  ${menu[orden.nombres_platos[items - 1]].get_precio()}  ") # Muestra en orden lo que pidio el usuario y lo que cuesta

print(f"\n {orden.descuentos()}")

x = int(input(
    "¿Cómo desea pagar? Ingrese 1 para tarjeta o 2 para efectivo: "))
if x == 1:
    medio_pago = Tarjeta(orden.costo)
    medio_pago.pagar()
elif x == 2:
    medio_pago = Efectivo(orden.costo)
    medio_pago.pagar()
else:
    print("Opción de pago no válida")
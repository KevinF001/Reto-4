# Reto-4
# Ejercicio de clase
Para el ejercicio de clase construi la figura geometrica creando cordenadas con la clase punto y calculando la distancia entre estas de manera ordenada, despues simplemente utilize formulas matematicas como el teorema del coseno, la formula de heron o la formula de la distancia dados dos puntos; con el fin de calcular las diferentes cosas, lo más dificil fue lograr cubrir todos los imprevistos que pudieran surgir y dar entradas comodas con instrucciones claras.

```Python
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return self.x, self.y    # Retorna dos puntos que componen una cordenada.

class Line:
    def __init__(self, initial_point, final_point):
        self.initial_point = initial_point
        self.final_point = final_point

    def length(self):
        x1, y1 = self.initial_point.coordinates() # Con la composición de Point y el metodo coordinates() crear una cordenada inicial y otra final.
        x2, y2 = self.final_point.coordinates()
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Calcula la distancia entre a cordenada incial y final.

class Shape:
    def __init__(self):
      pass

    def initialize_shape(self, x):  # Para incializar se determina la cantidad de vertices que tendra la figura esto dado por x que es una entrada para el usuario.
        if x == 4:
            self.vertices = [] # Crea una lista para posteriormente guardar las cordenadas en formato de tuplas. 
            for n in range(1, 5): # Si son 4 se ejecuta 4 veces un bucle que permite ingresar una cordenada por cada iteración y para esto se aplica una composición de la clase punto con el metodo coordinates(). 
                c = ([float(coordinate) for coordinate in input(f"Ingrese la cordenada {n}: ").split(',')]) # n simboliza la cordenada actual.
                punto = Point(c[0], c[1])
                x_nu, y_nu = punto.coordinates()
                self.vertices.append((x_nu, y_nu)) # Tras crearse la cordenada se guarda en la lista.
        elif x == 3:
            self.vertices = []
            for n in range(1, 4): # Si son 3 hace exactamnete lo mismo solo que una vez menos.
                c = ([float(coordinate) for coordinate in input(f"Ingrese la cordenada {n}: ").split(',')])
                punto = Point(c[0], c[1])
                x_nu, y_nu = punto.coordinates()
                self.vertices.append((x_nu, y_nu))

    def get_vertices(self):
        return self.vertices
                                # Los metodos principales se ejecutan posteriormente en las clases hijas y para garantizar el poliformismo se pone la condición  "NotImplementedError".
    def compute_perimeter(self):
        raise NotImplementedError("Subclases deben implementar compute_perimeter()")

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_angles(self):
        raise NotImplementedError("Subclases deben implementar compute_angles()")
    def regular (self):
        raise NotImplementedError("Subclases deben implementar compute_angles()")


class Rectangle(Shape): 
    def __init__(self):
        super().__init__()  # sides es una lista que pose el valor de todas las longiudes de los lados de la figura.
                                # Esto ocurre más abajo a la hora de instanciar Shape y sus metodos, sides se crea con composición de Point y Line junto con sus metodos. 
    def compute_perimeter(self): 
        return sum(sides)   

    def compute_area(self):
        return sides[0] * sides[1] # Multiplica el dato 1 y 2 de la lista sides, correspondientes a base y altura.

    def compute_angles(self): # Como más adelante se comprueba que la figura es un rectangulo, al verificar que sus lados opuestos son iguales en longitud
      return [90, 90, 90, 90]   # y sus diagonales son las mismas; se puede afirmar con toda seguridad que sus ángulos internos son de 90° todos.
    
    def regular(self): 
       return "No es regular" # Un rectangulo no es una figura regular; por no tener todos sus lados iguales.


class Square(Rectangle):
    def __init__(self):
        super().__init__() # Square hereda todos los metodos de Rectangle menos regular(), esto porque un cuadrado si es regular. En el caso de los ángulos se comprueban
                              # igual solo que esta vez todos los lados deben ser iguales.
    def regular(self):
       return "regular"

class Triangle(Shape): 
    def __init__(self):
        pass

    def triangle_type(self):
        if sides[0] == sides[1] == sides[2]:
            return "Equilatero"                                                       # Dadas las longitudes de los lados guardadas en sides se hacen analisis para verificar el tipo
        elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:      # de triangulo dado por el usuario.
            return "Isosceles"
        elif sides[0] ** 2 + sides[2] ** 2 == sides[1] ** 2:
            return "Rectangulo"
        elif sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]:
            return "Escaleno"

    def compute_perimeter(self):
        return sum(sides) 

    def compute_area(self):
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) # Formula de Heron para calcular el área apartir de la longitud de los tres lados.

    def compute_angles(self):
        ca = math.acos((sides[0] ** 2 - sides[1] ** 2 - sides[2] ** 2) / (-2 * sides[1] * sides[2])) * (180 / math.pi)
        cb = math.acos((sides[1] ** 2 - sides[0] ** 2 - sides[2] ** 2) / (-2 * sides[0] * sides[2])) * (180 / math.pi)  # Para calcular los ángulos internos se usa el teorema del coseno
        cc = math.acos((sides[2] ** 2 - sides[0] ** 2 - sides[1] ** 2) / (-2 * sides[0] * sides[1])) * (180 / math.pi)    # y luego una simple regla de tres para pasar el resultado a grados.
        return [ca, cb, cc] # Guarda el valor en grados de todos los ángulos internos
    
    def regular(self):
      triangle_type = self.triangle_type()
      if triangle_type == "Equilatero" or triangle_type == "Isosceles": # Solo los triangulos equilateros e isosceles son regulares.
        return "regular"
      else:
        return "No regular"

class Equilateral(Triangle):  # Todos los tipos de triangulos son clases hijas de Triangle, por lo que heredan todos sus metodos
    def __init__(self):
        super().__init__()

class Isosceles(Triangle):
    def __init__(self):
        super().__init__()

class Scalene(Triangle):
    def __init__(self):
        super().__init__()

class RectangleTriangle(Triangle):
    def __init__(self):
        super().__init__()

fo = Shape() # Instanciazión de la clase Shape()

print("   -Bienvenido- \n El siguiente programa permite analizar algunos tipos de tetaedros y triangulos, dadas sus cordenadas en el plano. Por favor ingrese datos coherentes :) \n")
while True:
    x = int(input("Ingrese la cantidad de cordenadas de su figura (vertices), si desea salir selecione 1: \n ")) # Entrada principal
    if x == 4:
        fo.initialize_shape(x) # Llama al metodo initialize_shape() para el objeto fo.
        vertices = fo.get_vertices() # LLama al metodo get_vertices() que contiene todas las cordenadas ingresadas por el usuario par el objeto fo y luego reasigna esos valores a la variable vertices.
        sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
        rectangulo = Rectangle()

        if sum(sides)/4 == sides[0]: # Instanciaciones e impreciones para las clases Square o Rectangle; (segun corresponda).
            cu = Square()
            diagonal_1 = Line(Point(vertices[0][0], vertices[0][1]), Point(vertices[2][0], vertices[2][1])).length()
            diagonal_2 = Line(Point(vertices[1][0], vertices[1][1]), Point(vertices[3][0], vertices[3][1])).length()
            if diagonal_1 != diagonal_2:
              raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

            print(f"\n La figura corresponde a un cuadrado de lados {sides[0]} con vertices en las cordenadas: {fo.get_vertices()} ")
            print(f"   Su perimetro es de: {cu.compute_perimeter()} y su área de {cu.compute_area()}")
            print(f"   Es una figura {cu.regular()}  y sus angulos internos son: {cu.compute_angles()} \n")

        elif sides[0] == sides[2] and sides[1] == sides[3]:
            diagonal_1 = Line(Point(vertices[0][0], vertices[0][1]), Point(vertices[2][0], vertices[2][1])).length()
            diagonal_2 = Line(Point(vertices[1][0], vertices[1][1]), Point(vertices[3][0], vertices[3][1])).length()
            if diagonal_1 != diagonal_2:
              raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

            print(f"\n La figura corresponde a un rectangulo de lados {sides[0]} x {sides[1]} con vertices en las cordenadas: {fo.get_vertices()} ")
            print(f"   Su perimetro es de: {rectangulo.compute_perimeter()} y su área de: {rectangulo.compute_area()}")
            print(f"   Es una figura {rectangulo.regular()}  y sus angulos internos son: {rectangulo.compute_angles()} \n")

        else:
          raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")


    elif x == 3:  # Instnaciaiones e impreciones para los 4 tipos de clasese hijas de Triangle; (segun corresponda).
        fo.initialize_shape(x)
        vertices = fo.get_vertices()
        sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
        triangulo = Triangle()

        if triangulo.triangle_type() == "Equilatero":
            if sum(triangulo.compute_angles()) != 180 and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[1]) and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[2]):
                raise ValueError("Los datos ingresados no corresponden a un triangulo")
            else:
                eq = Equilateral()
                print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo equilátero con todos sus lados de valor {sides[0]} por lo que es una figura {triangulo.regular()}")
                print(f" Su perímetro es de: {eq.compute_perimeter()} y su área de: {eq.compute_area()}")
                print(f" Sus ángulos internos son: {eq.compute_angles()} \n")

        elif triangulo.triangle_type() == "Isosceles":
            if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] != triangulo.compute_angles()[1] and triangulo.compute_angles()[0] != triangulo.compute_angles()[2] and triangulo.compute_angles()[1] != triangulo.compute_angles()[2]):
                raise ValueError("Los datos ingresados no corresponden a un triangulo")
            else:
                iso = Isosceles()
                print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo isósceles de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()}  ")
                print(f"   Su perímetro es de: {iso.compute_perimeter()} y su área es: {iso.compute_area()}")
                print(f"   Sus ángulos internos son: {iso.compute_angles()} \n ")

        elif triangulo.triangle_type() == "Escaleno":
            if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] == triangulo.compute_angles()[1] or triangulo.compute_angles()[0] == triangulo.compute_angles()[2] or triangulo.compute_angles()[1] == triangulo.compute_angles()[2]):
                raise ValueError("Los datos ingresados no corresponden a un triangulo")
            else:
              es = Scalene()
              print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde con un triángulo escaleno de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()} ")
              print(f"   Su perímetro es de: {es.compute_perimeter()} y su área es: {es.compute_area()}")
              print(f"   Sus ángulos internos son: {es.compute_angles()} \n ")

        elif triangulo.triangle_type() == "Rectangulo":
          if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] != 90 and triangulo.compute_angles()[1] != 90 and triangulo.compute_angles()[2] != 90):
              raise ValueError("Los datos ingresados no corresponden a un triangulo")
          else:
            rec = RectangleTriangle()
            print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo rectángulo de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()} ")
            print(f"   Su perímetro es de: {rec.compute_perimeter()} y su área de: {rec.compute_area()}")
            print(f"   Sus ángulos internos son: {rec.compute_angles()} \n ")

        else:
          raise ValueError("Los datos ingresados no corresponden a un triangulo")

    elif x == 1:  # Forma para terminar el programa.
          break

    else:    # Caso de ingreso para un valor no definido
      raise ValueError("Opción no válida")
```
# Restaurante 2.0
Para este ejercicio añadí el encapsulamineto con seters y geters desde la clase Menu, depues agrege el metodo de pago y actualize la forma de hacer descuentos. 
```Python
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

```

"""Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender
las ventajas de la programación orientada a objetos.
En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita actualizar
lo siguiente:
Identifica tres tipos de usuarios de su aplicación.

Identifica tres atributos por tipo de usuario.
Identifica tres acciones que pueden desarrollar cada tipo de usuario. Las acciones se deben ejecutar de
forma interna en nuestra aplicación. Por ejemplo, acceder a datos sensibles, registrar nuevos usuarios,
enviar solicitudes de información adicional.
Piense en nuevos atributos y acciones que pueden realizar los objetos.
Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
gráfica. Desarrollen el ejercicio de forma intuitiva."""


class Vendedor:
    """Clase que crea la instancia de vendedor, sus métodos guardan los montos de las ventas realizadas por el vendedor, calculan la comisión y bonos por ventas"""

    #atributos de instancia
    def __init__(self, nombre, dpto, com_dpto, meta_diaria):
        self.nombre = nombre
        self.dpto = dpto
        self.com_dpto = com_dpto
        self.meta_diaria = meta_diaria
        print(f"El vendedor {self.nombre}, trabaja en el departamento de {self.dpto} y recibe una comisión de {self.com_dpto} % por cada venta")
    
    #métodos de la clase:
    #ingresa datos de una venta y acumula los montos de venta en una lista para posteriormente calcular comisiones y bonos.
    def ingresar_venta (self, cant_prod, precio_prod):
        venta = cant_prod*precio_prod
        montos_ventas=[]
        venta.append(montos_ventas)
        total_ventas = sum(montos_ventas)
        return total_ventas

    #calcula la comision de venta segun el precio de vanta y el departamento en que trabaja el vendedor
    def calcular_comision (self, precio_venta):
        self.com_venta = (precio_venta*(self.com_dpto/100))
        print(f"El vendedor {self.nom} recibe $ {self.com_venta} por una venta de {self.precio_venta}")
    #calcula si el vendedor recibe bono segun la cantidad de productos vendidos por dia
    def calcular_bono (self, ventas_diarias ):
        if ventas_diarias >= self.meta_diaria:
            return True
        else:
            return False
    
    
            
class Cliente:
    """Clase que crea la instancia cliente, sus métodos registran datos de compra, datos del cliente para envio y calcula precio de envio"""
   
    #atributos de la instancia:
    def __init__(self, nombre, rut, region):
        self.nombre = nombre
        self.rut = rut
        self.region = region

    #métodos:
    def seleccionar_productos (self, nom_producto, cantidad):
        lista_productos=[]
        lista_cantidad=[]
        nom_producto.append(lista_productos)
        cantidad.append(lista_cantidad)
        compra= dict(zip(lista_productos, lista_cantidad))

    def registrar_datos (self, mail, direccion):
        datos_solicitados=["nombre", "mail", "direccion"]
        datos_ingresados=[self.nombre, mail, direccion]
        datos_cliente= dict(zip(datos_solicitados, datos_ingresados))

    def calcular_envio (self, region):  
        if region == "Metropolitana":
            envio = 3000
        else:
            envio = 4000
    

class Encargado_de_stock:
    """Clase que contiene métodos de gestion de stock de productos"""
 
    #atributos de la instancia
    def __init__(self, id_empleado, sector):
        self.id_empleado = id_empleado
        self.sector = sector
        
    #metodos:      
    def ingresar_productos(self, nom_producto, cantidad):
        print(f"Se han agregado {cantidad} unidades del producto {nom_producto}")  

    def actualizar_productos(self, nom_producto, cantidad):
        print(f"Se ha actualizado el stock: Actualmente existen {cantidad} unidades del producto {nom_producto}")

    def eliminar_productos(self, nom_producto):
        print(f"Se ha eliminado del stock el producto {nom_producto}")



        
    


    




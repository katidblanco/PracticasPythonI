import mysql.connector

class Catalogo:

    def __init__(self, host, user, password, database, port):
        try:
            self.conn=mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=port
            )


            self.cursor=self.conn.cursor(dictionary=True)
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos(
                codigo INT,
                descripcion VARCHAR (255) NOT NULL,
                cantidad INT(4) NOT NULL,
                precio DECIMAL(10,2) NOT NULL,
                imagen_url VARCHAR (255),
                proveedor INT (3)) ''')
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    #Metodo agregar producto

    def agregar_prod(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        prod_existe = self.cursor.fetchone()
        if prod_existe:
            return False
        sql = f"INSERT INTO productos \
                (codigo, descripcion, cantidad, precio, imagen_url, proveedor)\
                VALUES\
                ({codigo}, '{descripcion}', {cantidad}, {precio}, '{imagen}',{proveedor})"
        self.cursor.execute(sql)
        self.conn.commit()
        return True
    
    #Metodo consultar producto

    def consultar_prod(self, codigo):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()







#Main
catalogo=Catalogo(host='localhost', user='root', password='1234', database='miapp', port=3307)

#Agregamos productos
catalogo.agregar_prod(1,'teclado', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_prod(2,'mouse', 5, 2500, 'mouse.jpg', 101)
catalogo.agregar_prod(3,'monitor', 8, 45000, 'monitor.jpg', 101)

#Consulta de productos por código
cod_prod = int(input("Ingresa el codigo del producto para consultar "))
producto = catalogo.consultar_prod(cod_prod)
if producto:
    print(f"Producto encontrado: {producto ['codigo']}-{producto['descripcion']}")
else:
    print(f"producto {cod_prod} no encontrado")
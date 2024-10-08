#-------------------------------------------------------------------- 
# Instalar con pip install Flask 
from flask import Flask, request, jsonify 
from flask import request 

# Instalar con pip install flask-cors 
from flask_cors import CORS 

# Instalar con pip install mysql-connector-python 
import mysql.connector 

# Si es necesario, pip install Werkzeug 
from werkzeug.utils import secure_filename 

# No es necesario instalar, es parte del sistema standard de Python 
import os 
import time 


#--------------------------------------------------------------------
#Definimos la clase catalogo
#--------------------------------------------------------------------

app = Flask(__name__) 
CORS(app) # Esto habilitará CORS para todas las rutas


class Catalogo:

    def __init__(self, host, user, password, database, port):
        
            self.conn=mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                port = port
                
            )

            self.cursor=self.conn.cursor()

            # Intentamos seleccionar la base de datos 
            try: self.cursor.execute(f"USE {database}")
            except mysql.connector.Error as err: 
                 # Si la base de datos no existe, la creamos 
                if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR: 
                    self.cursor.execute(f"CREATE DATABASE {database}") 
                    self.conn.database = database 
                else: 
                    raise err
                

        # Una vez que la base de datos está establecida, creamos la tabla si no existe
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos ( 
                            codigo INT AUTO_INCREMENT, 
                            descripcion VARCHAR(255) NOT NULL, 
                            cantidad INT NOT NULL, precio DECIMAL(10, 2) NOT NULL, 
                            imagen_url VARCHAR(255), proveedor INT)''') 
            self.conn.commit()
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True 
            self.cursor.close() 
            self.cursor = self.conn.cursor(dictionary=True) 


    #Metodo agregar producto***********************************************************

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
    
    #Metodo consultar producto***********************************************************

    def consultar_prod(self, codigo):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def listar_productos(self): 
        self.cursor.execute("SELECT * FROM productos") 
        productos = self.cursor.fetchall() 
        return productos

    #Método Eliminar producto***********************************************************
    def eliminar_producto(self, codigo): 
        # Eliminamos un producto de la tabla a partir de su código 
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}") 
        self.conn.commit() 
        return self.cursor.rowcount > 0


    #********************************************************************






#MAIN MAIN MAIN*******************************************************************************************

catalogo=Catalogo(host='localhost', user='root', password='1234', database='miapp', port=3307)

#Agregamos productos
catalogo.agregar_prod(1,'teclado', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_prod(2,'mouse', 5, 2500, 'mouse.jpg', 101)
catalogo.agregar_prod(3,'monitor', 8, 45000, 'monitor.jpg', 101)


''' 
#Consulta de productos por código
cod_prod = int(input("Ingresa el codigo del producto para consultar "))
producto = catalogo.consultar_prod(cod_prod)
if producto:
    print(f"Producto encontrado: {producto ['codigo']}-{producto['descripcion']}")
else:
    print(f"producto {cod_prod} no encontrado")
'''
# Carpeta para guardar las imagenes 
ruta_destino = './static/imagenes/'



# LISTAR PRODUCTO**********************************


@app.route("/productos", methods=["GET"]) 
def listar_productos(): 
    productos = catalogo.listar_productos() 
    return jsonify(productos)



#ELIMINAR PRODUCTO****************************************************************************

@app.route("/productos/<int:codigo>", methods=["DELETE"])
def eliminar_producto(codigo): 
    # Primero, obtén la información del producto para encontrar la imagen 
    producto = catalogo.consultar_producto(codigo) 
    if producto: 
        # Eliminar la imagen asociada si existe 
        ruta_imagen = os.path.join(ruta_destino, producto['imagen_url']) 
        if os.path.exists(ruta_imagen): 
            os.remove(ruta_imagen) 
            # Luego, elimina el producto del catálogo 
            if catalogo.eliminar_producto(codigo): 
                return jsonify({"mensaje": "Producto eliminado"}), 200 
            else: 
                return jsonify({"mensaje": "Error al eliminar el producto"}), 500 
        else: 
                return jsonify({"mensaje": "Producto no encontrado"}), 404

if __name__ == "__main__": 
    app.run(debug=True)
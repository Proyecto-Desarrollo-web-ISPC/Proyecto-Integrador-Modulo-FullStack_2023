import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.connection = None
        self.cursor = None 
    
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database
            )
            
            self.cursor = self.connection.cursor()
            
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
            print("No se pudo establecer la conexión: {}".format(error))
            
    def commit(self):
        if self.connection:
            self.connection.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
            
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
    
    
    #completar los datos con sus datos personales
    
connection = DatabaseConnection(
host='localhost',
user='root', 
password='*****',
port='3306',
database='campeones_del_mundo'
)
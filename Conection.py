import mysql
import mysql.connector

class Connecion:
    
    def __init__(self) -> None:
        self.config={
            'user':'ADMIN',
            'password':'2003',
            'host':'localhost',
            'database':'usuarios_web',
            'auth_plugin': 'caching_sha2_password'
           # 'raise_on_warnings': True

            
        }
    
    def conectar(self):
        try:
            Connecion=mysql.connector.Connect(**self.config)
            Cursor=Connecion.cursor()
        except mysql.connector.Error as e :
            print("error en la bd  -->" , e)

if __name__ == '__main__':
    Connecion1=Connecion()
    
    Connecion1.conectar()
    print(Connecion1)
           
        
        
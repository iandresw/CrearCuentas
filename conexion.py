

import pyodbc


class ConexionBD:
    def __init__(self, tipo_bd):
        self.tipo_bd = tipo_bd
        if self.tipo_bd == 'sqlserver':
            self.conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=ESCRITORIOAB\\SQLEXPRESS2012;'
                'PORT=1433;'
                'UID=sa;'
                'PWD=mgia730@lc@3b3s;'
                'DATABASE=OCOTEPEQUE'
            )
        elif self.tipo_bd == 'odbc':
            self.conexion = pyodbc.connect(
                'DSN=SAFT;'
                'UID=sa;'
                'PWD=mgia730@lc@3b3s'
            )
        else:
            raise ValueError("Tipo de base de datos no válido")

    def obtener_cursor(self):
        return self.conexion.cursor()

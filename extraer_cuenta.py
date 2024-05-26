from Form_Cuenta import Form_Cuenta
from conexion import ConexionBD


class Consulta_cuenta(Form_Cuenta):
    def __init__(self) -> None:
        pass

    def extraer_lista_Cuentas(self):
        conexion = ConexionBD(tipo_bd='sqlserver')
        cursor = conexion.obtener_cursor()
        query = "SELECT ctaNombre, ctaSAMI, ctaTipo, ctaGOB FROM CuentasDB"
        cursor.execute(query)
        cuentasList = []
        cuentasName = []
        for row in cursor:
            cuentasList.append(row)
            ctaNombre = row[0]
            cuentasName.append(ctaNombre)

        cursor.close()
        conexion.conexion.close()
        return cuentasName, cuentasList

    def extraer_ult_PO(self):
        conexion = ConexionBD(tipo_bd='sqlserver')
        cursor = conexion.obtener_cursor()
        query = f"SELECT COUNT(CtaIngreso) AS Expr1 FROM CuentaIngreso_A WHERE (CtaIngreso LIKE '11111921%') AND (Anio = 2024)"
        cursor.execute(query)
        ultimaCtaPO = cursor.fetchone()
        cuentaPO = "11111921" + str(ultimaCtaPO[0])
        cuentaPO = Form_Cuenta.formatear_cuenta(self, cuentaPO)
        cursor.close()
        conexion.conexion.close()
        return cuentaPO

    def buscarUtlmaCta(self, cta):
        cta = cta.replace(" ", "")
        conexion = ConexionBD(tipo_bd='sqlserver')
        cursor = conexion.obtener_cursor()
        query = f"""
                SELECT MAX(CtaIngreso) AS Expr1
                FROM CuentaIngreso_A
                WHERE (CtaIngreso LIKE '{cta}%')
        """
        cursor.execute(query)
        cuenta = cursor.fetchone()
        if cuenta[0] is None or len(cuenta[0]) == 8:
            cuenta = Form_Cuenta.procesar_cuenta(self, cta)
            cuenta = cuenta.replace(" ", "")
            cuenta = Form_Cuenta.formatear_cuenta(self, cuenta)
        else:
            cuenta = Form_Cuenta.procesar_cuenta(self, cuenta[0])
            cuenta = cuenta.replace(" ", "")
            cuenta = Form_Cuenta.formatear_cuenta(self, cuenta)
        cursor.close()
        conexion.conexion.close()
        # Limpiar la Combobox antes de agregar nuevos elementos
        return cuenta  # Guardar los resultados de la consulta

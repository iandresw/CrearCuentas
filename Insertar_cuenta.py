from conexion import ConexionBD


class InsertarCuentas:
    def __init__(self) -> None:
        pass

    def inserta_A(self, ctaIngreso, anio, valorPermOp, valorRenovacion, nombreCtaIngreso, ctaPermOp, ctaRecuperacion, tipo):
        self.conexion = ConexionBD(tipo_bd='sqlserver')
        cursor = self.conexion.obtener_cursor()
        query = """
        INSERT INTO CuentaIngreso_A (CtaIngreso, Anio, Rango, ValorPermOp, ValorMensual, ValorRenovacion,
                                     ValorMultaSinPermiso, NombreCtaIngreso, CtaPermOP, CtaRecuperacion,
                                     Tipo, RangoR, Categoria, CtaInteres, CtaRecargos)
        VALUES (?, ?, 0, ?, 0, ?, 0, ?, ?, ?, ?, 0, 0, '1111121', '111121')
        """
        cursor.execute(query, (ctaIngreso, anio, valorPermOp, valorRenovacion,
                       nombreCtaIngreso, ctaPermOp, ctaRecuperacion, tipo))
        self.conexion.conexion.commit()
        cursor.close()

    def inserta_Contable(self, ctaIngreso, ctaContable):
        self.conexion = ConexionBD(tipo_bd='sqlserver')
        cursor = self.conexion.obtener_cursor()
        query = """
        INSERT INTO CuentaIngreso (CtaIngreso, CtaContable, AplicaPermOP, AplicaDescTerEd, Anio)
        VALUES (?, ?, 0, 0, 0)
        """
        cursor.execute(query, (ctaIngreso, ctaContable))
        self.conexion.conexion.commit()
        cursor.close()

    def insertar_SAMI(self, ctaIngreso, ctaNombreGral, ctaGOB):
        self.conexion = ConexionBD(tipo_bd='sqlserver')
        cursor = self.conexion.obtener_cursor()
        query = "INSERT INTO CuentaSAMI (CtaIngreso, NombreCuenta, CtaGob) VALUES(?,?,?)"
        cursor.execute(query, (ctaIngreso, ctaNombreGral, ctaGOB))
        self.conexion.conexion.commit()
        cursor.close()

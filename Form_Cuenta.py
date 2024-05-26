from conexion import ConexionBD


class Form_Cuenta:
    def __init__(self):
        self.conexion = ConexionBD(tipo_bd='sqlserver')

    def formatear_cuenta(self, cuenta):
        # Ejemplo de formateo asumiendo que cuenta es un string de longitud 11
        return f"{cuenta[0]}-{cuenta[1:3]}-{cuenta[3:6]}-{cuenta[6:8]}-{cuenta[8:]}"

    def formatear_cuentaContable(self, cuenta):
        # Ejemplo de formateo asumiendo que cuenta es un string de longitud 11
        tipo = cuenta[3:6]
        if tipo == "112":
            cta_recuperacion = '11212206'
        elif tipo == '113':
            cta_recuperacion = '11212204'
        elif tipo == '114':
            cta_recuperacion = '11212205'
        return f"4-{tipo}-{cuenta[6:8]}", cta_recuperacion

    def procesar_cuenta(self, cuenta):
        if len(cuenta) == 10 or len(cuenta) == 9 or len(cuenta) == 11:
            base = cuenta[:-2]  # '11111301'
            auxiliar = cuenta[-2:]  # '01'
            auxiliar_int = int(auxiliar)
            nuevo_auxiliar = auxiliar_int + 1
            # Mantener dos dígitos
            nuevo_auxiliar_str = f"{nuevo_auxiliar:02d}"
            nueva_cuenta = base + nuevo_auxiliar_str
            return nueva_cuenta
        if len(cuenta) == 8:
            return cuenta+"01"
        else:
            return cuenta

    def procesar_cuentaPO(self, cuenta):
        if len(cuenta) == 10 or len(cuenta) == 11:
            base = cuenta[:-3]  # '111113001'
            auxiliar = cuenta[-3:]  # '01'
            auxiliar_int = int(auxiliar)
            nuevo_auxiliar = auxiliar_int + 1
            # Mantener dos dígitos
            nuevo_auxiliar_str = f"{nuevo_auxiliar:03d}"
            nueva_cuenta = base + nuevo_auxiliar_str
            return nueva_cuenta
        if len(cuenta) == 8:
            return cuenta+"01"
        else:
            return cuenta

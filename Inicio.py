

from tkinter import ttk, Frame, Text, Label, Button, Entry, Checkbutton, Tk, BooleanVar
from conexion import ConexionBD
from extraer_cuenta import Consulta_cuenta
from Insertar_cuenta import InsertarCuentas
from Form_Cuenta import Form_Cuenta


class Aplicacion(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1060, height=400)
        self.master = master
        self.pack()
        self.crear_campos()

    def crear_campos(self):
        self.lbTitle = Label(self, text="Seleccione La Actividad")
        self.lbTitlePO = Label(self, text="Ultima Cuenta PO")
        self.lbTitleSAMI = Label(self, text="Cuenta SAMI")

        self.lbTitleCuenta = Label(self, text="Cuenta Ingreso")
        self.lbTitleNameCta = Label(self, text="Nombre Cuenta Ingreso")
        self.lbTitleCtaPO = Label(self, text="Cuenta PO")
        self.lbTitleCtaNamePO = Label(self, text="Nombre Cuenta PO")
        self.lbTitleValorePO = Label(self, text="Valor PO")

        self.chkAgregarPoVar = BooleanVar()
        self.chkCategoriasVar = BooleanVar()
        self.chkAgregarPo = Checkbutton(
            self, text="¿Agregar Permiso de Operacion?", variable=self.chkAgregarPoVar, command=self.verificar_PO)
        self.chkCategorias = Checkbutton(
            self, text="¿Agregar Categorias?", variable=self.chkCategoriasVar, command=self.verificar_categorias)
        self.txtcuentaSAMI = Entry(self)
        self.txtCuenta1 = Entry(self)
        self.txtCuenta2 = Entry(self)
        self.txtCuenta3 = Entry(self)
        self.txtCuenta4 = Entry(self)
        self.txtCtaNombre1 = Entry(self)
        self.txtCtaNombre2 = Entry(self)
        self.txtCtaNombre3 = Entry(self)
        self.txtCtaNombre4 = Entry(self)
        self.txtCtaPO1 = Entry(self)
        self.txtCtaPO2 = Entry(self)
        self.txtCtaPO3 = Entry(self)
        self.txtCtaPO4 = Entry(self)
        self.txtValorPO1 = Entry(self)
        self.txtValorPO2 = Entry(self)
        self.txtValorPO3 = Entry(self)
        self.txtValorPO4 = Entry(self)
        self.txtCtaNombrePO1 = Entry(self)
        self.txtCtaNombrePO2 = Entry(self)
        self.txtCtaNombrePO3 = Entry(self)
        self.txtCtaNombrePO4 = Entry(self)
        self.txtctaUltimoPO = Entry(self)
        self.btnSalir = Button(self, text="Salir", command=self.master.quit)
        self.btnGuardar = Button(self, text="Guardar", command=self.guardar)
        self.btnLimpiar = Button(self, text="Limpiar",
                                 command=self.limpiarCamposTodo)
        self.combobox = ttk.Combobox(self)
        # empaquedado
        self.lbTitle.place(x=10, y=10, width=300, height=30)
        self.combobox.place(x=10, y=40, width=300, height=30)

        self.lbTitlePO.place(x=320, y=10, width=200, height=30)
        self.txtctaUltimoPO.place(x=320, y=40, width=200, height=30)

        self.lbTitleSAMI.place(x=530, y=10, width=200, height=30)
        self.txtcuentaSAMI.place(x=530, y=40, width=200, height=30)

        self.lbTitleCuenta.place(x=10, y=80, width=100, height=30)
        self.lbTitleNameCta.place(x=120, y=80, width=300, height=30)
        self.lbTitleCtaPO.place(x=430, y=80, width=100, height=30)
        self.lbTitleCtaNamePO.place(x=540, y=80, width=400, height=30)
        self.lbTitleValorePO.place(x=950, y=80, width=100, height=30)

        self.txtCuenta1.place(x=10, y=120, width=100, height=30)
        self.txtCtaNombre1.place(x=120, y=120, width=300, height=30)

        self.chkCategorias.place(x=10, y=160, width=200, height=30)
        self.chkAgregarPo.place(x=220, y=160, width=200, height=30)
        self.btnSalir.place(x=10, y=310, width=100, height=30)
        self.btnGuardar.place(x=120, y=310, width=100, height=30)
        self.btnLimpiar.place(x=230, y=310, width=100, height=30)
        self.consultar_datos()
        self.combobox.bind("<<ComboboxSelected>>", self.mostrar_seleccion)

    def consultar_datos(self):
        # Limpiar la Combobox antes de agregar nuevos elementos
        self.combobox['values'] = []
        self.datos = []  # Guardar los resultados de la consulta
        nombres = []
        nombres, self.datos = Consulta_cuenta.extraer_lista_Cuentas(self)
        self.combobox['values'] = nombres

    def mostrar_seleccion(self, event):
        seleccion = self.combobox.get()
        self.txtCtaNombre1.delete(0, 1000)
        self.txtCuenta1.delete(0, 1000)
        self.txtcuentaSAMI.delete(0, 1000)
        self.txtctaUltimoPO.delete(0, 1000)
        self.ultCuentaPO = Consulta_cuenta.extraer_ult_PO(self)
        self.txtctaUltimoPO.insert(0, self.ultCuentaPO)

        for dato in self.datos:
            if dato[0] == seleccion:
                self.txtCtaNombre1.insert(0, dato[0])
                self.txtCuenta1.insert(
                    0, Consulta_cuenta.buscarUtlmaCta(self, dato[3]))
                self.txtcuentaSAMI.insert(0, dato[1])

                break
        self.verificar_PO()
        self.verificar_categorias()

    def verificar_categorias(self):
        if self.chkCategoriasVar.get():
            self.agregar_categorias()
        else:
            self.remover_categorias()

    def verificar_PO(self):
        if self.chkAgregarPoVar.get():
            self.limpiarPO()
            self.agregar_PO()
        else:
            self.remover_PO()

    def remover_categorias(self):
        self.txtCuenta2.place_forget()
        self.txtCuenta3.place_forget()
        self.txtCuenta4.place_forget()
        self.txtCtaNombre2.place_forget()
        self.txtCtaNombre3.place_forget()
        self.txtCtaNombre4.place_forget()
        self.txtCtaPO2.place_forget()
        self.txtCtaPO3.place_forget()
        self.txtCtaPO4.place_forget()
        self.txtCtaNombrePO2.place_forget()
        self.txtCtaNombrePO3.place_forget()
        self.txtCtaNombrePO4.place_forget()
        self.txtValorPO2.place_forget()
        self.txtValorPO3.place_forget()
        self.txtValorPO4.place_forget()

    def guardar(self):
        if self.chkCategoriasVar.get():
            # Lógica para guardar los datos
            InsertarCuentas.inserta_A(self, self.cuentaPO2, 2024, self.txtValorPO2.get(
            ), self.txtValorPO2.get(), self.txtCtaNombrePO2.get(), "", "11212209", 1)
            InsertarCuentas.inserta_Contable(self, self.cuentaPO2, "4-119-21")
            InsertarCuentas.insertar_SAMI(
                self, self.cuentaPO2, 'Permiso para Operacion de Negocios', '12.5.99.02.30.00')

            InsertarCuentas.inserta_A(self, self.cuentaPO3, 2024, self.txtValorPO3.get(
            ), self.txtValorPO3.get(), self.txtCtaNombrePO3.get(), "", "11212209", 1)
            InsertarCuentas.inserta_Contable(self, self.cuentaPO3, "4-119-21")
            InsertarCuentas.insertar_SAMI(
                self, self.cuentaPO3, 'Permiso para Operacion de Negocios', '12.5.99.02.30.00')

            InsertarCuentas.inserta_A(self, self.cuentaPO4, 2024, self.txtValorPO4.get(
            ), self.txtValorPO4.get(), self.txtCtaNombrePO4.get(), "", "11212209", 1)
            InsertarCuentas.inserta_Contable(self, self.cuentaPO4, "4-119-21")
            InsertarCuentas.insertar_SAMI(
                self, self.cuentaPO4, 'Permiso para Operacion de Negocios', '12.5.99.02.30.00')

            cta_contable, cta_recuperacion = Form_Cuenta.formatear_cuentaContable(
                self, self.cuenta2)
            InsertarCuentas.inserta_A(self, self.cuenta2, 2024, 0, 0, self.txtCtaNombre2.get(
            ), self.cuentaPO2, cta_recuperacion, 1)
            InsertarCuentas.inserta_Contable(self, self.cuenta2, cta_contable)
            InsertarCuentas.insertar_SAMI(
                self, self.txtcuentaSAMI.get(), self.combobox.get(), self.cuenta2)

            cta_contable, cta_recuperacion = Form_Cuenta.formatear_cuentaContable(
                self, self.cuenta3)
            InsertarCuentas.inserta_A(self, self.cuenta3, 2024, 0, 0, self.txtCtaNombre3.get(
            ), self.cuentaPO3, cta_recuperacion, 1)
            InsertarCuentas.inserta_Contable(self, self.cuenta3, cta_contable)
            InsertarCuentas.insertar_SAMI(
                self, self.txtcuentaSAMI.get(), self.combobox.get(), self.cuenta3)

            cta_contable, cta_recuperacion = Form_Cuenta.formatear_cuentaContable(
                self, self.Cuenta4)
            InsertarCuentas.inserta_A(self, self.Cuenta4, 2024, 0, 0, self.txtCtaNombre4.get(
            ), self.cuentaPO4, cta_recuperacion, 1)
            InsertarCuentas.inserta_Contable(self, self.Cuenta4, cta_contable)
            InsertarCuentas.insertar_SAMI(
                self, self.txtcuentaSAMI.get(), self.combobox.get(), self.Cuenta4)
            print("Datos guardados")
        else:
            cuentaPO1 = self.txtCtaPO1.get().replace("-", "")
            InsertarCuentas.inserta_A(self, cuentaPO1, 2024, self.txtValorPO1.get(
            ), self.txtValorPO1.get(), self.txtCtaNombrePO1.get(), "", "11212209", 1)
            InsertarCuentas.inserta_Contable(self, cuentaPO1, "4-119-21")
            InsertarCuentas.insertar_SAMI(
                self, "12.5.99.02.30.00", 'Permiso para Operacion de Negocios', cuentaPO1)
            cuenta = self.txtCuenta1.get().replace("-", "")
            cta_contable, cta_recuperacion = Form_Cuenta.formatear_cuentaContable(
                self, cuenta)
            InsertarCuentas.inserta_A(
                self, cuenta, 2024, 0, 0, self.txtCtaNombre1.get(), cuentaPO1, cta_recuperacion, 0)
            InsertarCuentas.inserta_Contable(self, cuenta, cta_contable)
            InsertarCuentas.insertar_SAMI(
                self, self.txtcuentaSAMI.get(), self.combobox.get(), cuenta)

            print("Datos guardados")
        self.limpiarCamposTodo()

    def agregar_categorias(self):
        self.txtCuenta2.place(x=10, y=190, width=100, height=30)
        self.txtCuenta3.place(x=10, y=230, width=100, height=30)
        self.txtCuenta4.place(x=10, y=270, width=100, height=30)
        self.txtCtaNombre2.place(x=120, y=190, width=300, height=30)
        self.txtCtaNombre3.place(x=120, y=230, width=300, height=30)
        self.txtCtaNombre4.place(x=120, y=270, width=300, height=30)
        self.txtCtaPO2.place(x=430, y=190, width=100, height=30)
        self.txtCtaPO3.place(x=430, y=230, width=100, height=30)
        self.txtCtaPO4.place(x=430, y=270, width=100, height=30)
        self.txtCtaNombrePO2.place(x=540, y=190, width=400, height=30)
        self.txtCtaNombrePO3.place(x=540, y=230, width=400, height=30)
        self.txtCtaNombrePO4.place(x=540, y=270, width=400, height=30)
        self.txtValorPO2.place(x=950, y=190, width=100, height=30)
        self.txtValorPO3.place(x=950, y=230, width=100, height=30)
        self.txtValorPO4.place(x=950, y=270, width=100, height=30)

        self.limpiarCampos()
        if self.txtCuenta1:
            def procesar_cuenta(cuenta):
                if len(cuenta) == 10 or len(cuenta) == 11:
                    base = cuenta[:-2]  # '11111301'
                    auxiliar = cuenta[-2:]  # '01'
                    auxiliar_int = int(auxiliar)
                    nuevo_auxiliar = auxiliar_int + 1
                    # Mantener dos dígitos
                    nuevo_auxiliar_str = f"{nuevo_auxiliar:02d}"
                    nueva_cuenta = base + nuevo_auxiliar_str
                    return nueva_cuenta
                else:
                    return cuenta
            cuenta1 = self.txtCuenta1.get().replace("-", "")
            if len(cuenta1) == 8:

                self.txtCuenta2.insert(
                    0, Form_Cuenta.formatear_cuenta(self, cuenta1+"01"))
                self.txtCuenta3.insert(
                    0, Form_Cuenta.formatear_cuenta(self, cuenta1+"02"))
                self.txtCuenta4.insert(
                    0, Form_Cuenta.formatear_cuenta(self, cuenta1+"03"))
                self.Cuenta4 = self.txtCuenta4.get().replace("-", "")
            else:
                self.txtCuenta2.insert(0, self.txtCuenta1.get())
                self.cuenta2 = self.txtCuenta2.get().replace("-", "")
                self.txtCuenta3.insert(0, Form_Cuenta.formatear_cuenta(
                    self, procesar_cuenta(self.cuenta2)))
                self.cuenta3 = self.txtCuenta3.get().replace("-", "")
                self.txtCuenta4.insert(0, Form_Cuenta.formatear_cuenta(
                    self, procesar_cuenta(self.cuenta3)))
                self.Cuenta4 = self.txtCuenta4.get().replace("-", "")

            cuentaPO1 = self.txtctaUltimoPO.get().replace("-", "")
            if len(cuentaPO1) == 8:
                self.txtCtaPO2.insert(
                    0, Form_Cuenta.formatear_cuenta(self, cuentaPO1+"001"))
                self.txtCtaPO3.insert(
                    0, Form_Cuenta.formatear_cuenta(self, cuentaPO1+"002"))
                self.txtCtaPO4.insert(
                    0, Form_Cuenta.formatear_cuenta(self, cuentaPO1+"003"))
                self.cuentaPO4 = self.txtCtaPO4.get().replace("-", "")
            else:
                self.cuentaPO2 = self.txtctaUltimoPO.get().replace("-", "")
                self.txtCtaPO2.insert(0, Form_Cuenta.formatear_cuenta(
                    self, procesar_cuenta(self.cuentaPO2)))
                self.cuentaPO2 = self.txtCtaPO2.get().replace("-", "")
                self.txtCtaPO3.insert(0, Form_Cuenta.formatear_cuenta(
                    self, procesar_cuenta(self.cuentaPO2)))
                self.cuentaPO3 = self.txtCtaPO3.get().replace("-", "")
                self.txtCtaPO4.insert(0, Form_Cuenta.formatear_cuenta(
                    self, procesar_cuenta(self.cuentaPO3)))
                self.cuentaPO4 = self.txtCtaPO4.get().replace("-", "")

            self.txtCtaNombre2.insert(0, self.txtCtaNombre1.get() + " Cat. A")
            self.txtCtaNombre3.insert(0, self.txtCtaNombre1.get() + " Cat. B")
            self.txtCtaNombre4.insert(0, self.txtCtaNombre1.get() + " Cat. C")

            self.txtCtaNombrePO2.insert(0, "PO " + self.txtCtaNombre2.get())
            self.txtCtaNombrePO3.insert(0, "PO " + self.txtCtaNombre3.get())
            self.txtCtaNombrePO4.insert(0, "PO " + self.txtCtaNombre4.get())

    def remover_PO(self):
        self.txtCtaPO1.place_forget()
        self.txtCtaNombrePO1.place_forget()
        self.txtValorPO1.place_forget()

    def agregar_PO(self):
        self.txtCtaPO1.place(x=430, y=120, width=100, height=30)
        self.txtCtaNombrePO1.place(x=540, y=120, width=400, height=30)
        self.txtValorPO1.place(x=950, y=120, width=100, height=30)
        self.txtCtaNombrePO1.insert(0, "PO " + self.txtCtaNombre1.get())
        self.cuentaPO1 = self.txtctaUltimoPO.get().replace("-", "")
        self.txtCtaPO1.insert(0, Form_Cuenta.formatear_cuenta(
            self, Form_Cuenta.procesar_cuenta(self, self.cuentaPO1)))

    def limpiarCampos(self):
        self.txtCuenta2.delete(0, 100)
        self.txtCuenta3.delete(0, 100)
        self.txtCuenta4.delete(0, 100)
        self.txtCtaNombre2.delete(0, 100)
        self.txtCtaNombre3.delete(0, 100)
        self.txtCtaNombre4.delete(0, 100)
        self.txtCtaNombrePO2.delete(0, 100)
        self.txtCtaNombrePO3.delete(0, 100)
        self.txtCtaNombrePO4.delete(0, 100)
        self.txtValorPO2.delete(0, 100)
        self.txtValorPO3.delete(0, 100)
        self.txtValorPO4.delete(0, 100)
        self.txtCtaPO2.delete(0, 100)
        self.txtCtaPO3.delete(0, 100)
        self.txtCtaPO4.delete(0, 100)

    def limpiarCamposTodo(self):
        self.txtCuenta1.delete(0, 100)
        self.txtCuenta2.delete(0, 100)
        self.txtCuenta3.delete(0, 100)
        self.txtCuenta4.delete(0, 100)
        self.txtCtaNombre1.delete(0, 100)
        self.txtCtaNombre2.delete(0, 100)
        self.txtCtaNombre3.delete(0, 100)
        self.txtCtaNombre4.delete(0, 100)
        self.txtCtaNombrePO1.delete(0, 100)
        self.txtCtaNombrePO2.delete(0, 100)
        self.txtCtaNombrePO3.delete(0, 100)
        self.txtCtaNombrePO4.delete(0, 100)
        self.txtValorPO1.delete(0, 100)
        self.txtValorPO2.delete(0, 100)
        self.txtValorPO3.delete(0, 100)
        self.txtValorPO4.delete(0, 100)
        self.txtCtaPO1.delete(0, 100)
        self.txtCtaPO2.delete(0, 100)
        self.txtCtaPO3.delete(0, 100)
        self.txtCtaPO4.delete(0, 100)

    def limpiarPO(self):
        self.txtCtaNombrePO1.delete(0, 100)
        self.txtValorPO1.delete(0, 100)
        self.txtCtaPO1.delete(0, 100)


if __name__ == "__main__":
    root = Tk()
    root.wm_title = ("Cuentas")
    app = Aplicacion(root)
    app.mainloop()

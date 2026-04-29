import tkinter as tk
from tkinter import ttk, messagebox
import platform

# Importación de DAOs del equipo
from DAOempleado import DAOempleado
from DAOdepartamento import DAOdepartamento
from DAOproyecto import DAOproyecto
from DAORegistroTiempo import DAORegistroTiempo

# Importación de Clases de Negocio
from empleado import empleado
from departamentos import departamentos
from proyecto import proyecto
from registro_tiempo import RegistroTiempo

class EcoTechApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EcoTech Solutions - Sistema de Gestión")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")
        
        # Variables de sesión
        self.rol_actual = None
        self.usuario_conectado = None
        
        # Inicialización de DAOs
        self.dao_emp = DAOempleado()
        self.dao_depto = DAOdepartamento()
        self.dao_proy = DAOproyecto()
        self.dao_tiempo = DAORegistroTiempo()

        # Ocultar ventana principal hasta login
        self.withdraw()
        self.mostrar_login()

    def mostrar_login(self):
        self.login_win = tk.Toplevel(self)
        self.login_win.title("Acceso al Sistema")
        self.login_win.geometry("350x300")
        self.login_win.configure(bg="#1a1a1a")
        self.login_win.resizable(False, False)
        self.login_win.grab_set() # Bloquea interacción con otras ventanas

        tk.Label(self.login_win, text="ECOTECH SOLUTIONS", fg="#cc0000", bg="#1a1a1a", 
                 font=("Arial", 14, "bold")).pack(pady=20)
        
        tk.Label(self.login_win, text="Usuario:", fg="white", bg="#1a1a1a").pack()
        self.ent_user = tk.Entry(self.login_win, justify="center")
        self.ent_user.pack(pady=5)

        tk.Label(self.login_win, text="Contraseña:", fg="white", bg="#1a1a1a").pack()
        self.ent_pass = tk.Entry(self.login_win, show="*", justify="center")
        self.ent_pass.pack(pady=5)

        tk.Button(self.login_win, text="INGRESAR", bg="#cc0000", fg="white", width=15,
                  command=self.validar_acceso).pack(pady=20)

    def validar_acceso(self):
        user = self.ent_user.get()
        password = self.ent_pass.get()

        if user == "admin" and password == "admin123":
            self.rol_actual = "admin"
        elif user == "empleado" and password == "123":
            self.rol_actual = "empleado"
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            return

        self.login_win.destroy()
        self.deiconify() # Muestra ventana principal
        self.setup_ui()
        self.aplicar_restricciones()

    def setup_ui(self):
        # Panel Lateral
        self.sidebar = tk.Frame(self, bg="#1a1a1a", width=200)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="ECOTECH", fg="#cc0000", bg="#1a1a1a", 
                 font=("Arial", 16, "bold")).pack(pady=20)

        # Botones del Panel Lateral
        self.btn_emp = self.crear_btn_sidebar("👥 Empleados", self.show_empleados)
        self.btn_depto = self.crear_btn_sidebar("🏢 Departamentos", self.show_deptos)
        self.btn_proy = self.crear_btn_sidebar("📁 Proyectos", self.show_proyectos)
        self.btn_tiempo = self.crear_btn_sidebar("⏱ Registro Tiempo", self.show_tiempo)
        
        tk.Frame(self.sidebar, bg="#333333", height=2).pack(fill="x", pady=10)
        tk.Button(self.sidebar, text="🚪 Salir", bg="#1a1a1a", fg="white", border=0, 
                  command=self.quit).pack(side="bottom", fill="x", pady=10)

        # Área de Contenido
        self.main_content = tk.Frame(self, bg="white")
        self.main_content.pack(side="right", expand=True, fill="both")
        
        self.show_welcome()

    def crear_btn_sidebar(self, texto, comando):
        btn = tk.Button(self.sidebar, text=texto, bg="#1a1a1a", fg="white", 
                        font=("Arial", 10), border=0, anchor="w", padx=20, pady=10,
                        command=comando)
        btn.pack(fill="x")
        return btn

    def aplicar_restricciones(self):
        if self.rol_actual == "empleado":
            self.btn_emp.config(state="disabled")
            self.btn_depto.config(state="disabled")
            self.btn_proy.config(state="disabled")
            messagebox.showinfo("Modo Empleado", "Acceso limitado a Registro de Tiempo.")

    def show_welcome(self):
        self.limpiar_contenido()
        tk.Label(self.main_content, text=f"Bienvenido, {self.rol_actual.upper()}", 
                 font=("Arial", 20, "bold"), bg="white").pack(pady=50)
        tk.Label(self.main_content, text="Seleccione una opción del menú lateral", 
                 bg="white", fg="gray").pack()

    def limpiar_contenido(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    # --- SECCIÓN EMPLEADOS ---
    def show_empleados(self):
        self.limpiar_contenido()
        tk.Label(self.main_content, text="Gestión de Empleados", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        form = tk.Frame(self.main_content, bg="white", pady=10)
        form.pack()

        labels = ["Nombre:", "Dirección:", "Teléfono:", "Email:", "Fecha (AAAA-MM-DD):", "Salario:"]
        self.entries_emp = []
        for i, text in enumerate(labels):
            tk.Label(form, text=text, bg="white").grid(row=i, column=0, sticky="e", padx=5, pady=2)
            ent = tk.Entry(form, width=30)
            ent.grid(row=i, column=1, padx=5, pady=2)
            self.entries_emp.append(ent)

        tk.Button(form, text="Guardar Empleado", bg="#cc0000", fg="white", 
                  command=self.guardar_empleado).grid(row=6, columnspan=2, pady=10)

        # Tabla
        self.tree_emp = ttk.Treeview(self.main_content, columns=("ID", "Nombre", "Email", "Salario"), show="headings")
        self.tree_emp.heading("ID", text="ID")
        self.tree_emp.heading("Nombre", text="Nombre")
        self.tree_emp.heading("Email", text="Email")
        self.tree_emp.heading("Salario", text="Salario")
        self.tree_emp.pack(expand=True, fill="both", padx=10, pady=10)
        self.refresh_empleados()

    def guardar_empleado(self):
        datos = [e.get() for e in self.entries_emp]
        if "" in datos:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        try:
            nuevo = empleado(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])

            res = self.dao_emp.registrar(nuevo)
            messagebox.showinfo("Resultado", res)
            self.refresh_empleados()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el objeto empleado: {e}")

    def refresh_empleados(self):
        for i in self.tree_emp.get_children(): self.tree_emp.delete(i)
        for row in self.dao_emp.lista():
            # Cambiamos los números por los nombres de las columnas de tu MySQL
            self.tree_emp.insert("", "end", values=(
                row["idempleado"], 
                row["nombre"], 
                row["email"], 
                row["salario"]
            ))

    # --- SECCIÓN DEPARTAMENTOS ---
    def show_deptos(self):
        self.limpiar_contenido()
        tk.Label(self.main_content, text="Gestión de Departamentos", font=("Arial", 18, "bold"), bg="white").pack(pady=10)

        form = tk.Frame(self.main_content, bg="white", pady=10)
        form.pack()

        # Definimos los 4 campos necesarios
        labels = ["Nombre Depto:", "Descripción:", "Persona a Cargo:", "Cant. Personas:"]
        self.entries_depto = [] # Limpiamos la lista

        for i, text in enumerate(labels):
            tk.Label(form, text=text, bg="white").grid(row=i, column=0, sticky="e", padx=5, pady=2)
            ent = tk.Entry(form, width=30)
            ent.grid(row=i, column=1, padx=5, pady=2)
            self.entries_depto.append(ent) # Aquí se guardan los 4 cuadros de texto

        tk.Button(form, text="Guardar Departamento", bg="#cc0000", fg="white", 
                  command=self.guardar_depto).grid(row=4, columnspan=2, pady=10)

        # Tabla de Departamentos (Treeview)
        self.tree_depto = ttk.Treeview(self.main_content, columns=("ID", "Nombre", "Cargo"), show="headings")
        self.tree_depto.heading("ID", text="ID")
        self.tree_depto.heading("Nombre", text="Departamento")
        self.tree_depto.heading("Cargo", text="Encargado")
        self.tree_depto.pack(expand=True, fill="both", padx=10, pady=10)
        self.refresh_departamentos()

    def guardar_depto(self):
        # Obtenemos los textos de los 4 cuadros
        datos = [e.get() for e in self.entries_depto]


        if len(datos) < 4:
            messagebox.showerror("Error", "El formulario no se cargó correctamente.")
            return

        if "" in datos:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        try:
            # nombre, descripcion, personacargo, cantidadpersonas
            nuevo = departamentos(datos[0], datos[1], datos[2], int(datos[3]))

            res = self.dao_depto.registrar(nuevo)
            messagebox.showinfo("Resultado", res)
            self.refresh_departamentos()
        except ValueError:
            messagebox.showerror("Error", "En 'Cant. Personas' debes ingresar un número.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema: {e}")

    def refresh_departamentos(self):
        for i in self.tree_depto.get_children(): self.tree_depto.delete(i)
        lista = self.dao_depto.lista()
        for row in lista:
            # Usamos los nombres de las columnas de tu MySQL
            self.tree_depto.insert("", "end", values=(
                row["iddepartamento"], 
                row["nombre"], 
                row["personacargo"], 
                row["cantidadpersonas"]
            ))

    # --- SECCIÓN PROYECTOS ---
    def show_proyectos(self):
        self.limpiar_contenido()
        tk.Label(self.main_content, text="Gestión de Proyectos", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        form = tk.Frame(self.main_content, bg="white", pady=10)
        form.pack()

        labels = ["Nombre Proyecto:", "Descripción:", "Fecha Inicio (AAAA-MM-DD):"]
        self.entries_proy = []
        for i, text in enumerate(labels):
            tk.Label(form, text=text, bg="white").grid(row=i, column=0, sticky="e", padx=5, pady=2)
            ent = tk.Entry(form, width=30)
            ent.grid(row=i, column=1, padx=5, pady=2)
            self.entries_proy.append(ent)

        tk.Button(form, text="Guardar Proyecto", bg="#cc0000", fg="white", 
                  command=self.guardar_proyecto).grid(row=3, columnspan=2, pady=10)

        # Tabla de Proyectos
        self.tree_proy = ttk.Treeview(self.main_content, columns=("ID", "Nombre", "Fecha"), show="headings")
        self.tree_proy.heading("ID", text="ID")
        self.tree_proy.heading("Nombre", text="Nombre Proyecto")
        self.tree_proy.heading("Fecha", text="Fecha Inicio")
        self.tree_proy.pack(expand=True, fill="both", padx=10, pady=10)
        self.refresh_proyectos()

    def guardar_proyecto(self):
        datos = [e.get() for e in self.entries_proy]
        if "" in datos:
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return
        
        from proyecto import Proyecto # Asegúrate que la clase empiece con Mayúscula
        nuevo = Proyecto()
        nuevo.set_nombre(datos[0])
        nuevo.set_descripcion(datos[1])
        nuevo.set_fecha_inicio(datos[2])
        
        res = self.dao_proy.registrar(nuevo)
        messagebox.showinfo("Resultado", res)
        self.refresh_proyectos()

    def refresh_proyectos(self):
        for i in self.tree_proy.get_children(): self.tree_proy.delete(i)
        for row in self.dao_proy.lista():
            self.tree_proy.insert("", "end", values=(
                row["idproyecto"], 
                row["nombre"], 
                row["fecha_inicio"]
            ))

    # --- SECCIÓN REGISTRO DE TIEMPO ---
    def show_tiempo(self):
        self.limpiar_contenido()
        tk.Label(self.main_content, text="Registro de Horas Trabajadas", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        form = tk.Frame(self.main_content, bg="white")
        form.pack(pady=10)

        tk.Label(form, text="Nombre Empleado:", bg="white").grid(row=0, column=0)
        self.ent_t_emp = tk.Entry(form); self.ent_t_emp.grid(row=0, column=1)
        
        tk.Label(form, text="Nombre Proyecto:", bg="white").grid(row=1, column=0)
        self.ent_t_proy = tk.Entry(form); self.ent_t_proy.grid(row=1, column=1)
        
        tk.Label(form, text="Horas:", bg="white").grid(row=2, column=0)
        self.ent_t_hrs = tk.Entry(form); self.ent_t_hrs.grid(row=2, column=1)

        tk.Button(form, text="Registrar Horas", bg="#cc0000", fg="white", 
                  command=self.guardar_tiempo).grid(row=3, columnspan=2, pady=10)

    def guardar_tiempo(self):
        emp_nom = self.ent_t_emp.get()
        proy_nom = self.ent_t_proy.get()
        hrs = self.ent_t_hrs.get()
        
        # Validar contra base de datos
        lista_e = self.dao_emp.lista()
        lista_p = self.dao_proy.lista()
        
        nuevo_reg = RegistroTiempo()
        nuevo_reg.set_id_empleado(emp_nom)
        nuevo_reg.set_id_proyecto(proy_nom)
        nuevo_reg.set_horas_trabajadas(hrs)
        
        res = self.dao_tiempo.registrar(nuevo_reg, lista_e, lista_p)
        messagebox.showinfo("Registro de Tiempo", res)

if __name__ == "__main__":
    app = EcoTechApp()
    app.mainloop()

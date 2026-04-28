import tkinter as tk
from tkinter import ttk, messagebox
from DAOempleado import DAOempleado
from empleado import empleado
from DAOdepartamento import DAOdepartamento
from departamentos import departamentos
from DAOproyecto import DAOproyecto
from proyecto import proyecto
from DAORegistroTiempo import DAORegistroTiempo
from registro_tiempo import RegistroTiempo

dao_emp = DAOempleado()
dao_dep = DAOdepartamento()
dao_proy = DAOproyecto()
dao_tiempo = DAORegistroTiempo()

class SistemaGestionEcoTech:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoTech Solutions - Sistema de Gestión")
        self.root.geometry("700x600")
        self.root.configure(bg="#1a1a1a")
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.crear_menu_principal()
    
    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def crear_menu_principal(self):
        self.limpiar_ventana()
        

        frame_header = tk.Frame(self.root, bg="#cc0000", height=100)
        frame_header.pack(fill=tk.X)
        
        tk.Label(frame_header, text="ECOTECH SOLUTIONS", bg="#cc0000", fg="white", 
                 font=("Arial", 24, "bold"), pady=30).pack()
        
        frame_main = tk.Frame(self.root, bg="#1a1a1a")
        frame_main.pack(expand=True, fill=tk.BOTH)
        
        tk.Label(frame_main, text="PANEL DE ADMINISTRACIÓN", bg="#1a1a1a", fg="#ffffff", 
                 font=("Arial", 14, "bold")).pack(pady=20)
        
        opciones = [
            ("👥 GESTIÓN DE EMPLEADOS", self.menu_empleados),
            ("🏢 GESTIÓN DE DEPARTAMENTOS", self.menu_departamentos),
            ("📁 GESTIÓN DE PROYECTOS", self.menu_proyectos),
            ("⏱️ REGISTRO DE TIEMPO", self.menu_registro_tiempo),
            ("🚪 SALIR", self.root.quit)
        ]
        
        for texto, comando in opciones:
            btn = tk.Button(frame_main, text=texto, command=comando, width=35, height=2,
                          bg="#cc0000", fg="white", font=("Arial", 11, "bold"),
                          highlightbackground="#1a1a1a") # Necesario para Mac
            btn.pack(pady=10)

    def menu_empleados(self):
        self.limpiar_ventana()
        self.header_secundario("GESTIÓN DE EMPLEADOS")
        
        frame_body = tk.Frame(self.root, bg="#1a1a1a")
        frame_body.pack(expand=True)
        
        tk.Button(frame_body, text="Registrar Nuevo Empleado", command=self.form_empleado, 
                 width=30, height=2, bg="#cc0000", fg="white", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Ver Lista de Empleados", command=self.listar_empleados, 
                 width=30, height=2, bg="white", fg="black", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Volver al Menú", command=self.crear_menu_principal, 
                 width=30, height=2, bg="#333333", fg="white", font=("Arial", 11), highlightbackground="#1a1a1a").pack(pady=20)

    def form_empleado(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Nuevo Empleado")
        ventana.geometry("500x500")
        ventana.configure(bg="white")
        ventana.lift()
        ventana.focus_force()
        
        tk.Label(ventana, text="DATOS DEL EMPLEADO", bg="#cc0000", fg="white", font=("Arial", 14, "bold"), pady=15).pack(fill=tk.X)
        
        container = tk.Frame(ventana, bg="white", padx=40, pady=30)
        container.pack(fill=tk.BOTH, expand=True)
        
        campos = ["Nombre", "Dirección", "Teléfono", "Email", "Fecha Inicio", "Salario"]
        entradas = {}
        
        for i, campo in enumerate(campos):
            lbl = tk.Label(container, text=campo + ":", bg="white", fg="black", font=("Arial", 11, "bold"), anchor="w")
            lbl.grid(row=i, column=0, pady=10, sticky="w")
            
            ent = tk.Entry(container, font=("Arial", 11), bg="#f0f0f0", fg="black", width=25, highlightthickness=1)
            ent.grid(row=i, column=1, pady=10, padx=10, sticky="ew")
            entradas[campo] = ent

        def guardar():
            try:
                n, d, t, e, f, s = [entradas[c].get() for c in campos]
                if not all([n, d, t, e, f, s]):
                    messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
                    return
                nuevo = empleado(n, d, t, e, f, float(s))
                res = dao_emp.registrar(nuevo)
                messagebox.showinfo("Sistema", res)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "El salario debe ser un número.")

        btn_guardar = tk.Button(ventana, text="GUARDAR REGISTRO", command=guardar, bg="#cc0000", fg="white", font=("Arial", 12, "bold"), pady=10, highlightbackground="white")
        btn_guardar.pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=20)

    def menu_departamentos(self):
        self.limpiar_ventana()
        self.header_secundario("GESTIÓN DE DEPARTAMENTOS")
        frame_body = tk.Frame(self.root, bg="#1a1a1a")
        frame_body.pack(expand=True)
        tk.Button(frame_body, text="Crear Departamento", command=self.form_departamento, width=30, height=2, bg="#cc0000", fg="white", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Ver Departamentos", command=self.listar_departamentos, width=30, height=2, bg="white", fg="black", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Volver", command=self.crear_menu_principal, width=30, height=2, bg="#333333", fg="white", font=("Arial", 11), highlightbackground="#1a1a1a").pack(pady=20)

    def form_departamento(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Nuevo Departamento")
        ventana.geometry("500x400")
        ventana.configure(bg="white")
        tk.Label(ventana, text="DATOS DEL DEPARTAMENTO", bg="#cc0000", fg="white", font=("Arial", 14, "bold"), pady=15).pack(fill=tk.X)
        container = tk.Frame(ventana, bg="white", padx=40, pady=30)
        container.pack(fill=tk.BOTH, expand=True)
        campos = ["Nombre", "Descripción", "Gerente", "Cant. Personas"]
        entradas = {}
        for i, campo in enumerate(campos):
            tk.Label(container, text=campo + ":", bg="white", fg="black", font=("Arial", 11, "bold")).grid(row=i, column=0, pady=10, sticky="w")
            ent = tk.Entry(container, font=("Arial", 11), bg="#f0f0f0", fg="black", width=25)
            ent.grid(row=i, column=1, pady=10, padx=10)
            entradas[campo] = ent
        def guardar():
            try:
                n, d, g, c = [entradas[ca].get() for ca in campos]
                if not all([n, d, g, c]):
                    messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
                    return
                nuevo = departamentos(n, d, g, int(c))
                res = dao_dep.registrar(nuevo)
                messagebox.showinfo("Sistema", res)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        tk.Button(ventana, text="GUARDAR DEPARTAMENTO", command=guardar, bg="#cc0000", fg="white", font=("Arial", 12, "bold"), pady=10, highlightbackground="white").pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=20)

    def menu_proyectos(self):
        self.limpiar_ventana()
        self.header_secundario("GESTIÓN DE PROYECTOS")
        frame_body = tk.Frame(self.root, bg="#1a1a1a")
        frame_body.pack(expand=True)
        tk.Button(frame_body, text="Nuevo Proyecto", command=self.form_proyecto, width=30, height=2, bg="#cc0000", fg="white", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Ver Proyectos", command=self.listar_proyectos, width=30, height=2, bg="white", fg="black", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Volver", command=self.crear_menu_principal, width=30, height=2, bg="#333333", fg="white", font=("Arial", 11), highlightbackground="#1a1a1a").pack(pady=20)

    def form_proyecto(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Nuevo Proyecto")
        ventana.geometry("500x350")
        ventana.configure(bg="white")
        tk.Label(ventana, text="DATOS DEL PROYECTO", bg="#cc0000", fg="white", font=("Arial", 14, "bold"), pady=15).pack(fill=tk.X)
        container = tk.Frame(ventana, bg="white", padx=40, pady=30)
        container.pack(fill=tk.BOTH, expand=True)
        campos = ["Nombre", "Descripción", "Fecha Inicio"]
        entradas = {}
        for i, campo in enumerate(campos):
            tk.Label(container, text=campo + ":", bg="white", fg="black", font=("Arial", 11, "bold")).grid(row=i, column=0, pady=10, sticky="w")
            ent = tk.Entry(container, font=("Arial", 11), bg="#f0f0f0", fg="black", width=25)
            ent.grid(row=i, column=1, pady=10, padx=10)
            entradas[campo] = ent
        def guardar():
            n, d, f = [entradas[ca].get() for ca in campos]
            if not all([n, d, f]):
                messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
                return
            nuevo = proyecto(n, d, f)
            res = dao_proy.registrar(nuevo)
            messagebox.showinfo("Sistema", res)
            ventana.destroy()
        tk.Button(ventana, text="GUARDAR PROYECTO", command=guardar, bg="#cc0000", fg="white", font=("Arial", 12, "bold"), pady=10, highlightbackground="white").pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=20)


    def menu_registro_tiempo(self):
        self.limpiar_ventana()
        self.header_secundario("REGISTRO DE TIEMPO")
        frame_body = tk.Frame(self.root, bg="#1a1a1a")
        frame_body.pack(expand=True)
        tk.Button(frame_body, text="Registrar Horas", command=self.form_tiempo, width=30, height=2, bg="#cc0000", fg="white", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Ver Historial", command=self.listar_tiempos, width=30, height=2, bg="white", fg="black", font=("Arial", 11, "bold"), highlightbackground="#1a1a1a").pack(pady=10)
        tk.Button(frame_body, text="Volver", command=self.crear_menu_principal, width=30, height=2, bg="#333333", fg="white", font=("Arial", 11), highlightbackground="#1a1a1a").pack(pady=20)

    def form_tiempo(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Horas")
        ventana.geometry("500x450")
        ventana.configure(bg="white")
        tk.Label(ventana, text="REGISTRO DE HORAS", bg="#cc0000", fg="white", font=("Arial", 14, "bold"), pady=15).pack(fill=tk.X)
        container = tk.Frame(ventana, bg="white", padx=40, pady=30)
        container.pack(fill=tk.BOTH, expand=True)
        campos = ["Empleado", "Proyecto", "Fecha", "Horas", "Descripción"]
        entradas = {}
        for i, campo in enumerate(campos):
            tk.Label(container, text=campo + ":", bg="white", fg="black", font=("Arial", 11, "bold")).grid(row=i, column=0, pady=10, sticky="w")
            ent = tk.Entry(container, font=("Arial", 11), bg="#f0f0f0", fg="black", width=25)
            ent.grid(row=i, column=1, pady=10, padx=10)
            entradas[campo] = ent
        def guardar():
            try:
                e, p, f, h, d = [entradas[ca].get() for ca in campos]
                if not all([e, p, f, h, d]):
                    messagebox.showwarning("Atención", "Todos los campos son obligatorios.")
                    return
                nuevo = RegistroTiempo(e, p, f, float(h), d)
                res = dao_tiempo.registrar(nuevo, dao_emp.lista(), dao_proy.lista())
                messagebox.showinfo("Sistema", res)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Las horas deben ser un número.")
        tk.Button(ventana, text="GUARDAR REGISTRO", command=guardar, bg="#cc0000", fg="white", font=("Arial", 12, "bold"), pady=10, highlightbackground="white").pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=20)


    def listar_empleados(self):
        self.ventana_lista("LISTA DE EMPLEADOS", ("ID", "Nombre", "Direccion", "Teléfono", "Email", "Salario"), dao_emp.lista())

    def listar_departamentos(self):
        self.ventana_lista("LISTA DE DEPARTAMENTOS", ("ID", "Nombre", "Descripción", "Gerente", "Personas"), dao_dep.lista())

    def listar_proyectos(self):
        self.ventana_lista("LISTA DE PROYECTOS", ("ID", "Nombre", "Descripción", "Inicio"), dao_proy.lista())

    def listar_tiempos(self):
        datos = [(r.get_id_empleado(), r.get_id_proyecto(), r.get_fecha(), r.get_horas_trabajadas(), r.get_descripcion()) for r in dao_tiempo.listar()]
        self.ventana_lista("HISTORIAL DE TIEMPO", ("Empleado", "Proyecto", "Fecha", "Horas", "Tarea"), datos)

    def ventana_lista(self, titulo, columnas, datos):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("800x400")
        tk.Label(ventana, text=titulo, bg="#cc0000", fg="white", font=("Arial", 12, "bold"), pady=10).pack(fill=tk.X)
        tree = ttk.Treeview(ventana, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        for d in datos:
            tree.insert("", tk.END, values=d)
        tree.pack(fill=tk.BOTH, expand=True)

    def header_secundario(self, titulo):
        frame_h = tk.Frame(self.root, bg="#cc0000", height=60)
        frame_h.pack(fill=tk.X)
        tk.Label(frame_h, text=titulo, bg="#cc0000", fg="white", font=("Arial", 16, "bold"), pady=20).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaGestionEcoTech(root)
    root.mainloop()

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

class EcoTechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EcoTech Solutions")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        # Estilos para las tablas
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background="#ffffff", foreground="#000000", fieldbackground="#ffffff", font=("Arial", 10))
        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#cc0000", foreground="white")
        self.style.map("Treeview", background=[('selected', '#cc0000')])

        # --- ESTRUCTURA PRINCIPAL (Ventana Única) ---
        
        # 1. Panel Lateral (Menú de navegación)
        self.sidebar = tk.Frame(self.root, bg="#1a1a1a", width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False) # Evita que se encoja
        
        # Logo/Título en Sidebar
        tk.Label(self.sidebar, text="ECOTECH", bg="#1a1a1a", fg="#cc0000", font=("Arial", 20, "bold"), pady=20).pack()
        tk.Label(self.sidebar, text="Solutions", bg="#1a1a1a", fg="white", font=("Arial", 12)).pack()
        
        tk.Frame(self.sidebar, bg="#333333", height=2).pack(fill=tk.X, pady=20)

        # Botones del Sidebar
        self.crear_boton_sidebar("👥 Empleados", self.show_empleados)
        self.crear_boton_sidebar("🏢 Departamentos", self.show_departamentos)
        self.crear_boton_sidebar("📁 Proyectos", self.show_proyectos)
        self.crear_boton_sidebar("⏱️ Registro de Tiempo", self.show_tiempo)
        
        tk.Frame(self.sidebar, bg="#1a1a1a").pack(expand=True) # Espaciador
        
        self.crear_boton_sidebar("🚪 Salir", self.root.quit, color="#333333")

        # 2. Área de Contenido Principal
        self.main_content = tk.Frame(self.root, bg="white")
        self.main_content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Mostrar bienvenida al inicio
        self.show_welcome()

    def crear_boton_sidebar(self, texto, comando, color="#1a1a1a"):
        btn = tk.Button(self.sidebar, text=texto, command=comando, 
                      bg=color, fg="white", font=("Arial", 11, "bold"),
                      relief=tk.FLAT, pady=15, cursor="hand2", 
                      activebackground="#cc0000", activeforeground="white",
                      highlightbackground="#1a1a1a", anchor="w", padx=20)
        btn.pack(fill=tk.X)

    def clear_main(self):
        """Limpia el área de contenido principal."""
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_main()
        tk.Label(self.main_content, text="Bienvenido al Sistema de Gestión", bg="white", fg="#333333", font=("Arial", 22, "bold"), pady=50).pack()
        tk.Label(self.main_content, text="Seleccione una opción del menú lateral para comenzar.", bg="white", fg="#666666", font=("Arial", 14)).pack()
        
        # Imagen decorativa o logo grande
        tk.Label(self.main_content, text="🏢", bg="white", font=("Arial", 100)).pack(pady=50)

    # --- SECCIÓN EMPLEADOS ---
    def show_empleados(self):
        self.clear_main()
        self.header_seccion("Gestión de Empleados")
        
        # Panel superior: Formulario
        form_frame = tk.LabelFrame(self.main_content, text=" Registrar Nuevo Empleado ", bg="white", font=("Arial", 10, "bold"), padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)
        
        campos = ["Nombre", "Dirección", "Teléfono", "Email", "Fecha Inicio", "Salario"]
        self.ents_emp = {}
        
        # Grid para el formulario (2 columnas)
        for i, campo in enumerate(campos):
            r, c = i // 3, (i % 3) * 2
            tk.Label(form_frame, text=campo + ":", bg="white", font=("Arial", 10)).grid(row=r, column=c, sticky="w", pady=5, padx=5)
            ent = tk.Entry(form_frame, width=20, bg="#f9f9f9")
            ent.grid(row=r, column=c+1, pady=5, padx=5)
            self.ents_emp[campo] = ent
            
        tk.Button(form_frame, text="Guardar Empleado", bg="#cc0000", fg="white", font=("Arial", 10, "bold"), 
                 command=self.save_empleado, padx=20, highlightbackground="white").grid(row=2, column=0, columnspan=6, pady=15)

        # Panel inferior: Lista
        list_frame = tk.Frame(self.main_content, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        cols = ("ID", "Nombre", "Dirección", "Teléfono", "Email", "Salario")
        self.tree_emp = ttk.Treeview(list_frame, columns=cols, show="headings")
        for col in cols:
            self.tree_emp.heading(col, text=col)
            self.tree_emp.column(col, width=100)
        
        self.tree_emp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scroll = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree_emp.yview)
        self.tree_emp.configure(yscroll=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.refresh_empleados()

    def save_empleado(self):
        try:
            data = {c: self.ents_emp[c].get() for c in self.ents_emp}
            if not all(data.values()):
                messagebox.showwarning("Aviso", "Todos los campos son obligatorios.")
                return
            nuevo = empleado(data["Nombre"], data["Dirección"], data["Teléfono"], data["Email"], data["Fecha Inicio"], float(data["Salario"]))
            res = dao_emp.registrar(nuevo)
            messagebox.showinfo("Éxito", res)
            self.refresh_empleados()
            for e in self.ents_emp.values(): e.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "El salario debe ser un número.")

    def refresh_empleados(self):
        for item in self.tree_emp.get_children(): self.tree_emp.delete(item)
        for d in dao_emp.lista(): self.tree_emp.insert("", tk.END, values=d)

    # --- SECCIÓN DEPARTAMENTOS ---
    def show_departamentos(self):
        self.clear_main()
        self.header_seccion("Gestión de Departamentos")
        
        form_frame = tk.LabelFrame(self.main_content, text=" Crear Departamento ", bg="white", font=("Arial", 10, "bold"), padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)
        
        campos = ["Nombre", "Descripción", "Gerente", "Cant. Personas"]
        self.ents_dep = {}
        for i, campo in enumerate(campos):
            tk.Label(form_frame, text=campo + ":", bg="white").grid(row=0, column=i*2, padx=5, pady=5)
            ent = tk.Entry(form_frame, width=15, bg="#f9f9f9")
            ent.grid(row=0, column=i*2+1, padx=5, pady=5)
            self.ents_dep[campo] = ent
            
        tk.Button(form_frame, text="Crear", bg="#cc0000", fg="white", command=self.save_dep, highlightbackground="white").grid(row=1, column=0, columnspan=8, pady=10)

        list_frame = tk.Frame(self.main_content, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        cols = ("ID", "Nombre", "Descripción", "Gerente", "Personas")
        self.tree_dep = ttk.Treeview(list_frame, columns=cols, show="headings")
        for col in cols: self.tree_dep.heading(col, text=col); self.tree_dep.column(col, width=120)
        self.tree_dep.pack(fill=tk.BOTH, expand=True)
        self.refresh_dep()

    def save_dep(self):
        try:
            d = {c: self.ents_dep[c].get() for c in self.ents_dep}
            if not all(d.values()): return
            nuevo = departamentos(d["Nombre"], d["Descripción"], d["Gerente"], int(d["Cant. Personas"]))
            dao_dep.registrar(nuevo)
            self.refresh_dep()
            for e in self.ents_dep.values(): e.delete(0, tk.END)
        except: messagebox.showerror("Error", "Dato inválido")

    def refresh_dep(self):
        for item in self.tree_dep.get_children(): self.tree_dep.delete(item)
        for d in dao_dep.lista(): self.tree_dep.insert("", tk.END, values=d)

    # --- SECCIÓN PROYECTOS ---
    def show_proyectos(self):
        self.clear_main()
        self.header_seccion("Gestión de Proyectos")
        
        form_frame = tk.LabelFrame(self.main_content, text=" Nuevo Proyecto ", bg="white", font=("Arial", 10, "bold"), padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)
        
        campos = ["Nombre", "Descripción", "Fecha Inicio"]
        self.ents_proy = {}
        for i, campo in enumerate(campos):
            tk.Label(form_frame, text=campo + ":", bg="white").grid(row=0, column=i*2, padx=5, pady=5)
            ent = tk.Entry(form_frame, width=20, bg="#f9f9f9")
            ent.grid(row=0, column=i*2+1, padx=5, pady=5)
            self.ents_proy[campo] = ent
        
        tk.Button(form_frame, text="Guardar Proyecto", bg="#cc0000", fg="white", command=self.save_proy, highlightbackground="white").grid(row=1, column=0, columnspan=6, pady=10)

        list_frame = tk.Frame(self.main_content, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        cols = ("ID", "Nombre", "Descripción", "Inicio")
        self.tree_proy = ttk.Treeview(list_frame, columns=cols, show="headings")
        for col in cols: self.tree_proy.heading(col, text=col); self.tree_proy.column(col, width=150)
        self.tree_proy.pack(fill=tk.BOTH, expand=True)
        self.refresh_proy()

    def save_proy(self):
        d = {c: self.ents_proy[c].get() for c in self.ents_proy}
        if not all(d.values()): return
        nuevo = proyecto(d["Nombre"], d["Descripción"], d["Fecha Inicio"])
        dao_proy.registrar(nuevo)
        self.refresh_proy()
        for e in self.ents_proy.values(): e.delete(0, tk.END)

    def refresh_proy(self):
        for item in self.tree_proy.get_children(): self.tree_proy.delete(item)
        for d in dao_proy.lista(): self.tree_proy.insert("", tk.END, values=d)

    # --- SECCIÓN REGISTRO TIEMPO ---
    def show_tiempo(self):
        self.clear_main()
        self.header_seccion("Registro de Tiempo")
        
        form_frame = tk.LabelFrame(self.main_content, text=" Registrar Horas ", bg="white", font=("Arial", 10, "bold"), padx=20, pady=20)
        form_frame.pack(fill=tk.X, padx=20, pady=10)
        
        campos = ["Empleado", "Proyecto", "Fecha", "Horas", "Descripción"]
        self.ents_t = {}
        for i, campo in enumerate(campos):
            tk.Label(form_frame, text=campo + ":", bg="white").grid(row=0, column=i*2, padx=5, pady=5)
            ent = tk.Entry(form_frame, width=12, bg="#f9f9f9")
            ent.grid(row=0, column=i*2+1, padx=5, pady=5)
            self.ents_t[campo] = ent
            
        tk.Button(form_frame, text="Registrar", bg="#cc0000", fg="white", command=self.save_tiempo, highlightbackground="white").grid(row=1, column=0, columnspan=10, pady=10)

        list_frame = tk.Frame(self.main_content, bg="white")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        cols = ("Empleado", "Proyecto", "Fecha", "Horas", "Tarea")
        self.tree_t = ttk.Treeview(list_frame, columns=cols, show="headings")
        for col in cols: self.tree_t.heading(col, text=col); self.tree_t.column(col, width=130)
        self.tree_t.pack(fill=tk.BOTH, expand=True)
        self.refresh_tiempo()

    def save_tiempo(self):
        try:
            d = {c: self.ents_t[c].get() for c in self.ents_t}
            if not all(d.values()): return
            nuevo = RegistroTiempo(d["Empleado"], d["Proyecto"], d["Fecha"], float(d["Horas"]), d["Descripción"])
            res = dao_tiempo.registrar(nuevo, dao_emp.lista(), dao_proy.lista())
            messagebox.showinfo("Info", res)
            self.refresh_tiempo()
            for e in self.ents_t.values(): e.delete(0, tk.END)
        except: messagebox.showerror("Error", "Dato inválido")

    def refresh_tiempo(self):
        for item in self.tree_t.get_children(): self.tree_t.delete(item)
        for r in dao_tiempo.listar():
            self.tree_t.insert("", tk.END, values=(r.get_id_empleado(), r.get_id_proyecto(), r.get_fecha(), r.get_horas_trabajadas(), r.get_descripcion()))

    # --- UTILIDADES ---
    def header_seccion(self, titulo):
        f = tk.Frame(self.main_content, bg="white", pady=20)
        f.pack(fill=tk.X)
        tk.Label(f, text=titulo, bg="white", fg="#333333", font=("Arial", 18, "bold"), padx=20).pack(side=tk.LEFT)
        tk.Frame(self.main_content, bg="#eeeeee", height=1).pack(fill=tk.X, padx=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = EcoTechApp(root)
    root.mainloop()

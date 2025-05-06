import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f8ff')
        
        self.fuente_titulo = Font(family='Helvetica', size=16, weight='bold')
        self.fuente_normal = Font(family='Arial', size=11)
        self.fuente_botones = Font(family='Arial', size=10, weight='bold')
        
        self.tareas = []
        self.configurar_estilos()
        self.crear_widgets()

    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('Titulo.TLabel', 
                        font=self.fuente_titulo, 
                        background='#f0f8ff', 
                        foreground='#2c3e50')

        style.configure('Boton.TButton', 
                        font=self.fuente_botones,
                        padding=8,
                        foreground='white',
                        background='#3498db')

        style.map('Boton.TButton',
                  background=[('active', '#2980b9')])

        style.configure('Lista.TFrame', 
                        background='white',
                        relief='sunken',
                        borderwidth=2)

    def crear_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        titulo = ttk.Label(main_frame, text="Task Manager", style='Titulo.TLabel')
        titulo.pack(pady=(0, 15))

        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)

        self.entrada_tarea = ttk.Entry(input_frame, font=self.fuente_normal, width=40)
        self.entrada_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        btn_agregar = ttk.Button(input_frame, text="➕ Agregar", style='Boton.TButton', command=self.agregar_tarea)
        btn_agregar.pack(side=tk.LEFT)

        lista_frame = ttk.Frame(main_frame, style='Lista.TFrame')
        lista_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        scrollbar = ttk.Scrollbar(lista_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(
            lista_frame,
            font=self.fuente_normal,
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50',
            selectbackground='#3498db',
            selectforeground='white',
            borderwidth=0,
            highlightthickness=0
        )
        self.lista_tareas.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_tareas.yview)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)

        btn_completar = ttk.Button(btn_frame, text="✔️ Completar", style='Boton.TButton', command=self.marcar_completada)
        btn_completar.pack(side=tk.LEFT, expand=True, padx=5)

        btn_eliminar = ttk.Button(btn_frame, text="🗑️ Eliminar", style='Boton.TButton', command=self.eliminar_tarea)
        btn_eliminar.pack(side=tk.LEFT, expand=True, padx=5)

        btn_limpiar = ttk.Button(btn_frame, text="🧹 Limpiar completadas", style='Boton.TButton', command=self.limpiar_completadas)
        btn_limpiar.pack(side=tk.LEFT, expand=True, padx=5)

        self.actualizar_lista_tareas()
        self.entrada_tarea.focus_set()

    def agregar_tarea(self):
        nueva_tarea = self.entrada_tarea.get().strip()
        if nueva_tarea:
            self.tareas.append(nueva_tarea)
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea antes de agregar.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            idx = seleccion[0]
            tarea = self.tareas[idx]
            if not tarea.startswith("✔️ "):
                self.tareas[idx] = "✔️ " + tarea
                self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            idx = seleccion[0]
            del self.tareas[idx]
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

    def limpiar_completadas(self):
        self.tareas = [t for t in self.tareas if not t.startswith("✔️ ")]
        self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea)


# Bloque principal que ejecuta la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()

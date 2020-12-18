# Practica Guiada CRUD

# PRACTICA GUIADA CRUD

########  Funciones
from tkinter import *
from tkinter import messagebox
import sqlite3

def conectionBBDD():
    #Crear la base de datos Usuarios
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE DATO_USUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			CEDULA_USUARIO VARCHAR(50),
			NOMBRE_USUARIO VARCHAR(50),
			APELLIDO_USUARIO VARCHAR(10),
			PASSWORD VARCHAR(50),
			DIRECCION_USUARIO VARCHAR(50),
			COMENTARIOS VARCHAR(100))

			''')

		messagebox.showinfo("BBDD","Base de datos creada con exito")

	except:

		messagebox.showwarning("¡Atención!", "La base de datos ya existe")

 
def salirAplicacion():

	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

	if valor=="yes":
		root.destroy()

def limpiarCampos():

	miNombre.set("")
	miCedula.set("")
	miDireccion.set("")
	miID.set("")
	miApellido.set("")
	miPass.set("")
	texto_comentario.delete(1.0,END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	#instruccion sql

	miCursor.execute("INSERT INTO DATO_USUARIOS VALUES(NULL,'" + miCedula.get() +
		"','" + miNombre.get() +
		"','" + miApellido.get() +
		"','" + miPass.get() + 
		"','" + miDireccion.get() +
		"','" + texto_comentario.get("1.0", END)+ "')")

	miConexion.commit()

	messagebox.showinfo("Base de Datos","Registro insertado con éxito")

def leer():

	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATO_USUARIOS WHERE ID=" + miID.get())

	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:

		miID.set(usuario[0])
		miCedula.set(usuario[1])
		miNombre.set(usuario[2])
		miApellido.set(usuario[3])
		miPass.set(usuario[4])
		miDireccion.set(usuario[5])
		texto_comentario.insert(1.0,usuario[6])
	miConexion.commit()

def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE DATO_USUARIOS SET NOMBRE_USUARIO='" + miCedula.get() +
		"', NOMBRE='" + miNombre.get() +
		"', APELLIDO='" + miApellido.get() +
		"', PASSWORD='" + miPass.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + texto_comentario.get("1.0", END) +
		"' WHERE ID =" + miID.get())

	miConexion.commit()
	messagebox.showinfo("Base de Datos","Registro Actualizado con éxito")
	
############# interfaz grafica
root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

##### CREACION DE MENU

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectionBBDD)
bbddMenu.add_command(label="salir",command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear Paciente", command=crear)
crudMenu.add_command(label="Leer Paciente", command=leer)
crudMenu.add_command(label="Actualizar Paciente", command=actualizar)
crudMenu.add_command(label="Borrar Paciente")

AyudaMenu=Menu(barraMenu, tearoff=0)
AyudaMenu.add_command(label="Licencia")
AyudaMenu.add_command(label="Acerca de la aplicación")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=AyudaMenu)

# CUADROS DE TEXROS

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miCedula=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()



cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx= 10 , pady=10)

cuadro_cedula=Entry(miFrame, textvariable=miCedula)
cuadro_cedula.grid(row=1, column=1, padx= 10 , pady=10)

cuadro_nombre = Entry(miFrame, textvariable=miNombre)
cuadro_nombre.grid (row = 2 , column = 1,  padx =10, pady =10) # posiciono el cuadro de texto en el frame 

cuadro_apellido= Entry(miFrame, textvariable=miApellido)
cuadro_apellido.grid (row = 3 , column = 1,  padx =10, pady =10)# pad x y pad y sub espacion entre los cuadros de texto

cuadro_password = Entry(miFrame, textvariable=miPass)
cuadro_password.grid (row = 4 , column = 1,  padx =10, pady =10)
cuadro_password.config(show = "*")

cuadro_direccion = Entry(miFrame, textvariable=miDireccion)
cuadro_direccion.grid (row =5 , column = 1,  padx =10, pady =10)

texto_comentario =Text(miFrame, width = 50 ,height =20) 
texto_comentario.grid(row = 6, column = 1, padx =10, pady =10)

scrollvar = Scrollbar(miFrame, command = texto_comentario.yview, bg = "papaya whip") 
scrollvar.grid(row =6 , column = 2, sticky = "nsew" )     

texto_comentario.config(yscrollcommand = scrollvar.set)


##############SELLOS ################################################################

IDLabel = Label(miFrame, text="ID:")
IDLabel.grid (row = 0 , column = 0, sticky = "e",  padx =10, pady =10)

CedulaLabel = Label(miFrame, text="Cedula:")
CedulaLabel.grid (row = 1 , column = 0, sticky = "e",  padx =10, pady =10)

nombreLabel = Label(miFrame, text = "Nombres ")
nombreLabel.grid (row = 2 , column = 0, sticky = "e",  padx =10, pady =10)# posiciono el  texto en el frame 

ApellidoLabel = Label(miFrame, text = "Apellidos")
ApellidoLabel.grid (row = 3 , column = 0, sticky = "e",  padx =10, pady =10) # sticky trabaja con los puntos caridanes para posicionar el texto, 
                                                         #e east alineados a la izquierda
PassLabel = Label(miFrame, text = "Password")
PassLabel.grid (row = 4 , column = 0 , sticky = "e",  padx =10, pady =10)

DireccionLabel = Label(miFrame, text = "Dirección")
DireccionLabel.grid (row = 5 , column = 0 , sticky = "e",  padx =10, pady =10)

ComentLabel = Label(miFrame, text = "Comentarios")
ComentLabel.grid (row =6 , column = 0 , sticky = "e",  padx =10, pady =10)

#################################BOTONES

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear Paciente", command=crear)
botonCrear.grid(row = 1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Consultar Paciente", command=leer)
botonLeer.grid(row = 1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar Paciente", command=actualizar)
botonActualizar.grid(row = 1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar Paciente")
botonBorrar.grid(row = 1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
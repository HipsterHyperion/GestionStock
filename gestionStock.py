class Contador:

	def __init__(self):
		self.__mmm = 0
		self.nnn = 0
		self.ret = 0

	def masUno(self):
		self.__mmm = self.__mmm + 1 
		return self.__mmm
	
	def queda(self, entero):
		self.nnn = entero
		return None

	def otro(self, entero):
		self.ret = entero
		return  None

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clase Item_Stock >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Item_Stock:

	def __init__(self, cod_Item, item, marca, rubro, cod_Proveedor, u_Med, cant_Existente, v_Min, v_Max, precio_U, p_Ganancia):
		self.__cod_Item = cod_Item
		self.__item = item
		self.__marca = marca
		self.__rubro = rubro
		self.__cod_Proveedor = cod_Proveedor
		self.__u_Med = u_Med
		self.__cant_Existente = cant_Existente
		self.__v_Min = v_Min
		self.__v_Max = v_Max
		self.__precio_U = precio_U
		self.__p_Ganancia = p_Ganancia

	def __str__(self):
		a = str(self.__cod_Item) + str(self.__item) + str(self.__marca) + str(self.__rubro) + str(self.__cod_Proveedor)
		b = str(self.__u_Med) + str(self.__cant_Existente) + str(self.__v_Min) + str(self.__v_Max) + str(self.__precio_U)
		return a + b + str(self.__p_Ganancia)

	def getCod(self):
		return self.__cod_Item
	def getItem(self):
		return self.__item
	def getMarca(self):
		return self.__marca
	def getRubro(self):
		return self.__rubro
	def getCod_Proveedor(self):
		return self.__cod_Proveedor
	def getU_Med(self):
		return self.__u_Med
	def getCant_Existente(self):
		return self.__cant_Existente
	def getV_Min(self):
		return self.__v_Min
	def getV_Max(self):
		return self.__v_Max
	def getPrecio_U(self):
		return self.__precio_U
	def getP_Ganancia(self):
		return self.__p_Ganancia

	def setCod(self, cod_Item):
		self.__cod_Item = cod_Item
	def setItem(self, item):
		self.__item = item
	def setMarca(self, marca):
		self.__marca = marca
	def setRubro(self, rubro):
		self.__rubro = rubro
	def setCod_Proveedor(self, cod_Proveedor):
		self.__cod_Proveedor = cod_Proveedor
	def setU_Med(self, u_Med):
		self.__u_Med = u_Med
	def setCant_Existente(self, cant_Existente):
		self.__cant_Existente = cant_Existente
	def setV_Min(self, v_Min):
		self.__v_Min = v_Min
	def setV_Max(self, v_Max):
		self.__v_Max = v_Max
	def setPrecio_U(self, precio_U):
		self.__precio_U = precio_U
	def setP_Ganancia(self, p_Ganancia):
		self.__p_Ganancia = p_Ganancia

	def dameTupla(self):
		return (self.__cod_Item,self.__item,self.__marca,self.__rubro,self.__cod_Proveedor,self.__u_Med,self.__cant_Existente,self.__v_Min,self.__v_Max,self.__precio_U,self.__p_Ganancia)

	def tuplaUno(self):
		return (self.__cod_Item,self.__item,self.__marca,self.__rubro,self.__cod_Proveedor,self.__u_Med)

	def tuplaDos(self):
		return (self.__cant_Existente,self.__v_Min,self.__v_Max,self.__precio_U,self.__p_Ganancia)

	
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clase Proveedor >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>	

class Proveedor:

	def __init__ (self, cod_Proveedor,nombre, direccion, telefono):
		self.__cod_Proveedor = cod_Proveedor
		self.__nombre = nombre
		self.__direccion = direccion
		self.__telefono = telefono

	def getCod(self):
		return self.__cod_Proveedor
	def getNombre(self):
		return self.__nombre
	def getDireccion(self):
		return self.__direccion
	def getTelefono(self):
		return self.__telefono

	def setCod(self, cod_Proveedor):
		self.__cod_Proveedor = cod_Proveedor
	def setNombre(self, nombre):
		self.__nombre = nombre
	def setDireccion(self, direccion):
		self.__direccion = direccion
	def setTelefono(self, telefono):
		self.__telefono = telefono

	def dameTupla(self):
		return (self.__cod_Proveedor,self.__nombre,self.__direccion,self.__telefono)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clase T_Stock >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class T_Stock:

	def __init__(self):
		'''
		i0 = Item_Stock(100,"ARROZ GRANO GRANDE","CONDOR","Alimentos",20,"1LT",8000,500,10000,20,30)
		i1 = Item_Stock(107,"ARROZ GRANOGRANDE","GALLO","Alimentos",20,"1KG",6000,200,8000,25,30)
		i2 = Item_Stock(200,"ACEITE DE GIRASOL","NATURA","Alimentos",30,"1LT",9800,600,10000,40,30)
		i3 = Item_Stock(201,"ACEITE DE GIRASOL","COCINERO","Alimentos",32,"1LT",900,500,10000,30,30)
		i4 = Item_Stock(410,"AGUA MINERAL S/GAS BAJO SODIO","SER","Alimentos",300,"1.5LT",20,50,3000,10,35)
		i5 = Item_Stock(412,"AGUA SABORIZADA LIMA LIMON CON GAS","SER","Alimentos",300,"2LT",1570,50,3000,12,35)
		i6 = Item_Stock(478,"ALFAJOR CHOCOLATE TITA","TERRABUSI","Alimentos",579,"36GR",2000,200,5000,3,30)
		i7 = Item_Stock(479,"ALFAJOR CHOCOLATE RODESIA","TERRABUSI","Alimentos",579,"40GR",1290,200,3500,4,30)
		i8 = Item_Stock(1209,"LECHE DESCREMADA PASTEURIZADA DESLACTOSADA","LA SERENISIMA","Alimentos",231," 1TL",2300,1000,12000,230,30)
		i9 = Item_Stock(1208,"LECHE DESCREMADA PASTEURIZADA","LA SERENISIMA","Alimentos",231,"1TL",5300,2000,14000,130,30)
		j0 = Item_Stock(2301,"ANTITRANSPIRANTE ROLL ON CLASICO","ETIQUET","PERFUMERIA",204,"60gr",300,450,2000,25,30)
		j1 = Item_Stock(2302,"ANTITRANSPIRANTE ROLL ON CLASICO","DOVE","PERFUMERIA",204,"60gr",460,300,2000,35,30)
		j2 = Item_Stock(667,"ARVEJAS SECAS REMOJADAS","NOEL","Alimentos",20,"300GR",1203,500,3000,10,30)
		self.__item = {100:i0, 107:i1, 200:i2, 201:i3, 410:i4, 412:i5, 478:i6, 479:i7, 1209:i8, 1208:i9, 2301:j0, 2302:j1, 667:j2}
		#'''
		self.__item = {}
		
	def getTabla(self):
		return self.__item

	def aStock(self, cod_Item, item):
		x = 0
		if not self.__item.get(cod_Item):
			x = 1
			self.__item[cod_Item] = item
		return x
	
	def bStock(self, cod_Item):
		return self.__item.pop(cod_Item)
		
	def cStock(self, cod_Item):
		return self.__item.get(cod_Item)
		
	def mStock(self, cod_Item, item):
		self.__item[cod_Item] = item
		return None

	def lProdSMin(self):
		qwerty = list(filter(lambda x : x.getCant_Existente() < x.getV_Min(), self.__item.values()))
		www = {}
		for e in qwerty:
			www[e.getCod()] = e
		return www

	def vaciar(self):
		self.__item = {}
		return None


#<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clase T_Proveedor >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class T_Proveedor:

	def __init__(self):
		'''
		i0 = Proveedor(100,"Juan Perez","Belgrano 1827, San Luis, 5700, Argentina","2664-786543")
		i1 = Proveedor(2301,"Jose Lopez","Junin 444, Mendoza,5500, Argentina","261-3452677")
		self.__prov = {100:i0, 2301:i1}
		#'''
		self.__prov = {}
		
	def getTabla(self):
		return self.__prov

	def aProv(self, cod_Prov, prov):
		x = 0
		if not self.__prov.get(cod_Prov):
			self.__prov[cod_Prov] = prov
			x = 1
		return x
	
	def bProv(self, cod_Prov):
		if self.__prov.get(cod_Prov):
			b = self.__prov.pop(cod_Prov)
		return b

	def cProv(self, cod_Prov):
		return self.__prov.get(cod_Prov)
	
	def mProv(self, cod_Prov, prov):
		self.__prov[cod_Prov] = prov
		return None

	def lNbreProvs(self):
		qwerty = list(map(dameNombre, self.__prov.values()))
		i = 0
		www = []
		while i < len(qwerty):
			aux = reduce(dameMenor, qwerty)
			www.append(('',aux,'',''))
			qwerty.remove(aux)
		return www

	
	def vaciar(self):
		self.__prov = {}
		return None


#<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clase BD_Stock >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class BD_Stock:
	
	def __init__(self):
		self.__cant_Usuarios = 1
		self.__acceso = {"A-Admin":"Ad1"}
		self.__nbreTablas = {"T_Stock":0,"T_Proveedor":1}
		self.__tablas = []
		self.__tablas.append(T_Stock())
		self.__tablas.append(T_Proveedor())

#inicS: 0 para User, 1 para Admin.
	def inicS(self, user, clave):
		if self.__acceso.get("A-"+user) == clave:
			esAdmin = 1
		elif self.__acceso.get("N-"+user) == clave:
			esAdmin = 0
		else:
			esAdmin = -1
		return esAdmin
   	 		
	def regUs(self,nombre,clave,tipo):    	
		if self.__acceso.get("A-"+nombre) == self.__acceso.get("N-"+nombre):
			self.__acceso[tipo+nombre] = clave
			self.__cant_Usuarios = len(self.__acceso)
			exito = 1
		else:
			exito = -1
		return exito
	
	def elimUs(self,user):
		self.__acceso.pop(user)
		self.__cant_Usuarios = len(self.__acceso)
		return None

	def cargaBD(self,archivo): #try y catch
		try:
			f = open(archivo+".txt","r")
			l = f.readline().split(";")
			self.__cant_Usuarios = int(l[0])
			self.__acceso={}
			self.getTProveedor3().vaciar()
			self.getTStock3().vaciar()
			k = f.readline().split(";")
			i = 0
			while i < int(l[0]):
				m = k[i].replace('(','')
				n = m.replace(')','')
				m = n.replace("'",'') 
				self.insertarAcceso(m.split(', '))
				i+=1
			k = f.readline().split(";")
			i = 0
			while i < int(l[1]):
				m = k[i].replace('(','')
				n = m.replace(')','')
				m = n.replace("'",'') 
				self.insertarTStock(m.split(', '))
				i+=1
			k = f.readline().split(";")
			i = 0
			while i < int(l[2]):
				m = k[i].replace('(','')
				n = m.replace(')','')
				m = n.replace("'",'') 
				self.insertarTProveedor(m.split(', '))
				i+=1
			f.close()
			exito = 1
		except:
			self.backUp(archivo)
			exito = 2
		return exito
	
	def backUp(self, archivo):
		f = open(archivo+".txt","w")
		f.write(str(len(self.__acceso))+";"+str(len(self.__tablas[0].getTabla()))+";"+str(len(self.__tablas[1].getTabla()))+";\n")
		f.write(self.getAcceso2()+'\n')
		f.write(self.getTStock2()+'\n')
		f.write(self.getTProveedor2())
		f.close()
		return None

	def getAcceso(self):
		return self.__acceso

	def getTStock(self):
		return self.__tablas[0].getTabla()
	
	def getTProveedor(self):
		return self.__tablas[1].getTabla()
	
	def getTStock3(self):
		return self.__tablas[0]
	
	def getTProveedor3(self):
		return self.__tablas[1]

	def getAcceso2(self):
		acum = ''
		l = self.__acceso.items()
		for i in l:
			acum += str(i) + ';'
		return acum
	
	def getTStock2(self):
		acum = ''
		l = self.__tablas[0].getTabla().values()
		for i in l:
			acum += str(i.dameTupla()) + ';'
		return acum
	
	def getTProveedor2(self):
		acum = ''
		l = self.__tablas[1].getTabla().values()
		for i in l:
			acum += str(i.dameTupla()) + ';'
		return acum
	
	def insertarAcceso(self, tupla):
		self.__acceso[tupla[0]]=tupla[1]
		return None

	def insertarTStock(self, tupla):
		i = Item_Stock(int(tupla[0]),tupla[1],tupla[2], tupla[3], int(tupla[4]), tupla[5], int(tupla[6]),int(tupla[7]),int(tupla[8]),int(tupla[9]),int(tupla[10]))
		self.__tablas[0].aStock(int(tupla[0]),i)

	def insertarTProveedor(self, tupla):
		i = Proveedor(int(tupla[0]), tupla[1], tupla[2], tupla[3])
		self.__tablas[1].aProv(int(tupla[0]),i)

##:￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼

#<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from tkinter import *
from tkinter import messagebox
from tkinter import Tk
from tkinter import ttk 
from functools import reduce

#print(b[1].configure('width'))
#b[1].configure(width=100)

def dameNombre(x):
	return x.getNombre()

def dameCodigo(x):
	return x.getCod()

def dameMenor(x, y):
	z = x
	if y < x:
		z = y
	return z
	
def tuplatupla(x):
	return x.dameTupla()

def vaciarEntrada():
	for e in entrada:
		e.delete(0,100)
	return None

def ocultito():
	vaciarEntrada()
	tablaUsuario.place(x=oculto,y=oculto)
	tablaStock1.place(x=oculto,y=oculto)
	tablaStock2.place(x=oculto,y=oculto)
	tablaProveedor.place(x=oculto,y=oculto)
	for e in etiq:
		e.place(x=oculto,y=oculto)
	for e in b:
		e.place(x=oculto,y=oculto)
	for e in entrada:
		e.place(x=oculto,y=oculto)
	return None

def ocultar():
	ocultito()
	for e in menu:
		e.place(x=oculto,y=oculto)
	return None

def iniciar():
	ret = bd.inicS(entrada[0].get(),entrada[-1].get())
	if ret == 1 or ret == 0:
		ocultar()
		raiz.geometry(dimension2)
		menu[3].place(x=30,y=40)
		menu[4].place(x=posx,y=100)
		menu[5].place(x=30,y=190)
		menu[6].place(x=30,y=130)
		menu[7].place(x=30,y=220)
		menu[8].place(x=30,y=340)
		mmm.otro(ret)
	else:
		messagebox.showerror("Error", "Usuario o clave incorrecto.")
	if ret == 1:
		raiz.geometry(dimension3)
		menu[9].place(x=30,y=280)
		menu[12].place(x=30,y=400)
		menu[10].place(x=30,y=430)
		menu[13].place(x=30,y=460)
	return None
		
def salir():
	ocultar()
	raiz.geometry(dimension1)
	menu[0].place(x=30, y=70)
	entrada[0].place(x=30, y=100)
	menu[1].place(x=30,y=130)
	entrada[-1].place(x=30, y=160)
	menu[2].place(x=30,y=190)
	return None

def mas():
	nnn = mmm.masUno()
	if nnn%2 == 0:
		tablaStock1.place(x=possx, y=100)
		tablaStock2.place(x=oculto, y=oculto)
		if mmm.ret:
			b[4].place(x=1000, y=430)
			b[11].place(x=possx, y=430)
			etiq[4].place(x=possx, y=490)
			etiq[5].place(x=possx+300, y=490)
			etiq[6].place(x=possx+600, y=490)
			etiq[7].place(x=possx, y=550)
			etiq[8].place(x=possx+300, y=550)
			etiq[9].place(x=possx+600, y=550)
			etiq[10].place(x=oculto, y=oculto)
			etiq[11].place(x=oculto, y=oculto)
			etiq[12].place(x=oculto, y=oculto)
			etiq[13].place(x=oculto, y=oculto)
			etiq[14].place(x=oculto, y=oculto)
			etiq[15].place(x=possx, y=407)
			etiq[16].place(x=1000, y=407)
			entrada[3].place(x=possx, y=520)
			entrada[4].place(x=possx+300, y=520)
			entrada[5].place(x=possx+600, y=520)
			entrada[6].place(x=possx, y=580)
			entrada[7].place(x=possx+300, y=580)
			entrada[8].place(x=possx+600, y=580)
			entrada[9].place(x=oculto, y=oculto)
			entrada[10].place(x=oculto, y=oculto)
			entrada[11].place(x=oculto, y=oculto)
			entrada[12].place(x=oculto, y=oculto)
			entrada[13].place(x=oculto, y=oculto)
	else:
		tablaStock1.place(x=oculto, y=oculto)
		tablaStock2.place(x=possx, y=100)
		if mmm.ret:
			b[4].place(x=oculto, y=oculto)
			b[11].place(x=oculto, y=oculto)
			etiq[4].place(x=oculto, y=oculto)
			etiq[5].place(x=oculto, y=oculto)
			etiq[6].place(x=oculto, y=oculto)
			etiq[7].place(x=oculto, y=oculto)
			etiq[8].place(x=oculto, y=oculto)
			etiq[9].place(x=oculto, y=oculto)
			etiq[10].place(x=possx, y=490)
			etiq[11].place(x=possx+300, y=490)
			etiq[12].place(x=possx+600, y=490)
			etiq[13].place(x=possx, y=550)
			etiq[14].place(x=possx+300, y=550)
			etiq[15].place(x=oculto, y=oculto)
			etiq[16].place(x=oculto, y=oculto)
			entrada[3].place(x=oculto, y=oculto)
			entrada[4].place(x=oculto, y=oculto)
			entrada[5].place(x=oculto, y=oculto)
			entrada[6].place(x=oculto, y=oculto)
			entrada[7].place(x=oculto, y=oculto)
			entrada[8].place(x=oculto, y=oculto)
			entrada[9].place(x=possx, y=520)
			entrada[10].place(x=possx+300, y=520)
			entrada[11].place(x=possx+600, y=520)
			entrada[12].place(x=possx, y=580)
			entrada[13].place(x=possx+300, y=580)

def comunStock():
	ocultito()
	entrada[2].place(x=possx, y=44)
	b[6].place(x=possx+305, y=40)
	b[2].place(x=1000, y=40)
	tablaStock1.place(x=possx, y=100)
	if mmm.ret:
		b[3].place(x=possx, y=640)
		b[4].place(x=1000, y=430)
		b[5].place(x=1000, y=640)
		b[11].place(x=possx, y=430)
		etiq[4].place(x=possx, y=490)
		etiq[5].place(x=possx+300, y=490)
		etiq[6].place(x=possx+600, y=490)
		etiq[7].place(x=possx, y=550)
		etiq[8].place(x=possx+300, y=550)
		etiq[9].place(x=possx+600, y=550)
		etiq[15].place(x=possx, y=407)
		etiq[16].place(x=1000, y=407)
		etiq[17].place(x=possx+260, y=460)
		etiq[18].place(x=possx, y=670)
		etiq[19].place(x=1000, y=670)
		entrada[3].place(x=possx, y=520)
		entrada[4].place(x=possx+300, y=520)
		entrada[5].place(x=possx+600, y=520)
		entrada[6].place(x=possx, y=580)
		entrada[7].place(x=possx+300, y=580)
		entrada[8].place(x=possx+600, y=580)
	return None

def ts():
	comunStock()
	llenarTablaStock(bd.getTStock())
	return None

def vm():
	comunStock()
	llenarTablaStock(bd.getTStock3().lProdSMin())
	return None

def comunProv():
	ocultito()
	entrada[2].place(x=possx, y=44)
	b[10].place(x=possx+305, y=40)
	tablaProveedor.place(x=possx,y=100)
	if mmm.ret:
		b[7].place(x=possx, y=640)
		b[8].place(x=1000, y=400)
		b[9].place(x=1000, y=640)
		b[12].place(x=possx, y=400)
		etiq[4].place(x=possx, y=490)
		etiq[5].place(x=possx+300, y=490)
		etiq[-1].place(x=possx, y=550)
		etiq[-2].place(x=possx+300, y=550	)
		etiq[15].place(x=possx, y=377)
		etiq[16].place(x=1000, y=377)
		etiq[18].place(x=possx, y=670)
		etiq[19].place(x=1000, y=670)
		entrada[3].place(x=possx, y=520)
		entrada[4].place(x=possx+300, y=520)
		entrada[5].place(x=possx, y=580)
		entrada[6].place(x=possx+300, y=580)
	return None


def tp():
	comunProv()
	m = list(map(tuplatupla, bd.getTProveedor().values()))
	llenarTablaProveedor(m)
	return None

def np():
	comunProv()
	llenarTablaProveedor(bd.getTProveedor3().lNbreProvs())
	return None

def st():
	ocultito()
	txt = menu[12].get()
	t = 0
	if len(txt) > 2:
		t = bd.cargaBD(txt)
		if t == 1:
			messagebox.showinfo("Listo", "Base de Datos cargada.")
		else:
			messagebox.showinfo("Listo", "Se generó un nuevo archivo.")
		mmm.queda(txt)
		menu[11].place(x=30,y=520)
		menu[14].place(x=30,y=550)
	else:
		messagebox.showerror("Error", "Ingrese un nombre del archivo.")
	return None

def bu():
	ocultito()
	bd.backUp(mmm.nnn)
	messagebox.showinfo("Listo", "Base de Datos actualizada.")
	return None

def tu():
	ocultito()
	etiq[0].place(x=possx,y=70)
	tablaUsuario.place(x=possx,y=130)
	llenarTablaUsuario(bd. getAcceso())
	b[1].place(x=possx,y=280)
	etiq[1].place(x=possx,y=310)
	etiq[2].place(x=possx,y=400)
	entrada[0].place(x=possx, y=430)
	etiq[3].place(x=possx,y=460)
	entrada[1].place(x=possx, y=490)
	b[-1].place(x=possx, y=520)
	b[0].place(x=possx,y=550)
	return None

def ru():
	if len(entrada[0].get()) > 2 and len(entrada[1].get()) > 2:
		tipo = "A-"
		if sera.get() == 0:
			tipo = "N-"
		ret = bd.regUs(entrada[0].get(),entrada[1].get(),tipo)
		if ret == 1:
			vaciarEntrada()
			llenarTablaUsuario(bd.getAcceso())
			messagebox.showinfo("Listo", "Usuario registrado.")
		else:
			messagebox.showwarning("Alerta", "Nombre de Usuario ocupado.")
	else:
		messagebox.showerror("Error", "Nombre de Usuario y Clave deben tener almenos tres caracteres.")
	return None

def eu():
	t = tablaUsuario.item(tablaUsuario.selection(), 'text')
	if t != '':
		bd.elimUs(t)
		llenarTablaUsuario(bd. getAcceso())
		messagebox.showinfo("Listo", "Usuario eliminado.")
	return None

def validar():
	x = 1
	for i in entrada[3:13]:
		if len(i.get())==0:
			x = 0
	return x

def ai():
	if validar() == 1 :
		try:
			item = Item_Stock(int(entrada[3].get()), entrada[4].get(), entrada[5].get(), entrada[6].get(), int(entrada[7].get()), entrada[8].get(), int(entrada[9].get()), int(entrada[10].get()), int(entrada[11].get()), int(entrada[12].get()), int(entrada[13].get()))
			if bd.getTStock3().aStock(int(entrada[3].get()),item):
				vaciarEntrada()
				llenarTablaStock(bd.getTStock())
				messagebox.showinfo("Listo", "Item Agregado.")
			else:
				messagebox.showwarning("Alerta", "Item ya existe.")
		except:
			messagebox.showerror("Error", "Algo salió mal.")

	else:
		messagebox.showerror("Error", "Debe llenar todos los campos.")
	return None

def bi():
	t = tablaStock1.item(tablaStock1.selection(), 'values')
	if t != '':
		bd.getTStock3().bStock(int(t[0]))
		llenarTablaStock(bd.getTStock())
		messagebox.showinfo("Listo", "Item eliminado.")
	else:
		messagebox.showerror("Error", "Algo salió mal.")
	return None

def ci():
	try:
		if len(entrada[2].get()) > 0:
			n = int(entrada[2].get())
			if bd.getTStock3().cStock(n):
				m = {}
				m[n] =  bd.getTStock3().cStock(n)
				llenarTablaStock(m)
			else:
				messagebox.showerror("Error", "Codigo no se encuentra.")

		else:
			llenarTablaStock(bd.getTStock())
	except ValueError:
		messagebox.showerror("Error", "Codigo invalido.")
	return None

def mi():
	if validar() == 1 :
		try:
			item = Item_Stock(int(entrada[3].get()), entrada[4].get(), entrada[5].get(), entrada[6].get(), int(entrada[7].get()), entrada[8].get(), int(entrada[9].get()), int(entrada[10].get()), int(entrada[11].get()), int(entrada[12].get()), int(entrada[13].get()))
			bd.getTStock3().mStock(int(entrada[3].get()),item)
			vaciarEntrada()
			llenarTablaStock(bd.getTStock())
			messagebox.showinfo("Listo", "Item Actualizado.")
		except:
			messagebox.showerror("Error", "Algo salió mal.")

	else:
		messagebox.showerror("Error", "Deben tener los campos llenos.")
	return None

def di():
	t = tablaStock1.item(tablaStock1.selection(), 'values')
	if t != '':
		vaciarEntrada()
		item = bd.getTStock3().cStock(int(t[0]))
		entrada[3].insert(END, str(item.getCod()))
		entrada[4].insert(END, item.getItem())
		entrada[5].insert(END, item.getMarca())
		entrada[6].insert(END, item.getRubro())
		entrada[7].insert(END, str(item.getCod_Proveedor()))
		entrada[8].insert(END, item.getU_Med())
		entrada[9].insert(END, str(item.getCant_Existente()))
		entrada[10].insert(END, str(item.getV_Min()))
		entrada[11].insert(END, str(item.getV_Max()))
		entrada[12].insert(END, str(item.getPrecio_U()))
		entrada[13].insert(END, str(item.getP_Ganancia()))
	else:
		messagebox.showerror("Error", "Debe seleccionar en la tabla primero.")
	return None

def validar2():
	x = 1
	for i in entrada[3:7]:
		if len(i.get())==0:
			x = 0
	return x

def ap():
	if validar2() == 1 :
		try:
			prov = Proveedor(int(entrada[3].get()), entrada[4].get(), entrada[5].get(), entrada[6].get())
			if bd.getTProveedor3().aProv(int(entrada[3].get()),prov):
				vaciarEntrada()
				m = list(map(tuplatupla, bd.getTProveedor().values()))
				llenarTablaProveedor(m)
				messagebox.showinfo("Listo", "Proveedor Agregado.")
			else:
				messagebox.showwarning("Alerta", "Proveedor ya existe.")
		except:
			messagebox.showerror("Error", "Algo salió mal.")

	else:
		messagebox.showerror("Error", "Debe llenar todos los campos.")
	return None

def bp():
	t = tablaProveedor.item(tablaProveedor.selection(), 'values')
	if t != '':
		if t[0] != '':
			bd.getTProveedor3().bProv(int(t[0]))
			m = list(map(tuplatupla, bd.getTProveedor().values()))
			llenarTablaProveedor(m)
			messagebox.showinfo("Listo", "Proveedor eliminado.")
		else:
			messagebox.showerror("Error", "Algo salió mal.")
	else:
		messagebox.showerror("Error", "Debe seleccionar en la tabla primero.")
	return None

def cp():
	if len(entrada[2].get()) > 0:
		n = int(entrada[2].get())
		if bd.getTProveedor3().cProv(n):
			m = []
			m.append(bd.getTProveedor3().cProv(n).dameTupla())
			llenarTablaProveedor(m)
		else:
			messagebox.showerror("Error", "Codigo no se encuentra.")
	else:
		m = list(map(tuplatupla, bd.getTProveedor().values()))
		llenarTablaProveedor(m)
	return None

def mp():
	if validar2() == 1 :
		try:
			prov = Proveedor(int(entrada[3].get()), entrada[4].get(), entrada[5].get(), entrada[6].get())
			bd.getTProveedor3().bProv(int(entrada[3].get()),prov)
			vaciarEntrada()
			m = list(map(tuplatupla, bd.getTProveedor().values()))
			llenarTablaProveedor(m)
			messagebox.showinfo("Listo", "Proveedor Agregado.")
		except:
			messagebox.showerror("Error", "Algo salió mal.")

	else:
		messagebox.showerror("Error", "Deben los campos llenos.")
	return None

def dp():
	t = tablaProveedor.item(tablaProveedor.selection(), 'values')
	if t != '':
		if t[0] != '':
			vaciarEntrada()
			prov = bd.getTProveedor3().cProv(int(t[0]))
			entrada[3].insert(END, str(prov.getCod()))
			entrada[4].insert(END, prov.getNombre())
			entrada[5].insert(END, prov.getDireccion())
			entrada[6].insert(END, prov.getTelefono())
		else:
			messagebox.showerror("Error", "Hubo un problema.")
	else:
		messagebox.showerror("Error", "Debe seleccionar en la tabla primero.")
	return None

def vaciarTabla(tabla):
	d = tabla.get_children()
	for e in d:
		tabla.delete(e)
	return None

def llenarTablaUsuario(lista):
	vaciarTabla(tablaUsuario)
	for e in lista:
		tablaUsuario.insert("",0,text = e, values=(e,lista[e]))
	return None
		
def llenarTablaStock(lista):
	vaciarTabla(tablaStock1)
	vaciarTabla(tablaStock2)
	qwerty = list(map(dameCodigo, lista.values()))
	i = 0
	www = []
	while i < len(qwerty):
		aux= reduce(dameMenor, qwerty)
		www.append(aux)
		qwerty.remove(aux)
	for e in www:
		tablaStock1.insert("","end", values=(lista[e].tuplaUno()))
		tablaStock2.insert("","end", values=(lista[e].tuplaDos()))
	return None

def llenarTablaProveedor(lista):
	vaciarTabla(tablaProveedor)
	for e in lista:
		tablaProveedor.insert("","end", values=e)
	return None

dimension1 = '480x400'
dimension2 = '1280x450'
dimension3 = '1280x720'
ancho = 40
posx = 30
possx = 400
oculto = -900
borde = 2
color1 = 'SteelBlue4'
color2 = 'SteelBlue1'

bd = BD_Stock()
raiz = Tk()
mmm = Contador()
sera = IntVar()
raiz.geometry(dimension1)
raiz.configure(bg = color1)
raiz.title('Gestion de Stock y Empleados')

tablaUsuario = ttk.Treeview(raiz,height = 5, columns=('Nombre de Usuario','Clave'), show='headings')
tablaUsuario.heading('Nombre de Usuario',text = "Usuario")
tablaUsuario.column("Nombre de Usuario", width=200, minwidth=200, stretch=NO)
tablaUsuario.heading('Clave', text="Clave")
tablaUsuario.column("Clave", width=200,  minwidth=200, stretch=NO)

tablaStock1 = ttk.Treeview(raiz, height=14, columns=('Codigo','Nombre','Marca','Rubro','Codigo Prov.','Medida'), show='headings')
tablaStock1.heading('Codigo',text = "Codigo")
tablaStock1.column("Codigo", width=90, minwidth=90, stretch=NO)
tablaStock1.heading('Nombre', text="Nombre")
tablaStock1.column("Nombre", width=270,  minwidth=300, stretch=NO)
tablaStock1.heading('Marca', text="Marca")
tablaStock1.column("Marca", width=120,  minwidth=120, stretch=NO)
tablaStock1.heading('Rubro', text="Rubro")
tablaStock1.column("Rubro", width=120,  minwidth=120, stretch=NO)
tablaStock1.heading('Codigo Prov.', text="Codigo Prov.")
tablaStock1.column("Codigo Prov.", width=120,  minwidth=120, stretch=NO)
tablaStock1.heading('Medida', text="Medida")
tablaStock1.column("Medida", width=90,  minwidth=90, stretch=NO)

tablaStock2 = ttk.Treeview(raiz, height=14, columns=('Uds. Actual','Uds. Minimo','Uds. Maximo','Precio Unidad','Ganancia(%)'), show='headings')
tablaStock2.heading('Uds. Actual', text="Uds. Actual")
tablaStock2.column("Uds. Actual", width=150,  minwidth=150, stretch=NO)
tablaStock2.heading('Uds. Minimo', text="Uds. Minimo")
tablaStock2.column("Uds. Minimo", width=150,  minwidth=150, stretch=NO)
tablaStock2.heading('Uds. Maximo', text="Uds. Maximo")
tablaStock2.column("Uds. Maximo", width=150,  minwidth=150, stretch=NO)
tablaStock2.heading('Precio Unidad', text="Precio Unidad")
tablaStock2.column("Precio Unidad", width=150,  minwidth=150, stretch=NO)
tablaStock2.heading('Ganancia(%)', text="Ganancia(%)")
tablaStock2.column("Ganancia(%)", width=150,  minwidth=150, stretch=NO)

tablaProveedor = ttk.Treeview(raiz,height = 10, columns=('Codigo Proveedor','Nombre','Direccion','Telefono'), show='headings')
tablaProveedor.heading('Codigo Proveedor', text='Codigo Proveedor')
tablaProveedor.column('Codigo Proveedor', width=180, minwidth=180, stretch=NO)
tablaProveedor.heading('Nombre', text='Nombre')
tablaProveedor.column('Nombre', width=180, minwidth=180, stretch=NO)
tablaProveedor.heading('Direccion', text='Direccion')
tablaProveedor.column('Direccion', width=250, minwidth=250, stretch=NO)
tablaProveedor.heading('Telefono', text='Telefono')
tablaProveedor.column('Telefono', width=150, minwidth=150, stretch=NO)

etiq=[]
etiq.append(ttk.Label(raiz, width=ancho, anchor="center", background=color2, text="Usuarios Activos"))#0
etiq.append(ttk.Label(raiz, width=ancho, anchor="center", background=color2, text="Seleccione en la tabla para:"))#1
etiq.append(ttk.Label(raiz, width=ancho, anchor="center", background=color2, text="Nombre de Usuario"))#2
etiq.append(ttk.Label(raiz, width=ancho, anchor="center", background=color2, text="Clave"))#3
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Codigo"))#4
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Nombre"))#5
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Marca"))#6
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Rubro"))#7
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Codigo Prov."))#8
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Medida"))#9
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Uds. Actual"))#10
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Uds. Minimo"))#11
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Uds. Maximo"))#12
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Precio Unidad"))#13
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Ganancia(%)"))#14
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Seleccione en la tabla para:"))#15
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Seleccione en la tabla para:"))#16
etiq.append(ttk.Label(raiz, width=ancho+1, anchor="center", background=color2, text="Formulario de Item. (continua en 'Ver mas')"))#17
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Crea una entidad nuevo."))#18
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Reemplaza entidad existente."))#19
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Direccion"))#-2
etiq.append(ttk.Label(raiz, width=ancho-9, anchor="center", background=color2, text="Telefono"))#-1

menu=[]
menu.append(ttk.Label(raiz, width=ancho, anchor="center", borderwidth=borde, relief="groove", background=color2, font=("Verdana",10), text="Nombe de Usuario"))#0
menu.append(ttk.Label(raiz, width=ancho, anchor="center", borderwidth=borde, relief="groove", background=color2, text="Clave"))#1
menu.append(ttk.Button(raiz, width=ancho-1, text="Ingresar", command = iniciar))#2
menu.append(ttk.Label(raiz, width=ancho, anchor="center", borderwidth=borde, relief="groove", background=color2, text="Bienvenido"))#3
menu.append(ttk.Button(raiz, width=ancho-1, text="Tabla de Stock", command = ts))#4
menu.append(ttk.Button(raiz, width=ancho-1, text="Tabla de Proveedor", command = tp))#5
menu.append(ttk.Button(raiz, width=ancho-1, text="Listar Productos por debajo de Valor Minimo", command = vm))#6
menu.append(ttk.Button(raiz, width=ancho-1, text="Listar Nombre de Proveedores", command = np))#7
menu.append(ttk.Button(raiz, width=ancho-1, text="Cerrar Sesion de Trabajo", command = salir))#8
menu.append(ttk.Button(raiz, width=ancho-1, text="Tabla de Usuario", command = tu))#9
menu.append(ttk.Button(raiz, width=ancho-1, text="Iniciar Sesion de Trabajo", command = st))#10
menu.append(ttk.Button(raiz, width=ancho-1, text="Crear Back-Up", command = bu))#11
menu.append(ttk.Entry(raiz, width=ancho))#12
menu.append(ttk.Label(raiz, width=ancho, anchor="center", borderwidth=borde, relief="groove", text="Requiere ingresar nombre del archivo."))#13
menu.append(ttk.Label(raiz, width=ancho, anchor="center", borderwidth=borde, relief="groove", text="Guarda los cambios realizados."))#14

b=[]
b.append(ttk.Button(raiz, width=ancho-1, text="Registrar Usuario", command = ru))#0
b.append(ttk.Button(raiz, width=ancho-1, text="Eliminar Usuario", command = eu))#1
b.append(ttk.Button(raiz, width=ancho-10, text="Ver mas", command = mas))#2
b.append(ttk.Button(raiz, width=ancho-10, text="Agregar", command = ai))#3
b.append(ttk.Button(raiz, width=ancho-10, text="Eliminar", command = bi))#4
b.append(ttk.Button(raiz, width=ancho-10, text="Modificar", command = mi))#5
b.append(ttk.Button(raiz, width=ancho-10, text="Buscar", command = ci))#6
b.append(ttk.Button(raiz, width=ancho-10, text="Agregar", command = ap))#7
b.append(ttk.Button(raiz, width=ancho-10, text="Eliminar", command = bp))#8
b.append(ttk.Button(raiz, width=ancho-10, text="Modificar", command = mp))#9
b.append(ttk.Button(raiz, width=ancho-10, text="Buscar", command = cp))#10
b.append(ttk.Button(raiz, width=ancho-10, text="Actualizar", command = di))#11
b.append(ttk.Button(raiz, width=ancho-10, text="Actualizar", command = dp))#12
b.append(ttk.Checkbutton(raiz, text="Administrador", variable=sera))#-1

entrada=[]
entrada.append(ttk.Entry(raiz, width=ancho-8, font=("Verdana",12)))#0
entrada.append(ttk.Entry(raiz, width=ancho-8, font=("Verdana",12)))#1
entrada.append(ttk.Entry(raiz, width=ancho-10, font=("Verdana",12)))#2
entrada.append(ttk.Entry(raiz, width=ancho-9))#3
entrada.append(ttk.Entry(raiz, width=ancho-9))#4
entrada.append(ttk.Entry(raiz, width=ancho-9))#5
entrada.append(ttk.Entry(raiz, width=ancho-9))#6
entrada.append(ttk.Entry(raiz, width=ancho-9))#7
entrada.append(ttk.Entry(raiz, width=ancho-9))#8
entrada.append(ttk.Entry(raiz, width=ancho-9))#9
entrada.append(ttk.Entry(raiz, width=ancho-9))#10
entrada.append(ttk.Entry(raiz, width=ancho-9))#11
entrada.append(ttk.Entry(raiz, width=ancho-9))#12
entrada.append(ttk.Entry(raiz, width=ancho-9))#13
entrada.append(ttk.Entry(raiz, width=ancho, show="*"))#-1

menu[0].place(x=posx,y=70)
entrada[0].place(x=posx, y=100)
menu[1].place(x=posx,y=130)
entrada[-1].place(x=posx, y=160)
menu[2].place(x=posx, y=190)

raiz.mainloop()

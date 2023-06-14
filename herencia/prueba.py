from Individual import *
from empresa import *
from producto import *

ob1=Individual(1,'Individual','Camila Suarez','suarez1@gmail.com',3009258020)
ob2=empresa(1,'Empresa','ClasesConShreek',3026841004)
prod1=Producto(1,'Computador','Maquina Electronica',2049000)
prod2=Producto(2,'Televisor','Aparato Electronico',1000000)
ob1.setProducto(prod1)
ob1.setProducto(prod2)
print(ob1.getNombre())
print(ob1.getProducto())
for producto in ob1.getProducto():
    print(producto.getPrecio())

prod1.descuentoIndividual(0.4)
prod2.descuentoEmpresa(0.2)

for producto in ob1.getProducto():
    print(producto.getPrecio())

#
def verProductosDisponibles():
    print("Productos Disponibles")
    for producto, precio in productos.items():
        print(f"Producto : {producto} | Precio : {precio}")
        
        
def agregarCarrito():
    nombre_producto = input("Por favor ingrese el nombre del producto: ")
    if nombre_producto in productos:
        #agregar el producto
        carro[nombre_producto] = productos[nombre_producto]
    else:
        print("El producto no existe")
        
def vercarrito():
    total_a_pagar = 0
    
    for producto, precio in carro.items():
        print(f"Producto : {producto} | Precio : {precio}")
        total_a_pagar += precio
        
        
    print(f"El total a pagar es {total_a_pagar}")
    
def pagar():
    total_a_pagar = 0
    
    for producto, precio in carro.items():
        total_a_pagar += precio
        
    print(f"EL total a pagar es {total_a_pagar}")
    print("Confirmar pago")
    print("1. Si")
    print("2. No")
    confirmacion = int(input("Ingrese la opcion: "))
    
    if confirmacion == 1:
        print("Gracias por su compra")
    elif confirmacion == 2:
        print("Continuo la compra")
        
        
        
productos = {
    "papas": 2500,
    "gaseosa": 3000,
    "galletas": 1800,
    "chocolates":2200,
    "jugo" : 2800
}

opcion=5
carro={}

while(opcion != 4 and opcion != 0):
    print("1.ver productos disponibles")
    print("2.Agregar producto al carrito")
    print("3.Ver carrito de compras")
    print("4.pagar y salir")
    print("0. salir sin comprar")
    
    opcion=int(input("ingrese la opcion: "))
    
    match opcion:
        case 1: 
            verProductosDisponibles()
        case 2:
            agregarCarrito()
        case 3:
            vercarrito()
        case 4:
            pagar()
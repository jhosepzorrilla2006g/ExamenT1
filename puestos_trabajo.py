class Puesto:
    def __init__(self, codigo, descripcion, area, plazas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.area = area
        self.plazas = plazas
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} - {self.area} - {self.plazas} - {self.sueldo}"


lista = []


# 1. Agregar
def agregaPuesto():
    codigo = int(input("Codigo: "))
    descripcion = input("Descripcion: ")
    area = input("Area: ")
    plazas = int(input("Plazas: "))
    sueldo = float(input("Sueldo: "))

    
    if len(descripcion) < 3 or len(area) < 3 or codigo <= 0 or plazas <= 0 or sueldo <= 0:
        print("Datos invalidos")
        return

    
    for p in lista:
        if p.codigo == codigo or p.descripcion == descripcion or p.area == area:
            print("Ya existe un puesto similar")
            return

    nuevo = Puesto(codigo, descripcion, area, plazas, sueldo)
    lista.append(nuevo)


# 2. Mostrar
def mostrarTodo():
    for p in lista:
        print(p)


# 3. Borrar 
def borraPuesto():
    codigo = int(input("Codigo a borrar: "))

    
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j].codigo < lista[j+1].codigo:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    
    for i in range(len(lista)):
        if lista[i].codigo == codigo:
            del lista[i]
            print("Eliminado")
            return

    print("No encontrado")


# 4. Buscar sueldo 
def buscaSueldo():
    
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key.sueldo > lista[j].sueldo:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key

    sueldo = float(input("Sueldo a buscar: "))

    
    lower = 0
    higher = len(lista)

    encontrado = -1

    while lower + 1 < higher:
        middle = (lower + higher)//2
        if lista[middle].sueldo == sueldo:
            encontrado = middle
            break
        elif lista[middle].sueldo < sueldo:
            higher = middle
        else:
            lower = middle

    if encontrado == -1:
        print("No encontrado")
        return

    
    i = encontrado
    while i >= 0 and lista[i].sueldo == sueldo:
        print(lista[i])
        i -= 1

    i = encontrado + 1
    while i < len(lista) and lista[i].sueldo == sueldo:
        print(lista[i])
        i += 1


# 5. Puestos a contratar 
def puestosAContratar():
    monto = float(input("Monto total: "))

    
    for i in range(len(lista)-1):
        max = i
        for j in range(i+1, len(lista)):
            if lista[j].sueldo * lista[j].plazas > lista[max].sueldo * lista[max].plazas:
                max = j
        lista[i], lista[max] = lista[max], lista[i]

    total = 0

    for p in lista:
        costo = p.sueldo * p.plazas
        if total + costo <= monto:
            print(p)
            total += costo




# MENU
opc = 0
while opc != 6:
    opc = int(input("\n1-Agregar\n2-Mostrar\n3-Borrar\n4-Buscar sueldo\n5-Contratar\n6-Salir\n"))

    if opc == 1:
        agregaPuesto()
    elif opc == 2:
        mostrarTodo()
    elif opc == 3:
        borraPuesto()
    elif opc == 4:
        buscaSueldo()
    elif opc == 5:
        puestosAContratar()
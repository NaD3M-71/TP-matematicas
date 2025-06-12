##############
#Definición de funciones para validacion.
##############
# Funcion de validacion de numeros enteros y positivos.
def validar_numero(numero):
    es_valido = True  # Forzamos la variable a verdadero.
    for digito in numero:  # Itero la cantidad de caracteres que tiene el texto.
        if digito not in "0123456789": #Si el caracter no esta entre los números paso a False la varaible es valido
            es_valido = False
    if es_valido:  # Si todos eran números 
        if int(numero) <= 0:  # Me fijo si es mayor que 0
            es_valido = False
    return es_valido  # Devuelvo si true o false dependiendo si es valido o no.

# Validación de año de nacimiento (entre 1900 y 2024)
def validar_anio(anio):
    es_valido = True
    for digito in anio:
        if digito not in "0123456789":
            es_valido = False
    if es_valido:
        anio_int = int(anio)
        if anio_int < 1900 or anio_int > 2024:
            es_valido = False
    return es_valido

# # Validación de letra para saber si es una sola y si es valida dentro del abecedario.
def validar_letra(conjunto):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Almaceno las letras del abecedario en mayusculas. 
    if len(conjunto) == 1:  # Me fijo que sea una sola letra
        if conjunto.upper() in abecedario:  # Me aseguro que esté en el abecedario
            return True
    return False  # Si no esta en el abecedario devuelvo un false

# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Función para ordenar una lista de dígitos usando el método burbuja
def ordenar_lista(lista):
    lista = list(lista)  # Aseguro que lo que me pasen sea una lista (por si es set), le cambio el formato
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]: #Compara si es mayor que la siguiente posición.
                lista[j], lista[j + 1] = lista[j + 1], lista[j]# Intercambio los elementos si están desordenados
    return lista

# Función para calcular el producto cartesiano entre dos conjuntos
def producto_cartesiano(conjunto1, conjunto2):
    producto = []
    for elemento1 in conjunto1:
        for elemento2 in conjunto2:
            producto.append((elemento1, elemento2))
    return producto


###################
#programa
####################

conjuntos_dni = {} # Acá voy a guardar los conjuntos con las letras asociadas (nuestro ejemplo: G, R, M, H)
dnis_completos = {} # Diccionario para guardar los DNIs completos sin convertir a conjunto
anios_nacimiento = {} # Diccionario para guardar los años de nacimiento por letra

# Voy a pedir 4 DNIs, cada uno con una letra que lo identifique y su año de nacimiento
i = 1 #Inicializo una varaible en 1 para las vueltas del bucle
while i <= 4:
    letra_valida = False  # Inicio la variable en False para que ingrese en el bucle para pedir letra
    while not letra_valida:
        letra = input(f"Ingrese una letra para el grupo del DNI {i}: ")  # Pido la letra por pantalla
        letra = letra.upper()  # Paso a mayúscula para que sea más fácil comparar la letra ingresada
        if validar_letra(letra) and letra not in conjuntos_dni:  # Me fijo si está bien y no se repite.
            letra_valida = True  # Ahora sí es válida.
        else:
            print("Letra inválida o ya fue ingresada.")  # Si algo está mal y vuelvo a pedir una letra balida.

    dni_valido = False # Inicio la variable en False para que ingrese en el bucle para pedir un dni.
    while not dni_valido: 
        dni = input(f"Ingrese el DNI número {i} para el grupo {letra}: ")  # Pido el DNI
        if validar_numero(dni):  # abrimos el condicional para que valide si esta bien (sea entero y positivo)
            conjuntos_dni[letra] = set(dni)  # Guardo los dígitos únicos en un conjunto con la letra
            dnis_completos[letra] = dni  # Guardo el DNI completo sin convertir a conjunto
            dni_valido = True
        else:
            print("DNI inválido. Ingrese solo números enteros positivos.")  # Aviso si está mal

    # Pedir año de nacimiento
    anio_valido = False  # Inicializo en False para entrar al bucle de validación
    while not anio_valido:  # Mientras el año no sea válido, sigo pidiendo
        anio = input(f"Ingrese el año de nacimiento para el grupo {letra}: ")  # Pido el año por pantalla
        if validar_anio(anio):  # Verifico que el año esté en el rango válido
            anio_int = int(anio)  # Convierto a entero para poder trabajar con él
            # Verificar si el año ya fue ingresado para evitar repetidos
            if anio_int in anios_nacimiento.values():
                print(f"El año {anio_int} ya fue ingresado. Ingrese un año diferente (puede ser ficticio).")
            else:
                anios_nacimiento[letra] = anio_int  # Guardo el año en el diccionario
                anio_valido = True  # El año es válido, salgo del bucle
        else:
            print("Año inválido. Ingrese un año entre 1900 y 2024.")  # Aviso si el año está mal

    i = i + 1  # Paso al siguiente DNI

print("="*50)
print("A. OPERACIONES CON CONJUNTOS DE DNI")
print("="*50)

# Muestro los conjuntos que se generaron
print("\nConjuntos generados:")
for letra, conjunto in conjuntos_dni.items():#recorro por cada Key y el valor de los conjuntos
    print(f"{letra}: {conjunto}") #Imprimo Key y el valor de los conjuntos

# Calculo la unión total de todos los conjuntos
union_total = set() #creo un conjunto vacio donde se guardara los digitos sin repetir
for conjunto in conjuntos_dni.values(): #recorremos cada conjunto dentrode el diccionario conjuntos_dni
    union_total = union_total.union(conjunto) #en cada pasada agregamos los elementos actuales al conjunto union_total

# Calculo la intersección total (elemento repitido en todos los grupos)
listas_conjuntos = list(conjuntos_dni.values()) #Guardo todos los conjuntos en una lista para recorrerlas 1 a 1
interseccion_total = listas_conjuntos[0] # Tomo el primer conjunto como punto inicial para calcular la intersección
j = 1 # Empiezo desde el segundo conjunto (posición 1)
while j < len(listas_conjuntos): # Mientras todavía me falten conjuntos por recorrer...
    # Voy actualizando la intersección total con los elementos que están en común
    interseccion_total = interseccion_total.intersection(listas_conjuntos[j])
    j = j + 1 # Paso al siguiente conjunto


# Muestro las diferencias de cada grupo con respecto a los otros de a pares
print("\nDiferencias entre pares de conjuntos:")
letras = list(conjuntos_dni.keys())  # Obtengo todas las letras en una lista para poder hacer combinaciones
for i in range(len(letras)):  # Recorro desde la primera letra
    for j in range(i + 1, len(letras)):  # Recorro desde la siguiente letra para evitar repeticiones
        letra1 = letras[i]  # Primera letra del par
        letra2 = letras[j]  # Segunda letra del par
        conjunto1 = conjuntos_dni[letra1]  # Primer conjunto
        conjunto2 = conjuntos_dni[letra2]  # Segundo conjunto
        
        # Calculo diferencia del conjunto1 respecto al conjunto2
        diferencia1 = conjunto1 - conjunto2
        # Calculo diferencia del conjunto2 respecto al conjunto1
        diferencia2 = conjunto2 - conjunto1
        
        # Muestro las diferencias entre este par
        print(f"{letra1} - {letra2}: {diferencia1 if diferencia1 else 'Conjunto vacío'}")
        print(f"{letra2} - {letra1}: {diferencia2 if diferencia2 else 'Conjunto vacío'}")
        print()  # Línea en blanco para separar los pares

# Hago la diferencia simétrica (lo que no está en todos)

diferencia_simetrica = set()# Inicializo un conjunto vacío para ir acumulando
for conjunto in conjuntos_dni.values():# Recorro todos los conjuntos del diccionario
    union_temp = diferencia_simetrica.union(conjunto) # Guardo primero la unión de lo que ya tengo con el nuevo conjunto
    interseccion_temp = diferencia_simetrica.intersection(conjunto)# calculo la intersección de lo que ya tengo con el nuevo conjunto
    diferencia_simetrica = union_temp - interseccion_temp#saco la intersección de la unión para sacar la diferencia simétrica


# Muestro los resultados de todas las operaciones
print("\nOperaciones entre conjuntos:")
print("Unión:", union_total)
print("Intersección:", interseccion_total)
print("Diferencia Simétrica:", diferencia_simetrica)

# Cuento cuántas veces aparece cada dígito en cada grupo (usando los DNIs completos)
print("\nFrecuencia de dígitos (basada en DNIs completos):")  # Título para separar esta parte visualmente
for letra, dni_completo in dnis_completos.items():  # Recorro cada grupo con su letra y su DNI completo
    print(f"Grupo {letra} (DNI: {dni_completo}):")  # Imprimo el nombre del grupo y el DNI completo
    
    # Obtengo los dígitos únicos del DNI para ordenarlos
    digitos_unicos = list(set(dni_completo))  # Convierto a set para obtener únicos, luego a lista
    digitos_ordenados = ordenar_lista(digitos_unicos)  # Ordeno los dígitos únicos
    
    for digito in digitos_ordenados:  # Recorro cada dígito único ordenadamente
        contador = 0  # Inicializo el contador en cero
        for digito_en_dni in dni_completo:  # Recorro cada dígito del DNI completo
            if digito == digito_en_dni:  # Si el dígito es igual al que estoy contando...
                contador += 1  # ...sumo uno al contador
        print(f"  {digito}: {contador} vez/veces")  # Muestro cuántas veces apareció ese dígito

# Sumo todos los dígitos por grupo
print("\nSuma total por grupo:")  # Título para mostrar la suma por grupo
for letra, conjunto in conjuntos_dni.items():  # Recorro cada grupo y su conjunto de dígitos
    suma = 0  # Empiezo la suma en cero
    for d in conjunto:  # Recorro cada dígito del conjunto
        suma = suma + int(d)  # Sumo ese dígito (convertido a entero) al total
    print(f"{letra}: {suma}")  # Imprimo la suma total del grupo


# Condiciones lógicas que se piden
print("\nCondiciones lógicas:")  # Título para la parte de condiciones lógicas
for digito in interseccion_total:  # Recorro los dígitos que están en todos los conjuntos
    print(f"Dígito compartido: {digito}")  # Imprimo cuáles son los que se repiten en todos los grupos
    
for letra, conjunto in conjuntos_dni.items():  # Recorro cada grupo
    if len(conjunto) > 6:  # Si el grupo tiene más de 6 dígitos distintos...
        print(f"{letra} tiene Diversidad numérica alta.")  # ...aviso que tiene mucha variedad de números

print("\n" + "="*50)
print("B. OPERACIONES CON AÑOS DE NACIMIENTO")
print("="*50)

# Mostrar los años de nacimiento ingresados
print("\nAños de nacimiento por grupo:")
for letra, anio in anios_nacimiento.items():
    print(f"{letra}: {anio}")

# Contar años pares e impares usando estructuras repetitivas
pares = 0  # Contador para años pares
impares = 0  # Contador para años impares
print("\nClasificación por paridad:")
for letra, anio in anios_nacimiento.items():  # Recorro cada letra y su año correspondiente
    if anio % 2 == 0:  # Si el resto de dividir por 2 es 0, entonces es par
        print(f"{letra}: {anio} - Par")
        pares += 1  # Incremento el contador de pares
    else:  # Si no es par, entonces es impar
        print(f"{letra}: {anio} - Impar")
        impares += 1  # Incremento el contador de impares

print(f"\nResumen de paridad:")
print(f"Años pares: {pares}")
print(f"Años impares: {impares}")

# Verificar si todos nacieron después del 2000
todos_despues_2000 = True  # Asumo que todos nacieron después del 2000
for anio in anios_nacimiento.values():  # Recorro todos los años
    if anio <= 2000:  # Si encuentro alguno que nació en 2000 o antes
        todos_despues_2000 = False  # Cambio la variable a False

if todos_despues_2000:  # Si la variable sigue siendo True
    print("\nGrupo Z")  # Todos nacieron después del 2000
else:
    print("\nNo todos nacieron después del 2000")  # Al menos uno nació en 2000 o antes

# Verificar si alguno nació en año bisiesto
hay_bisiesto = False  # Inicializo la variable para saber si hay años bisiestos
print("\nVerificación de años bisiestos:")
for letra, anio in anios_nacimiento.items():  # Recorro cada letra y año
    if es_bisiesto(anio):  # Uso la función para verificar si es bisiesto
        print(f"{letra}: {anio} - Año bisiesto")
        hay_bisiesto = True  # Cambio la variable porque encontré un año bisiesto
    else:
        print(f"{letra}: {anio} - Año no bisiesto")

if hay_bisiesto:  # Si encontré al menos un año bisiesto
    print("\nTenemos un año especial")

# Calcular edades actuales 
anio_actual = 2025  # Defino el año actual para calcular edades
edades = {}  # Diccionario para guardar las edades por letra
print(f"\nEdades actuales (Segun con que edad finalizarán el año {anio_actual}):")
for letra, anio in anios_nacimiento.items():  # Recorro cada letra y año de nacimiento
    edad = anio_actual - anio  # Calculo la edad restando el año de nacimiento del actual
    edades[letra] = edad  # Guardo la edad en el diccionario
    print(f"{letra}: {edad} años")

# Crear conjuntos de años y edades para el producto cartesiano
conjunto_anios = set(anios_nacimiento.values())  # Convierto los años a conjunto (sin repetidos)
conjunto_edades = set(edades.values())  # Convierto las edades a conjunto (sin repetidos)

print(f"\nConjunto de años de nacimiento: {conjunto_anios}")
print(f"Conjunto de edades actuales: {conjunto_edades}")

# Calcular producto cartesiano entre años y edades
producto_cart = producto_cartesiano(conjunto_anios, conjunto_edades)  # Uso mi función para calcular el producto
print(f"\nProducto cartesiano entre años y edades:")
print("(Año de nacimiento, Edad actual)")
for par in producto_cart:  # Recorro cada par del producto cartesiano
    print(f"{par}")  # Muestro cada par (año, edad)

print(f"\nTotal de pares en el producto cartesiano: {len(producto_cart)}")  # Muestro cuántos pares hay en total
biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}
# Escribe una función llamada "agregar_libro" que permita añadir nuevos libros a la biblioteca. 
# La función debe pedir al usuario el título, autor y año del libro.
def agregar_libro(biblioteca):
    titulo = input('Ingresa el título del libro: ')
    autor = input('Ingresa el nombre del autor: ')
    año = int(input('Ingresa el año del libro: '))
    disponible = True
    biblioteca[titulo] = {"autor":autor,"año":año, "disponible":disponible}
    print(f"el libro{titulo} se a agregado correctamente")
    return biblioteca



# Escribe una función llamada "prestar_libro" que cambie el estado de un libro a no disponible.
# La función debe pedir al usuario el título del libro.
def prestar_libro(biblioteca):
    titulo = input('ingrese el nombre del libro que desea prestar: ')
    if titulo in biblioteca:
        biblioteca[titulo]["disponible"]= False
    print(f"el libro:  {titulo} se a prestado ")
    return biblioteca

# Escribe una función llamada "devolver_libro" que cambie el estado de un libro a disponible.
# La función debe pedir al usuario el título del libro.

def devolver_libro(biblioteca):
      titulo = input('ingrese el nombre del libro que desea devolver: ')
      if titulo in biblioteca:
            biblioteca[titulo]["disponible"]= True
      print(f"el libro: { titulo} se devolvio correctamente")
      return biblioteca

# Escribe una función llamada "mostrar_libros" que imprima todos los libros de la biblioteca, incluyendo su información y disponibilidad.
def mostrar_libros(biblioteca):
     print(biblioteca)
# Utiliza un bucle for para mostrar los libros publicados en un año específico que el usuario ingrese.
def libro_año(biblioteca):
    consulta= int(input('Ingresa el año de publicacion del libro del cual desea saber: '))
    libros_enc=[]

    for clave,valor in biblioteca.items():
        if consulta == valor['año']:
             libros_enc.append(clave)
        
    if libros_enc:
         return libros_enc
    else:       
     return 'No se encuentra un libro con ese año de publicacion'


          
opcion =''
while opcion != '6':
    opcion= input('Biblioteca Consulta\n'
                  'Elija una opcion \n' 
                  '1. Agregar un nuevo libro \n' 
                  '2. Prestar un libro\n'  
                  '3.Devolver un libro \n' 
                  '4. Ver todos los libros\n'
                  '5. ver libros publicados por año\n'
                  '6. Salir del programa\n '
                  )
    if opcion == '1':
         biblioteca.update(agregar_libro(biblioteca))
    elif opcion=='2':
         prestar_libro(biblioteca)
    elif opcion == '3':
         devolver_libro(biblioteca)
    elif opcion == '4':
         mostrar_libros(biblioteca)
    elif opcion == '5':
        print (libro_año(biblioteca))
    elif opcion == '6':
        print("Saliendo del programa...")
    else:
        print("Opción no válida, por favor elija nuevamente.")
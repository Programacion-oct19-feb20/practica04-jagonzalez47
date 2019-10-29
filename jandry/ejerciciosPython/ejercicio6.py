"""
   @autor:Jagonzalez47
   Nombre: ejercicio6.py
   descripcion: ...

   Jandry Gonzalez  19
   Suma de notas es: 30
   Suma promedio es: 15

"""
#System.out.println("Ingrese su nombre");
#nombre = entrada.nextLine();

nombre = input("Ingrese su nombre: ")

edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de su nota1: ")
nota2 = input("Ingrese el valor de su nota2: ")

suma = int(nota1) + int(nota2);
promedio = int(suma)/2

print("%s -- %s\nSu suma es: %s\n Su prmedio es: %s" % (nombre, edad, suma, promedio))




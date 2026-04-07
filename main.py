import sys
from logic.suma import digitsSum
from logic.palindromos import isPalindrome
from logic.ordenamiento import integerSort

def menu():
    while True:
        print("\n" + "="*30)
        print("   MENÚ DE FUNCIONALIDADES")
        print("="*30)
        print("1. Suma de dígitos")
        print("2. Verificador de palíndromos")
        print("3. Ordenamiento de lista (Quicksort)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            val = input("Ingrese el número a procesar: ")
            try:
                print(f"La suma de los dígitos es: {digitsSum(val)}")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

        elif opcion == "2":
            val = input("Ingrese el texto a verificar: ")
            resultado = "es un palíndromo" if isPalindrome(val) else "no es un palíndromo"
            print(f"El texto '{val}' {resultado}.")

        elif opcion == "3":
            val = input("Ingrese una lista de números separados por espacios: ")
            try:
                lista = [int(x) for x in val.split()]
                ordenada = integerSort(lista)
                print(f"Lista original: {lista}")
                print(f"Lista ordenada: {ordenada}")
            except ValueError:
                print("Error: Asegúrese de ingresar solo números enteros.")

        elif opcion == "4":
            print("¡Gracias por usar el sistema! Éxito en Clever Cloud.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
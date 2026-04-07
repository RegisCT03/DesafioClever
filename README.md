# Desafío Técnico - Clever Internship

Este repositorio contiene la resolución de los desafíos técnicos iniciales para el programa de **Clever Internship**. Las soluciones han sido implementadas en **Python**, priorizando la legibilidad del código, la inmutabilidad de los datos y el uso de algoritmos eficientes.

## Contenido del Proyecto

El proyecto resuelve los tres problemas planteados en el PDF:

1. **Suma de Dígitos**: Una función que recibe un número entero (o cadena numérica) y devuelve la suma de todos sus dígitos individuales.
      * *Ejemplo*: `12345` $\rightarrow$ $1+2+3+4+5=15$.
2. **Palíndromos**: Un verificador que determina si una cadena de texto se lee igual de izquierda a derecha que de derecha a izquierda.
      * *Ejemplos*: salas, oso, reconocer.
3. **Ordenamiento (Quicksort)**: Implementación de un algoritmo de ordenamiento ascendente propio, cumpliendo con la restricción de no utilizar funciones nativas como `sort()` o `sorted()`.

## Estructura de Archivos

Se ha seguido una estructura organizada por módulos para separar la lógica de negocio de las pruebas unitarias:

```text
DesafioClever/
├── logic/                 # Módulos con la lógica principal
│   ├── __init__.py        # Inicializador de paquete Python
│   ├── suma_de_digitos.py
│   ├── palindromos.py
│   └── ordenamiento.py
├── test/                  # Pruebas unitarias por cada desafío
│   ├── __init__.py
│   ├── test_suma.py
│   ├── test_palindromos.py
│   └── test_ordenamiento.py
├── .gitignore             # Exclusión de archivos temporales (__pycache__)
└── README.md              # Documentación del proyecto
```

## Ejecución de Pruebas

Para validar los resultados y asegurar que se cumplen los casos de ejemplo proporcionados en el PDF, ejecute los siguientes comandos desde la raíz del proyecto:

```powershell
# Probar Suma de Dígitos
python -m test.test_suma

# Probar Palíndromos
python -m test.test_palindromos

# Probar Ordenamiento
python -m test.test_ordenamiento
```

### Modo Interactivo
Para interactuar con el sistema y probar tus propios valores:
```powershell
python main.py
```

## Decisiones de Ingeniería Tomadas

  * **Algoritmo Quicksort**: Se seleccionó la estrategia de "Divide y Vencerás" para el ordenamiento, ofreciendo un rendimiento promedio superior a algoritmos básicos como el método de burbuja, demostrando un enfoque sólido en estructuras de datos.
  * **Inmutabilidad**: Siguiendo los requisitos del desafío, la función de ordenamiento devuelve una **nueva lista**, asegurando que la lista original proporcionada no sea modificada durante el proceso.
  * **Manejo de Tipos**: Las funciones están diseñadas para ser robustas, manejando tanto entradas numéricas como cadenas de texto cuando el contexto del desafío lo sugiere (ej. `inputInt = "999"`).

-----

**Desarrollado por:** Ma. Regina C. Trejo
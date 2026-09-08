# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Recetario
- Por qué lo elegí (5–8 líneas):
Elegí el recetario porque es una idea práctica para usar varios tipos de datos en Python. Cada receta combina texto para el título y la categoría, enteros para los minutos de cocción, y listas para los ingredientes y la preparación. Me sirve para arrancar con listas en esta entrega y dejar el proyecto acomodado para agregar búsquedas, filtros y ordenamientos en las que vienen.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Cada ítem del catálogo es una receta con título, categoría, tiempo, ingredientes y pasos.

La colección general de recetas y las listas de ingredientes y pasos son mutables (`list`) para poder agregar o modificar datos durante la ejecución. El título, la categoría (`str`) y el tiempo (`int`) son inmutables, así que si hay que cambiarlos directamente se reasigna el valor.

El Catálogo es la estructura general del sistema y adentro guarda la colección principal con todas las recetas. La pila y la cola las voy a usar más adelante: la pila para ir guardando el historial de las recetas que abro y la cola para seguir el orden de los pasos al cocinar.


## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |

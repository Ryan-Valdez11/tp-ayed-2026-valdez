# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Recetario
- Por qué lo eligieron (5–8 líneas):
Se eligió la temática de Recetario por la practicidad que ofrece para estructurar datos heterogéneos y del mundo real. Permite modelar entidades compuestas por atributos simples (como nombre, tiempo de cocción y categoría) y colecciones internas (como listas de ingredientes y pasos de preparación). Además, brinda una estructura ideal para aplicar las colecciones de Python en la primera entrega y profundizar más adelante con algoritmos de búsqueda, ordenamiento y estructuras lineales avanzadas.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Un ítem del catálogo es una **Receta**, la cual contiene información sobre su título, categoría, tiempo de preparación en minutos, una lista de ingredientes y la secuencia de pasos a seguir.

**Mutabilidad en las estructuras (E1):**
- **Estructuras Mutables:** La lista principal de recetas, la lista de ingredientes y la lista de pasos son mutables (tipos `list` y `dict` en Python). Permiten agregar, modificar o eliminar elementos dinámicamente durante la ejecución.
- **Estructuras Inmutables:** Los atributos individuales como el nombre, la categoría (de tipo `str`) y el tiempo de cocción (de tipo `int`) son inmutables. Una vez definidos, sus valores no se modifican directamente, sino que se reemplazan.

**Relación de componentes:**
- El **Catálogo** agrupa el conjunto de todas las recetas disponibles.
- La **Colección principal** es una lista que almacena las recetas del catálogo.
- La **Pila** y la **Cola** se utilizarán en entregas posteriores para gestionar el historial de navegación de recetas o el flujo de ejecución en modo cocina.

```text
+-------------------------------------------------------+
|                       CATÁLOGO                        |
|  +-------------------------------------------------+  |
|  | Colección Principal: [Receta 1, Receta 2, ...]  |  |
|  +-------------------------------------------------+  |
|                                                       |
|  Receta:                                              |
|  - Titulo (str)          -> Inmutable                 |
|  - Tiempo (int)          -> Inmutable                 |
|  - Ingredientes (list)   -> Mutable                   |
|  - Pasos (list)          -> Mutable                   |
+-------------------------------------------------------+'''


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

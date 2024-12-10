# Rectangular Panels Fitting

Este repositorio contiene una solución para encontrar la máxima cantidad de paneles rectangulares de dimensiones `a x b` que pueden caber dentro de un techo rectangular de dimensiones `x x y`. Los paneles pueden orientarse tanto en la posición `(a x b)` como rotados `(b x a)` y mezclarse en cualquier configuración.

## Descripción del Problema

El objetivo es calcular el número máximo de paneles que caben en un techo dado, sin superposiciones entre paneles. No se requiere una representación gráfica, pero el código utiliza una grilla interna para chequear la disponibilidad de espacios.

**Ejemplo:**

- Paneles de `1x2` en un techo de `2x4`: entran 4 paneles.
- Paneles de `1x2` en un techo de `3x5`: entran 7 paneles.
- Paneles de `2x2` en un techo de `1x10`: no entra ninguno (0).
- Caso no trivial: Paneles `2x3` en `5x5`: entran 4, una configuración compleja que no se deduce fácilmente con métodos simples.

## Solución y Enfoque

La solución implementa un **algoritmo de backtracking** sobre una representación tipo matriz booleana (`grid`), donde cada celda del techo es `False` si está libre y `True` si está ocupada. El algoritmo:

1. Recorre las celdas de la grilla en orden.
2. En cada celda libre, intenta:
   - Colocar un panel `a x b`.
   - Colocar un panel `b x a`.
   - No colocar ningún panel.
3. Cada elección se explora recursivamente (backtracking):
   - Si se coloca el panel, se marcan las celdas como ocupadas, se avanza a la siguiente celda y más tarde se "revierte" para explorar otras configuraciones.
   - Se toman todos los resultados posibles y se elige el máximo.

De esta forma, el algoritmo explora el espacio completo de posibilidades, garantizando una solución óptima.

## Fortalezas

- **Exactitud:** Encuentra la solución óptima, probando todas las configuraciones.
- **Generalidad:** Permite mezclas complejas de paneles en orientaciones diferentes.
- **Simplicidad conceptual:** El enfoque backtracking es relativamente sencillo de entender y mantener.

## Debilidades

- **Complejidad alta (exponencial):** Para techos grandes y paneles pequeños, el tiempo de ejecución se dispara.  
- **Solo para enteros:** Esta versión asume dimensiones enteras para tratar el problema como una matriz discreta.  
- **Sin optimizaciones avanzadas:** No utiliza heurísticas ni podas más allá de las restricciones espaciales. En problemas reales de gran escala, no es práctico.

## Ejecución

```bash
# Clona este repositorio
git clone https://github.com/smorenom24/ruuf_postulacion.git
cd ruuf_postulacion

# Ejecuta el código
python3 rectangulos.py

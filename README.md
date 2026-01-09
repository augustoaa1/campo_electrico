# Campo eléctrico de una carga puntual

Este repositorio contiene un ejercicio personal en Python cuyo objetivo es practicar el uso de listas, bucles y funciones, aplicados a un problema sencillo de electrostática.

El programa calcula el campo eléctrico generado por una carga puntual para distintas distancias, utilizando la expresión analítica del modelo clásico.

---

## Objetivo del ejercicio

- Practicar estructuras básicas de Python:
  - listas
  - bucles `for`
  - comprensión de listas
  - funciones
---

##  Modelo físico

El campo eléctrico generado por una carga puntual $q$ a una distancia $r$ está dado por:

$$
E = k \frac{q}{r^2}
$$

donde:
- $k = 9 \times 10^9 \, \text{N·m}^2/\text{C}^2$
- $q$ es la carga eléctrica
- $r$ es la distancia a la carga

---

## Descripción del código
La función recibe una carga eléctrica y una lista de distancias, calcula el campo eléctrico correspondiente a cada distancia y devuelve una lista de strings con los resultados formateados. La funcion no imprime resultados, sino que devuelve datos, permitiendo reutilizarla en otros contextos.

---

## Ejemplo de uso

`q = 2e-6  # C`

`distancias = [1, 10, 20, 50]  # m`

`resultados = campo_electrico(q, distancias)`

`print("\n".join(resultados))
`

Salida esperada:

`E = 1.8e+04 N/C, r = 1 m`

`E = 1.8e+02 N/C, r = 10 m`

`E = 4.5e+01 N/C, r = 20 m`

`E = 7.2e+00 N/C, r = 50 m`

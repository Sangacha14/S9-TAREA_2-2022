""" Modulo: Es un archivo con extensión .py o .pyc (Python compilado), que posee su propio espacio de nombres y que puede
contener variables, funciones, clases o incluso otros módulos.
¿Para qué sirven?
Para organizar mejor el código y poder reutilizarlo mejor.
Modularización y reutilización"""

#import funcionesMatemáticas
from Curso.modulos.funcionesMatemáticas import sumar,multiplicar

print(sumar(5, 6))
print(multiplicar(5, 6))
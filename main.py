from model.app import App

if __name__ == "__main__":
    app = App()
    app.Run()

"""Modelo primer parcial práctico
Objetivos de Aprobación Directa (Solo resuelven esta parte del parcial, si aprobaron la
primera. Esta parte del parcial no permite el uso de material propio. Deberán
programar desde cero, presentando pantalla completa y prendiendo cámara.):

Una empresa se dedica al almacenamiento y posterior distribución de smartphones en el país. Para ello cuentan con 20 depósitos en Berazategui, que generalmente se encuentran en
las inmediaciones de las estaciones del ferrocarril.
Los depósitos pueden almacenar una entre 4 marcas diferentes de smartphones: Xiaomi, Nubia, Infinix y Samsung.
La oficina central, recibe mensualmente una planilla de existencias donde se indican las
existencias de cada 

smartphone para cada depósito.
Realizar un menú de opciones:

1. Obtener existencias: para ello deberá crear una función que cargue la existencia de
cada smartphone en todos los depósitos.
2. Calcular por cada depósito la cantidad total de unidades almacenadas entre todos los
smartphones.
3. Nombre del smartphone  que almaceno menos unidades en cada depósito.
4. Máxima cantidad de unidades almacenados de cada smartphone.
5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de cada marca de smartphone.
6. Cantidad de depósitos que hayan almacenado más de 50000 unidades entre las 4 marcas de
smartphone.
7. Porcentaje de unidades de cada  marca de smartphone sobre el total de unidades almacenadas. Además
mostrar la marca del smartphone con el máximo porcentaje sobre el total almacenado.
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a
menor"""
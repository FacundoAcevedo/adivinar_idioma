#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Facundo Acevedo <facevedo[AT]openmailbox[DOT]org>
#
# Distributed under terms of the GPLv3+ license.

import csv
import re
"""
Genera los datasets en csv
"""


# Estructura del csv:
# palabra,cantidad de letras, cantidad de vocales, cantidad de consonantes, cantidad de
# letras, cantidad de simbolos, idioma

def datasetear(archivo_entrada, salida, idioma):
    """Sanitiza y transforma una lista en un dataset"""

    try:
        with open(archivo_entrada, 'r') as f:
            # Abrimos el csv de salida
            with open(salida, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(
                        csvfile, delimiter=' ', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)

                    for linea in f.readlines():
                        #Sanitizamos la palabra
                        palabra = sanitizar(linea)
                        if palabra:
                            cant_letras = len(palabra)
                            cant_vocales, cant_consonantes, cant_simbolos = contar(
                                palabra)
                            csv_writer.writerow(
                                [palabra, cant_letras, cant_vocales,
                                 cant_consonantes, cant_simbolos, idioma])
    except ValueError:
        print("error blaah")


def sanitizar(linea):
    """Si la linea tiene numeros devuelve vacio
    en caso contrario quita los finales de linea """
    #quito las palabras que tengan numeros
    if re.findall(r'\d+', linea):
        return ""
    return linea.strip()


def contar(palabra):
    """devuelve una tupla con la cantidad de vocales, consonantes y simbolos"""
    voc = 0
    cons = 0
    sim = 0
    for letra in palabra:
        if letra in ("A", "E", "I", "O", "U", "Á", "É", "Í", "Ó", "Ú",
                     "a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"):
            voc += 1
        #simbolos
        elif letra in ("'", "-", "."):
            sim += 1
        else:
            cons += 1

    return voc, cons, sim

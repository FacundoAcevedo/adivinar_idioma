#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Facundo Acevedo <facevedo[AT]openmailbox[DOT]org>
#
# Distributed under terms of the GPLv3+ license.


from sklearn import tree
import csv
from generar_datasets import contar

# levanto los idiomas en dos listas como lo necesita el arbol


def entrenar(archivos):
    data = []
    target = []

    for archivo in archivos:
        with open(archivo, 'r', newline='') as csvfile:
                csv_reader = csv.reader(
                    csvfile, delimiter=' ', quotechar='|',
                    quoting=csv.QUOTE_MINIMAL)
                for linea in csv_reader:
                    data.append([linea[1], linea[2], linea[3], linea[4]])
                    target.append(linea[5])

    #Entrenamiento
    ct = tree.DecisionTreeClassifier()
    ct.fit(data, target)

    return ct


def adivinar(palabra, ct):
    letras = len(palabra)
    voc, cons, simb = contar(palabra)
    res = ct.predict([[letras, voc, cons, simb]])
    return res


def testear():
    ct = entrenar(
        ["esp.csv", "eng_acotado.csv"])
    palabras = (
        "hola",
        "dia",
        "onomatopeya",
        "estereotipo",
        "mitocondira",
        "ñandu",
        "constitution",
        "monster",
        "ranger",
        "t-shirt",
        "recycle",
        "effort",
        "playstation")
    for palabra in palabras:
        print(palabra + "->" + adivinar(palabra, ct)[0])

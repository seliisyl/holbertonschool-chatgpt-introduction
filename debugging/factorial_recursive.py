#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description de la fonction:
    Calcule le factoriel d'un nombre donné.

    Paramètres:
    - n (int): Le nombre dont on veut calculer le factoriel.

    Retours:
    int: Le résultat du calcul du factoriel de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Appel de la fonction factorial avec l'argument passé en ligne de commande
f = factorial(int(sys.argv[1]))
print(f)

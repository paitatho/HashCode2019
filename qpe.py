# -*- coding: utf-8 -*-

import math
import numpy as np
import itertools as it

class NomClasse:
    #ici variable globales
    def __init__(self):
        self.attribut = 2


    def fonction(self, argument):
        return self.attribut + argument


C = NomClasse()
print(C.fonction(1))




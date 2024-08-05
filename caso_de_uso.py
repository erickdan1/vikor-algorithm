import numpy as np
import pyvikor as pvk

# Definir a matriz de decisão
mtx = np.array([
    [1, 3000],
    [2, 3750],
    [5, 4500]
])

# Estabelecer os pesos
w = np.array([0.5, 0.5])

# Definir os tipos de critério
ctr_type = ['minimização', 'maximização']

pvk.vikor(mtx, w, ctr_type)

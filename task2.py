#Marinés Garcìa
###Task 2: Ingeniería de Datos

import pandas as pd
import numpy as np

# Fijamos semilla para reproducibilidad
np.random.seed(42)

def dataset():
    # Crear un DataFrame simulado con valores faltantes y ruidosos
    data = {
        'Edad': np.random.randint(18, 70, size=100),
        'Salario': np.random.randint(30000, 150000, size=100),
        'Compró_Producto': np.random.choice([0, 1], size=100, p=[0.3, 0.7])
    }
    df = pd.DataFrame(data)

    # Número de filas con NaN (10%)
    n_nan = int(0.10 * len(df))
    nan_indices = np.random.choice(df.index, size=n_nan, replace=False)

    df.loc[nan_indices, 'Edad'] = np.nan

    # Crear el vector desbalanceado
    compro_producto = np.array([0]*90 + [1]*10)
    np.random.shuffle(compro_producto)
    df['Compró_Producto'] = compro_producto

    return df

def edad(df):
    # Imputar valores faltantes en 'Edad' con el promedio
    prom_edad = df['Edad'].mean()
    for i in range(len(df)):
        if pd.isna(df.loc[i, 'Edad']):
            df.loc[i, 'Edad'] = prom_edad
    return df


# Laboratorio 1 - IA

**Nombres:** Camila Richter - 23183 y Marinés García - 23391
**Curso:** Inteligencia Artificial
**Tema:** Ingeniería de Datos y Métricas de Evaluación

---

## 📌 Descripción del laboratorio

Este laboratorio tiene como objetivo aplicar conceptos básicos de **Ingeniería de Datos** y **Evaluación de Modelos** mediante la implementación de funciones en Python utilizando únicamente las librerías **pandas** y **numpy**.

El proyecto está organizado en diferentes *tasks*, los cuales pueden ejecutarse de forma independiente a través de un menú interactivo en consola.

---

## 🧪 Task 2 – Ingeniería de Datos

En este task se simula un conjunto de datos y se realizan operaciones básicas de preprocesamiento.

### Funcionalidades:

* Creación de un **DataFrame de 100 filas** con las columnas:

  * `Edad`
  * `Salario`
  * `Compró_Producto`
* Introducción intencional de **valores nulos (NaN)** en el 10% de la columna `Edad`.
* Generación de **desbalance de clases** en `Compró_Producto`:

  * 90 valores en 0 (No compró)
  * 10 valores en 1 (Compró)
* Implementación de un algoritmo que **recorre la columna `Edad`** y reemplaza los valores nulos por el **promedio**, sin utilizar `sklearn`.

Archivo principal:

* `task2.py`

---

## 📊 Task 3 – Métricas de Evaluación

En este task se implementan métricas básicas para evaluar modelos de regresión.

### Métricas implementadas:

* **Error individual**
* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**

Se incluye una breve justificación del uso de RMSE y su penalización a errores grandes.

Archivo principal:

* `task3.py`

---

## 🧭 Ejecución del programa

El archivo `main.py` contiene un **menú interactivo** que permite al usuario seleccionar qué task ejecutar:

1. Task 2 – Ingeniería de Datos
2. Task 3 – Métricas de Evaluación
3. Salir

El menú se mantiene activo mediante un bucle `while` hasta que el usuario decide finalizar el programa.

Para ejecutar el laboratorio:

```bash
python main.py
```

---

## 🛠️ Tecnologías utilizadas

* Python 3
* pandas
* numpy
* math

---

## ✅ Conclusión

Este laboratorio refuerza conceptos fundamentales de preparación de datos y evaluación de modelos, enfatizando la comprensión del proceso mediante implementaciones manuales y control del flujo del progr

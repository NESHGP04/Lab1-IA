from task2 import dataset, edad
from task3 import MAE, RMSE, calcular_error_individual

def main():
    while True:
        print("\n====== LABORATORIO 1 IA ======")
        task = input("\nElija el task a revisar: \n1. Task 2 - Ingeniería de Datos \n2. Task 3 - Métricas de Evaluación \n3. Salir \n")
        
        if task == "1":
            print("\n Task 2 - Ingeniería de Datos")
            df = dataset()
            print("\nDataset original (con NaN en Edad):")
            print(df)

            df = edad(df)
            print("\nDataset después de imputar Edad:")
            print(df)

            print("\nRespuesta a la pregunta extra:")
            print("Usar el promedio sería una mala idea en situaciones donde la distribución de los datos es sesgada o contiene valores atípicos significativos. En estos casos, la mediana es una mejor opción porque no se ve afectada por valores extremos y proporciona una representación más precisa del valor de los datos.")

            return
        elif task == "2":
            print("\nTask 3 - Métricas de Evaluación\n")

            y_real = [100, 150, 200, 250, 300]
            y_pred = [110, 140, 210, 240, 500]

            errores = calcular_error_individual(y_real, y_pred)
            mae_value = MAE(y_real, y_pred)
            rmse_value = RMSE(y_real, y_pred)

            print("Errores individuales:", errores)
            print("MAE:", mae_value)
            print("RMSE:", rmse_value)

            print(
                "\nEl RMSE penaliza más el error del último dato porque al elevar los errores al cuadrado "
                "los errores grandes aumentan de forma desproporcionada su contribución al resultado final. "
                "Esto es importante en aplicaciones críticas."
            )

        elif task == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")
            return

if __name__ == "__main__":
    main()

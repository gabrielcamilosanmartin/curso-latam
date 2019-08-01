import pandas as pd # Permite trabajar con data frame
import numpy as np # Agrega mayor soporte para vectores y matrices
"""
La funcion se encarga de replazar los valores de una columna por los indicados, agrupando segun lo solicitado y crear columnas binarias con los datos de la columana indicada
Input:
	variables_originales: array con datos originales del data frame
	variables: array con nuevo nombre de las variables 
	columna: nombre de la columna sobre la que se trabajara
	df: dataframe con el que se trabajara
Output:
	Retorna un dataframe con las modificaciones en la columna señalada y las nuevas columnas binarias
"""
def bin_and_remplace(variables_originales, variables, columna, df):
    df[columna] = df[columna].replace(variables_originales,variables)
    for variable in variables:
    	if (df[columna].value_counts().index[0] != variable):
    		df['bin_'+columna.replace("-", "_")+'_'+variable.lower()] = np.where(df[columna] == variable, 1, 0)
    return df


"""
Resumen del desempeño de un modelo

    Input:
        modelo: modelo que se resumira


    Output: 
    	miestra por pantalle resumen de desempeño de un modelo
"""
def concise_summary(mod, print_fit=True):
  #guardamos los parámetros asociados a estadísticas de ajuste
  fit = pd.DataFrame({'Statistics': mod.summary2().tables[0][2][2:], 'Value': mod.summary2().tables[0][3][2:]})
  # guardamos los parámetros estimados por cada regresor.
  estimates = pd.DataFrame(mod.summary2().tables[1].loc[:, 'Coef.': 'Std.Err.'])
  # imprimir fit es opcional
  if print_fit is True:
    print("\nGoodness of Fit statistics\n", fit)
    print("\nPoint Estimates\n\n", estimates)


"""
Entrega la probabilidad dado el valor del modelo

    Input:
        x: valor del modelo

    Output: 
    	probabilida 
"""
def inveselogit(x):
  return (1/ (1+np.exp(-x)))
  

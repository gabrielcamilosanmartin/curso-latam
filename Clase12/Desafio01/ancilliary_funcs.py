import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pregunta2(df): 
    for date, row in df.iteritems():
        print('\n---'+date+'---')
        print(df[date].describe())
        
def pregunta3(df, var, print_list = False):
    total = df[var].count()
    count = df[var].isnull().sum()
    print("En " + var + "el numero de casos perdidos es " + str(count) ) 
    print("En " + var + "el porcentaje de casos perdidos es " + str(count/total*100) +"%")
    if (print_list):
        if (count > 0):
            print ('\nLos paises con valores perdidos son: ')
            print (df.loc[df[var].isnull()]['ccodealp'])
        else:
            print ('\nNo hay datos perdidos ')

def pregunta4(df_aux, var, true_mean, sample_mean = False) :
    plt.hist(df_aux[var].dropna(), color='lightgrey')
    plt.title(var)
    if (sample_mean):
        plt.axvline(df_aux[var].mean(),lw = 3,color = 'blue',linestyle = '--')
    if (true_mean):
        plt.axvline(df[var].mean(),lw = 3,color = 'tomato',linestyle = '--')
    plt.show()

def pregunta5(dataframe, plot_var, plot_by, global_stat= False, statistic='mean'):
    if statistic=='mean' :
        data = dataframe.groupby(plot_by)[plot_var].mean().dropna()
    else: 
        data = dataframe.groupby(plot_by)[plot_var].median().dropna()
    
    if global_stat:
        plt.axvline(df[plot_var].dropna().mean(),lw = 3,color = 'blue',linestyle = '--')
    
    plt.plot(data.values, data.index, '.', color='black')
    plt.show()


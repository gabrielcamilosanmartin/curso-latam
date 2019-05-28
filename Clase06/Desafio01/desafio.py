import pandas as pd
csv = pd.read_csv('athlete_events.csv')

ejercicio_1 = csv.shape
ejercicio_2 = len(csv['Sport'].value_counts())
verano = csv['Season'].value_counts()['Summer']
invierno = csv['Season'].value_counts()['Winter']
ejercicio_3 = [verano*100/(invierno+verano),invierno*100/(invierno+verano)]
ejercicio_4 = 
print(ejercicio_4)
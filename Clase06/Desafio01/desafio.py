import pandas as pd
csv = pd.read_csv('athlete_events.csv')

ejercicio_1 = csv.shape
print(ejercicio_1)
ejercicio_2 = len(csv['Games'].value_counts())
print(ejercicio_2)
ejercicio_3 = csv['Season'].value_counts(normalize = True)
print(ejercicio_3)
ejercicio_4 =  csv[(csv["Season"] == "Summer") & (csv["Year"] == csv[csv["Season"] == "Summer"].Year.min())].City.unique()
print(ejercicio_4)
ejercicio_5 = csv[(csv["Season"] == "Winter") & (csv["Year"] == csv[csv["Season"] == "Winter"].Year.min())].City.unique()
print(ejercicio_5)
ejercicio_6 = csv['NOC'].value_counts().head(10)
print(ejercicio_6)
ejercicio_7 = csv['Medal'].value_counts(normalize = True)
print(ejercicio_7)
ejercicio_8 = csv[(csv["Season"] == "Summer") & (csv["Year"] == csv[csv["Season"] == "Summer"].Year.min())].NOC.unique()
print(ejercicio_8)
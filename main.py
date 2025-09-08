import pandas as pd

ruta= "https://github.com/VMjavier/claseAnalisisDatos/raw/refs/heads/main/datos_reales.zip"
df=pd.rea_cvs(ruta)
print(df.head())

n =10 # Número de variables mas comunes a mostrar
Columna = "Crime" # Cambia esto por la columna que deseas analizar

topN = df[columna].value_counts().nlargest(n).index
ptl.figure(figsize= (10,6))
sns.countplot(data=df[df[columna].isin(topN)],
           x=columna,
            order=topN,
            palette="tab10")

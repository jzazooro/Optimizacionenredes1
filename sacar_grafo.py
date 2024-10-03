import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Cargar el modelo guardado
ruta_modelo_guardado = "modelo_xGBoost.joblib"
model = joblib.load(ruta_modelo_guardado)

# Obtener la importancia de las características
importancia = model.get_booster().get_score(importance_type='weight')

# Crear un DataFrame para visualizar la importancia
importancia_df = pd.DataFrame({'Característica': importancia.keys(), 'Importancia': importancia.values()})
importancia_df = importancia_df.sort_values(by='Importancia', ascending=False)

# Visualizar la importancia de las características
plt.figure(figsize=(10, 6))
plt.barh(importancia_df['Característica'], importancia_df['Importancia'], color='skyblue')
plt.xlabel('Importancia')
plt.title('Importancia de Características en el Modelo XGBoost')
plt.gca().invert_yaxis()  # Invertir el eje y para que la más importante esté arriba
plt.savefig('importancia_caracteristicas.png')
plt.show()

# Mostrar el DataFrame con las importancias
print(importancia_df)

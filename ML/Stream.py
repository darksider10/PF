import streamlit as st
import pandas as pd
import joblib
import requests
from io import BytesIO
import sklearn


# Función para cargar el modelo desde GitHub
def load_model():
    # URL raw del archivo .pkl en GitHub
    model_url = 'https://github.com/darksider10/PF/raw/main/ML/ModeloEntrenado.pkl'
    
    # Descargar el archivo .pkl desde la URL
    response = requests.get(model_url)
    
    # Guardar el archivo .pkl localmente
    with open('ModeloEntrenado.pkl', 'wb') as f:
        f.write(response.content)
    
    # Cargar el modelo desde el archivo descargado
    model = joblib.load('ModeloEntrenado.pkl')
    return model

model = load_model()

# Creando la interfaz de usuario
st.title('Predicción del Total Amount para viajes de Taxi')

tpep_pickup_datetime= st.number_input('Hora', min_value=0, max_value=23)
trip_distance = st.number_input('Distancia del viaje (millas)', min_value=0.0, format="%.2f")
pickup_zone = st.selectbox('Zona de recogida', options=[('6','EWR'),('5', 'Staten Island'),('3', 'Queens'),('4', 'Bronx'), ('-1', 'Desconocido'),('2', 'Brooklyn'),('1', 'Manhattan')], format_func=lambda x: x[1])

# Botón para realizar la predicción
if st.button('Predecir Total Amount'):
    X_new = pd.DataFrame([[tpep_pickup_datetime, trip_distance, int(pickup_zone[0])]], columns=['tpep_pickup_datetime', 'trip_distance', 'PickupZone'])
    y_pred_new = model.predict(X_new)
    st.success(f'La predicción del total_amount es: ${y_pred_new[0]:.2f}')

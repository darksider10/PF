import streamlit as st
import pandas as pd
import joblib

# Función para cargar el modelo
def load_model():
    model = joblib.load('random_forest_model.pkl')
    return model

model = load_model()


# Creando la interfaz de usuario
st.title('Predicción del Total Amount para viajes de Taxi')

# Recogiendo las entradas del usuario
passenger_count = st.number_input('Número de pasajeros', min_value=1, max_value=6, value=1)
trip_distance = st.number_input('Distancia del viaje (millas)', min_value=0.0, format="%.2f")
pickup_zone = st.selectbox('Zona de recogida', options=[('1', 'Manhattan'), ('2', 'Brooklyn'), ('3', 'Queens'), ('4', 'Bronx'), ('5', 'Staten Island'), ('-1', 'Desconocido')], format_func=lambda x: x[1])

# Botón para realizar la predicción
if st.button('Predecir Total Amount'):
    X_new = pd.DataFrame([[passenger_count, trip_distance, int(pickup_zone[0])]], columns=['passenger_count', 'trip_distance', 'PickupZone'])
    y_pred_new = model.predict(X_new)
    st.success(f'La predicción del total_amount es: ${y_pred_new[0]:.2f}')


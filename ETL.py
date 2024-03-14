import pandas as pd
import io

    
# Cargar archivo 'Alternative Fuel Vehicles US.csv'
ruta_archivo1 = "Datasets/Alternative_Fuel_Vehicles_US.csv"
df1 = pd.read_csv(ruta_archivo1)
        
# Eliminar columnas innecesarias del DataFrame
df1.drop(columns=['Heavy-Duty Power System', 'Notes', 'Drivetrain', 'Number of Passengers',
    'PHEV Total Range', 'Engine Cylinder Count', 'Transmission Make', 'Transmission Type', 
    'All-Electric Range', 'Alternative Fuel Economy City', 'Alternative Fuel Economy Highway', 'Alternative Fuel Economy Combined',
    'Conventional Fuel Economy City', 'Conventional Fuel Economy Highway', 'Conventional Fuel Economy Combined'], axis=1, inplace=True)

# Definir las categorías a eliminar
categories_to_remove = ['Refuse', 'School Bus', 'Street Sweeper', 'Tractor',
    'TractorVocational/Cab Chassis', 'Transit Bus',
    'Vocational/Cab Chassis', 'Vocational/Cab ChassisTractor',
    'Passenger Van/Shuttle Bus', 'Van', 'Pickup', 'Step Van', 'Vocational/Cab ChassisVan'
    ]

# Filtrar el DataFrame para eliminar las categorías especificadas
df1 = df1[~df1['Category'].isin(categories_to_remove)]

# Normalizar los valores de la columna 'Engine Size' para que todos tengan el formato 'X kW'
df1['Engine Size'] = df1['Engine Size'].str.replace(r'(\d+)\s*[kK][wW].*', r'\1 kW', regex=True)

# Reemplazar abreviaturas en la columna 'Engine Type' por su nombre completo
df1['Engine Type'] = df1['Engine Type'].replace({
    'SI': 'Spark Ignition',
    'e-motor': 'Electric Motor',
    'CI': 'Compression Ignition',
    'FC': 'Fuel Cell'
})

# Eliminar filas con valores faltantes en las columnas 'Engine Type' y 'Engine Size'
df1 = df1.dropna(subset=['Engine Type', 'Engine Size'])

# Eliminar filas duplicadas
df1 = df1.drop_duplicates()

# Renombrar las columnas del DataFrame
df1.columns = [
    'Categoría', 'Modelo', 'AñoModelo', 'Fabricante', 
    'Combustible', 'TipoMotor', 'TamañoMotor'
]

df1["ID"] = df.index

# Guardar el DataFrame en un archivo CSV
df1.to_csv('Datasets/Clean Alternative_Fuel_Vehicles_US.csv', index=False)

#-------------------------------------------------------------------------------
# Cargar archivo 'Alternative Fuel Vehicles US.csv'
ruta_archivo2 = 'Datasets/Electric_and_Alternative_Fuel_Charging_Stations.csv'
df2 = pd.read_csv(ruta_archivo2)

# Filtrar las filas donde la columna 'State' es igual a 'NY'
df2 = df2[df2['State'] == 'NY']

# Lista de columnas a eliminar
columns_to_drop = [
    "Intersection Directions", "Plus4", "Expected Date", "Cards Accepted",
    "BD Blends", "NG Fill Type Code", "NG PSI", "EV Other Info",
    "Federal Agency ID", "Federal Agency Name", "Federal Agency Code",
    "Geocode Status", "Date Last Confirmed", "Owner Type Code", "Facility Type",
    "CNG Dispenser Num", "CNG On-Site Renewable Source",
    "CNG Total Compression Capacity", "CNG Storage Capacity",
    "LNG On-Site Renewable Source", "E85 Other Ethanol Blends",
    "LPG Nozzle Types", "Hydrogen Pressures", "Hydrogen Standards",
    "CNG Fill Type Code", "CNG PSI", "CNG Vehicle Class",
    "LNG Vehicle Class", "EV On-Site Renewable Source",
    "Intersection Directions (French)", "Access Days Time (French)",
    "BD Blends (French)", "Groups With Access Code (French)", "Hydrogen Status Link", "LPG Primary",
    "E85 Blender Pump", "Hydrogen Is Retail", "EV Connector Types", "ZIP", "EV Level2 EVSE Num", "Open Date","EV Pricing",
    "EV DC Fast Count", "Restricted Access", "Access Days Time", "Access Detail Code", "Updated At", "Status Code", "Access Code"
]

# Eliminar las columnas del dataframe
df2.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Aplicar una función para simplificar los valores de "Groups With Access Code" a "Public" o "Private"
df2['Groups With Access Code'] = df2['Groups With Access Code'].apply(lambda x: "Public" if "Public" in x else ("Private" if "Private" in x else x))

# Eliminar columnas  del DataFrame
columns_to_drop = ['Station Phone', 'EV Network', 'EV Network Web', 'NG Vehicle Class', 'Country', 'EV Pricing (French)', 'EV Level1 EVSE Num' ]
df2.drop(columns=columns_to_drop, inplace=True)

# Traducción y Renombramiento de columnas al español
columnas_en_espanol = {
    'Fuel Type Code': 'CodigoCombustible',
    'Station Name': 'NombreEstacion',
    'Street Address': 'Dirección',
    'City': 'Ciudad',
    'State': 'Estado',
    'Groups With Access Code': 'AccesoPublico',
    'Latitude': 'Latitud',
    'Longitude': 'Longitud',
    'ID': 'IDEstacion',
}
df2.rename(columns=columnas_en_espanol, inplace=True)

# ajuste de datos
df2['AccesoPublico'] = df2['AccesoPublico'].replace({'Public': True, 'Private': False})

df2["ID"] = df2.index

# Guardar el DataFrame en un archivo CSV
df2.to_csv('Datasets/Clean Electric_and_Alternative_Fuel_Charging_Stations.csv', index=False)


#------------------------------------------------------------------------------
# Cargar archivo 'Alternative Fuel Vehicles US.csv'
ruta_archivo3 = 'Datasets/Light_Duty_Vehicles.csv'
df3 = pd.read_csv(ruta_archivo3)

# Eliminar columnas que no vamos a utilizar porque no necesitamos la información o porque la misma se encuentra disponible de forma más detallada en otro dataset.

df3.drop(columns=[ 'Notes', 'Drivetrain', 'PHEV Total Range', 'Engine Cylinder Count','Transmission Type', 'Engine Description','Fuel Configuration ID', 
'Manufacturer URL', 'Fuel Code', 'PHEV Type', 'Alternative Fuel Economy City', 'Alternative Fuel Economy Highway','Alternative Fuel Economy Combined', 
'Conventional Fuel Economy City', 'Conventional Fuel Economy Highway', 'Conventional Fuel Economy Combined', 'Engine Type', 'Engine Size', 
'Fuel Configuration Name', 'Electric-Only Range'], axis=1, inplace=True)

# Filtramos el dataset para incluir solo "Sedans" y "SUVs"
df3 = df3[df3['Category'].isin(['Sedan', 'SUV'])]

# Filtrar el DataFrame para incluir solo registros desde 2017 hasta 2022
df3 = df3[(df3['Model Year'] >= 2017) & (df3['Model Year'] <= 2022)]

# Cambiar los nombres de las columnas al español
df3.columns = [
    'IDVehículo', 'IDCombustible', 'IDFabricante', 
    'IDCategoría', 'Modelo', 'AñoModelo', 
    'Fabricante', 'Categoría', 'Combustible'
]

# Guardar el DataFrame en un archivo CSV
df3.to_csv('Datasets/Clean Light_Duty_Vehicles.csv', index=False)


#------------------------------------------------------------------------------

# Cargar archivo 'Alternative Fuel Vehicles US.csv'
ruta_archivo4 = 'Datasets/Vehicle_Fuel_Economy_Data.csv'
df4 = pd.read_csv(ruta_archivo4)


# Las columnas que vamos a dejar en el dataset por su importancia para nuestro objetivo
columns_to_keep_corrected = [
    'Year', 'Manufacturer', 'Model', 'VClass', 'fuelType', 'fuelType1', 
    'city08', 'highway08', 'comb08', 
    'cityA08', 'highwayA08', 'combA08', 
    'co2', 'co2TailpipeGpm', 
    'phevBlended', 
    'range',
    'fuelCost08', 
    'fuelCostA08', 
]
# Filtramos el dataframe para mantener solo las columnas seleccionadas
df4 = df4[columns_to_keep_corrected]


# Eliminamos duplicados estrictos (donde todas las columnas relevantes son idénticas)
df4 = df4.drop_duplicates()


# Filtrar el dataframe para incluir solo vehículos desde el año 2017 en adelante
df4 = df4[df4['Year'] >= 2017]

#  Cambiar los nombres de las columnas al español
df4.rename(columns={
    'Year': 'Año',
    'Manufacturer': 'Fabricante',
    'Model': 'Modelo',
    'VClass': 'ClaseVehículo',
    'fuelType': 'TipoCombustible',
    'fuelType1': 'TipoCombustible1',
    'city08': 'Ciudad08',
    'highway08': 'Carretera08',
    'comb08': 'Combinado08',
    'cityA08': 'CiudadA08',
    'highwayA08': 'CarreteraA08',
    'combA08': 'CombinadoA08',
    'co2': 'CO2',
    'co2TailpipeGpm': 'CO2TuboEscapeGpm',
    'phevBlended': 'HibridoEnchufable',
    'range': 'Rango',
    'fuelCost08': 'CostoCombustible08',
    'fuelCostA08': 'CostoCombustibleA08'
}, inplace=True)

# Eliminar 'TipoCombustible' y renombrar 'TipoCombustible1' a 'TipoCombustible'
df4.drop(columns=['TipoCombustible'], inplace=True)
df4.rename(columns={'TipoCombustible1': 'TipoCombustible'}, inplace=True)

# Eliminar 'CO2TuboEscapeGpm' y renombrar 'CO2' a 'CO2(g/pm)'
df4.drop(columns=['CO2TuboEscapeGpm'], inplace=True)
df4.rename(columns={'CO2': 'CO2(g/pm)'}, inplace=True)

# Renombrar 'Rango' a 'RangoAutonomia'
df4.rename(columns={'Rango': 'RangoAutonomia'}, inplace=True)

# Eliminar 'CostoCombustibleA08' y renombrar 'CostoCombustible08' a 'CostoCombustible'
df4.drop(columns=['CostoCombustibleA08'], inplace=True)
df4.rename(columns={'CostoCombustible08': 'CostoCombustible'}, inplace=True)

# Eliminar columnas específicas de economía de combustible en ciudad y carretera
df4.drop(columns=['Ciudad08', 'Carretera08', 'CiudadA08', 'CarreteraA08'], inplace=True)

# Renombrar columnas de eficiencia de combustible
df4.rename(columns={'Combinado08': 'EficienciaConv', 'CombinadoA08': 'EficienciaAlt'}, inplace=True)
df4 = df.dropna()

df4["ID"] = df.index

# Guardar el DataFrame en un archivo CSV
df4.to_csv('Datasets/Clean Vehicle_Fuel_Economy_Data.csv', index=False)

#-----------------------------------------------------------------------------
import dbf
from simpledbf import Dbf5

ruta_archivo00 = "Datasets/taxi_zones.dbf"
dbf = Dbf5(ruta_archivo00)
df00 = dbf.to_dataframe()

# Guardar el DataFrame en un archivo CSV
df00.to_csv('Datasets/Taxi_zones.csv', index=False)

ruta_archivo5 = "Datasets/taxi+_zone_lookup.csv"
df5 = pd.read_csv(ruta_archivo5)

ruta_archivo6 = "Datasets/Taxi_zones.csv"
df6 = pd.read_csv(ruta_archivo6)

# Merge

df_merged = pd.merge(df5, df6, on='LocationID', how='inner')

# Guardar el DataFrame en un archivo CSV
df_merged.to_csv('Datasets/Merge_Taxi_zones.csv', index=False)

#-----------------------------------------------------------------------------

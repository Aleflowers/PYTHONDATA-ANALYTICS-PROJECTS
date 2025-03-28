#!/usr/bin/env python
# coding: utf-8

# # ¡Hola Alejandra! 😊
# 
# Mi nombre es **Alejandro Castellanos** y hoy tengo el placer de ser el revisor de tu proyecto.
# 
# Voy a revisar todo tu código con detalle, buscando tanto los puntos fuertes como aquellos en los que podrías mejorar. Te dejaré comentarios a lo largo del notebook, destacando lo que has hecho bien y sugiriendo ajustes donde sea necesario. Si encuentro algún error, no te preocupes, te lo haré saber de forma clara y te daré información útil para que puedas corregirlo en la próxima. Si en algún punto tienes comentarios, siéntete libre de dejarlos también.
# 
# 
# Encontrarás mis comentarios específicos dentro de cajas verdes, amarillas o rojas, es muy importante que no muevas, modifiques o borres mis comentarios, con el fin de tener un seguimiento adecuado de tu proceso.:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si todo está perfecto.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# Puedes responderme de esta forma:
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# </div>
# 
# A continuación te dejaré un comentario general con mi valoración del proyecto. **¡Mi objetivo es que sigas aprendiendo y mejorando con cada paso!**

# ----

# <div class="alert alert-block alert-success">
# <b>Comentario General del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
#     
# Alewjandra, completaste todas las tareas propuestas para el proyecto de manera sobresaliente, lo que te ha llevado a una aprobación bien merecida. Demuestras un excelente manejo de las herramientas de visualización de datos y de las pruebas de hipótesis, lo cual fortalece notablemente tu análisis. Continúa desarrollando estas habilidades, ya que estás en el camino correcto para lograr aún más en futuros proyectos. Éxitos en tu próximo sprint 🚀
# 
# </div>

# ----
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Configurar estilo de gráficos
sns.set(style="whitegrid")

# 1. Importar los archivos CSV
file_01 = '/datasets/project_sql_result_01.csv'
file_04 = '/datasets/project_sql_result_04.csv'


# Leer los datasets
df_companies = pd.read_csv(file_01)
df_neighborhoods = pd.read_csv(file_04)




# 2. EXPLORACION DE LOS DATOS
# 
# info() y describe() verifican tipos de datos, valores faltantes y estadísticas descriptivas.

# In[11]:


print("Información general sobre los datos de empresas de taxis:")
print(df_companies.info())  

print("\nDescripción estadística de la cantidad de viajes por empresa:")
print(df_companies.describe())  

print("\nVista previa de los datos:")
print(df_companies.head())

print("\nEmpresas con la mayor cantidad de viajes:")
print(df_companies.sort_values(by='trips_amount', ascending=False).head(5))

# Revisar duplicados en los nombres de empresas
duplicated_names = df_companies['company_name'].duplicated().sum()
print(f"Número de nombres duplicados en 'company_name': {duplicated_names}")

# Revisar valores negativos en trips_amount
negative_trips = (df_companies['trips_amount'] < 0).sum()
print(f"Número de valores negativos en 'trips_amount': {negative_trips}")



# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Muy buen trabajo explorando los datos y haciendo la comprobación de los datos duplicados.
# 
# </div>

# In[13]:


# Información básica
print("Información general sobre los datos de barrios:")
print(df_neighborhoods.info())

print("\nDescripción estadística del promedio de finalización de viajes por barrio:")
print(df_neighborhoods.describe())

print("\nVista previa de los datos:")
print(df_neighborhoods.head())

# Verificar duplicados
duplicated_locations = df_neighborhoods['dropoff_location_name'].duplicated().sum()
print(f"\nNombres duplicados en 'dropoff_location_name': {duplicated_locations}")

# Verificar valores extremos
print("\nBarrios con valores extremadamente altos en 'average_trips':")
print(df_neighborhoods[df_neighborhoods['average_trips'] > (df_neighborhoods['average_trips'].mean() + 3 * df_neighborhoods['average_trips'].std())])

print("\nBarrios con valores extremadamente bajos en 'average_trips':")
print(df_neighborhoods[df_neighborhoods['average_trips'] < (df_neighborhoods['average_trips'].mean() - 3 * df_neighborhoods['average_trips'].std())])

print("\nBarrios con el mayor promedio de finalización de viajes:")
print(df_neighborhoods.sort_values(by='average_trips', ascending=False).head(10))


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
# 
# Excelente análisis exploratorio de datos, esto permite tener una visión preliminar de la información con la que estamos trabajando.
# </div>

# 4.IDENTIFICAR LOS 10 PRINCIPALES BARRIOS EN TÉRMINOS DE FINALIZACION 
# ( se muestran los lugares de finalización con más viajes promedio)

# In[28]:


top_10_neighborhoods = df_neighborhoods.sort_values(by='average_trips', ascending=False).head(10)
print(top_10_neighborhoods)

top_10_companies = df_companies.sort_values(by='trips_amount', ascending=False).head(10)
print(top_10_companies)


# HACER GRÁFICOS: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones

# In[25]:


# (a) Empresas de taxis y número de viajes
top_10_companies = df_companies.sort_values(by='trips_amount', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_companies, x='trips_amount', y='company_name', palette="viridis", orient='h')
plt.title('Top 10 Empresas de taxis por número de viajes (15-16 Nov 2017)', fontsize=16)
plt.xlabel('Número de viajes', fontsize=12)
plt.ylabel('Empresa de taxis', fontsize=12)
plt.tight_layout()
plt.show()


# Este gráfico permitirá identificar visualmente cuál es la empresa con más viajes y cuántos viajes hicieron las siguientes empresas, comparando las diferencias entre ellas de manera clara.
# La empresa Flash Cab tiene la mayor cantidad de viajes, con 19,558 viajes, lo que sugiere que es una de las principales empresas en la flota de taxis en Chicago durante los días seleccionados.
# Posteriormente a los resultados hay que analizar la empresa Flash Cab cuál es la razón por la cual está lidereando el mercado para poder mejorar la propia compañia de taxis. 

# # (b) Los 10 barrios principales por finalización de viajes

# In[26]:


plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_neighborhoods, x='average_trips', y='dropoff_location_name', palette="coolwarm")
plt.title('Top 10 Barrios por Promedio de Finalización de Viajes (Nov 2017)', fontsize=16)
plt.xlabel('Promedio de viajes', fontsize=12)
plt.ylabel('Barrio', fontsize=12)
plt.tight_layout()
plt.show()


# Las empresas de taxis podrían orientar sus recursos y flotas hacia las zonas con más alta demanda, como Loop, River North, y Streeterville, donde el número de viajes es significativamente mayor.
# También podrían investigar las necesidades de transporte en las áreas con menor actividad, como Museum Campus o Gold Coast, para optimizar la cobertura de estos barrios y equilibrar la distribución de viajes.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
#     
# Perfecto has encontrado la información correctra sobre el top 10 de empresas y barrios. Muy buen uso de los recursos gráficos, y también está muy bien incluir tus comentarios, los cuales son completamente pertinentes
# 
# </div>

# Paso 5. Prueba de hipótesis (Python)

# In[ ]:





# In[49]:


import pandas as pd
import scipy.stats as stats

# Cargar el archivo CSV
df = pd.read_csv('/datasets/project_sql_result_07.csv')

# Asegurarse de que las columnas tienen el formato correcto
df['start_ts'] = pd.to_datetime(df['start_ts'])

# Filtrar los datos solo para los sábados
df['day_of_week'] = df['start_ts'].dt.dayofweek
df_saturdays = df[df['day_of_week'] == 5]  # 5 corresponde al sábado

# Clasificar los viajes según el clima: "bad" para condiciones desfavorables
df_saturdays['is_bad_weather'] = df_saturdays['weather_conditions'].str.lower() == 'bad'


# Crear dos grupos: sábados con clima desfavorable ("bad") y favorable ("good")
bad_weather_saturdays = df_saturdays[df_saturdays['is_bad_weather'] == True]
good_weather_saturdays = df_saturdays[df_saturdays['is_bad_weather'] == False]

# Asegurarse de que hay suficientes datos en ambos grupos
print(f"Sábados con clima desfavorable: {len(bad_weather_saturdays)}")
print(f"Sábados con clima favorable: {len(good_weather_saturdays)}")


# Realizar la prueba t para comparar las duraciones promedio
t_stat, p_value = stats.ttest_ind(
    bad_weather_saturdays['duration_seconds'], 
    good_weather_saturdays['duration_seconds'], 
    equal_var=False  # Asumimos que las varianzas pueden ser diferentes
)

# Imprimir los resultados
print(f'Estadístico t: {t_stat}')
print(f'Valor p: {p_value}')

# Comparar el valor p con el nivel de significación (alfa)
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula: La duración promedio de los viajes cambia los sábados con clima desfavorable.")
else:
    print("No rechazamos la hipótesis nula: No hay suficiente evidencia para afirmar que la duración promedio de los viajes cambia los sábados con clima desfavorable.")

    
    


# Hipótesis Nula (H₀): La duración promedio de los viajes no cambia entre los sábados con clima desfavorable y los sábados con clima favorable.
# Hipótesis Alternativa (H₁): La duración promedio de los viajes sí cambia entre los sábados con clima desfavorable y favorable.
# 
# Estadístico t = 7.19
# Valor p = 
# 6.73×10−12
# 6.73×10−12 (muy pequeño)
# Ya que el valor p es mucho menor que el nivel de significación de 0.05 (𝑝<0.05), rechazamos la hipótesis nula. Esto significa que la duración promedio de los viajes cambia en función de si el clima es desfavorable o favorable.
# 

# El resultado del código indica que existe una diferencia estadísticamente significativa entre las duraciones promedio de los viajes realizados los sábados con clima desfavorable y aquellos con clima favorable.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor (1ra Iteración)</b> <a class=“tocSkip”></a>
#     
# Alejandra excelente forma de aplicar las condiciones para crear subconjuntos de datos. Asimismo, la metodología que empleaste para hacer la prueba de hipótesis fue perfecta. Felicitaciones.
#  
# 
# </div>

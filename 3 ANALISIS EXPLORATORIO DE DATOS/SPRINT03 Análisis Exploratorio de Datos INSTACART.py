#!/usr/bin/env python
# coding: utf-8

# # ¡Llena ese carrito!

# # Introducción
# 
# Instacart es una plataforma de entregas de comestibles donde la clientela puede registrar un pedido y hacer que se lo entreguen, similar a Uber Eats y Door Dash.
# El conjunto de datos que te hemos proporcionado tiene modificaciones del original. Redujimos el tamaño del conjunto para que tus cálculos se hicieran más rápido e introdujimos valores ausentes y duplicados. Tuvimos cuidado de conservar las distribuciones de los datos originales cuando hicimos los cambios.
# 
# Debes completar tres pasos. Para cada uno de ellos, escribe una breve introducción que refleje con claridad cómo pretendes resolver cada paso, y escribe párrafos explicatorios que justifiquen tus decisiones al tiempo que avanzas en tu solución.  También escribe una conclusión que resuma tus hallazgos y elecciones.
# 

# ## Diccionario de datos
# 
# Hay cinco tablas en el conjunto de datos, y tendrás que usarlas todas para hacer el preprocesamiento de datos y el análisis exploratorio de datos. A continuación se muestra un diccionario de datos que enumera las columnas de cada tabla y describe los datos que contienen.
# 
# - `instacart_orders.csv`: cada fila corresponde a un pedido en la aplicación Instacart.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'user_id'`: número de ID que identifica de manera única la cuenta de cada cliente.
#     - `'order_number'`: el número de veces que este cliente ha hecho un pedido.
#     - `'order_dow'`: día de la semana en que se hizo el pedido (0 si es domingo).
#     - `'order_hour_of_day'`: hora del día en que se hizo el pedido.
#     - `'days_since_prior_order'`: número de días transcurridos desde que este cliente hizo su pedido anterior.
# - `products.csv`: cada fila corresponde a un producto único que pueden comprar los clientes.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'product_name'`: nombre del producto.
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
# - `order_products.csv`: cada fila corresponde a un artículo pedido en un pedido.
#     - `'order_id'`: número de ID que identifica de manera única cada pedido.
#     - `'product_id'`: número ID que identifica de manera única cada producto.
#     - `'add_to_cart_order'`: el orden secuencial en el que se añadió cada artículo en el carrito.
#     - `'reordered'`: 0 si el cliente nunca ha pedido este producto antes, 1 si lo ha pedido.
# - `aisles.csv`
#     - `'aisle_id'`: número ID que identifica de manera única cada categoría de pasillo de víveres.
#     - `'aisle'`: nombre del pasillo.
# - `departments.csv`
#     - `'department_id'`: número ID que identifica de manera única cada departamento de víveres.
#     - `'department'`: nombre del departamento.

# # Paso 1. Descripción de los datos
# 
# Lee los archivos de datos (`/datasets/instacart_orders.csv`, `/datasets/products.csv`, `/datasets/aisles.csv`, `/datasets/departments.csv` y `/datasets/order_products.csv`) con `pd.read_csv()` usando los parámetros adecuados para leer los datos correctamente. Verifica la información para cada DataFrame creado.
# 

# ## Plan de solución
# 
# Escribe aquí tu plan de solución para el Paso 1. Descripción de los datos.

# In[1]:


# importar librerías
import pandas as pd


# In[2]:


# leer conjuntos de datos en los DataFrames
df_car_orders=pd.read_csv('/datasets/instacart_orders.csv', sep=';') #pedidos en la aplicación instacart
df_product=pd.read_csv('/datasets/products.csv',sep=';') #catálogo de productos
df_aisles=pd.read_csv('/datasets/aisles.csv',sep=';') #categoría de pasillo de víveres
df_departments=pd.read_csv('/datasets/departments.csv',sep=';') #categoría de departamento de víveres
df_order_product=pd.read_csv('/datasets/order_products.csv',sep=';') #ordenes de productos





# In[3]:


# mostrar información del DataFrame

df_car_orders.info()
print(df_car_orders.head())


print(df_car_orders['days_since_prior_order'].value_counts(dropna=False).sort_index())

#llenar los valores nulos identificados en info()
#df_car_orders['days_since_prior_order'] = df_car_orders['days_since_prior_order'].fillna(0)

df_car_orders.info()


print('********Dataset duplicados :')
print(df_car_orders[df_car_orders.duplicated()])










# In[4]:


# mostrar información del DataFrame
df_product.info()
#print(df_product.head())

#identificar valores nulos
print("*****Agrupación y conteo de los nulos*****")
print(df_product['product_name'].value_counts(dropna=False).sort_index())

#llenar los valores nulos identificados en info()
#df_product['product_name'] = df_product['product_name'].fillna(" ")

df_car_orders.info()

print('*******Dataset duplicados :*****')
print(df_product[df_product.duplicated()])







# In[5]:


# mostrar información del DataFrame
df_aisles.info()
print (df_aisles.head)

print('*******Dataset duplicados :*****')
print(df_aisles[df_aisles.duplicated()])


# In[6]:


# mostrar información del DataFrame
df_departments.info()
print (df_departments)

print('*******Dataset duplicados :*****')
print(df_departments[df_departments.duplicated()])


# In[7]:


# mostrar información del DataFrame
df_order_product=pd.read_csv('/datasets/order_products.csv',sep=';') #ordenes de productos
df_order_product.info()
print(df_order_product.head())

print("*****Agrupación y conteo de los nulos*****")
print(df_order_product['order_id'].value_counts(dropna=False).sort_index())
print(df_order_product['product_id'].value_counts(dropna=False).sort_index())
print(df_order_product['add_to_cart_order'].value_counts(dropna=False).sort_index())
print(df_order_product['reordered'].value_counts(dropna=False).sort_index())


print('*******Dataset duplicados :*****')
print(df_order_product[df_order_product.duplicated()])


# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 1. Descripción de los datos.
# 
# Los siguientes dataframes tienen valores nulos:
# df_car_orders[day_sinces_prior_order]=28819 reg nulos
# df_order_product[product_name] =1258 reg nulos
# 
# df_order[]= en este data frame no entiendo porque el data.info() no me indica el numero de nulos en la información.
# 
# Los siguientes DataFrames no tienen valores nulos (ausented) con el data.info:
# 
# df_departments no me marca nulos el data.info()
# df_aisles no me marca nulos el data.info()
# 

# # Paso 2. Preprocesamiento de los datos
# 
# Preprocesa los datos de la siguiente manera:
# 
# - Verifica y corrige los tipos de datos (por ejemplo, asegúrate de que las columnas de ID sean números enteros).
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.
# 
# Asegúrate de explicar qué tipos de valores ausentes y duplicados encontraste, cómo los completaste o eliminaste y por qué usaste esos métodos. ¿Por qué crees que estos valores ausentes y duplicados pueden haber estado presentes en el conjunto de datos?

# ## Plan de solución
# 
# Escribe aquí tu plan para el Paso 2. Preprocesamiento de los datos.

# ## Encuentra y elimina los valores duplicados (y describe cómo tomaste tus decisiones).

# ### `orders` data frame

# In[8]:


# Revisa si hay pedidos duplicados
print(df_car_orders[df_car_orders['order_id'].duplicated()])

filtro= (df_car_orders.loc[df_car_orders['order_id']==794638])
                       
print( filtro)



# ¿Tienes líneas duplicadas? Si sí, ¿qué tienen en común?

# In[9]:


# Basándote en tus hallazgos,
# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.

filtro= (df_car_orders.loc[(df_car_orders['order_dow']==3) & (df_car_orders['order_hour_of_day']==2) ])
                           
print(filtro[filtro['order_id'].duplicated()])


# ¿Qué sugiere este resultado? Hay registros duplicados en las transacciones del miercoles a las 2 pm y hay que eliminarlos

# In[10]:


# Elimina los pedidos duplicados
df_car_orders=df_car_orders.drop_duplicates()
print(df_car_orders.duplicated())

#verificando los pedidos duplicados , si ya no hay
#filtro= (df_car_orders.loc[(df_car_orders['order_dow']==3) & (df_car_orders['order_hour_of_day']==2) ])                           
#print(filtro[filtro['order_id'].duplicated()])


# In[11]:


# Vuelve a verificar si hay filas duplicadas
print(df_car_orders[df_car_orders.duplicated()])




# In[12]:


# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
#df_car_orders.duplicated(subset=['order_id'])


print(df_car_orders[df_car_orders.duplicated(subset=['order_id'], keep=False)])



# Describe brevemente tus hallazgos y lo que hiciste con ellos

# ### `products` data frame

# In[13]:


# Verifica si hay filas totalmente duplicadas

print(df_product[df_product.duplicated()])


# In[14]:


# Revisa únicamente si hay ID de departamentos duplicados

print(df_product[df_product.duplicated(subset=['department_id'])])

print(df_product['department_id'].value_counts())


#df_product.info()



# 

# In[15]:


# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
#print(df_product[df_product.duplicated(subset=['product_name'])])

df_product['product_name']=df_product['product_name'].str.upper()
print(df_product['product_name'].value_counts().sort_values(ascending=False))

#print(df_product['product_name'].unique())


# In[16]:


# Revisa si hay nombres duplicados de productos no faltantes
print(df_product['product_name'].value_counts().sort_values(ascending=False))


# Describe brevemente tus hallazgos y lo que hiciste con ellos. Hay registros duplicados , pero si borro algunos hay el riesgo que el borrado exista en la tabla de ordenes y ya no ligue el producto.

# ### `departments` data frame

# In[17]:


# Revisa si hay filas totalmente duplicadas
print( df_departments[df_departments.duplicated()])

#df_depart.info()


# In[18]:


# Revisa únicamente si hay IDs duplicadas de productos
print(df_product['department_id'].value_counts().sort_values(ascending=False))



# Describe brevemente tus hallazgos y lo que hiciste con ellos. El dataFrame de departamentos no tiene duplicados , en el segundo ejercicio solicita verificar los productos pero el dataframe no tiene columna de productos.

# ### `aisles` data frame

# In[19]:


# Revisa si hay filas totalmente duplicadas
print( df_aisles[df_aisles.duplicated()])


# In[20]:


# Revisa únicamente si hay IDs duplicadas de productos
#df_aisles.info()

print(df_aisles['aisle_id'].value_counts().sort_values(ascending=False))



# Describe brevemente tus hallazgos y lo que hiciste con ellos. No hay duplicados en aisles

# ### `order_products` data frame

# In[21]:


# Revisa si hay filas totalmente duplicadas
#df_order_product.info()

print(df_order_product[df_order_product.duplicated()])

df_order_product.info()


# In[22]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
print(df_order_product['order_id'].value_counts())


# Describe brevemente tus hallazgos y lo que hiciste con ellos.R=Order products no se visualiza tiene filas duplicadas

# ## Encuentra y elimina los valores ausentes
# 
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
# 
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[23]:


df_product=pd.read_csv('/datasets/products.csv',sep=';') #catálogo de productos


# Encuentra los valores ausentes en la columna 'product_name'
df_product.info()
df_product100=df_product[df_product['product_name'].isna()]
print(df_product100)

#print(df_product.isna().sum())
#df_product['product_name'] = df_product['product_name'].fillna(" ")



# Describe brevemente cuáles son tus hallazgos. R= Hay 1258 reg. en product_name con valores ausentes.

# In[24]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
df_product100=df_product[df_product['product_name'].isna()]
print(df_product100)



# Describe brevemente cuáles son tus hallazgos. R: Así es todos los ausentes son del pasillo (aisle )= 100

# In[25]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
df_product100=df_product[df_product['product_name'].isna()]
print(df_product100)



# Describe brevemente cuáles son tus hallazgos. R== Los productos que su product name es nulo tienen  aisle= 100 y department_id=21 

# In[26]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.
 
#df_aisles.info()

#print("****Productos con aisle=100")
#df_product100=df_product[df_product['aisle_id']==100]
#print(df_product100)

print("****Departamento con department_id=21")
df_depart21=df_departments[df_departments['department_id']==21 ]
print(df_depart21)

print("****Aisle=100")
df_aisle100=df_aisles[df_aisles['aisle_id']==100]
print(df_aisle100)




# Describe brevemente cuáles son tus hallazgos.R= probablemente los que esten en departamento Missing y pasillo Missing son productos no encontrados.

# In[27]:


# Completa los nombres de productos ausentes con 'Unknown'


#llenar los valores nulos identificados en info()
df_product['product_name'] = df_product['product_name'].fillna("Unknown")

print(df_product['product_name'].unique())
print(" ")
print(" ")
print("*****Imprime los valores ausentes")
df_product100=df_product[df_product['product_name'].isna()]
print(df_product100)
print(" ")
print(" ")

print("*****Validando que no haya valores ausentes")
df_product.info()



# Describe brevemente tus hallazgos y lo que hiciste con ellos. R= Los valores nulos identificados en la columna product_name se remplazaron con la cadena ="Unknown"

# ### `orders` data frame

# In[28]:


# Encuentra los valores ausentes

#df_car_orders.info()
print(" ")
print(" ")
print("***Los valores ausentes en days_since_prior_order")
print(df_car_orders[df_car_orders['days_since_prior_order'].isna()])
print(" ")
print(" ")
print("Valores ausentes de toda la fila ")
print(df_car_orders[df_car_orders.isna()])
#df_car_orders['days_since_prior_order'] = df_car_orders['days_since_prior_order'].isna()

#llenar los valores nulos identificados en info()
#df_car_orders['days_since_prior_order'] = df_car_orders['days_since_prior_order'].fillna(0)


 
                       


# In[29]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?



df_ausente = df_car_orders[~(df_car_orders['order_number'] == 1) & (df_car_orders['days_since_prior_order'].isna())]
print(df_ausente)





# Describe brevemente tus hallazgos y lo que hiciste con ellos. R= Los valores ausentes se encuentran en el order_number=1 .

# ### `order_products` data frame

# In[30]:


# Encuentra los valores ausentes
df_order_product.info()
print("")
print("**Valores ausentes por columna")
valores_ausentes_por_columna=df_order_product.isna().sum()
print (valores_ausentes_por_columna)
print("")




# In[31]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?

print("**Valor mínimo")
print(" ")
valor_min=df_order_product.min()
print(valor_min)
print("**Valor máximo")
print(" ")
valor_max=df_order_product.max()
print(valor_max)


# Describe brevemente cuáles son tus hallazgos. R= en add_to_cart_order el mínimo es 1 y el maximo es 64. Es en la única columna que me aparecen valores ausentes durante la revisión.

# In[32]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'

print("**Pedidos que tienen un valor ausente en add_to_cart")
pedidos_con_ausentes=df_order_product[df_order_product['add_to_cart_order'].isna()]['order_id']
print (pedidos_con_ausentes)




# Describe brevemente cuáles son tus hallazgos. R= me muestra los pedidos que tienen un valor ausente en la orden

# In[33]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.
df_order_product.info()

df_order_product['add_to_cart_order'].fillna(999, inplace=True)

df_order_product['add_to_cart_order']=df_order_product['add_to_cart_order'].astype(int)

print("")
print("Convertida la columna de float a int")

df_order_product.info()


# Describe brevemente tus hallazgos y lo que hiciste con ellos. R= a los valores ausentes se les llenó con 999

# ## Conclusiones
# 
# Escribe aquí tus conclusiones intermedias sobre el Paso 2. Preprocesamiento de los datos
# 
# Son importantes los métodos isna(), fillna()
# Filtrar dataframes
# y data.info
# 
# para ir monitoreando los valores nulos y eliminarlos
# 
# 

# # Paso 3. Análisis de los datos
# 
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
# 
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# ### [A1] Verifica que los valores sean sensibles

# In[34]:


df_car_orders.info()

print (sorted(df_car_orders['order_hour_of_day'].unique()))

print("")
print("")
print("")



print (sorted(df_car_orders['order_dow'].unique()))

print("")
print("")
print("")



# In[35]:


#Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
import matplotlib.pyplot as plt


#agrupación de la información, numero de personas que hacen pedidos en determinado hora del día.
data_orders =df_car_orders.groupby("order_hour_of_day")["order_id"].count().reset_index(name='numbers_of_orders')

print(data_orders.head(5))

data_orders.plot( kind= "bar", 
                 xlabel= "Hora", 
                 ylabel= "Personas", 
                 title= "Pedidos por hora",
                 color="blue") 


plt.show()


# Escribe aquí tus conclusiones R=El horario donde más pedidos hacen

# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[36]:


#Para cada hora del día, ¿cuántas personas hacen órdenes?
data_orders = df_car_orders.groupby("order_hour_of_day")['user_id'].nunique().reset_index(name='number_of_users')
#data_orders =df_car_orders.groupby("order_hour_of_day")['order_number']["user_id"].count().reset_index(name='numbers_of_orders')

print(data_orders.head(5))

data_orders.plot( kind= "bar", 
                 xlabel= "Hora", 
                 ylabel= "Personas", 
                 title= "Personas que hacen ordenes por hora",
                 color="blue") 


plt.show()


# Escribe aquí tus conclusiones, R = Las horas con mayor consumo es de las 11 de las mañana a las 5 pm de la tarde.

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[37]:


pedidos_por_dia=df_car_orders["order_dow"].value_counts().sort_index()

#crear el gráfico de barras
plt.figure(figsize=(10,6))
pedidos_por_dia.plot(kind="bar", title="Número de pedidos por día de la semana", xlabel="Dia de la semana", ylabel="Numero de pedidos") 

plt.show()


# Los domingos y Lunes son los días que mas víveres compran. 

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[38]:


tiempo_prox_pedido = df_car_orders.groupby('days_since_prior_order')['user_id'].nunique()

# Crear el gráfico de barras
tiempo_prox_pedido.plot(kind='bar',
    xlabel='Días de espera para el siguiente pedido',
    ylabel='Número de clientes',
    title='Días que esperan los clientes para realizar el siguiente pedido')

# Mostrar el gráfico
plt.show()






# Escribe aquí tus conclusiones R= La mayoría espera 30 días para realizar su siguiente pedido. ( mensual ) Y el que le sigue es semanal de 7 días o 6 .  Ya los siguientes rangos abarcan menos numero de personas 0 días como 800 personas, pudiera ser un restaurantero que necesita víveres todos los días para tener surtido su restaurante.

# # [B] Intermedio (deben completarse todos para aprobar)
# 
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[39]:


# Filtrar el DataFrame para incluir solo los pedidos realizados los miércoles y domingos
miercoles_orders = df_car_orders[df_car_orders['order_dow'] == 3]
sabado_orders = df_car_orders[df_car_orders['order_dow'] == 6]


# Agrupar por la hora del día y contar el número de pedidos para cada hora en los miércoles y domingos

pedidos_por_hora_miercoles = miercoles_orders.groupby('order_hour_of_day').size()
pedidos_por_hora_sabados = sabado_orders.groupby('order_hour_of_day').size()


# Unir los datos en un solo DataFrame
data = {'Miércoles': pedidos_por_hora_miercoles, 'Sábados': pedidos_por_hora_sabados}
df_combined = pd.DataFrame(data).fillna(0)  # Llenar con 0 si no hay pedidos el sábados
print(df_combined)

# Graficar el comportamiento de pedidos los miércoles y domingos por hora del día
df_combined.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Hora del día')
plt.ylabel('Número de pedidos')
plt.title('Pedidos los miércoles y sábados por hora del día')
plt.grid(True)
plt.show()


# Escribe aquí tus conclusiones: Para ambos días las horas con mayor número de pedidos es entre 10 am 5 pm.
# 

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[40]:


#2. Grafica la dis# Contar el número de órdenes por cliente
ordenes_por_cliente = df_car_orders.groupby('user_id').size()
print(ordenes_por_cliente.head(5))

# Contar el número de clientes que han realizado un determinado número de órdenes
distribucion_ordenes = ordenes_por_cliente.value_counts().sort_index()
print(distribucion_ordenes.head(5))

# Graficar la distribución del número de órdenes por cliente
distribucion_ordenes.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Número de órdenes')
plt.ylabel('Número de clientes')
plt.title('Distribución del número de órdenes por cliente')
plt.grid(True)
plt.show()


# In[41]:


Hay 56,000 clientes que piden solo una orden.


# Escribe aquí tus conclusiones

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[48]:


# Agrupar por el identificador y nombre del producto y contar la frecuencia de cada producto
merged_df = pd.merge(df_order_product, df_product, on='product_id', how='inner')
frecuencia_productos = merged_df.groupby(['product_id', 'product_name']).size()

#print(frecuencia_productos)

# Ordenar los resultados por frecuencia en orden descendente y tomar los primeros 20 productos
top_20_productos = frecuencia_productos.sort_values(ascending=False).head(20)

print(top_20_productos)


# Escribe aquí tus conclusiones

# # [C] Difícil (deben completarse todos para aprobar)
# 
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[50]:


# Contar el número de productos por orden
productos_por_orden = df_order_product.groupby('order_id').size()
print(productos_por_orden.head(5))


distribucion_ordenesxprod = productos_por_orden.value_counts().sort_index()
print(distribucion_ordenesxprod.head(5))

# Graficar la distribución del número de órdenes por cliente
distribucion_ordenesxprod.plot(kind='bar', figsize=(20, 12))
plt.xlabel('Número de productos')
plt.ylabel('Número de ordenes')
plt.title('Distribución del número de productos por orden')
plt.grid(True)
plt.show()


# Escribe aquí tus conclusiones : En su mayoría de 25,000 a 30,000 ordenes llevan de 4 a 10 productos en sus ordenes.

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[51]:


# Agrupar por el identificador y nombre del producto y contar la frecuencia de cada producto
merged_df = pd.merge(df_order_product, df_product, on='product_id', how='inner')
frecuencia_productos = merged_df.groupby(['product_id', 'product_name']).size()

#print(frecuencia_productos)

# Ordenar los resultados por frecuencia en orden descendente y tomar los primeros 20 productos
top_20_productos = frecuencia_productos.sort_values(ascending=False).head(20)

print(top_20_productos)


# Escribe aquí tus conclusiones Este ejercicio esta repetido con la pregunta 7.7

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# In[47]:


# Contar la frecuencia de cada producto
frecuencia_productos = df_order_product['product_id'].value_counts()

# Contar la frecuencia de cada producto cuandot se vuelve a pedir
frecuencia_repedidos = df_order_product[df_order_product['reordered'] == 1]['product_id'].value_counts()

# Calcular la proporción de repeticiones para cada producto
proporcion_repedidos = (frecuencia_repedidos / frecuencia_productos).fillna(0)

print(proporcion_repedidos)


# In[ ]:





# In[ ]:





# Escribe aquí tus conclusiones

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[45]:


# Fusionar los DataFrames df_order_product y df_product para obtener el nombre de los productos
merged_order_product= pd.merge(df_order_product, df_product, on='product_id', how='inner')
#Fusionar los productos con las ordenes de productos
merged_df_cli = pd.merge(merged_order_product, df_car_orders, on='order_id', how='inner')

# Contar la frecuencia de cada producto por cliente
frecuencia_productos_cliente = merged_df_cli.groupby(['user_id', 'product_id']).size()

# Identificar los productos que un cliente ha vuelto a pedir
productos_repedidos_cliente = merged_df_cli[merged_df_cli['reordered'] == 1].groupby(['user_id', 'product_id']).size()

# Calcular la proporción de productos que un cliente ha vuelto a pedir de todos los productos que ha pedido
proporcion_productos_repedidos = productos_repedidos_cliente.div(frecuencia_productos_cliente, fill_value=0).groupby(['user_id']).mean()

print(proporcion_productos_repedidos)


# In[ ]:


####Conclusiones , con el resultado se puede ver la preferencia del cliente a ciertos productos, entre más cercano a uno es que siempre lo está reordenando. 


# In[ ]:


### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?


# In[46]:


#Fusionar los DataFrames df_order_product y df_product para obtener el nombre de los productos

merged_df = pd.merge(df_order_product, df_product, on='product_id', how='inner')

# Filtrar las filas donde el producto se agrega al carrito por primera vez

primeras_veces = merged_df[merged_df['add_to_cart_order'] == 1]
# Contar la frecuencia de cada producto que se agrega al carrito por primera vez

contar_productos = primeras_veces['product_name'].value_counts().head(20)
print(contar_productos)


# In[ ]:


La Bananana y la Bag organic banana son los víveres que tienen como prioridad para ingresarlos en el carrito y adicional es un producto con alto consumo de los clientes ( frecuente)


# In[ ]:


#CONCLUSIONES DEL PROYECTO

En el proyecto se analiza el comportamiento de consumo de los clientes. Horarios y días pico.
Si el cliente tiene preferencia por algún producto y que tan frecuentemente lo solicita.
Los productos mayormente vendidos y preferidos por el cliente . 


En cuanto a lo técnico , el proyecto ya estuvo muy elevado. Yo si tuve que pedir apoyo a alguien cercano para poder resolverlo,
debido a la complejidad . 

Borré varias líneas de mi proyecto por accidente casi al final por eso las ultimas conclusiones pueden estar en otro formato.
Me falta el expertaise para Jupiter Notebook y pithon.

Algo adicional es que el tiempo que marca el contenido de estudio , muchas veces no se cumple, termina uno llevándose más tiempo.




# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ¡Hola!<br />
# Soy **Francisco Cortés**, estoy contento de revisar tu proyecto y ser parte de tu proceso de aprendizaje.
# A lo largo del texto, haré algunas observaciones sobre mejoras en el código y también haré comentarios sobre tus percepciones sobre el tema. Si existe algún error en el código, no te preocupes, estoy aquí para ayudarte a mejorarlo, en la primera iteración te lo señalaré para que tengas la oportunidad de corregirlo, pero si aún no encuentras una solución para esta tarea, te daré una pista más precisa en la próxima iteración y también algunos ejemplos prácticos. Estaré abierto a retroalimentación y discusiones sobre el tema.<br />
# Encontrarás mis comentarios a continuación - **por favor no los muevas, modifiques o borres**.
# Revisaré cuidadosamente tu código para comprobar que se han cumplido con los requisitos y te proporcionaré mis comentarios en cajas verdes, amarillas o rojas como esta:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si la ejecución fue perfecta succesfully.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si existe alguna recomendación para que tu código mejore.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si existen correcciones necesarias para cumplir con los requisitos. El trabajo no puede ser aceptado si hay alguna caja roja.
# </div>
# 
# Puedes responderme de la siguiente manera:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante.</b> <a class="tocSkip"></a>
# </div>
# 

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[5]:


import pandas as pd# Importar pandas


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[7]:


df=pd.read_csv ('/datasets/music_project_en.csv')# Leer el archivo y almacenarlo en df


# Muestra las 10 primeras filas de la tabla:

# In[8]:


print(df.head(10))# Obtener las 10 primeras filas de la tabla df


# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[9]:


print(df.info())# Obtener la información general sobre nuestros datos


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. Utilizar el snake_case en userID`Detecta el tercer problema por tu cuenta y descríbelo aquí`.
# 
# 
# 

# ción?`
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`

# Todos los datos son de tipo string, cada usuario escucha canciones a cierta hora y día de la semana en cierta ciudad.
# 

# Yo creo si son suficientes datos para comprobar la hipótesis. ( Borré parte de las preguntas y ya no supe como restarurarlas)

# In[ ]:


Si hay valores ausentes en la tabla que despliega info hay algunos datos que no se están contando en cada tipo de dato por ejemplo
1   Track     63736 non-null  object
 2   artist    57512 non-null  object
 3   genre     63881 non-null  object
el número de registros non-null es menor a el total de filas: 
    RangeIndex: 65079 entries, 0 to 65078


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# No te preocupes!
# <br />
# En la parte de arriba dentro de 'Edit' existe la opción 'Undo Delete Cells' que recupera las celdas que han sido borradas. Si no fue lo que paso y no borraste la celda, puedes usar 'ctrl + z' para regresar el text.<br/>
# Buenas observaciones las que haces.
# </div>
# 

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[10]:


print (df.columns)# Muestra los nombres de las columnas


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[11]:


new_columns=[]

# Bucle en los encabezados poniendo todo en minúsculas

for old_column in df.columns:
    column_lowered=old_column.lower()
    new_columns.append(column_lowered)
    
print( new_columns )


# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[12]:


new_columns=[]

# Bucle en los encabezados eliminando los espacios

for old_column in df.columns:
    column_lowered=old_column.lower()
    column_stripped=column_lowered.strip()
    new_columns.append(column_stripped)

df.columns=new_columns

print(df.columns) #mostrar lo de dataframe df


# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[13]:


# Cambiar el nombre de la columna "userid"

df.rename(columns={'userid':'user_id'}, inplace=True)

print(df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[14]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)
print(df.info())


# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Bien hecho, se reemplazaron los nombres de las columnas correctamente
# </div>
# 

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[15]:


print(df.isna().sum())# Calcular el número de valores ausentes


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[16]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
for column in df.columns :

    df[column].fillna('unknown', inplace=True)
    
print(df.isna().sum())# Calcular el número de valores ausentes



# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[17]:


print(df.isna().sum())# Contar valores ausentes


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto, buena manera de reemplazar los valores ausentes
# </div>
# 

# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[18]:


print(df.duplicated().sum())# Contar duplicados explícitos


# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[20]:


df.drop_duplicates(inplace=True)# Eliminar duplicados explícitos


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[21]:


print(df.duplicated().sum())# Comprobar de nuevo si hay duplicados



# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[22]:


print(df['genre'].unique())# Inspeccionar los nombres de géneros únicos


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[23]:


wrong_genres=["hip", "hop", "hip-hop"]
correct_genre="hiphop"


def replace_wrong_genres (df, column, wrong_genres, correct_genre):# Función para reemplazar duplicados implícitos
    for wrong_value in wrong_genres:
        df[column]=df[column].replace(wrong_genres, correct_genre)
    return df



# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[24]:


df= replace_wrong_genres (df, 'genre', wrong_genres,correct_genre)# Eliminar duplicados implícitos


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[25]:


print(df['genre'].unique())# Comprobación de duplicados implícitos



# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`

# Aunque se utilizó unique para visualizar los datos, me parece complicado encontrar facilmente errores solo visualizando y encontrar todas las versiones de error de escritura. Se realizó una lista con los valores erroneos identificados y una variable con el valor correcto. Esos datos se pasaron como parámetros , junto con el df y la columna de interes. Y se recorrió con un bucle y con el método replace se selecconó lo erroneo , para remplazar el valor correcto. Con la función y el bucle se optimiza el estar haciendo replace por cada error encontrado. Al final se obtuvieron los valores unicos con la los valores corregidos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Bien hecho, se eliminaron los duplicados explicitos correctamente y los duplicados implicitos se reemplazaron, es correcto lo que dices, encontrar los valores implicitos es difícil, ya que requiren conocimientos previos de los datos
# </div>
# 

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[26]:


print(df.groupby(by="city")["track"].count())# Contar las canciones reproducidas en cada ciudad


# In[ ]:





# In[ ]:





# `Comenta tus observaciones aquí`

# Según los números Springfield escucha más música que Shelbyville.

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[27]:


print( df.groupby(by="day").count())

#print(df.groupby(by=["city","day"])["track"].count())# Calcular las canciones reproducidas en cada uno de los tres días


# `Comenta tus observaciones aquí`

# El miércoles es cuando más música escuchan en ambas ciudades.Y el lunes es cuando menos canciones se ven registradas.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto, se agruparon los datos de una buena manera. Recomiendo en el segundo ejemplo seleccionar una sola columna para que los resultados sean similares a la agrupación anterior donde usaste 'track'
# </div>
# 

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[39]:


# Declara la función number_tracks() con dos parámetros: day= y city=.
def number_tracks (df,pday,pcity):
    df['day']==pday
    
    #df['day']==pday and df['city']==pcity #haciendo el filtro
    *return df[(df['day'] == pday) & (df['city'] == pcity)]['user_id'].count()
    


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[40]:


day="Monday"
city="Springfield"
spring_Lun =number_tracks (df,day,city)# El número de canciones reproducidas en Springfield el lunes
#print (spring_Lun.count())
print (spring_Lun)




# In[41]:


# El número de c"anciones reproducidas en Shelbyville el lunes
day="Monday"
city="Shelbyville"
shelb_Lun =number_tracks (df,day,city)# El número de canciones reproducidas en Springfield el lunes

print (shelb_Lun)


# In[43]:


# El número de canciones reproducidas en Springfield el miércoles
day="Wednesday"
city="Springfield"
sprin_wedn =number_tracks (df,day,city)# El número de canciones reproducidas en Springfield el lunes

print (sprin_wedn)


# In[46]:


# El número de canciones reproducidas en Shelbyville el miércoles
day="Wednesday"
city="Shelbyville"
shelb_wedn =number_tracks (df,day,city)# El número de canciones reproducidas en Springfield el lunes

print (shelb_wedn)


# In[47]:


# El número de canciones reproducidas en Springfield el viernes
day="Friday"
city="Springfield"
sprin_frid =number_tracks (df,day,city)# El número de canciones reproducidas en Springfield el lunes

print (sprin_frid)


# In[48]:


# El número de canciones reproducidas en Shelbyville el viernes
day="Friday"
city="Shelbyville"
shelb_fri =number_tracks (df,day,city)# El número de canciones reproducidas en Springfield el lunes

print (shelb_fri)


# **Conclusiones**
# 
# `Comenta si la hipótesis es correcta o se debe rechazar. Explica tu razonamiento.`

# In[ ]:


A los ususarios de Shelbyville les gusta escuchar más música a la mitad de la semana , los miércoles.
A los usuarios de Springfield les gusta escuchar más música al inicio y final de la semana, lunes y viernes
Los usuarios de Springfield escuchan más música que los de Shelbyville.


# In[ ]:


Gracias por la retroalimentación ya me sentía muy enfrascada con la función de number_tracks.


# Necesito apoyo en la sintaxis desde la función number_tracks(), me siento algo perdida en el código de como realizarla, me está marcando errores pero no sé como debe ser la manera correcta HELP!. Por lo tanto aún no puedo sacar mis conclusiones

# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Cuidado!<br />
# 
# Te explico lo que se necesita hacer:<br />
# 
# El ejercicio requiere que regreses el numero total de canciones reproducidas por ciudad y por día.<br />
# Pandas nos permite facilmente filtrar los datos usando la siguiente sintaxis:<br /><br />
# 
# <strong>df[(df['day'] == 'Monday')</strong><br /><br />
# 
# De esta manera el resultado que obtenemos es todas las filas que pertenezcan a lunes, NO hay necesidad de hacer un ciclo FOR<br />
#    
# Para filtrar por ciudad es exactamente lo mismo, pero utilizando las columnas respectivas:<br /><br />
# 
# <strong>df[(df['city'] == 'Springfield')</strong><br /><br />
# 
# Ahora, lo que necesitas es juntar ambos filtros, hay muchas maneras de hacerlo, puedes hacer que el dataframe se iguale al filtro siguiente, ejemplo:<br /><br />
# 
# <strong>df = df[(df['day'] == 'Monday')<br />
# df = df[(df['city'] == 'Springfield')</strong><br /><br />
# 
# De esta manera en la primera línea df ya se filtro por 'Monday', y es este mismo dataframe e que se utiliza para filtrar por la ciudad.<br />
#     
# Alternativamente puedes mezclar ambos en una misma línea:<br /><br />
# 
# <strong>df[(df['day'] == 'Monday') & (df['city'] == 'Springfield')]</strong><br />
#     
# Por último lo que necesitas es hacer un conteo de las filas que hay.<br />
# 
# El siguiente es un ejemplo de como puede ser tu función:<br /><br />
# <strong>
# def number_tracks (df,pday,pcity):<br />
#     return df[(df['day'] == pday) & (df['city'] == pcity)]['user_id'].count()<br />
# </strong>
# </div>
# 
# 
# 

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.`

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# [Volver a Contenidos](#back)

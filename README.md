# PI02
Este es el segundo proyecto individual 02- DataPT11
En esta etapa del proyecto, se llevó a cabo el proceso de Extracción, Transformación y Carga (ETL) de los datasets seleccionados. El objetivo principal fue analizar la cantidad de datos y realizar una unión adecuada para mejorar el procesamiento de la información. Como resultado, se generaron cuatro datasets principales: `df_combinado`, `df_nacional`, `df_partidos` y `df_indicadores`. 

Durante la etapa de transformación, se aplicaron diversas técnicas para garantizar la calidad y relevancia de los datos. Se llevaron a cabo acciones como la limpieza de registros duplicados, la normalización de variables y la eliminación de aquellos datos considerados redundantes o irrelevantes para los objetivos del proyecto.

El dataset df_combinado se creó como una combinación de varios datasets, permitiendo un análisis integral de los datos de acceso a internet en Argentina. Por otro lado, df_nacional contiene información específica a nivel nacional, mientras que df_partidos se enfoca en los datos a nivel de partidos y localidades. y por ultimo df_combinado contiene datos de las provincias. 

Es importante destacar que la selección y descarte de datasets se realizó de manera cuidadosa, teniendo en cuenta la calidad y pertinencia de la información para este proyecto en particular.

Con la finalización de la etapa de ETL, los datasets resultantes están listos para ser utilizados en el siguiente paso del análisis, donde se buscarán relaciones, patrones y se generarán insights significativos.

# EDA - Análisis Exploratorio de los datos

En este proyecto de análisis de datos, se exploran y analizan cuatro dataframes diferentes: `df_combinado`, `df_nacional`y `df_partidos`. Cada uno de ellos proporciona información relevante sobre distintos aspectos relacionados con las conexiones de internet, indicadores económicos y datos demográficos en Argentina.

## Conceptos relevantes para el análisis de los datos
- **ADSL**: ADSL (Asymmetric Digital Subscriber Line) es una tecnología de conexión a Internet de banda ancha que utiliza líneas telefónicas para transmitir datos. Proporciona una velocidad de descarga más rápida en comparación con la velocidad de carga. Es ampliamente utilizado en hogares y pequeñas empresas.

- **Cablemodem**: El cablemodem es un dispositivo que permite la conexión a Internet a través de las redes de cable de televisión. Utiliza la infraestructura de televisión por cable para transmitir datos de alta velocidad. Es una opción popular para conexiones de Internet de alta velocidad en hogares y negocios.

- **Fibra óptica**: La fibra óptica es una tecnología de transmisión de datos que utiliza hilos delgados de vidrio o plástico para transmitir señales de luz. Proporciona velocidades de conexión extremadamente rápidas y mayor capacidad de ancho de banda en comparación con otras tecnologías. La fibra óptica es conocida por su alta velocidad y estabilidad, y es utilizada en conexiones de Internet de alta velocidad y redes de telecomunicaciones.

- **Wireless**: Wireless, también conocido como conexión inalámbrica, se refiere a la tecnología que permite la transmisión de datos sin cables físicos. Utiliza ondas de radio o señales de infrarrojos para enviar y recibir datos. Las conexiones inalámbricas son ampliamente utilizadas en dispositivos móviles, como teléfonos inteligentes, tabletas y computadoras portátiles, así como en redes Wi-Fi para acceder a Internet.

--

- **Banda ancha fija**: La banda ancha fija se refiere a una conexión de Internet de alta velocidad y constante que utiliza cables físicos, como cables coaxiales o fibra óptica, para transmitir datos. Proporciona una velocidad de conexión más rápida y estable en comparación con las conexiones de acceso telefónico, lo que permite una transferencia eficiente de datos y un acceso rápido a Internet. Ejemplos: ADSL, Cablemodem, Fibra óptica.

- **Dial up**: Dial up es una forma de conexión a Internet que utiliza una línea telefónica y un módem para establecer una conexión temporal. Requiere marcar un número telefónico y establecer una conexión punto a punto con un proveedor de servicios de Internet (ISP). Sin embargo, las conexiones de acceso telefónico son más lentas en comparación con las tecnologías modernas, como la banda ancha, y están siendo reemplazadas por opciones de conexión más rápidas. Ejemplos: ISDN (Integrated Services Digital Network) y modem de acceso telefónico.

--

- **Mbps (Media de bajada)**: Mbps (Megabits por segundo) es una unidad de medida utilizada para expresar la velocidad de transferencia de datos en una conexión a Internet. Representa la cantidad de megabits que pueden ser transferidos por segundo. La velocidad de bajada se refiere a la velocidad a la cual los datos pueden ser descargados desde Internet hacia el dispositivo del usuario. Cuanto mayor sea el valor de Mbps, más rápido será el proceso de descarga de datos.


A continuación, se presenta una descripción detallada de cada dataframe y los principales hallazgos encontrados en el análisis.

## df_combinado

El dataframe `df_combinado` contiene datos relacionados con los tipos de conexiones de internet, tanto en términos de cantidad como de velocidades. A continuación se enumeran algunas de las columnas importantes en este dataframe:

- adsl, cablemodem, fibra óptica, wireless, Otros: Cantidad de conexiones de cada tipo.
- accesos por cada 100 hogares: Número de accesos a internet por cada 100 hogares.
- Total_conexion: Total de conexiones de internet registradas.

## df_nacional

El dataframe `df_nacional` proporciona información a nivel nacional sobre las conexiones de internet y algunos indicadores económicos. A continuación se destacan algunas columnas clave:

- banda ancha fija, dial up, mbps (Media de bajada): Cantidad de conexiones según el tipo.
- ingresos (miles de pesos): Ingresos económicos registrados.
- adsl, cablemodem, fibra óptica, wireless, Otras conexiones, total de conexiones de cada tipo.

## df_partidos

El dataframe `df_partidos` contiene datos específicos sobre los diferentes partidos y localidades de Argentina. Algunas columnas relevantes son:

- Provincia, Partido, Localidad: Información geográfica de los datos.
- ADSL, CableModem, Fibra Optica, Otras conexiones: Cantidad de conexiones según el tipo.
- Poblacion: Número de habitantes registrados.

## ETL

El archivo ETL contiene las distintas transformaciones de los distintos df, como por ejemplo eliminacion de datos duplicados, datos nulos, vacios. ademas de las uniones de los archivos .csv.

## EDA

tratamos en el eda de realizar suficientes analisis para poder decidir cuales era los kpi que podriamos realizar en un futuro

## Conclusiones

si bien se han estudiado las distintas formas de conexiones utilizadas en argentina desde 2017 la que mas ah crecido y demostrado que es la mas elegida los ultimos años es la de fibra optica, ya que permite una mayor velocidad, mas estabilidad en la continuidad del plan elegido, asimismo notamos que aun en muchas provincias no se llegan a los mismos valores, ya que hay muchas zonas rurales y zonas urbanas en el interior del pais que aun no se instalaron muchas conexiones de fibra optica. 

A pesar de todo sigue siendo la forma mas rentable el invertir en conexion de fibra optica.

# Ejercicios básicos en R

# Calculadora simple
# Realizamos operaciones aritméticas directamente en la consola

3 + 5 * 2  # Multiplicación tiene precedencia, el resultado es 13
10^2       # Elevamos 10 al cuadrado, el resultado es 100
sqrt(144)  # Calculamos la raíz cuadrada de 144, el resultado es 12
log(pi)    # Calculamos el logaritmo natural (base e) de la constante pi (π ≈ 3.14159), el resultado es aproximadamente 1.14473

# Asignación de variables
# Asignamos el valor 100 a la variable 'a' usando el operador de asignación '<-'

a <- 100

# Imprimimos el valor de la variable 'a' en la consola
a

# Recalculamos el valor de 'a' sumándole 50 a su valor actual
a <- a + 50

# Volvemos a imprimir el valor actualizado de 'a'
a

# Vectores numéricos
# Creamos un vector numérico llamado 'v' que contiene los elementos 10, 20, 30, 40 y 50
v <- c(10, 20, 30, 40, 50)

# Mostramos la longitud del vector 'v', es decir, el número de elementos que contiene
length(v)

# Multiplicamos cada elemento del vector 'v' por 2
v * 2

# Sumamos 5 a cada elemento del vector 'v'
v + 5

# Funciones elementales
# Aplicamos algunas funciones estadísticas básicas al vector 'v'

mean(v) # Calcula la media (promedio) de los elementos de 'v'
sum(v)  # Calcula la suma de todos los elementos de 'v'
min(v)  # Encuentra el valor mínimo dentro de 'v'
max(v)  # Encuentra el valor máximo dentro de 'v'
sd(v)   # Calcula la desviación estándar de los elementos de 'v', una medida de dispersión

# ¿Qué sucede si insertas un NA en v y vuelves a calcular mean(v)?
# 'NA' representa un valor faltante (Not Available)

v_con_na <- c(10, 20, 30, NA, 50)
mean(v_con_na) # El resultado será NA, ya que la función mean no puede calcular la media con valores faltantes por defecto

# Prueba luego con mean(v, na.rm = TRUE).
# El argumento 'na.rm = TRUE' le indica a la función mean que ignore los valores NA al realizar el cálculo

mean(v_con_na, na.rm = TRUE) # El resultado será la media de los valores no faltantes (10, 20, 30, 50), que es 27.5

# Indexación básica
# Accedemos a elementos específicos de un vector utilizando su índice (posición)

# Extrae el tercer elemento de v
v[3] # Los índices en R comienzan en 1, por lo que el tercer elemento es 30

# Extrae los elementos de la 2ª a la 4ª posición
v[2:4] # Usamos el operador ':' para crear una secuencia de índices del 2 al 4, resultando en los elementos 20, 30 y 40

# Operaciones lógicas
# Creamos un vector 'w' y luego aplicamos un filtro lógico

w <- c(5, 15, 25, 35, 45)

# Crea un filtro 'sel' que es un vector lógico (TRUE/FALSE) indicando qué elementos de 'w' son mayores que 20
sel <- w > 20
sel # Muestra el vector de booleanos: FALSE FALSE  TRUE  TRUE  TRUE

# Aplica el filtro 'sel' a 'w' para extraer solo los elementos donde 'sel' es TRUE
w[sel] # Esto devuelve los elementos de 'w' que son mayores que 20: 25, 35, 45

# Usa which() para obtener los índices donde w == 25
which(w == 25) # La función which() devuelve los índices donde la condición (w == 25) es TRUE. En este caso, el resultado es 3 (el tercer elemento)

# Redondeo
# Utilizamos la función round() para redondear el valor de pi a diferentes números de decimales

pi # Muestra el valor de la constante pi (π ≈ 3.14159265359)

round(pi, 0) # Redondea pi a 0 decimales, resultando en 3
round(pi, 1) # Redondea pi a 1 decimal, resultando en 3.1
round(pi, 3) # Redondea pi a 3 decimales, resultando en 3.142

# Secuencias y repeticiones
# Generamos secuencias de números y repetimos patrones

# Genera una secuencia de números que comienza en 0, termina en 1 y tiene un incremento de 0.2
seq(0, 1, by = 0.2) # El resultado es: 0.0 0.2 0.4 0.6 0.8 1.0

# Repite la secuencia 1:3 (que es 1, 2, 3) cada elemento 4 veces
rep(1:3, each = 4) # El resultado es: 1 1 1 1 2 2 2 2 3 3 3 3

# Uso de paste()
# Concatenamos cadenas de texto (strings)

# Junta "Hola" y "mundo" con un espacio como separador (por defecto)
paste("Hola", "mundo") # El resultado es: "Hola mundo"

# Junta "Hola" y "mundo" sin ningún separador
paste0("Hola", "mundo") # El resultado es: "Holamundo"

# Primer histograma
# Creamos un vector de 100 números aleatorios que siguen una distribución normal y luego dibujamos un histograma

# Genera 100 números aleatorios de una distribución normal estándar (media 0, desviación estándar 1)
v <- rnorm(100)

# Dibuja un histograma de los valores en el vector 'v'
hist(v) # Al ejecutar esta línea, se abrirá una ventana gráfica mostrando el histograma.
# El histograma muestra la frecuencia de los valores en diferentes rangos,
# y para datos generados de una distribución normal, debería tener una forma de campana.

# Ejercicios intermedios en R

# Cuantiles y resumen
# Generamos un vector 'v' con 200 números aleatorios de una distribución normal

v <- rnorm(200)

# Calculamos los cuantiles de 'v' con la función quantile()
quantile(v)
# Por defecto, quantile() muestra los valores mínimo (0%), primer cuartil (25%),
# mediana (50%), tercer cuartil (75%) y máximo (100%).
# Los cuartiles dividen los datos ordenados en cuatro partes iguales.
# - El primer cuartil (Q1) indica el valor por debajo del cual se encuentra el 25% de los datos.
# - La mediana (Q2 o segundo cuartil) es el valor central; el 50% de los datos está por debajo y el 50% por encima.
# - El tercer cuartil (Q3) indica el valor por debajo del cual se encuentra el 75% de los datos.

# Obtenemos un resumen estadístico de 'v' con la función summary()
summary(v)
# summary() proporciona información descriptiva como el mínimo, primer cuartil, mediana,
# media, tercer cuartil y máximo.

# ¿Qué indican los cuartiles?
# Los cuartiles nos dan una idea de la distribución y la dispersión de los datos.
# - El rango intercuartílico (IQR = Q3 - Q1) mide la dispersión del 50% central de los datos.
# - Comparar las distancias entre el mínimo y Q1, Q1 y la mediana, la mediana y Q3, y Q3 y el máximo
#   puede dar una idea de la simetría de la distribución.

# Ordenación y rangos
# Creamos un vector 'w' con 10 números aleatorios únicos entre 1 y 20

w <- sample(1:20, 10)
w # Mostramos el vector original

# Ordenamos 'w' en orden creciente usando sort()
sort(w)

# Ordenamos 'w' en orden decreciente usando sort() con el argumento decreasing = TRUE
sort(w, decreasing = TRUE)

# Obtenemos el orden de los índices que producirían un vector ordenado con order()
order(w)
# order() devuelve un vector de índices. Si usamos estos índices para acceder a los elementos de 'w',
# obtendremos el vector ordenado en orden creciente: w[order(w)]

# Obtenemos los rangos de cada elemento de 'w' con rank()
rank(w, ties.method = "min")
# rank() asigna un rango a cada valor en el vector.
# El argumento ties.method = "min" especifica que en caso de empates (valores iguales),
# se asigne el rango más bajo posible.

# Manejo de NA
# Creamos un vector 'u' que contiene algunos valores NA (Not Available)

u <- c(NA, 2, NA, 5, 8, NA)
u # Mostramos el vector con valores NA

# Contamos el número de valores NA en 'u' usando sum(is.na(u))
is.na(u) # is.na() devuelve un vector lógico (TRUE/FALSE) donde TRUE indica la presencia de un NA
sum(is.na(u)) # TRUE se interpreta como 1 y FALSE como 0, por lo que sum() cuenta los TRUEs (los NAs)

# Eliminamos los valores NA de 'u' usando indexación lógica con !is.na(u)
u[!is.na(u)] # !is.na(u) invierte el vector lógico de is.na(u), seleccionando solo los valores que NO son NA

# Tablas y frecuencias
# Creamos un factor 'colores' con repeticiones de diferentes colores

colores <- factor(c("rojo", "azul", "rojo", "verde", "azul"))
colores # Mostramos el factor

# Generamos una tabla de frecuencias de los niveles del factor 'colores' con table()
table(colores)
# table() muestra cuántas veces aparece cada nivel (categoría) en el factor.

# Matrices y apply()
# Construimos una matriz 'm' de 3 filas y 4 columnas, llenada con los números del 1 al 12 por filas

m <- matrix(1:12, nrow = 3, byrow = TRUE)
m # Mostramos la matriz

# Usamos apply() para calcular la suma de cada fila (margen 1) de la matriz 'm'
apply(m, 1, sum)
# apply(matriz, margen, función) aplica la 'función' a las filas (margen 1) o columnas (margen 2) de la 'matriz'.

# Usamos apply() para calcular la media de cada columna (margen 2) de la matriz 'm'
apply(m, 2, mean)

# Listas
# Creamos una lista 'l' que contiene diferentes tipos de datos con nombres

l <- list(nombre = "Ana", edades = c(20, 30, 40), activo = TRUE)
l # Mostramos la lista

# Accedemos al elemento llamado "nombre" de la lista usando el operador '$'
l$nombre

# Accedemos al segundo elemento del vector "edades" dentro de la lista
l$edades[2]

# Data frame simple
# Construimos un data frame 'df' con una columna 'id' y una columna 'score' con números aleatorios

df <- data.frame(id = 1:5, score = rnorm(5))
df # Mostramos el data frame

# Añadimos una nueva columna llamada 'passed' al data frame 'df'
# Esta columna será TRUE si el valor en la columna 'score' es mayor que 0, y FALSE en caso contrario
df$passed <- df$score > 0
df # Mostramos el data frame con la nueva columna

# Funciones propias
# Escribimos una función llamada 'f' que toma un argumento 'x' y devuelve x^2 + 2*x + 1

f <- function(x) x^2 + 2 * x + 1
# La sintaxis para definir una función es: nombre_funcion <- function(argumentos) { cuerpo_de_la_funcion }

# Probamos la función 'f' con el valor 5
f(5) # Esto calculará 5^2 + 2*5 + 1 = 25 + 10 + 1 = 36

# Usamos sapply() para aplicar la función 'f' a cada elemento del vector 1:10
sapply(1:10, f)
# sapply() es una función que aplica una función a cada elemento de un vector o lista y devuelve un vector o matriz con los resultados.

# Control de flujo
# Implementamos un bucle 'for' para calcular los primeros 10 factoriales

factoriales <- numeric(10) # Creamos un vector numérico vacío para almacenar los factoriales
factorial_actual <- 1

for (i in 1:10) {
  factorial_actual <- factorial_actual * i
  factoriales[i] <- factorial_actual
}

factoriales # Mostramos el vector de factoriales

# Reescribimos el cálculo del factorial con un bucle 'while' hasta que el factorial sea mayor que 1e5 (100,000)

factorial_while <- 1
n <- 1

while (factorial_while <= 1e5) {
  factorial_while <- factorial_while * n
  print(paste("Factorial de", n, "es:", factorial_while)) # Imprimimos cada factorial calculado
  n <- n + 1
}

# Factores ordenados
# Creamos un factor ordenado 'talla' con niveles definidos

talla <- factor(c("S", "M", "L", "M", "S"), levels = c("S", "M", "L"), ordered = TRUE)
talla # Mostramos el factor ordenado

# Comprobamos qué elementos de 'talla' son mayores que "M"
talla > "M"
# En un factor ordenado, las comparaciones se realizan según el orden de los niveles.
# "L" es mayor que "M", pero "S" y "M" no lo son.

# Ejercicios avanzados en R

# tapply() en agrupaciones
# Creamos un data frame con un factor 'grupo' y valores numéricos 'valor'
df <- data.frame(grupo = rep(LETTERS[1:3], each = 5), valor = rnorm(15))
df # Mostramos el data frame

# Usamos tapply() para calcular la media de la columna 'valor' para cada nivel del factor 'grupo'
tapply(df$valor, df$grupo, mean)
# tapply(x, index, fun) aplica la función 'fun' a los subconjuntos de 'x' definidos por los niveles de 'index'.
# En este caso, calcula la media de 'valor' para cada grupo en 'grupo'.

# Funciones anónimas
# Aplicamos una función anónima (sin nombre) a cada número del 1 al 5 usando sapply()
sapply(1:5, function(x) ifelse(x %% 2 == 0, "par", "impar"))
# function(x) ... define una función que toma un argumento 'x'.
# ifelse(condicion, valor_si_true, valor_si_false) evalúa la condición y devuelve el valor correspondiente.
# x %% 2 == 0 verifica si 'x' es divisible por 2 (es par).

# Expresiones regulares
# Definimos un texto que contiene URLs
text <- "Visita http://example.com y https://r-project.org"
text # Mostramos el texto original

# Eliminamos las URLs del texto usando gsub() y una expresión regular
gsub("http(s)?://[^[:space:]]+", "", text)
# gsub(pattern, replacement, x) busca el 'pattern' en la cadena 'x' y lo reemplaza con 'replacement'.
# La expresión regular "http(s)?://[^[:space:]]+" busca:
# - "http" seguido opcionalmente de "s" (http o https)
# - "://" seguido de uno o más caracteres que no sean espacios en blanco "[^[:space:]]+"

# cut() y cuantiles
# Generamos 100 números aleatorios de una distribución normal
datos <- rnorm(100)

# Calculamos los cuartiles de los datos
cuartiles <- quantile(datos)
cuartiles # Mostramos los valores de los cuartiles

# Dividimos los datos en cuartiles usando cut()
cortes_cuartiles <- cut(datos, breaks = cuartiles, labels = FALSE, include.lowest = TRUE)
# cut(x, breaks, labels, include.lowest) divide el vector 'x' en intervalos definidos por 'breaks'.
# labels = FALSE asigna números enteros a los intervalos.
# include.lowest = TRUE incluye el valor mínimo en el primer intervalo.
table(cortes_cuartiles) # Mostramos la frecuencia de los datos en cada cuartil (aproximadamente igual)

# Fechas y horas
# Convertimos una cadena de texto a un objeto de clase Date
fecha_string <- "21/04/2025"
fecha_objeto <- as.Date(fecha_string, format = "%d/%m/%Y")
fecha_objeto # Mostramos el objeto Date
# as.Date(x, format) convierte 'x' a un objeto Date según el formato especificado.
# "%d" para el día, "%m" para el mes y "%Y" para el año con cuatro dígitos.

# Sumamos 30 días a la fecha convertida
fecha_futura <- fecha_objeto + 30
fecha_futura

# Calculamos la diferencia en días entre la fecha futura y la fecha actual del sistema
diferencia_dias <- fecha_futura - Sys.Date()
diferencia_dias
# Sys.Date() devuelve la fecha actual del sistema.
# La resta de objetos Date da como resultado un objeto difftime, que representa una diferencia de tiempo.

# Complejos y módulo
# Definimos un número complejo 'z'
z <- 3 + 4i
z # Mostramos el número complejo

# Obtenemos el módulo (magnitud) de 'z' con Mod()
modulo_z <- Mod(z)
modulo_z # El módulo es sqrt(Re(z)^2 + Im(z)^2) = sqrt(3^2 + 4^2) = sqrt(25) = 5

# Obtenemos el argumento (ángulo en radianes) de 'z' con Arg()
argumento_z <- Arg(z)
argumento_z # El argumento es atan(Im(z) / Re(z))

# Dibujamos el punto (Re(z), Im(z)) en un plot
plot(Re(z), Im(z), pch = 19, col = "blue", xlab = "Parte Real", ylab = "Parte Imaginaria",
     main = "Representación de un número complejo")
abline(h = 0, v = 0, lty = 3) # Añadimos ejes de referencia
text(Re(z) + 0.2, Im(z), labels = paste("3 + 4i")) # Etiquetamos el punto

# Pila con RC (Reference Classes)
# Definimos una clase Stack usando Reference Classes
Stack <- setRefClass("Stack",
                     fields = list(items = "list"),
                     methods = list(
                       put = function(item) {
                         items <<- c(items, list(item)) # Añadimos un elemento al final de la lista
                       },
                       pop = function() {
                         if (length(items) > 0) {
                           last_item <- items[[length(items)]] # Obtenemos el último elemento
                           items <<- items[-length(items)]    # Eliminamos el último elemento
                           return(last_item)
                         } else {
                           stop("La pila está vacía")
                         }
                       },
                       size = function() {
                         return(length(items)) # Devuelve el número de elementos en la pila
                       }
                     ))

# Creamos una instancia de la clase Stack
mi_pila <- Stack$new()

# Usamos los métodos de la pila
mi_pila$put(10)
mi_pila$put(20)
mi_pila$size()
mi_pila$pop()
mi_pila$size()

# Histogramas avanzados
# Generamos 1000 números aleatorios de una distribución normal
datos_hist <- rnorm(1000)

# Dibujamos histogramas con diferentes números de bins
hist(datos_hist, breaks = 10, main = "Histograma con 10 bins")
hist(datos_hist, breaks = 50, main = "Histograma con 50 bins")
hist(datos_hist, breaks = 100, main = "Histograma con 100 bins")
# El argumento 'breaks' controla el número de barras (bins) en el histograma, afectando la visualización de la distribución.

# Programación vectorizada vs bucles
# Creamos vectores de diferentes tamaños
tamanios <- 10^c(1, 3, 6)
resultados_tiempo <- list()

for (n in tamanios) {
  x <- 1:n
  
  # Medición con sapply (vectorizado)
  tiempo_sapply_inicio <- Sys.time()
  resultado_sapply <- sapply(x, function(val) val^3 + val^2 + 1 / (val + 10))
  tiempo_sapply_fin <- Sys.time()
  tiempo_sapply <- tiempo_sapply_fin - tiempo_sapply_inicio
  
  # Medición con bucle for
  tiempo_for_inicio <- Sys.time()
  resultado_for <- numeric(n)
  for (i in 1:n) {
    resultado_for[i] <- x[i]^3 + x[i]^2 + 1 / (x[i] + 10)
  }
  tiempo_for_fin <- Sys.time()
  tiempo_for <- tiempo_for_fin - tiempo_for_inicio
  
  resultados_tiempo[[as.character(n)]] <- data.frame(
    Tamanio = n,
    Tiempo_sapply = as.numeric(tiempo_sapply),
    Tiempo_for = as.numeric(tiempo_for)
  )
}

resultados_tiempo_df <- do.call(rbind, resultados_tiempo)
print(resultados_tiempo_df)
# Generalmente, las operaciones vectorizadas con sapply (y otras funciones como apply, lapply, etc.)
# son más eficientes en R que los bucles explícitos, especialmente para vectores grandes, debido a la
# optimización interna en C/Fortran.

# Función de orden superior
# Definimos una función 'dualize' que toma una función 'f' y devuelve una nueva función que aplica 'f' dos veces

dualize <- function(f) {
  function(x) f(f(x))
}

# Probamos 'dualize' con la función sqrt (raíz cuadrada)
raiz_doble <- dualize(sqrt)
raiz_doble(16) # sqrt(sqrt(16)) = sqrt(4) = 2

# Probamos 'dualize' con la función log (logaritmo natural)
log_doble <- dualize(log)
log_doble(exp(exp(2))) # log(log(exp(exp(2)))) = log(exp(2)) = 2
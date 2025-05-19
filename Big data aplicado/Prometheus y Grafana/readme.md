# Ejercicio 5: Preguntas teóricas sobre Prometheus

### 1. ¿Cuál es la diferencia entre un **Counter** y un **Gauge**?

- **Counter**:  
  - Solo puede **incrementar** (o resetear a cero al reiniciar).  
  - Mide valores acumulativos como número total de peticiones o errores.  
  - Ejemplo: `http_requests_total`.

- **Gauge**:  
  - Puede **subir y bajar** libremente.  
  - Mide valores variables en el tiempo, como uso de memoria o peticiones en curso.  
  - Ejemplo: `http_requests_in_flight`.

---

### 2. ¿Por qué Prometheus hace **scraping** en lugar de usar **push**?

- Control centralizado: el servidor decide cuándo y qué métrica recolectar.  
- Facilidad para manejar firewalls y redes (el servidor accede a los targets).  
- Soporta detección automática y ajustes dinámicos.  
- Garantiza consistencia temporal en la recolección de datos.

> Para casos especiales, Prometheus puede usar **Pushgateway** para recibir métricas push.

---

### 3. ¿Qué ventaja tiene usar **Histogram** frente a un simple **Gauge** para medir latencias?

- **Gauge** solo mide un valor puntual de latencia.  
- **Histogram** captura la **distribución completa** de latencias divididas en buckets.  
- Permite calcular percentiles (p50, p95, p99), medias y totales.  
- Ofrece análisis más profundo del rendimiento.

---

### 4. ¿Qué problemas podrían surgir si usas muchas **etiquetas dinámicas** (por ejemplo, user ID)?

- Alta cardinalidad, creando muchas series métricas únicas.  
- Consumo excesivo de memoria y almacenamiento.  
- Degradación del rendimiento en consultas y scrape.  
- Riesgo de agotamiento de recursos y caídas.  
- Dificultad para analizar datos debido al ruido y volumen.

> Se recomienda evitar etiquetas con valores altamente variables y usar agregaciones cuando sea posible.

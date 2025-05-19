const express = require('express');
const { register, requestCounter, durationHistogram, inFlightGauge } = require('./metrics');

const app = express();
const PORT = 8080;

// Middleware para métricas en vuelo
app.use((req, res, next) => {
  inFlightGauge.inc();
  res.on('finish', () => {
    inFlightGauge.dec();
  });
  next();
});

app.get('/cities', (req, res) => {
  const start = Date.now();

  // Simulación de datos
  const cities = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla'];
  res.json(cities);

  // Métricas
  requestCounter.inc({ route: '/cities', method: req.method });
  durationHistogram.observe({ route: '/cities', method: req.method }, (Date.now() - start) / 1000);
});

// Endpoint de métricas para Prometheus
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});

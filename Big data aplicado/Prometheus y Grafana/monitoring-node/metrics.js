const client = require('prom-client');

// Registro global de métricas
const register = new client.Registry();

// Contador de peticiones
const requestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Número total de peticiones HTTP',
  labelNames: ['method', 'route']
});

// Histograma de duración
const durationHistogram = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duración de las peticiones HTTP en segundos',
  labelNames: ['method', 'route'],
  buckets: [0.1, 0.5, 1, 2, 5]
});

// Gauge para peticiones en vuelo
const inFlightGauge = new client.Gauge({
  name: 'http_requests_in_flight',
  help: 'Número de peticiones en curso'
});

// Registrar todas las métricas en el registry
register.registerMetric(requestCounter);
register.registerMetric(durationHistogram);
register.registerMetric(inFlightGauge);
client.collectDefaultMetrics({ register });

module.exports = {
  register,
  requestCounter,
  durationHistogram,
  inFlightGauge
};

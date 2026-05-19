# \# DataOps — E-commerce Price Intelligence Platform

# 

# \## Mon rôle

# Je suis responsable DataOps : infrastructure, automatisation, monitoring et qualité des données.

# 

# \## Structure du repo

# \- `docker-compose.yml` : lance tous les services du projet

# \- `.github/workflows/ci.yml` : pipeline CI/CD automatique

# \- `monitoring/prometheus.yml` : collecte des métriques

# \- `monitoring/grafana/` : dashboards de visualisation

# 

# \## Lancer le projet

# ```bash

# docker compose up -d

# ```

# 

# \## Services

# | Service | Port | Description |

# |---|---|---|

# | Apache NiFi | 8443 | Ingestion temps réel |

# | Apache Airflow | 8080 | Orchestration batch |

# | Prometheus | 9090 | Monitoring |

# | Grafana | 3000 | Dashboard |


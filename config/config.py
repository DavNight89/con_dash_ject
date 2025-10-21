# Construction Project Dashboard Configuration

PROJECT_CONFIG = {
    "project_name": "Commercial Building Construction",
    "project_start_date": "2024-01-15",
    "project_end_date": "2024-12-20",
    "total_budget": 5000000,  # $5M
    "currency": "USD",
    "timezone": "UTC"
}

# KPI Thresholds
KPI_THRESHOLDS = {
    "schedule": {
        "spi_good": 1.0,
        "spi_warning": 0.95,
        "days_variance_good": 0,
        "days_variance_warning": -10
    },
    "cost": {
        "cpi_good": 1.0,
        "cpi_warning": 0.95,
        "cost_variance_good": 0
    },
    "safety": {
        "days_since_incident_good": 30,
        "days_since_incident_warning": 14,
        "trir_good": 2.0,
        "trir_warning": 3.0
    },
    "quality": {
        "inspection_pass_rate_good": 85,
        "inspection_pass_rate_warning": 75,
        "punch_list_threshold": 20
    },
    "productivity": {
        "equipment_utilization_target": 80,
        "material_waste_target": 5
    }
}

# Chart Colors
COLORS = {
    "primary": "#1f4e79",
    "secondary": "#4a90d9",
    "success": "#28a745",
    "warning": "#ffc107",
    "danger": "#dc3545",
    "info": "#17a2b8"
}
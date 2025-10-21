# 🏗️ Construction Project Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF6C37)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.15%2B-3F4F75)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **An interactive web dashboard for tracking construction project Key Performance Indicators (KPIs)**

This project demonstrates expertise in **data visualization**, **business intelligence**, and **construction project management** through a comprehensive dashboard built with Python, Streamlit, and Plotly.

![Dashboard Preview](https://via.placeholder.com/800x400/1f4e79/ffffff?text=Construction+Dashboard+Preview)

## ✨ **Live Demo**

🌐 **[View Live Dashboard](https://your-app-url.streamlit.app)** *(Deploy to get live URL)*

## 🎯 **Key Highlights**

- 📊 **Professional KPI Tracking** - Industry-standard construction metrics
- 🎮 **Interactive Visualizations** - Dynamic charts with hover details  
- 📈 **Real-time Calculations** - Automated SPI, CPI, and TRIR computations
- 🎨 **Executive Dashboard** - Color-coded status indicators and trends
- 📋 **Excel Integration** - Professional templates for offline use
- 🏗️ **Realistic Data** - 40 weeks of simulated construction project data

## 📊 Features

### Schedule Performance Metrics
- **Planned % Complete vs. Actual % Complete** - Visual comparison of project progress
- **Schedule Performance Index (SPI)** - Earned Value / Planned Value calculation
- **Days Ahead/Behind Schedule** - Timeline variance tracking
- **Critical Path Tasks Status** - Task progress monitoring with Gantt-style visualization

### Cost Performance Metrics
- **Budget vs. Actual Spending** - Financial performance tracking
- **Cost Performance Index (CPI)** - Earned Value / Actual Cost calculation
- **Forecasted Cost at Completion** - Project cost projections
- **Cost Variance by Category** - Detailed cost breakdown analysis

### Productivity Metrics
- **Labor Hours per Unit of Work** - Efficiency tracking
- **Equipment Utilization Rate** - Asset performance monitoring
- **Material Waste Percentage** - Resource optimization tracking

### Safety Metrics
- **Days Since Last Incident** - Safety performance tracking
- **Total Recordable Incident Rate (TRIR)** - Industry-standard safety metric
- **Near-Miss Reports** - Proactive safety monitoring

### Quality Metrics
- **Punch List Items** - Quality issue tracking
- **Inspection Pass Rate** - Quality assurance metrics
- **Rework Costs** - Quality impact on budget

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
1. Double-click `setup.bat` to install dependencies and generate sample data
2. Double-click `run_dashboard.bat` to launch the dashboard
3. Open your web browser to the displayed URL (typically http://localhost:8501)

### Option 2: Manual Setup
1. Install Python (3.8 or higher)
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate sample data:
   ```bash
   python src/data_generator.py
   ```
4. Run the dashboard:
   ```bash
   streamlit run src/dashboard.py
   ```

## 📁 Project Structure

```
con_dash_ject/
│
├── src/
│   ├── dashboard.py          # Main Streamlit dashboard application
│   └── data_generator.py     # Generates realistic construction project data
│
├── data/                     # Generated CSV data files (created after running setup)
│   ├── schedule_data.csv     # Schedule performance data
│   ├── cost_data.csv         # Cost performance data
│   ├── productivity_data.csv # Productivity metrics data
│   ├── safety_data.csv       # Safety metrics data
│   ├── quality_data.csv      # Quality metrics data
│   ├── critical_path_tasks.csv # Critical path tasks
│   └── cost_breakdown.csv    # Cost breakdown by category
│
├── config/
│   └── config.py            # Configuration settings and thresholds
│
├── setup.bat                # Windows setup script
├── run_dashboard.bat        # Windows run script
├── requirements.txt         # Python package dependencies
└── README.md               # This file
```

## 🎯 Key Performance Indicators (KPIs)

### Schedule Performance Index (SPI)
- **Formula:** Earned Value ÷ Planned Value
- **Interpretation:** 
  - SPI > 1.0: Project ahead of schedule
  - SPI = 1.0: Project on schedule
  - SPI < 1.0: Project behind schedule

### Cost Performance Index (CPI)
- **Formula:** Earned Value ÷ Actual Cost
- **Interpretation:**
  - CPI > 1.0: Project under budget
  - CPI = 1.0: Project on budget
  - CPI < 1.0: Project over budget

### Total Recordable Incident Rate (TRIR)
- **Formula:** (Number of recordable incidents × 200,000) ÷ Total hours worked
- **Benchmark:** Industry average is typically around 2.0

## 🛠️ Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework for data science
- **Plotly** - Interactive data visualization
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib/Seaborn** - Additional plotting capabilities

## 📈 Sample Project Scenario

The dashboard simulates a **Commercial Building Construction** project with the following characteristics:

- **Timeline:** January 2024 - December 2024 (12 months)
- **Budget:** $5,000,000
- **Project Type:** Commercial building construction
- **Key Phases:** Site preparation, foundation, structural steel, MEP systems, interior finishes
- **Team Size:** ~50-100 workers (varying by phase)
- **Equipment:** Multiple pieces of construction equipment with utilization tracking

## 🔧 Customization

### Adding Your Own Data
1. Replace the CSV files in the `data/` directory with your actual project data
2. Ensure the column names match the expected format (see `data_generator.py` for reference)
3. Adjust thresholds in `config/config.py` to match your project requirements

### Modifying KPI Thresholds
Edit `config/config.py` to adjust warning and target thresholds for different metrics:

```python
KPI_THRESHOLDS = {
    "schedule": {
        "spi_good": 1.0,
        "spi_warning": 0.95,
        # ... other thresholds
    }
}
```

## 🎮 Dashboard Navigation

The dashboard includes several sections accessible via the sidebar:

1. **Overview** - High-level KPI summary with key charts
2. **Schedule Performance** - Detailed schedule analysis
3. **Cost Performance** - Comprehensive cost tracking
4. **Productivity** - Productivity metrics and trends
5. **Safety** - Safety performance monitoring
6. **Quality** - Quality assurance tracking
7. **Critical Path** - Critical path tasks and timeline

## 📊 Business Intelligence Features

- **Real-time KPI Cards** - Color-coded status indicators
- **Interactive Charts** - Hover for detailed information
- **Date Range Filtering** - Focus on specific time periods
- **Responsive Design** - Works on desktop and tablet devices
- **Export Capabilities** - Charts can be saved as images

## 🚦 Status Indicators

- 🟢 **Green** - Performance meeting or exceeding targets
- 🟡 **Yellow** - Performance below target but within warning threshold
- 🔴 **Red** - Performance significantly below target requiring attention

## 📝 Future Enhancements

Potential areas for expansion:
- Real-time data integration from project management systems
- Advanced analytics and predictive modeling
- Mobile-responsive design improvements
- Additional construction-specific metrics
- Integration with IoT sensors for real-time productivity tracking
- Automated reporting and alerts

## 🤝 Contributing

This project is designed as a demonstration of construction project dashboard capabilities. Feel free to fork and adapt it for your specific needs.

## 📄 License

This project is provided as-is for educational and demonstration purposes.

---

**Created for demonstrating skills in:**
- Data Visualization with Python
- Business Intelligence Dashboard Development
- Construction Industry KPI Understanding
- Interactive Web Application Development
- Data Analysis and Reporting

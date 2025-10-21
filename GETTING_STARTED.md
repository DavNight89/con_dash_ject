# 🏗️ Construction Dashboard - Getting Started Guide

## Project Overview

This project creates a comprehensive interactive dashboard for tracking construction project Key Performance Indicators (KPIs). It demonstrates expertise in:

- **Data Visualization** with Python (Plotly, Streamlit)
- **Business Intelligence** for construction projects
- **Construction Industry KPIs** understanding and implementation
- **Interactive Web Applications** development

## What's Included

### 📊 KPIs Tracked

**Schedule Performance:**
- Planned % vs. Actual % Complete
- Schedule Performance Index (SPI) = Earned Value / Planned Value
- Days ahead/behind schedule
- Critical path tasks status

**Cost Performance:**
- Budget vs. Actual Spending
- Cost Performance Index (CPI) = Earned Value / Actual Cost  
- Forecasted cost at completion
- Cost variance by category

**Productivity Metrics:**
- Labor hours per unit of work
- Equipment utilization rate
- Material waste percentage

**Safety Metrics:**
- Days since last incident
- Total Recordable Incident Rate (TRIR)
- Near-miss reports

**Quality Metrics:**
- Punch list items
- Inspection pass rate
- Rework costs

### 🎯 Sample Project Scenario

The dashboard simulates a realistic **Commercial Building Construction** project:

- **Timeline:** 12 months (Jan 2024 - Dec 2024)
- **Budget:** $5,000,000
- **Current Status:** ~67% complete (as of Oct 2024)
- **Project Type:** Multi-story commercial building
- **Key Phases:** Site prep → Foundation → Steel → MEP → Finishes

## 🚀 Quick Start Options

### Option 1: Automated Setup (Windows)
```bash
# PowerShell (Recommended)
./setup.ps1

# Or Command Prompt
setup.bat
```

### Option 2: Manual Setup
```bash
# Install Python packages
pip install -r requirements.txt

# Generate sample data  
python src/data_generator.py

# Launch dashboard
streamlit run src/dashboard.py
```

### Option 3: Python Launcher
```bash
python launch_dashboard.py
```

## 📁 Project Structure

```
con_dash_ject/
├── 📊 src/
│   ├── dashboard.py          # Main Streamlit application
│   ├── data_generator.py     # Realistic data generator
│   └── analytics.py          # Advanced analytics engine
├── 📈 data/                  # Generated CSV datasets (7 files)
├── ⚙️ config/
│   └── config.py             # Settings and KPI thresholds  
├── 🚀 Launch Scripts:
│   ├── setup.ps1             # PowerShell setup
│   ├── setup.bat             # Windows batch setup
│   ├── launch_dashboard.py   # Python launcher
│   └── test_setup.py         # Verification script
└── 📋 requirements.txt       # Python dependencies
```

## 🎮 Using the Dashboard

### Navigation Sections:
1. **Overview** - Executive summary with key metrics
2. **Schedule Performance** - SPI trends and progress tracking  
3. **Cost Performance** - CPI analysis and budget variance
4. **Productivity** - Efficiency metrics and trends
5. **Safety** - Incident tracking and TRIR monitoring
6. **Quality** - Inspection rates and rework analysis
7. **Critical Path** - Task timeline and status

### Key Features:
- **Interactive Charts** - Hover for detailed data points
- **Date Range Filtering** - Focus on specific time periods
- **Color-coded KPIs** - Instant visual status assessment  
- **Real-time Calculations** - Live KPI computations
- **Export Capabilities** - Save charts and data

## 📊 Understanding the KPIs

### Schedule Performance Index (SPI)
- **Formula:** Earned Value ÷ Planned Value
- **Good:** SPI ≥ 1.0 (on or ahead of schedule)
- **Warning:** SPI < 0.95 (behind schedule)

### Cost Performance Index (CPI)  
- **Formula:** Earned Value ÷ Actual Cost
- **Good:** CPI ≥ 1.0 (under or on budget)
- **Warning:** CPI < 0.95 (over budget)

### Total Recordable Incident Rate (TRIR)
- **Formula:** (Incidents × 200,000) ÷ Total Hours Worked
- **Industry Average:** ~2.0
- **Target:** < 2.0

## 🎨 Customization Options

### Replace Sample Data:
1. Update CSV files in `/data/` directory
2. Match column names from `data_generator.py`
3. Restart dashboard

### Modify KPI Thresholds:
Edit `config/config.py`:
```python
KPI_THRESHOLDS = {
    "schedule": {"spi_good": 1.0, "spi_warning": 0.95},
    "cost": {"cpi_good": 1.0, "cpi_warning": 0.95},
    # ... customize as needed
}
```

### Add New Metrics:
1. Update data generator with new columns
2. Add chart functions to `dashboard.py`
3. Update analytics in `analytics.py`

## 🛠️ Technical Implementation

### Technologies:
- **Streamlit** - Web application framework
- **Plotly** - Interactive data visualization  
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **SciPy** - Advanced analytics

### Data Generation:
- Realistic construction project simulation
- 40 weeks of historical data
- Statistically sound variance patterns
- Industry-standard KPI calculations

### Analytics Features:
- Project health scoring (0-100)
- Completion date prediction
- Risk trend identification  
- Earned Value Management (EVM) metrics
- Productivity benchmarking

## 📈 Sample Insights

Current project status shows:
- **Schedule:** Slightly behind (SPI ~0.95)
- **Cost:** Over budget (CPI ~0.92) 
- **Safety:** Good performance (45+ days incident-free)
- **Quality:** Meeting standards (85%+ pass rate)

## 🔧 Troubleshooting

### Common Issues:

**"Streamlit not found"**
```bash
pip install streamlit
```

**"No data files"**  
```bash
python src/data_generator.py
```

**"Import errors"**
```bash
pip install -r requirements.txt
```

**Port already in use**
```bash
streamlit run src/dashboard.py --server.port 8502
```

## 📝 Next Steps / Enhancements

**Potential Improvements:**
- Real-time data integration (APIs, databases)
- Mobile-responsive design
- Advanced predictive analytics
- Automated reporting and alerts
- IoT sensor integration
- Multi-project comparison
- Resource optimization algorithms

## 🎯 Learning Objectives Demonstrated

This project showcases:
- ✅ **Data Visualization Mastery** - Interactive charts and dashboards
- ✅ **Business Intelligence Skills** - KPI development and monitoring  
- ✅ **Construction Domain Knowledge** - Industry-standard metrics
- ✅ **Python Proficiency** - Multiple libraries and frameworks
- ✅ **Web Development** - User-friendly interface design
- ✅ **Project Management** - Earned Value Management implementation

---

**Ready to explore construction project analytics!** 🏗️📊
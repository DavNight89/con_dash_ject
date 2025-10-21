import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import os

# Set page configuration
st.set_page_config(
    page_title="Construction Project Dashboard",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f4e79;
        margin: 0.5rem 0;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f4e79;
    }
    .metric-label {
        font-size: 1rem;
        color: #666;
        margin-bottom: 0.5rem;
    }
    .status-good {
        color: #28a745;
    }
    .status-warning {
        color: #ffc107;
    }
    .status-danger {
        color: #dc3545;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load all construction project data"""
    try:
        # Check if data files exist, if not generate them
        data_dir = "data"
        if not os.path.exists(data_dir):
            st.error("Data directory not found. Please run data_generator.py first.")
            return None, None, None, None, None, None, None
        
        schedule_df = pd.read_csv(f"{data_dir}/schedule_data.csv")
        cost_df = pd.read_csv(f"{data_dir}/cost_data.csv")
        productivity_df = pd.read_csv(f"{data_dir}/productivity_data.csv")
        safety_df = pd.read_csv(f"{data_dir}/safety_data.csv")
        quality_df = pd.read_csv(f"{data_dir}/quality_data.csv")
        critical_path_df = pd.read_csv(f"{data_dir}/critical_path_tasks.csv")
        cost_breakdown_df = pd.read_csv(f"{data_dir}/cost_breakdown.csv")
        
        # Convert date columns
        for df in [schedule_df, cost_df, productivity_df, safety_df, quality_df]:
            df['Date'] = pd.to_datetime(df['Date'])
        
        return schedule_df, cost_df, productivity_df, safety_df, quality_df, critical_path_df, cost_breakdown_df
    
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None, None, None, None, None, None

def create_kpi_cards(schedule_df, cost_df, safety_df, quality_df):
    """Create KPI summary cards"""
    
    if len(schedule_df) == 0:
        return
        
    # Get latest data
    latest_schedule = schedule_df.iloc[-1]
    latest_cost = cost_df.iloc[-1]
    latest_safety = safety_df.iloc[-1]
    latest_quality = quality_df.iloc[-1]
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        spi_status = "status-good" if latest_schedule['SPI'] >= 1.0 else "status-danger"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Schedule Performance Index (SPI)</div>
            <div class="metric-value {spi_status}">{latest_schedule['SPI']:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
        days_status = "status-good" if latest_schedule['Days_Variance'] >= 0 else "status-danger"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Days Ahead/Behind Schedule</div>
            <div class="metric-value {days_status}">{latest_schedule['Days_Variance']:+.1f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        cpi_status = "status-good" if latest_cost['CPI'] >= 1.0 else "status-danger"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Cost Performance Index (CPI)</div>
            <div class="metric-value {cpi_status}">{latest_cost['CPI']:.3f}</div>
        </div>
        """, unsafe_allow_html=True)
        
        variance_status = "status-good" if latest_cost['Cost_Variance'] >= 0 else "status-danger"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Cost Variance</div>
            <div class="metric-value {variance_status}">${latest_cost['Cost_Variance']:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        safety_status = "status-good" if latest_safety['Days_Since_Last_Incident'] > 30 else "status-warning"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Days Since Last Incident</div>
            <div class="metric-value {safety_status}">{latest_safety['Days_Since_Last_Incident']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        trir_status = "status-good" if latest_safety['TRIR'] <= 2.0 else "status-danger"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Recordable Incident Rate</div>
            <div class="metric-value {trir_status}">{latest_safety['TRIR']:.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        pass_rate_status = "status-good" if latest_quality['Inspection_Pass_Rate_Pct'] >= 85 else "status-warning"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Inspection Pass Rate</div>
            <div class="metric-value {pass_rate_status}">{latest_quality['Inspection_Pass_Rate_Pct']:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Open Punch List Items</div>
            <div class="metric-value">{latest_quality['Punch_List_Items']}</div>
        </div>
        """, unsafe_allow_html=True)

def create_schedule_charts(schedule_df):
    """Create schedule performance charts"""
    
    st.subheader("📅 Schedule Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Progress tracking chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=schedule_df['Date'],
            y=schedule_df['Planned_Progress_Pct'],
            mode='lines',
            name='Planned Progress',
            line=dict(color='blue', width=3)
        ))
        fig.add_trace(go.Scatter(
            x=schedule_df['Date'],
            y=schedule_df['Actual_Progress_Pct'],
            mode='lines',
            name='Actual Progress',
            line=dict(color='red', width=3)
        ))
        
        fig.update_layout(
            title="Planned vs Actual Progress",
            xaxis_title="Date",
            yaxis_title="Progress (%)",
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # SPI trend chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=schedule_df['Date'],
            y=schedule_df['SPI'],
            mode='lines+markers',
            name='SPI',
            line=dict(color='green', width=3)
        ))
        fig.add_hline(y=1.0, line_dash="dash", line_color="black", 
                      annotation_text="Target SPI = 1.0")
        
        fig.update_layout(
            title="Schedule Performance Index (SPI) Trend",
            xaxis_title="Date",
            yaxis_title="SPI",
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)

def create_cost_charts(cost_df, cost_breakdown_df):
    """Create cost performance charts"""
    
    st.subheader("💰 Cost Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Budget vs Actual spending
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=cost_df['Date'],
            y=cost_df['Cumulative_Budget'],
            mode='lines',
            name='Budget',
            line=dict(color='blue', width=3)
        ))
        fig.add_trace(go.Scatter(
            x=cost_df['Date'],
            y=cost_df['Cumulative_Spent'],
            mode='lines',
            name='Actual Spent',
            line=dict(color='red', width=3)
        ))
        
        fig.update_layout(
            title="Budget vs Actual Spending",
            xaxis_title="Date",
            yaxis_title="Cost ($)",
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # CPI trend
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=cost_df['Date'],
            y=cost_df['CPI'],
            mode='lines+markers',
            name='CPI',
            line=dict(color='purple', width=3)
        ))
        fig.add_hline(y=1.0, line_dash="dash", line_color="black", 
                      annotation_text="Target CPI = 1.0")
        
        fig.update_layout(
            title="Cost Performance Index (CPI) Trend",
            xaxis_title="Date",
            yaxis_title="CPI",
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Cost breakdown by category
    st.subheader("Cost Variance by Category")
    fig = px.bar(
        cost_breakdown_df,
        x='Category',
        y=['Budget', 'Actual'],
        title="Budget vs Actual by Category",
        barmode='group',
        color_discrete_map={'Budget': 'lightblue', 'Actual': 'darkblue'}
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

def create_productivity_charts(productivity_df):
    """Create productivity metrics charts"""
    
    st.subheader("⚡ Productivity Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Labor hours per unit
        fig = px.line(
            productivity_df,
            x='Date',
            y='Labor_Hours_Per_Unit',
            title='Labor Hours per Unit of Work',
            markers=True
        )
        fig.add_hline(y=productivity_df['Labor_Hours_Per_Unit'].mean(), 
                      line_dash="dash", line_color="red",
                      annotation_text=f"Average: {productivity_df['Labor_Hours_Per_Unit'].mean():.1f}")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Equipment utilization
        fig = px.line(
            productivity_df,
            x='Date',
            y='Equipment_Utilization_Pct',
            title='Equipment Utilization Rate (%)',
            markers=True,
            color_discrete_sequence=['orange']
        )
        fig.add_hline(y=80, line_dash="dash", line_color="green",
                      annotation_text="Target: 80%")
        st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        # Material waste
        fig = px.line(
            productivity_df,
            x='Date',
            y='Material_Waste_Pct',
            title='Material Waste Percentage',
            markers=True,
            color_discrete_sequence=['red']
        )
        fig.add_hline(y=5, line_dash="dash", line_color="green",
                      annotation_text="Target: <5%")
        st.plotly_chart(fig, use_container_width=True)

def create_safety_charts(safety_df):
    """Create safety metrics charts"""
    
    st.subheader("🛡️ Safety Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Days since last incident
        fig = px.line(
            safety_df,
            x='Date',
            y='Days_Since_Last_Incident',
            title='Days Since Last Incident',
            markers=True,
            color_discrete_sequence=['green']
        )
        fig.add_hline(y=30, line_dash="dash", line_color="orange",
                      annotation_text="Target: >30 days")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # TRIR trend
        fig = px.line(
            safety_df,
            x='Date',
            y='TRIR',
            title='Total Recordable Incident Rate (TRIR)',
            markers=True,
            color_discrete_sequence=['purple']
        )
        fig.add_hline(y=2.0, line_dash="dash", line_color="red",
                      annotation_text="Industry Average: 2.0")
        st.plotly_chart(fig, use_container_width=True)
    
    # Near miss reports
    st.subheader("Near Miss Reports")
    fig = px.bar(
        safety_df,
        x='Date',
        y='Near_Miss_Count',
        title='Weekly Near Miss Reports',
        color='Near_Miss_Count',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_quality_charts(quality_df):
    """Create quality metrics charts"""
    
    st.subheader("✅ Quality Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Inspection pass rate
        fig = px.line(
            quality_df,
            x='Date',
            y='Inspection_Pass_Rate_Pct',
            title='Inspection Pass Rate (%)',
            markers=True,
            color_discrete_sequence=['green']
        )
        fig.add_hline(y=85, line_dash="dash", line_color="blue",
                      annotation_text="Target: >85%")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Punch list items
        fig = px.line(
            quality_df,
            x='Date',
            y='Punch_List_Items',
            title='Weekly Punch List Items',
            markers=True,
            color_discrete_sequence=['orange']
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Rework costs
    st.subheader("Rework Costs")
    fig = px.bar(
        quality_df,
        x='Date',
        y='Rework_Cost',
        title='Weekly Rework Costs ($)',
        color='Rework_Cost',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_critical_path_view(critical_path_df):
    """Create critical path tasks view"""
    
    st.subheader("🎯 Critical Path Tasks")
    
    # Status color mapping
    status_colors = {
        'Completed': '#28a745',
        'In Progress': '#ffc107',
        'Not Started': '#dc3545'
    }
    
    # Create Gantt-like chart
    fig = go.Figure()
    
    for i, task in critical_path_df.iterrows():
        start_date = pd.to_datetime(task['Start'])
        end_date = pd.to_datetime(task['End'])
        
        fig.add_trace(go.Scatter(
            x=[start_date, end_date],
            y=[task['Task'], task['Task']],
            mode='lines',
            line=dict(color=status_colors[task['Status']], width=10),
            name=task['Status'],
            showlegend=i == 0 or task['Status'] != critical_path_df.iloc[i-1]['Status']
        ))
    
    fig.update_layout(
        title="Critical Path Tasks Timeline",
        xaxis_title="Date",
        yaxis_title="Tasks",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tasks summary table
    st.subheader("Tasks Summary")
    
    # Style the dataframe
    styled_df = critical_path_df.copy()
    
    def color_status(val):
        if val == 'Completed':
            return 'background-color: #d4edda; color: #155724'
        elif val == 'In Progress':
            return 'background-color: #fff3cd; color: #856404'
        else:  # Not Started
            return 'background-color: #f8d7da; color: #721c24'
    
    styled_df = styled_df.style.applymap(color_status, subset=['Status'])
    st.dataframe(styled_df, use_container_width=True)

def main():
    """Main dashboard function"""
    
    # Header
    st.markdown('<h1 class="main-header">🏗️ Construction Project Dashboard</h1>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("Navigation")
    
    # Load data
    data = load_data()
    if data[0] is None:
        st.error("Unable to load data. Please check that all data files exist in the 'data' directory.")
        st.info("To generate sample data, run: `python src/data_generator.py`")
        return
    
    schedule_df, cost_df, productivity_df, safety_df, quality_df, critical_path_df, cost_breakdown_df = data
    
    # Sidebar filters
    st.sidebar.subheader("Date Range Filter")
    min_date = schedule_df['Date'].min().date()
    max_date = schedule_df['Date'].max().date()
    
    start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
    end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)
    
    # Filter data based on date range
    mask = (schedule_df['Date'].dt.date >= start_date) & (schedule_df['Date'].dt.date <= end_date)
    filtered_schedule = schedule_df.loc[mask]
    filtered_cost = cost_df.loc[mask]
    filtered_productivity = productivity_df.loc[mask]
    filtered_safety = safety_df.loc[mask]
    filtered_quality = quality_df.loc[mask]
    
    # Dashboard sections
    section = st.sidebar.selectbox(
        "Choose Section",
        ["Overview", "Schedule Performance", "Cost Performance", "Productivity", "Safety", "Quality", "Critical Path"]
    )
    
    if section == "Overview":
        create_kpi_cards(filtered_schedule, filtered_cost, filtered_safety, filtered_quality)
        
        col1, col2 = st.columns(2)
        with col1:
            create_schedule_charts(filtered_schedule)
        with col2:
            create_cost_charts(filtered_cost, cost_breakdown_df)
            
    elif section == "Schedule Performance":
        create_kpi_cards(filtered_schedule, filtered_cost, filtered_safety, filtered_quality)
        create_schedule_charts(filtered_schedule)
        
    elif section == "Cost Performance":
        create_cost_charts(filtered_cost, cost_breakdown_df)
        
    elif section == "Productivity":
        create_productivity_charts(filtered_productivity)
        
    elif section == "Safety":
        create_safety_charts(filtered_safety)
        
    elif section == "Quality":
        create_quality_charts(filtered_quality)
        
    elif section == "Critical Path":
        create_critical_path_view(critical_path_df)
    
    # Project info in sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("Project Information")
    st.sidebar.info(f"""
    **Project:** Commercial Building Construction
    
    **Timeline:** Jan 2024 - Dec 2024
    
    **Budget:** $5,000,000
    
    **Current Status:** {filtered_schedule.iloc[-1]['Actual_Progress_Pct']:.1f}% Complete
    
    **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
    """)

if __name__ == "__main__":
    main()
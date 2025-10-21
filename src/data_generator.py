import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_construction_data():
    """
    Generate realistic construction project data for dashboard demonstration
    """
    
    # Set random seed for reproducible data
    np.random.seed(42)
    random.seed(42)
    
    # Project timeline
    project_start = datetime(2024, 1, 15)
    project_end = datetime(2024, 12, 20)
    current_date = datetime(2024, 10, 20)
    
    # Generate weekly data points
    weeks = pd.date_range(start=project_start, end=current_date, freq='W')
    
    # Task categories for a commercial building construction project
    task_categories = [
        "Site Preparation", "Foundation", "Structural Steel", "Concrete Work",
        "MEP Rough-in", "Exterior Envelope", "Interior Framing", "Drywall",
        "Flooring", "Electrical Finish", "Plumbing Finish", "HVAC Finish",
        "Painting", "Final Inspections"
    ]
    
    # Generate project schedule data
    schedule_data = []
    cost_data = []
    productivity_data = []
    safety_data = []
    quality_data = []
    
    cumulative_planned = 0
    cumulative_actual = 0
    cumulative_budget = 0
    cumulative_spent = 0
    
    for i, week in enumerate(weeks):
        # Schedule Performance Metrics
        planned_progress = min((i + 1) * 100 / len(weeks), 100)
        
        # Add some realistic variance - projects typically fall behind schedule
        actual_progress_base = planned_progress * np.random.normal(0.95, 0.1)
        actual_progress = max(0, min(actual_progress_base, 100))
        
        # Calculate earned value and planned value
        planned_value = planned_progress * 5000000 / 100  # $5M total project
        earned_value = actual_progress * 5000000 / 100
        
        # Schedule Performance Index
        spi = earned_value / planned_value if planned_value > 0 else 1.0
        
        # Days ahead/behind (simplified calculation)
        days_variance = (actual_progress - planned_progress) * 350 / 100  # 350 total days
        
        schedule_data.append({
            'Date': week,
            'Week': i + 1,
            'Planned_Progress_Pct': round(planned_progress, 2),
            'Actual_Progress_Pct': round(actual_progress, 2),
            'Planned_Value': round(planned_value, 2),
            'Earned_Value': round(earned_value, 2),
            'SPI': round(spi, 3),
            'Days_Variance': round(days_variance, 1)
        })
        
        # Cost Performance Metrics
        weekly_budget = 150000 + np.random.normal(0, 20000)  # ~$150k per week
        weekly_actual = weekly_budget * np.random.normal(1.05, 0.15)  # Typically over budget
        
        cumulative_budget += weekly_budget
        cumulative_spent += weekly_actual
        
        # Cost Performance Index
        cpi = earned_value / cumulative_spent if cumulative_spent > 0 else 1.0
        
        # Forecasted cost at completion
        forecasted_cost = 5000000 / cpi if cpi > 0 else 5000000
        
        cost_data.append({
            'Date': week,
            'Week': i + 1,
            'Weekly_Budget': round(weekly_budget, 2),
            'Weekly_Actual': round(weekly_actual, 2),
            'Cumulative_Budget': round(cumulative_budget, 2),
            'Cumulative_Spent': round(cumulative_spent, 2),
            'CPI': round(cpi, 3),
            'Forecasted_Cost': round(forecasted_cost, 2),
            'Cost_Variance': round(cumulative_budget - cumulative_spent, 2)
        })
        
        # Productivity Metrics
        labor_hours = np.random.normal(2000, 300)  # Weekly labor hours
        work_units = np.random.normal(50, 10)  # Units of work completed
        labor_hours_per_unit = labor_hours / work_units if work_units > 0 else 40
        
        equipment_utilization = np.random.normal(75, 15)  # Equipment utilization %
        material_waste = np.random.normal(8, 3)  # Material waste %
        
        productivity_data.append({
            'Date': week,
            'Week': i + 1,
            'Labor_Hours': round(labor_hours, 0),
            'Work_Units': round(work_units, 1),
            'Labor_Hours_Per_Unit': round(labor_hours_per_unit, 2),
            'Equipment_Utilization_Pct': round(max(0, min(100, equipment_utilization)), 1),
            'Material_Waste_Pct': round(max(0, material_waste), 2)
        })
        
        # Safety Metrics
        # Simulate incident occurrences (rare events)
        incident_occurred = np.random.random() < 0.05  # 5% chance per week
        near_miss_count = np.random.poisson(2)  # Average 2 near-misses per week
        
        # Calculate days since last incident (cumulative)
        if i == 0:
            days_since_incident = 45  # Start with 45 days
        else:
            if incident_occurred:
                days_since_incident = 0
            else:
                days_since_incident = safety_data[-1]['Days_Since_Last_Incident'] + 7
        
        # TRIR calculation (incidents per 200,000 hours worked)
        total_incidents = sum([1 for s in safety_data if s['Incident_Occurred']] + [1 if incident_occurred else 0])
        total_hours = sum([p['Labor_Hours'] for p in productivity_data]) + labor_hours
        trir = (total_incidents * 200000) / total_hours if total_hours > 0 else 0
        
        safety_data.append({
            'Date': week,
            'Week': i + 1,
            'Incident_Occurred': incident_occurred,
            'Near_Miss_Count': near_miss_count,
            'Days_Since_Last_Incident': days_since_incident,
            'TRIR': round(trir, 2)
        })
        
        # Quality Metrics
        inspections_conducted = np.random.poisson(8)  # Average 8 inspections per week
        inspections_passed = np.random.binomial(inspections_conducted, 0.85)  # 85% pass rate
        punch_list_items = np.random.poisson(15)  # Average 15 punch list items per week
        rework_cost = np.random.normal(8000, 3000)  # Average $8k rework per week
        
        quality_data.append({
            'Date': week,
            'Week': i + 1,
            'Inspections_Conducted': inspections_conducted,
            'Inspections_Passed': inspections_passed,
            'Inspection_Pass_Rate_Pct': round((inspections_passed / inspections_conducted * 100) if inspections_conducted > 0 else 0, 1),
            'Punch_List_Items': punch_list_items,
            'Rework_Cost': round(max(0, rework_cost), 2)
        })
    
    # Convert to DataFrames
    schedule_df = pd.DataFrame(schedule_data)
    cost_df = pd.DataFrame(cost_data)
    productivity_df = pd.DataFrame(productivity_data)
    safety_df = pd.DataFrame(safety_data)
    quality_df = pd.DataFrame(quality_data)
    
    return schedule_df, cost_df, productivity_df, safety_df, quality_df

def generate_critical_path_tasks():
    """Generate critical path tasks with status tracking"""
    
    tasks = [
        {"Task": "Site Survey & Permits", "Status": "Completed", "Start": "2024-01-15", "End": "2024-02-15", "Critical": True},
        {"Task": "Excavation & Site Prep", "Status": "Completed", "Start": "2024-02-15", "End": "2024-03-15", "Critical": True},
        {"Task": "Foundation Pour", "Status": "Completed", "Start": "2024-03-15", "End": "2024-04-30", "Critical": True},
        {"Task": "Structural Steel Erection", "Status": "Completed", "Start": "2024-04-30", "End": "2024-06-15", "Critical": True},
        {"Task": "Concrete Deck Pour", "Status": "Completed", "Start": "2024-06-15", "End": "2024-07-30", "Critical": True},
        {"Task": "Exterior Envelope", "Status": "In Progress", "Start": "2024-07-30", "End": "2024-09-30", "Critical": True},
        {"Task": "MEP Rough-in", "Status": "In Progress", "Start": "2024-08-15", "End": "2024-10-30", "Critical": True},
        {"Task": "Interior Framing", "Status": "Not Started", "Start": "2024-10-30", "End": "2024-12-15", "Critical": True},
        {"Task": "Final Inspections", "Status": "Not Started", "Start": "2024-12-15", "End": "2024-12-20", "Critical": True}
    ]
    
    return pd.DataFrame(tasks)

def generate_cost_breakdown():
    """Generate cost breakdown by category"""
    
    categories = [
        {"Category": "Site Work", "Budget": 450000, "Actual": 467000, "Variance": -17000},
        {"Category": "Concrete", "Budget": 850000, "Actual": 823000, "Variance": 27000},
        {"Category": "Structural Steel", "Budget": 1200000, "Actual": 1255000, "Variance": -55000},
        {"Category": "MEP Systems", "Budget": 950000, "Actual": 982000, "Variance": -32000},
        {"Category": "Envelope/Roofing", "Budget": 680000, "Actual": 701000, "Variance": -21000},
        {"Category": "Interior Finishes", "Budget": 520000, "Actual": 485000, "Variance": 35000},
        {"Category": "Equipment", "Budget": 350000, "Actual": 375000, "Variance": -25000}
    ]
    
    return pd.DataFrame(categories)

if __name__ == "__main__":
    # Generate all datasets
    schedule_df, cost_df, productivity_df, safety_df, quality_df = generate_construction_data()
    critical_path_df = generate_critical_path_tasks()
    cost_breakdown_df = generate_cost_breakdown()
    
    # Save to CSV files
    schedule_df.to_csv('data/schedule_data.csv', index=False)
    cost_df.to_csv('data/cost_data.csv', index=False)
    productivity_df.to_csv('data/productivity_data.csv', index=False)
    safety_df.to_csv('data/safety_data.csv', index=False)
    quality_df.to_csv('data/quality_data.csv', index=False)
    critical_path_df.to_csv('data/critical_path_tasks.csv', index=False)
    cost_breakdown_df.to_csv('data/cost_breakdown.csv', index=False)
    
    print("Construction project data generated successfully!")
    print(f"Schedule data: {len(schedule_df)} weeks")
    print(f"Cost data: {len(cost_df)} weeks")
    print(f"Productivity data: {len(productivity_df)} weeks")
    print(f"Safety data: {len(safety_df)} weeks")
    print(f"Quality data: {len(quality_df)} weeks")
    print(f"Critical path tasks: {len(critical_path_df)} tasks")
    print(f"Cost breakdown: {len(cost_breakdown_df)} categories")
"""
Excel Template Generator for Construction Project Dashboard
Creates a comprehensive Excel workbook with all KPI tracking sheets
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def create_excel_template():
    """Create a comprehensive Excel template for construction project tracking"""
    
    # Create Excel writer object
    template_path = "Construction_Project_Dashboard_Template.xlsx"
    
    with pd.ExcelWriter(template_path, engine='openpyxl') as writer:
        
        # Sheet 1: Project Overview
        create_project_overview_sheet(writer)
        
        # Sheet 2: Schedule Tracking
        create_schedule_tracking_sheet(writer)
        
        # Sheet 3: Cost Tracking
        create_cost_tracking_sheet(writer)
        
        # Sheet 4: Productivity Metrics
        create_productivity_sheet(writer)
        
        # Sheet 5: Safety Tracking
        create_safety_sheet(writer)
        
        # Sheet 6: Quality Metrics
        create_quality_sheet(writer)
        
        # Sheet 7: Critical Path Tasks
        create_critical_path_sheet(writer)
        
        # Sheet 8: Cost Breakdown
        create_cost_breakdown_sheet(writer)
        
        # Sheet 9: KPI Dashboard
        create_kpi_dashboard_sheet(writer)
        
        # Sheet 10: Instructions
        create_instructions_sheet(writer)
    
    print(f"✅ Excel template created: {template_path}")
    return template_path

def create_project_overview_sheet(writer):
    """Create project overview and settings sheet"""
    
    overview_data = {
        'Project Information': [
            'Project Name',
            'Project Manager',
            'Client/Owner',
            'Contract Value',
            'Project Start Date',
            'Planned End Date',
            'Current Date',
            'Project Location',
            'Contract Type',
            'Project Phase'
        ],
        'Value': [
            'Commercial Building Construction',
            '[Enter PM Name]',
            '[Enter Client Name]',
            '$5,000,000',
            '2024-01-15',
            '2024-12-20',
            datetime.now().strftime('%Y-%m-%d'),
            '[Enter Location]',
            'Fixed Price',
            'Construction'
        ],
        'Notes': [
            'Update project name as needed',
            'Primary project manager contact',
            'Client organization name',
            'Total contract amount',
            'Official project start date',
            'Contractual completion date',
            'Update weekly',
            'Job site address',
            'Contract delivery method',
            'Current project phase'
        ]
    }
    
    df = pd.DataFrame(overview_data)
    df.to_excel(writer, sheet_name='Project Overview', index=False, startrow=1)

def create_schedule_tracking_sheet(writer):
    """Create schedule performance tracking sheet"""
    
    # Create 52 weeks of template rows
    weeks = pd.date_range(start='2024-01-15', periods=52, freq='W')
    
    schedule_template = {
        'Date': weeks,
        'Week': range(1, 53),
        'Planned_Progress_Pct': [i * 100/52 for i in range(1, 53)],
        'Actual_Progress_Pct': [''] * 52,  # To be filled by user
        'Planned_Value': [i * 5000000/52 for i in range(1, 53)],
        'Earned_Value': ['=D2*$B$2/100'] + [''] * 51,  # Formula for first row
        'SPI': ['=F2/E2'] + [''] * 51,  # Formula for first row
        'Days_Variance': ['=(D2-C2)*365/100'] + [''] * 51,  # Formula for first row
        'Notes': [''] * 52
    }
    
    df = pd.DataFrame(schedule_template)
    df.to_excel(writer, sheet_name='Schedule Tracking', index=False)

def create_cost_tracking_sheet(writer):
    """Create cost performance tracking sheet"""
    
    weeks = pd.date_range(start='2024-01-15', periods=52, freq='W')
    
    cost_template = {
        'Date': weeks,
        'Week': range(1, 53),
        'Weekly_Budget': [96000] * 52,  # ~$96k per week for $5M project
        'Weekly_Actual': [''] * 52,  # To be filled by user
        'Cumulative_Budget': ['=SUM($C$2:C2)'] + [''] * 51,
        'Cumulative_Spent': ['=SUM($D$2:D2)'] + [''] * 51,
        'CPI': ['=Schedule_Tracking.F2/F2'] + [''] * 51,  # Reference to earned value
        'Forecasted_Cost': ['=5000000/G2'] + [''] * 51,
        'Cost_Variance': ['=E2-F2'] + [''] * 51,
        'Notes': [''] * 52
    }
    
    df = pd.DataFrame(cost_template)
    df.to_excel(writer, sheet_name='Cost Tracking', index=False)

def create_productivity_sheet(writer):
    """Create productivity metrics tracking sheet"""
    
    weeks = pd.date_range(start='2024-01-15', periods=52, freq='W')
    
    productivity_template = {
        'Date': weeks,
        'Week': range(1, 53),
        'Labor_Hours': [''] * 52,
        'Work_Units_Completed': [''] * 52,
        'Labor_Hours_Per_Unit': ['=C2/D2'] + [''] * 51,
        'Equipment_Utilization_Pct': [''] * 52,
        'Material_Waste_Pct': [''] * 52,
        'Equipment_Downtime_Hours': [''] * 52,
        'Rework_Hours': [''] * 52,
        'Notes': [''] * 52
    }
    
    df = pd.DataFrame(productivity_template)
    df.to_excel(writer, sheet_name='Productivity Metrics', index=False)

def create_safety_sheet(writer):
    """Create safety tracking sheet"""
    
    weeks = pd.date_range(start='2024-01-15', periods=52, freq='W')
    
    safety_template = {
        'Date': weeks,
        'Week': range(1, 53),
        'Incident_Occurred': ['No'] * 52,  # Dropdown: Yes/No
        'Incident_Type': [''] * 52,
        'Near_Miss_Count': [''] * 52,
        'Safety_Training_Hours': [''] * 52,
        'Days_Since_Last_Incident': [''] * 52,
        'Total_Work_Hours': [''] * 52,
        'TRIR': ['=(COUNTIF($C$2:C2,"Yes")*200000)/SUM($H$2:H2)'] + [''] * 51,
        'Safety_Observations': [''] * 52,
        'Corrective_Actions': [''] * 52
    }
    
    df = pd.DataFrame(safety_template)
    df.to_excel(writer, sheet_name='Safety Tracking', index=False)

def create_quality_sheet(writer):
    """Create quality metrics tracking sheet"""
    
    weeks = pd.date_range(start='2024-01-15', periods=52, freq='W')
    
    quality_template = {
        'Date': weeks,
        'Week': range(1, 53),
        'Inspections_Conducted': [''] * 52,
        'Inspections_Passed': [''] * 52,
        'Inspection_Pass_Rate_Pct': ['=D2/C2*100'] + [''] * 51,
        'Punch_List_Items_Added': [''] * 52,
        'Punch_List_Items_Closed': [''] * 52,
        'Open_Punch_Items': [''] * 52,
        'Rework_Cost': [''] * 52,
        'Quality_Issues': [''] * 52,
        'Lessons_Learned': [''] * 52
    }
    
    df = pd.DataFrame(quality_template)
    df.to_excel(writer, sheet_name='Quality Metrics', index=False)

def create_critical_path_sheet(writer):
    """Create critical path tasks sheet"""
    
    tasks_template = {
        'Task_ID': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008', 'T009', 'T010'],
        'Task_Name': [
            'Site Survey & Permits',
            'Excavation & Site Prep',
            'Foundation Pour',
            'Structural Steel Erection',
            'Concrete Deck Pour',
            'Exterior Envelope',
            'MEP Rough-in',
            'Interior Framing',
            'Finishes',
            'Final Inspections'
        ],
        'Planned_Start': [
            '2024-01-15', '2024-02-15', '2024-03-15', '2024-04-30',
            '2024-06-15', '2024-07-30', '2024-08-15', '2024-10-30',
            '2024-11-30', '2024-12-15'
        ],
        'Planned_End': [
            '2024-02-15', '2024-03-15', '2024-04-30', '2024-06-15',
            '2024-07-30', '2024-09-30', '2024-10-30', '2024-12-15',
            '2024-12-15', '2024-12-20'
        ],
        'Actual_Start': [''] * 10,
        'Actual_End': [''] * 10,
        'Status': ['Not Started'] * 10,  # Dropdown: Not Started/In Progress/Completed/On Hold
        'Percent_Complete': [''] * 10,
        'Critical_Path': ['Yes'] * 10,  # Dropdown: Yes/No
        'Notes': [''] * 10
    }
    
    df = pd.DataFrame(tasks_template)
    df.to_excel(writer, sheet_name='Critical Path Tasks', index=False)

def create_cost_breakdown_sheet(writer):
    """Create cost breakdown by category sheet"""
    
    categories_template = {
        'Cost_Category': [
            'Site Work',
            'Concrete Work',
            'Structural Steel',
            'MEP Systems',
            'Envelope/Roofing',
            'Interior Finishes',
            'Equipment & Tools',
            'Labor',
            'Materials',
            'Subcontractors',
            'Other/Contingency'
        ],
        'Budget_Amount': [
            450000, 850000, 1200000, 950000, 680000, 520000,
            350000, 800000, 600000, 400000, 200000
        ],
        'Actual_Cost': [''] * 11,
        'Committed_Cost': [''] * 11,
        'Cost_Variance': ['=C2-B2'] + [''] * 10,
        'Percent_Complete': [''] * 11,
        'Forecast_Final_Cost': [''] * 11,
        'Notes': [''] * 11
    }
    
    df = pd.DataFrame(categories_template)
    df.to_excel(writer, sheet_name='Cost Breakdown', index=False)

def create_kpi_dashboard_sheet(writer):
    """Create KPI dashboard summary sheet"""
    
    kpi_data = {
        'KPI_Name': [
            'Schedule Performance Index (SPI)',
            'Cost Performance Index (CPI)',
            'Days Ahead/Behind Schedule',
            'Cost Variance',
            'Current Progress %',
            'Budget Utilization %',
            'Days Since Last Incident',
            'TRIR (This Year)',
            'Inspection Pass Rate %',
            'Open Punch List Items',
            'Labor Efficiency',
            'Equipment Utilization %'
        ],
        'Current_Value': [
            '=AVERAGE(Schedule_Tracking.G:G)',
            '=AVERAGE(Cost_Tracking.G:G)',
            '=AVERAGE(Schedule_Tracking.H:H)',
            '=SUM(Cost_Tracking.I:I)',
            '=MAX(Schedule_Tracking.D:D)',
            '=MAX(Cost_Tracking.F:F)/5000000*100',
            '=MAX(Safety_Tracking.G:G)',
            '=MAX(Safety_Tracking.I:I)',
            '=AVERAGE(Quality_Metrics.E:E)',
            '=MAX(Quality_Metrics.H:H)',
            '=AVERAGE(Productivity_Metrics.E:E)',
            '=AVERAGE(Productivity_Metrics.F:F)'
        ],
        'Target_Value': [1.0, 1.0, 0, 0, 100, 100, 30, 2.0, 85, 0, 40, 75],
        'Status': [''] * 12,  # Will be calculated based on current vs target
        'Trend': [''] * 12,   # Up/Down/Stable arrows
        'Notes': [''] * 12
    }
    
    df = pd.DataFrame(kpi_data)
    df.to_excel(writer, sheet_name='KPI Dashboard', index=False)

def create_instructions_sheet(writer):
    """Create instructions and formulas sheet"""
    
    instructions = {
        'Section': [
            'Getting Started',
            'Getting Started',
            'Getting Started',
            'Schedule Tracking',
            'Schedule Tracking', 
            'Cost Tracking',
            'Cost Tracking',
            'Safety Tracking',
            'Quality Metrics',
            'Formulas',
            'Formulas',
            'Formulas',
            'Data Entry Tips',
            'Data Entry Tips'
        ],
        'Instructions': [
            '1. Update Project Overview sheet with your project details',
            '2. Enter actual data weekly in each tracking sheet',
            '3. Review KPI Dashboard for automated calculations',
            'Enter Actual Progress % weekly (Column D)',
            'SPI and other metrics will calculate automatically',
            'Enter Weekly Actual costs (Column D)',
            'CPI and variances will calculate automatically',
            'Mark incidents as Yes/No, enter near-miss counts',
            'Enter inspection results and punch list items',
            'SPI = Earned Value / Planned Value',
            'CPI = Earned Value / Actual Cost',
            'TRIR = (Incidents × 200,000) / Total Hours',
            'Use consistent date formats (YYYY-MM-DD)',
            'Enter percentages as decimals (85% = 85, not 0.85)'
        ],
        'Sheet_Reference': [
            'Project Overview',
            'All Sheets',
            'KPI Dashboard',
            'Schedule Tracking',
            'Schedule Tracking',
            'Cost Tracking', 
            'Cost Tracking',
            'Safety Tracking',
            'Quality Metrics',
            'All Sheets',
            'All Sheets',
            'Safety Tracking',
            'All Sheets',
            'All Sheets'
        ]
    }
    
    df = pd.DataFrame(instructions)
    df.to_excel(writer, sheet_name='Instructions', index=False)

def create_sample_data_excel():
    """Create Excel file with sample data (similar to CSV data)"""
    
    # Load existing CSV data
    try:
        schedule_df = pd.read_csv('data/schedule_data.csv')
        cost_df = pd.read_csv('data/cost_data.csv')
        productivity_df = pd.read_csv('data/productivity_data.csv')
        safety_df = pd.read_csv('data/safety_data.csv')
        quality_df = pd.read_csv('data/quality_data.csv')
        critical_path_df = pd.read_csv('data/critical_path_tasks.csv')
        cost_breakdown_df = pd.read_csv('data/cost_breakdown.csv')
        
        # Create Excel file with sample data
        sample_path = "Construction_Project_Sample_Data.xlsx"
        
        with pd.ExcelWriter(sample_path, engine='openpyxl') as writer:
            schedule_df.to_excel(writer, sheet_name='Schedule Data', index=False)
            cost_df.to_excel(writer, sheet_name='Cost Data', index=False)
            productivity_df.to_excel(writer, sheet_name='Productivity Data', index=False)
            safety_df.to_excel(writer, sheet_name='Safety Data', index=False)
            quality_df.to_excel(writer, sheet_name='Quality Data', index=False)
            critical_path_df.to_excel(writer, sheet_name='Critical Path Tasks', index=False)
            cost_breakdown_df.to_excel(writer, sheet_name='Cost Breakdown', index=False)
        
        print(f"✅ Sample data Excel file created: {sample_path}")
        return sample_path
        
    except FileNotFoundError:
        print("❌ CSV data files not found. Run data_generator.py first.")
        return None

def main():
    """Generate both template and sample Excel files"""
    
    print("🏗️ Creating Excel Templates for Construction Dashboard")
    print("=" * 55)
    
    # Create empty template
    template_path = create_excel_template()
    
    # Create sample data file
    sample_path = create_sample_data_excel()
    
    print("\n📊 Excel Files Created:")
    print(f"📋 Template (blank): {template_path}")
    if sample_path:
        print(f"📈 Sample Data: {sample_path}")
    
    print("\n🎯 Template Features:")
    print("• Project Overview & Settings")
    print("• Schedule Performance Tracking") 
    print("• Cost Management")
    print("• Productivity Metrics")
    print("• Safety Tracking")
    print("• Quality Metrics")
    print("• Critical Path Tasks")
    print("• Automated KPI Dashboard")
    print("• Built-in Formulas & Instructions")
    
    print("\n💡 Usage:")
    print("1. Use the template for new projects")
    print("2. Reference sample data for realistic examples")
    print("3. Customize categories and formulas as needed")

if __name__ == "__main__":
    main()
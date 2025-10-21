import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

class ConstructionAnalytics:
    """Advanced analytics for construction project data"""
    
    def __init__(self, schedule_df, cost_df, productivity_df, safety_df, quality_df):
        self.schedule_df = schedule_df
        self.cost_df = cost_df
        self.productivity_df = productivity_df
        self.safety_df = safety_df
        self.quality_df = quality_df
    
    def calculate_project_health_score(self):
        """Calculate overall project health score (0-100)"""
        
        if len(self.schedule_df) == 0:
            return 50  # Neutral score if no data
        
        # Get latest values
        latest_schedule = self.schedule_df.iloc[-1]
        latest_cost = self.cost_df.iloc[-1]
        latest_safety = self.safety_df.iloc[-1]
        latest_quality = self.quality_df.iloc[-1]
        
        # Schedule health (25% weight)
        spi_score = min(100, latest_schedule['SPI'] * 100)
        schedule_health = spi_score * 0.25
        
        # Cost health (25% weight)
        cpi_score = min(100, latest_cost['CPI'] * 100)
        cost_health = cpi_score * 0.25
        
        # Safety health (25% weight)
        days_since = latest_safety['Days_Since_Last_Incident']
        safety_score = min(100, (days_since / 90) * 100)  # 90 days = 100%
        trir_score = max(0, 100 - (latest_safety['TRIR'] * 25))  # Lower TRIR is better
        safety_health = (safety_score + trir_score) / 2 * 0.25
        
        # Quality health (25% weight)
        pass_rate = latest_quality['Inspection_Pass_Rate_Pct']
        quality_health = pass_rate * 0.25
        
        total_health = schedule_health + cost_health + safety_health + quality_health
        return round(total_health, 1)
    
    def predict_completion_date(self):
        """Predict project completion date based on current performance"""
        
        if len(self.schedule_df) < 3:
            return None
        
        # Calculate trend in progress rate
        recent_data = self.schedule_df.tail(4)  # Last 4 weeks
        progress_rates = recent_data['Actual_Progress_Pct'].diff().dropna()
        
        if len(progress_rates) == 0 or progress_rates.mean() <= 0:
            return "Cannot predict - insufficient progress"
        
        current_progress = self.schedule_df.iloc[-1]['Actual_Progress_Pct']
        remaining_progress = 100 - current_progress
        
        avg_weekly_progress = progress_rates.mean()
        weeks_remaining = remaining_progress / avg_weekly_progress
        
        last_date = self.schedule_df.iloc[-1]['Date']
        predicted_date = last_date + pd.Timedelta(weeks=weeks_remaining)
        
        return predicted_date.strftime('%Y-%m-%d')
    
    def calculate_cost_forecast_confidence(self):
        """Calculate confidence level in cost forecast"""
        
        if len(self.cost_df) < 5:
            return "Insufficient data"
        
        # Analyze CPI stability
        recent_cpi = self.cost_df.tail(5)['CPI']
        cpi_std = recent_cpi.std()
        
        if cpi_std < 0.05:
            return "High Confidence"
        elif cpi_std < 0.1:
            return "Medium Confidence"
        else:
            return "Low Confidence"
    
    def identify_risk_trends(self):
        """Identify concerning trends in project metrics"""
        
        risks = []
        
        if len(self.schedule_df) < 3:
            return ["Insufficient data for trend analysis"]
        
        # Schedule risks
        recent_spi = self.schedule_df.tail(3)['SPI']
        if recent_spi.mean() < 0.95 and (recent_spi.iloc[-1] < recent_spi.iloc[0]):
            risks.append("Schedule Performance Index trending downward")
        
        # Cost risks  
        recent_cpi = self.cost_df.tail(3)['CPI']
        if recent_cpi.mean() < 0.95 and (recent_cpi.iloc[-1] < recent_cpi.iloc[0]):
            risks.append("Cost Performance Index trending downward")
        
        # Safety risks
        recent_incidents = self.safety_df.tail(4)['Near_Miss_Count']
        if recent_incidents.mean() > 3:
            risks.append("Higher than average near-miss incidents")
        
        # Quality risks
        recent_pass_rate = self.quality_df.tail(3)['Inspection_Pass_Rate_Pct']
        if recent_pass_rate.mean() < 80:
            risks.append("Inspection pass rate below 80%")
        
        recent_rework = self.quality_df.tail(3)['Rework_Cost']
        if recent_rework.mean() > 10000:
            risks.append("High rework costs detected")
        
        # Productivity risks
        recent_efficiency = self.productivity_df.tail(3)['Labor_Hours_Per_Unit']
        if len(recent_efficiency) > 1 and recent_efficiency.iloc[-1] > recent_efficiency.mean() * 1.2:
            risks.append("Labor efficiency declining")
        
        if not risks:
            risks.append("No significant risk trends detected")
        
        return risks
    
    def calculate_earned_value_metrics(self):
        """Calculate comprehensive earned value management metrics"""
        
        if len(self.schedule_df) == 0 or len(self.cost_df) == 0:
            return {}
        
        latest_schedule = self.schedule_df.iloc[-1]
        latest_cost = self.cost_df.iloc[-1]
        
        pv = latest_schedule['Planned_Value']  # Planned Value
        ev = latest_schedule['Earned_Value']   # Earned Value
        ac = latest_cost['Cumulative_Spent']   # Actual Cost
        
        # Calculate EVM metrics
        cv = ev - ac  # Cost Variance
        sv = ev - pv  # Schedule Variance
        
        spi = ev / pv if pv > 0 else 1.0
        cpi = ev / ac if ac > 0 else 1.0
        
        # Performance metrics
        tcpi = (5000000 - ev) / (5000000 - ac) if ac < 5000000 else float('inf')  # To-Complete Performance Index
        eac = ac + (5000000 - ev) / cpi if cpi > 0 else 5000000  # Estimate at Completion
        etc = eac - ac  # Estimate to Complete
        vac = 5000000 - eac  # Variance at Completion
        
        return {
            'Planned_Value': round(pv, 2),
            'Earned_Value': round(ev, 2),
            'Actual_Cost': round(ac, 2),
            'Cost_Variance': round(cv, 2),
            'Schedule_Variance': round(sv, 2),
            'SPI': round(spi, 3),
            'CPI': round(cpi, 3),
            'TCPI': round(tcpi, 3) if tcpi != float('inf') else 'N/A',
            'EAC': round(eac, 2),
            'ETC': round(etc, 2),
            'VAC': round(vac, 2)
        }
    
    def calculate_productivity_benchmarks(self):
        """Calculate productivity benchmarks and comparisons"""
        
        if len(self.productivity_df) == 0:
            return {}
        
        current = self.productivity_df.iloc[-1]
        
        # Historical averages
        avg_labor_efficiency = self.productivity_df['Labor_Hours_Per_Unit'].mean()
        avg_equipment_util = self.productivity_df['Equipment_Utilization_Pct'].mean()
        avg_waste = self.productivity_df['Material_Waste_Pct'].mean()
        
        # Performance vs averages
        labor_vs_avg = ((current['Labor_Hours_Per_Unit'] - avg_labor_efficiency) / avg_labor_efficiency) * 100
        equip_vs_avg = ((current['Equipment_Utilization_Pct'] - avg_equipment_util) / avg_equipment_util) * 100
        waste_vs_avg = ((current['Material_Waste_Pct'] - avg_waste) / avg_waste) * 100
        
        return {
            'Current_Labor_Hours_Per_Unit': round(current['Labor_Hours_Per_Unit'], 2),
            'Average_Labor_Hours_Per_Unit': round(avg_labor_efficiency, 2),
            'Labor_Efficiency_vs_Average': f"{labor_vs_avg:+.1f}%",
            'Current_Equipment_Utilization': f"{current['Equipment_Utilization_Pct']:.1f}%",
            'Average_Equipment_Utilization': f"{avg_equipment_util:.1f}%",
            'Equipment_Util_vs_Average': f"{equip_vs_avg:+.1f}%",
            'Current_Material_Waste': f"{current['Material_Waste_Pct']:.1f}%",
            'Average_Material_Waste': f"{avg_waste:.1f}%",
            'Waste_vs_Average': f"{waste_vs_avg:+.1f}%"
        }
    
    def generate_executive_summary(self):
        """Generate executive summary of project status"""
        
        health_score = self.calculate_project_health_score()
        completion_date = self.predict_completion_date()
        cost_confidence = self.calculate_cost_forecast_confidence()
        risks = self.identify_risk_trends()
        evm_metrics = self.calculate_earned_value_metrics()
        
        # Project status assessment
        if health_score >= 80:
            status = "🟢 Excellent"
        elif health_score >= 70:
            status = "🟡 Good"
        elif health_score >= 60:
            status = "🟠 Fair"
        else:
            status = "🔴 Poor"
        
        summary = {
            'Overall_Health_Score': f"{health_score}/100",
            'Project_Status': status,
            'Predicted_Completion': completion_date,
            'Cost_Forecast_Confidence': cost_confidence,
            'Primary_Risks': risks[:3],  # Top 3 risks
            'Current_CPI': evm_metrics.get('CPI', 'N/A'),
            'Current_SPI': evm_metrics.get('SPI', 'N/A'),
            'Estimated_Final_Cost': f"${evm_metrics.get('EAC', 0):,.0f}" if evm_metrics.get('EAC') else 'N/A'
        }
        
        return summary

def generate_analytics_report(schedule_df, cost_df, productivity_df, safety_df, quality_df):
    """Generate comprehensive analytics report"""
    
    analytics = ConstructionAnalytics(schedule_df, cost_df, productivity_df, safety_df, quality_df)
    
    report = {
        'executive_summary': analytics.generate_executive_summary(),
        'earned_value_metrics': analytics.calculate_earned_value_metrics(),
        'productivity_benchmarks': analytics.calculate_productivity_benchmarks(),
        'risk_analysis': analytics.identify_risk_trends()
    }
    
    return report
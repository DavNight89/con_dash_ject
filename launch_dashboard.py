"""
Simple launcher for the Construction Dashboard
This script handles common setup issues and launches the dashboard
"""

import subprocess
import sys
import os
import time
import streamlit   

def check_streamlit():
    """Check if streamlit is installed"""
    try:
        import streamlit
        return True
    except ImportError:
        return False

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages")
        return False

def check_data_files():
    """Check if data files exist"""
    data_files = [
        "data/schedule_data.csv",
        "data/cost_data.csv", 
        "data/productivity_data.csv",
        "data/safety_data.csv",
        "data/quality_data.csv",
        "data/critical_path_tasks.csv",
        "data/cost_breakdown.csv"
    ]
    
    missing_files = []
    for file_path in data_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    return len(missing_files) == 0, missing_files

def generate_data():
    """Generate sample data"""
    print("Generating sample data...")
    try:
        subprocess.check_call([sys.executable, "src/data_generator.py"])
        print("✅ Data generated successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to generate data")
        return False

def launch_dashboard():
    """Launch the Streamlit dashboard"""
    print("\n🏗️ Launching Construction Dashboard...")
    print("This will open your web browser automatically.")
    print("If it doesn't, go to: http://localhost:8501")
    print("\nPress Ctrl+C to stop the dashboard")
    print("=" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "src/dashboard.py"])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to launch dashboard: {e}")

def main():
    """Main launcher function"""
    print("🏗️ Construction Dashboard Launcher")
    print("=" * 40)
    
    # Check if streamlit is installed
    if not check_streamlit():
        print("📦 Streamlit not found. Installing packages...")
        if not install_requirements():
            print("Please install packages manually: pip install -r requirements.txt")
            return
    
    # Check if data files exist
    data_exists, missing_files = check_data_files()
    if not data_exists:
        print(f"📊 Data files missing: {len(missing_files)} files")
        if not generate_data():
            print("Please generate data manually: python src/data_generator.py")
            return
    else:
        print("✅ Data files found")
    
    # Launch dashboard
    launch_dashboard()

if __name__ == "__main__":
    main()
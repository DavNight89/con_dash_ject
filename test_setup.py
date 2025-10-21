"""
Test script to verify the construction dashboard setup
"""

import sys
import os

def test_python_version():
    """Test if Python version is sufficient"""
    print("Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is too old. Need 3.8+")
        return False

def test_required_packages():
    """Test if required packages can be imported"""
    required_packages = [
        ('pandas', 'Data manipulation'),
        ('numpy', 'Numerical computing'),
        ('streamlit', 'Web app framework'),
        ('plotly', 'Interactive plotting'),
    ]
    
    print("\nTesting required packages...")
    all_good = True
    
    for package, description in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - {description}")
        except ImportError:
            print(f"❌ {package} - {description} (Not installed)")
            all_good = False
    
    return all_good

def test_project_structure():
    """Test if project structure is correct"""
    print("\nTesting project structure...")
    
    required_dirs = ['src', 'config']
    required_files = [
        'src/dashboard.py',
        'src/data_generator.py',
        'src/analytics.py',
        'config/config.py',
        'requirements.txt',
        'setup.bat',
        'run_dashboard.bat'
    ]
    
    all_good = True
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✅ Directory: {directory}")
        else:
            print(f"❌ Directory missing: {directory}")
            all_good = False
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ File: {file_path}")
        else:
            print(f"❌ File missing: {file_path}")
            all_good = False
    
    return all_good

def test_data_generation():
    """Test if data can be generated"""
    print("\nTesting data generation...")
    
    try:
        # Import data generator
        sys.path.append('src')
        from data_generator import generate_construction_data, generate_critical_path_tasks, generate_cost_breakdown
        
        print("✅ Data generator imports successful")
        
        # Test data generation
        schedule_df, cost_df, productivity_df, safety_df, quality_df = generate_construction_data()
        critical_path_df = generate_critical_path_tasks()
        cost_breakdown_df = generate_cost_breakdown()
        
        print(f"✅ Generated {len(schedule_df)} weeks of schedule data")
        print(f"✅ Generated {len(cost_df)} weeks of cost data") 
        print(f"✅ Generated {len(productivity_df)} weeks of productivity data")
        print(f"✅ Generated {len(safety_df)} weeks of safety data")
        print(f"✅ Generated {len(quality_df)} weeks of quality data")
        print(f"✅ Generated {len(critical_path_df)} critical path tasks")
        print(f"✅ Generated {len(cost_breakdown_df)} cost categories")
        
        return True
        
    except Exception as e:
        print(f"❌ Data generation failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("🏗️ Construction Dashboard Setup Test")
    print("=" * 40)
    
    tests = [
        ("Python Version", test_python_version),
        ("Project Structure", test_project_structure),
        ("Data Generation", test_data_generation),
        ("Required Packages", test_required_packages),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        result = test_func()
        results.append((test_name, result))
    
    print(f"\n{'='*40}")
    print("TEST SUMMARY:")
    print("=" * 40)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 40)
    if all_passed:
        print("🎉 All tests passed! Your dashboard is ready to run.")
        print("\nNext steps:")
        print("1. Run 'python src/data_generator.py' to create sample data")
        print("2. Run 'streamlit run src/dashboard.py' to start the dashboard")
    else:
        print("⚠️ Some tests failed. Please address the issues above.")
        print("\nIf packages are missing, run:")
        print("pip install -r requirements.txt")

if __name__ == "__main__":
    main()
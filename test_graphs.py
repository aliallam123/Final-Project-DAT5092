import unittest
import subprocess
import os

class TestGraphGeneration(unittest.TestCase):
    
    def setUp(self):
        # Define the directory where your scripts are located
        self.script_dir = 'C:\\Users\\banta\\Downloads\\DAT5092 Final Project'

    def run_script(self, script_name):
        # Constructs the full path to the script
        script_path = os.path.join(self.script_dir, script_name)
        # Runs the script and waits for it to finish
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        # Check if the script executed successfully
        self.assertEqual(result.returncode, 0, f"Script {script_name} failed: {result.stderr}")

    def test_bar_graph_company_size(self):
        self.run_script('company_size_salary.py')
        
    def test_location_bar(self):
        self.run_script('location_bar.py')

    def test_location_salary(self):
        self.run_script('location_salary.py')

    def test_remote_workers_salary(self):
        self.run_script('remote_workers_salary.py')

    def test_salaries_over_the_years(self):
        self.run_script('salaries_over_the_years.py')

    def test_salary_experience_boxplot(self):
        self.run_script('salary_experience_boxplot.py')

if __name__ == '__main__':
    unittest.main()
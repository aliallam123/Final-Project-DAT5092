# Key Tests for AI/ML Salary Analysis Project
## Test Suite Overview
This document outlines the key tests for the Python scripts analyzing AI/ML salaries using various graphs. The tests ensure the correct functionality of data loading, graph generation, and statistical calculations.

### Test 1: Data Loading
Purpose: Ensure the dataset is loaded correctly without errors.
Coverage: Tests the pd.read_csv('ai_salaries.csv') function.
Expected Outcome: Dataframe df is not empty and contains expected columns like 'salary_in_usd'.
### Test 2: Graph Generation
Purpose: Verify that each graph type is generated without errors.
Coverage: Tests functions generating 5 bar graphs, 1 box plot, 1 treemap, 1 heatmap, and 1 line graph.
Expected Outcome: Each graph object is created successfully.
Sub-tests for Graph Generation
2.1 Bar Graphs
Ensure each of the 5 bar graphs is generated.
2.2 Box Plot
Confirm the box plot is generated.
2.3 Tree Map
Check the creation of the treemap.
2.4 Heatmap
Verify the heatmap is generated.
2.5 Line Graph
Ensure the line graph is produced.
### Test 3: Mean and Median Calculations
Purpose: Validate the correctness of mean and median salary calculations.


# Unit testing is in test_graphs.py file
## Otherwise, see below for unit testing code:
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

Coverage: Includes tests for calculations like df.groupby('company_size')['salary_in_usd'].mean().reset_index().
Expected Outcome: The calculated means and medians should match expected values based on the dataset.
#### Example Sub-test for Mean Calculation
3.1 Mean Salary by Company Size
Test if the mean salary calculation for different company sizes is accurate.

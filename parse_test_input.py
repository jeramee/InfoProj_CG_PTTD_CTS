# parse_test_input.py

import os
import sys
import pandas as pd
import xlrd  # Add xlrd to handle older .xls files

# Add the current directory or specific project root to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
project_root = os.path.abspath(os.path.join(script_dir, os.pardir))  # Assuming project root is one level up
sys.path.append(project_root)  # Add project root to system path

class ParseTestInput:
    def __init__(self, input_dir):
        """
        Initialize with the directory where input files are stored.
        """
        self.input_dir = os.path.abspath(input_dir)  # Absolute path for input directory
        self.files = {
            'control_genes': 'control_genes.txt',
            'down_genes': 'down_genes.txt',
            'up_genes': 'up_genes.txt',
            'regions_to_genes': 'regionsToGenes.xls',
            'known_genes': 'mm9.20150218.knownGene.xls',
            'cumulative_stats': 'up_genes.txt.regionsToGenes.xls.100.10.1000.cumulative.txt'
        }
    
    def load_text_file(self, file_name):
        """
        Loads a text file from the test input folder.
        
        Args:
            file_name (str): The name of the text file to load.
        
        Returns:
            list: A list of gene identifiers from the text file.
        """
        file_path = os.path.join(self.input_dir, file_name)
        try:
            print(f"Loading file from path: {file_path}")
            with open(file_path, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return []
    
    def load_excel_file(self, file_name):
        """
        Attempts to load an Excel file. If the file format is not supported, tries loading as a TSV or CSV.
        
        Args:
            file_name (str): The name of the Excel file to load.
        
        Returns:
            pd.DataFrame: A pandas DataFrame containing the file contents.
        """
        file_path = os.path.join(self.input_dir, file_name)
        try:
            print(f"Loading Excel file from path: {file_path}")
            # Use `openpyxl` for `.xlsx` and `xlrd` for `.xls`, but catch unsupported format errors
            if file_name.endswith('.xlsx'):
                return pd.read_excel(file_path, engine='openpyxl')
            elif file_name.endswith('.xls'):
                return pd.read_excel(file_path, engine='xlrd')
            else:
                print(f"Unsupported file extension for {file_name}.")
                return pd.DataFrame()
        except (ValueError, FileNotFoundError, pd.errors.EmptyDataError, xlrd.biffh.XLRDError) as e:
            print(f"Error loading {file_name} as Excel: {e}")
            print("Attempting to load as tab-separated text file instead.")
            try:
                return pd.read_csv(file_path, sep='\t')
            except Exception as e2:
                print(f"Error loading {file_name} as TSV: {e2}")
                return pd.DataFrame()

    def load_data(self):
        """
        Loads and processes all test input files.
        
        Returns:
            dict: A dictionary containing all parsed data from the input folder.
        """
        data = {}
        for key, file_name in self.files.items():
            if file_name.endswith('.txt'):
                data[key] = self.load_text_file(file_name)
            else:
                data[key] = self.load_excel_file(file_name)
        return data
    
    def parse_and_print(self):
        """
        Parse files and print their content.
        """
        data = self.load_data()
        for key, content in data.items():
            print(f"Content of {key}: {content}")

if __name__ == "__main__":
    input_dir = os.path.join(script_dir, "data", "test_input")  # Dynamically set the input directory
    parser = ParseTestInput(input_dir)
    parser.parse_and_print()

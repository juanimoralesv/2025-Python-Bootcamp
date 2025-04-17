# -*- coding: utf-8 -*-
"""
This is a compilation of the custom functions created for processing the
GCAT, or Jonathan McDowell's General Catalog of Artificial Space Objects.
"""

# Libraries
import requests
import pandas as pd

# Function for downloading files
def download_file(url, filename):
  response = requests.get(url)
  with open(filename, 'wb') as f:
    f.write(response.content)
    
# Function for initial file processing
def initial_processing(file_path):
  file_contents = open(file_path, encoding = 'ISO-8859-1').read() # read file
  if file_contents[0] == '#':
      file_contents = file_contents[1:] # remove first character
  else:
      print('First character not "#". URL:\n')
      print(f'{file_path}')
  lines = file_contents.split('\n') # split in lines
  if lines[1][0] == '#':
      second_line = lines.pop(1).strip()[1:] # store 2nd line without first character
  else:
      second_line = lines.pop(1).strip()
      print('Second line not starting with "#". URL:\n')
      print(f'{file_path}')
  file_contents = '\n'.join(lines) # restore file as a single string
  return file_contents, second_line

# Function for saving files
def save_file(file_path, file_contents):
  with open(file_path, 'w') as f:
    f.write(file_contents)
    
# Function for analyzing a `DataFrame`
def analyze_df(df):
    num_rows = df.shape[0]
    num_cols = df.shape[1]
    s_num_nulls = df.isnull().sum()
    total_nulls = df.isnull().sum().sum()
    # Prepare a report DataFrame
    df_report = pd.DataFrame(
        {
            'data_type': [df[col].dtype.name for col in df.columns],
            '#_unique': [df[col].nunique() for col in df.columns],
            '#_not_null': num_rows - s_num_nulls,
            '#_nulls': s_num_nulls,
            '%_nulls': 100 * df.isnull().mean().round(4)
        }
    )

    print(df_report, '\n')
    print('Additionally:\n')
    print(f'The total number of nulls is: {total_nulls}\n')
    print(f'And the DataFrame has {num_rows} rows and {num_cols} columns.')
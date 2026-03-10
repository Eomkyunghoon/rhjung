# Python VectorCAST Excel Converter Tool

## Overview
This repository contains a Python tool for converting VectorCAST test cases in Excel format. It includes the main application, parsers for `.tst` and `.env` files, and a build script for generating executable files.

## Components

### Main Application
The core of the converter that reads input files and generates Excel output.

### Parsers
- **.tst Parser**: Responsible for reading and processing `.tst` files.
- **.env Parser**: Handles `.env` files for configuration settings.

### Build Script
A script to build the main application into an executable format.

## Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To run the main application, execute:
```bash
python main.py input.tst output.xlsx
```
```
# requirements.txt

# Add necessary packages here
# Example:
pandas
openpyxl

# main.py

import sys
import pandas as pd

# Main application logic to convert VectorCAST files to Excel

def convert_to_excel(tst_file: str, output_file: str) -> None:
    # Logic to read .tst file and create an Excel file
    pass

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py input.tst output.xlsx")
        sys.exit(1)
    convert_to_excel(sys.argv[1], sys.argv[2])

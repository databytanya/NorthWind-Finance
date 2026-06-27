# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# ## Bronze Unzipper 
# 
# The raw data is provided by the user in a zip format. The purpose of this piece of code is to unzip the file and upload it in a folder

# CELL ********************

# MAGIC %%configure -f
# MAGIC {"defaultLakehouse": { 
# MAGIC         "name": "NorthWind_Finance_lakehouse"
# MAGIC     }
# MAGIC }


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import os 
path = r'/lakehouse/default/Files/Bronze_zip/Northwind-Finance-Dataset.zip'
out_path = r'/lakehouse/default/Files/Bronze_unzipped/'
import zipfile
import os
from pathlib import Path

def extract_zip(zip_path, extract_to):
    """
    Extract a zip file to a directory.
    
    Args:
        zip_path: Path to the zip file
        extract_to: Directory to extract to (defaults to a folder named after the zip)
    """
    zip_path = Path(zip_path)
    
    if not zip_path.exists():
        print(f"Error: {zip_path} not found")
        return
    
    # Default extraction directory
    if extract_to is None:
        extract_to = zip_path.parent / zip_path.stem
    
    extract_to = Path(extract_to)
    extract_to.mkdir(parents=True, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print(f"✓ Extracted to: {extract_to}")
    print(f"  Files: {len(zip_ref.namelist())}")

# Usage

extract_zip(path,out_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

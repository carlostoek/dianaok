#!/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python database/setup.py

# Run the main application
python main.py

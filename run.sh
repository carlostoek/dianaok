#!/bin/bash

# Step a: Install dependencies
pip install -r requirements.txt

# Step b: Run the codebase
export BOT_TOKEN='YOUR_ACTUAL_BOT_TOKEN'
python src/main.py

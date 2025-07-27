#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the bot and tests in parallel
python -m src.bot & pytest tests/

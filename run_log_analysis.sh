#!/bin/bash

SOURCE_DIR="logs/source"
DEST_DIR="logs/processed"

echo "Starting log analysis..."
python log_analysis_script.py $SOURCE_DIR $DEST_DIR
echo "Log analysis completed."
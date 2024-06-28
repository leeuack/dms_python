#!/bin/bash

# Get the current directory
current_dir=$(pwd)

# Run Jupyter Notebook with the current directory as the notebook directory
jupyter notebook --notebook-dir="$current_dir"

#!/bin/bash

# Function to check if a command exists
command_exists () {
    command -v "$1" >/dev/null 2>&1 ;
}

# Check if Python is installed
if command_exists python3; then
    echo "Python is already installed."
else
    echo "Python is not installed. Installing Python..."
    # Install Python (this example is for Ubuntu/Debian-based systems)
    sudo apt update
    sudo apt install -y python3
fi

# Check if pip is installed
if command_exists pip3; then
    echo "pip is already installed."
else
    echo "pip is not installed. Installing pip..."
    # Install pip (this example is for Ubuntu/Debian-based systems)
    sudo apt install -y python3-pip
fi

# Check if requirements.txt exists
if [ -f requirements.txt ]; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
else
    echo "requirements.txt not found!"
    exit 1
fi

# Run the main Python script
echo "Running the main script..."
python3 main.py

#!/bin/sh 

# This is to create a script to validate date input from user
# Include 
# - valid date format should be YYYY-MM-DD
# - valid date should be in the past
# - valid date should be after 1900-01-01
# - valid date should be before current date
# - valid date should be a real date (e.g. 2021-02-30 is not a real date)

# Get current date in YYYY-MM-DD format
current_date=$(date +%Y-%m-%d)
# Get user input
read -p "Enter a date (YYYY-MM-DD): " input_date
# Validate date format using regex
if ! echo "$input_date" | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' > /dev/null; then
    echo "Invalid date format. Please use YYYY-MM-DD."
    exit 1
fi
# Validate date is in the past and after 1900-01-01
if ! date -d "$input_date" > /dev/null 2>&1; then
    echo "Invalid date. Please enter a real date."
    exit 1
fi
if [ "$(date -d "$input_date" +%s)" -ge "$(date -d "$current_date" +%s)" ]; then
    echo "Invalid date. Date should be in the past."
    exit 1
fi
if [ "$(date -d "$input_date" +%s)" -le "$(date -d "1900-01-01" +%s)" ]; then
    echo "Invalid date. Date should be after 1900-01-01."
    exit 1      
    
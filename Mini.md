# Expense Tracker

## Overview

This project is a simple Expense Tracker application built using Python. It allows users to input expenses categorized by type and provides functionality to view total expenses by category and overall.

## Features

- Input expenses with associated categories
- View total expenses by category
- View overall total expenses
- Simple command-line interface

## Requirements

- Python 3.x
- CSV library (included in Python standard library)

## Installation

1. Clone the repository using `git clone https://github.com/your-username/Expense-Tracker.git`
2. Navigate to the project directory using `cd Expense-Tracker`
3. Run the application using `python main.py`

## Usage

1. Run the application using `python main.py`
2. Choose an option from the main menu:
   - **Add an Expense**: Input the amount and category of the expense.
   - **View Summaries**: Choose to view total spending by category or overall spending.
   - **Exit the Program**: Exit the application.
3. Follow the prompts to enter data or view summaries.

## Functions

- **amount()**: Prompts the user to enter an amount and category, storing the data in a dictionary and writing it to a CSV file.
- **total()**: Reads the CSV file and calculates the total amount for a specified category.
- **sum_all()**: Reads the CSV file and calculates the overall total amount of all expenses.
- **summary()**: Provides a menu for the user to choose between viewing total spending by category or overall spending.
- **main()**: The main function that drives the application, presenting the main menu and handling user input.

## Troubleshooting

- If the application fails to load data from the CSV file, ensure that the file is in the correct location.
- If the application fails to save data to the CSV file, ensure that the file is writable.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.


## Acknowledgments

- Python for providing a powerful programming language for building this application.
- CSV library for providing a simple way to read and write CSV files.
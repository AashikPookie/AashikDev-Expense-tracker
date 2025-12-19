# Expense Tracker

## Overview
A simple console-based expense tracking application built with Python. Allows users to track their expenses with dates, categories, and descriptions.

## Features
- Add expenses with date, category, description, and amount
- View all recorded expenses with running total
- View expenses grouped by category
- Delete expenses
- Persistent storage using JSON file

## How to Run
Run the application using `python main.py` in the console. The app presents an interactive menu for managing expenses.

## Project Structure
- `main.py` - Main application file with all expense tracking logic
- `expenses.json` - Data file storing expenses (created automatically on first use)

## Categories
Available expense categories:
1. Food
2. Transport
3. Entertainment
4. Utilities
5. Shopping
6. Other

## Data Storage
Expenses are stored in `expenses.json` with the following structure:
```json
{
  "date": "YYYY-MM-DD",
  "category": "Category Name",
  "description": "Description text",
  "amount": 0.00
}
```

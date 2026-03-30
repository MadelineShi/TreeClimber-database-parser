# TreeClimber Database Parser

This project parses course data from JSON files and populates a MySQL database.

## How to Run

1. Install dependencies:
pip install mysql-connector-python python-dotenv

2. Create a `.env` file:
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=TreeClimber

3. Run the parser:
python3 populate_db.py

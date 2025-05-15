Python Generators and SQL Integration

Python generators and MySQL is effectively used throughout this project to seed and stream data from the database with the least amount of memory.
Files

- `seed.py`: Install the database and imports user data from a CSV file.
- `0-main.py`: Entry script for running all setup and showing output of sample query.

Usage

Make sure you have:
- MySQL server running
- (`pip install mysql-connector-python`) `mysql-connector-python` installed
- A `user_data.csv` file in the same directory, having the right headers:
  - `user_id,name,email,age`

Then run:

```bash
chmod +x 0-main.py
./0-main.py

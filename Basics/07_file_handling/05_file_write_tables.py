"""
Write a program to generate multiplication tables from 2 to 20 and write it to
different files. Place these files in a folder for a 13-year-old.
"""

import os

# Create tables folder if it doesn't exist
os.makedirs("tables", exist_ok=True)

for table_num in range(2, 21):
    with open(f"tables/Table_of_{table_num}", "w") as f:
        for i in range(1, 11):
            f.write(f"{table_num} * {i} = {table_num * i}\n")

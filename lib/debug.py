from __init__ import CONN, CURSOR
from department import Department

import ipdb

# File is set up so that you can explore the DB using the Dept. class from an ipdb sesh.
def reset_database():
    Department.drop_table()
    Department.create_table()

    Department.create("Payroll", "Building A, 5th Floor") # Create & saves a new Dept. instance to DB
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

reset_database()
ipdb.set_trace()
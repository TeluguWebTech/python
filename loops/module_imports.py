#fmt:off

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from emp_data import employees
from modules import emp_city

for i in employees:
    print(i)

print(emp_city)

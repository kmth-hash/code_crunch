# https://leetcode.com/problems/rename-columns/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns = {
        "id" : "student_id" ,
        "first" : "first_name" ,
        "last": "last_name", 
        "age": "age_in_years"
    })
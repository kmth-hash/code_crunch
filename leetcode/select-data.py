# https://leetcode.com/problems/select-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    res = students[students['student_id']==101][['name' , 'age']]
    return(res)
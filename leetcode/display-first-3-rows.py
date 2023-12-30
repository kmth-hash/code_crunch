#https://leetcode.com/problems/display-the-first-three-rows/description/

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # ls = [i for i in employees.columns]

    # res = pd.DataFrame()

    # res[ls[0]] = employees[ls[0]]
    # res[ls[1]] = employees[ls[1]]
    # res[ls[2]] = employees[ls[2]]

    return(employees.head(3))
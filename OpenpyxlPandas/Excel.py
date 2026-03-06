from openpyxl import load_workbook
import pandas as pd
from pyparsing import sglQuotedString

# read excel sheet
# df = pd.read_excel("C:/Users/HP/Desktop/february/transactionDetails/AutomationPandas/excel.xlsx")

# writing to excel

data = {
    "Name": ["Ram", "Ravi", "Sita"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

df.to_excel("output.xlsx", index=False, engine="openpyxl")

# read a specific column
df = pd.read_excel("output.xlsx", usecols=["Name"], engine="openpyxl")
print(df)
#

#read a particular sheet
df = pd.read_excel("student.xlsx",
                   sheet_name="sheet1",
                   engine="openpyxl")
print(df)

#read all sheet
df = pd.read_excel("student.xlsx",
                   sheet_name=None)
print(df)

#writing Multiple sheets

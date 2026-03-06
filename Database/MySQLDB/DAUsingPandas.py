import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("Priyadarshee@2003")

engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost/school"
)
df =pd.read_sql('select * from students',engine)

print(df)

# average marks
print(df["marks"].mean())

#highest score
print(df[df["marks"]==df["marks"].max()])

#group by subjects
print(df.groupby("subject")["marks"].mean())


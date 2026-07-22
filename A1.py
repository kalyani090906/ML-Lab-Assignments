import pandas as pd

def load_data():
    df = pd.read_excel("marketing_campaign.xlsx")
    return df

df = load_data()

print(df.head())
print(df.info())





# ID	Nominal	
# Education	Nominal	
# Marital_Status	Nominal	
# Income	Ratio	
# Recency	Ratio	
# Dt_Customer	Interval
# MntWines	Ratio	
# AcceptedCmp1	Nominal
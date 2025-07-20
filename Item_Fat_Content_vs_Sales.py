import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading
df = pd.read_csv(r"C:\Users\ANURAG PAL\Documents\KCC INSTITUTE (COLLEGE)\Python practice\Projects\EDA\blinkit.csv")

#data cleaning 
df=df.dropna(subset=['Item_Identifier','Item_Fat_Content','Item_Visibility','Item_Type','Item_MRP','Outlet_Identifier','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type','Item_Outlet_Sales'])
df['Item_Fat_Content'].replace(["LF","low fat"],"Low Fat",inplace=True)
df['Item_Fat_Content'].replace("reg","Regular",inplace=True)
df['Item_Fat_Content'].drop_duplicates(inplace=True)
df.drop_duplicates(inplace=True)
df.drop_duplicates(subset="Item_Identifier",inplace=True)

#visualize
sns.violinplot(x='Outlet_Size', y='Item_Outlet_Sales', data=df)
plt.title('Outlet Sales over diffrent Outlet Size')
plt.show()
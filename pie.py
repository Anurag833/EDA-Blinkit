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
fig, ax= plt.subplots(2,2)
outlet_size = df['Outlet_Size'].value_counts()
outlet_loc = df['Outlet_Location_Type'].value_counts()
outlet_type = df['Outlet_Type'].value_counts()

# Chart 1
ax[0, 0].pie(outlet_size, labels=outlet_size.index, autopct='%1.1f%%', startangle=90)
ax[0, 0].set_title("Outlet Size Distribution")

# Chart 2
ax[0, 1].pie(outlet_loc, labels=outlet_loc.index, autopct='%1.1f%%', startangle=90)
ax[0, 1].set_title("Outlet Location Type")

# Chart 3
ax[1, 0].pie(outlet_type, labels=outlet_type.index, autopct='%1.1f%%', startangle=90)
ax[1, 0].set_title("Outlet Type Distribution")

# Chart 4 empty
ax[1, 1].axis('off')

plt.tight_layout()
plt.show()
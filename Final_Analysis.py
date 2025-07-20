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

#visualize-1
item= df['Item_Fat_Content'].value_counts()
plt.bar(item.index,item.values,color=['blue','green'])
plt.title("No of item in each fat category")
plt.xlabel("Fat Category")
plt.ylabel("Count")
plt.show()

#visualize-2
sns.countplot(x="Item_Fat_Content",data=df, hue='Item_Type', edgecolor='black')
plt.title("Item Type & Fat Category wise Count")
plt.xlabel('Fat Category')
plt.show()

#visualize-3
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


#visualize-4
sns.violinplot(x='Outlet_Size', y='Item_Outlet_Sales', data=df)
plt.title('Outlet Sales over diffrent Outlet Size')
plt.show()


#visualize-5
sns.scatterplot(x='Item_MRP', y='Item_Outlet_Sales', data=df,hue='Item_Fat_Content',style='Item_Fat_Content')
plt.title('sales of items over MRP')
plt.show()


#visualize-6
data= sns.FacetGrid(df,col='Outlet_Size')
data.map(plt.bar,'Item_Fat_Content','Item_Outlet_Sales')
plt.show()


#visualize-7
sns.pairplot(x_vars=["Outlet_Establishment_Year","Item_Weight"], y_vars=["Item_MRP","Item_Outlet_Sales"], data=df)
plt.show()


#visualize-8
sns.stripplot(x='Outlet_Type', y='Item_Outlet_Sales', data=df, size=2)
plt.title('sales on different outlet type')
plt.show()
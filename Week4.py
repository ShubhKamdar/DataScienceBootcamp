import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Question 1
# 1. Create a line plot of ZN and INDUS in the housing data.
# 	a. For ZN, use a solid green line. For INDUS, use a blue dashed line.
# 	b. Change the figure size to a width of 12 and height of 8.
# 	c. Change the style sheet to something you find https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html.

# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# print(df)
# df[["ZN","INDUS"]].plot(style={'ZN':'g','INDUS':'--b'})
# plt.show()

# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# df[["ZN","INDUS"]].plot(style={'ZN':'g','INDUS':'--b'},figsize=(12,8))
# plt.show()

# plt.style.use('dark_background')
# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# df[["ZN","INDUS"]].plot(style={'ZN':'g','INDUS':'--b'},figsize=(12,8))
# plt.show()




# Question2
# 2. Create a bar chart using col1 and col2 of dummy data.

# 	a. Give the plot a large title of your choosing.
# 	b. Move the legend to the lower-left corner.
# 	c. Do the same thing but with horizontal bars.
# 	d. Move the legend to the upper-right corner.

# df=pd.DataFrame(np.random.randn(10,4),columns=['1','2','3','4'])
# a=df[['1','2']].plot()
# a.set_title('Random',fontsize=50,y=1)
# plt.show()

# df=pd.DataFrame(np.random.randn(10,4),columns=['1','2','3','4'])
# a=df[['1','2']].plot(kind='bar')
# a.set_title('Random',fontsize=50,y=1)
# a.legend(loc=-0)
# plt.show()

# df=pd.DataFrame(np.random.randn(10,4),columns=['1','2','3','4'])
# a=df[['1','2']].plot(kind='barh')
# a.set_title('Random',fontsize=50,y=1)
# a.legend(loc=-0)
# plt.show()

# df=pd.DataFrame(np.random.randn(10,4),columns=['1','2','3','4'])
# a=df[['1','2']].plot(kind='bar')
# a.set_title('Random',fontsize=50,y=1)
# a.legend(loc=1)
# plt.show()

# 3. Create a histogram with pandas for using MEDV in the housing data.

# 	a. Set the bins to 20

# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# df[['MEDV']].hist(bins=20)
# plt.show()

# 4. Create a scatter plot of two heatmap entries that appear to have a very positive correlation.
# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# correlation=df.corr()
# sns.heatmap(correlation)
# df.plot(kind='scatter',x='LSTAT',y='MEDV')
# plt.show()

# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# correlation=df.corr()
# sns.heatmap(correlation)
# df.plot(kind='scatter',x='LSTAT',y='RM')
# plt.show()

# 5. Now, create a scatter plot of two heatmap entries that appear to have negative correlation.

# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# correlation=df.corr()
# sns.heatmap(correlation)
# df.plot(kind='scatter',x='AGE',y='NOX')
# plt.show()

# df=pd.read_csv('D:/Python Data Science/Bootcamp/boston_housing_data.csv')
# correlation=df.corr()
# sns.heatmap(correlation)
# df.plot(kind='scatter',x='TAX',y='INDUS')
# plt.show()
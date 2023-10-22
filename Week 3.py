import pandas as pd
import numpy as np

# Numpy Practice Questions
# 1. Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.
# 2. Find common elements between A and B. [Hint : Intersection of two sets]
# 3. Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]
# 4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
# 	url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# 	iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

# Question 1
# a=np.random.randint(10, size=(2,3))
# b=np.random.randint(10, size=(2,3))
# x=np.vstack((a,b))
# z=np.hstack((a,b))
# print(x)
# print(z)

# Question 2
# a=np.array([[0, 5, 5],[5 ,1 ,2],[7, 6, 7], [3 ,1 ,2]])
# b=np.array([[0, 99 ,99, 7 ,6 ,99],[99, 99, 2 ,99 ,99 ,2]])
# c=[]
# for row in a:
#     for iteminrow in row:
#         if iteminrow in b:
#             c.append(iteminrow)
# print(c)

# Question 3
# a=np.array([[0, 5, 5],[5 ,1 ,2],[7, 6, 7], [3 ,1 ,2]])
# b=[]
# for row in a:
#     for item in row:
#         if 5<item<=10:
#             b.append(item)
# print(b)

# Question 4
# 4. Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
# a=iris_2d[(iris_2d[:,2]>1.5) & (iris_2d[:,0]<5)]
# print(a)

# PANDAS Pracice Questions
# Practice Questions for Pandas
# 1. From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# 2. Replace missing values in Min.Price and Max.Price columns with their respective mean.
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

# 3. How to get the rows of a dataframe with row sum > 100?
# df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

# Question 1
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# a=df[::20]
# b=a[['Manufacturer', 'Model', 'Type']]
# print(b)

# Question 2
# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# minpricemean=df[ 'Min.Price'].mean()
# maxpricemean=df[ 'Max.Price'].mean()
# df['Min.Price'] = df['Min.Price'].fillna(minpricemean)
# df['Max.Price'] = df['Max.Price'].fillna(maxpricemean)
# print(df)

# Question 3
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
row=df.sum(axis=1)
print(df[row>100])
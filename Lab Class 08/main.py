import pandas as pd
data=pd.read_csv('HR_comma_sep.csv')
# print(data)
# step:1 missing any data .row ro colum
# print(data.isnull().values.any())

# step:2 data type
# print(data.dtypes)

# step:3 check unique values
# print(data.salary.unique())
# print(data.Department.unique())

clean_up_data={
   "salary":{
       'low':1,
       'medium':2,
       'high':3
   }
}

data.replace(clean_up_data,inplace=True)
print(data)

# step : 4 get dummies for the  Department
dummies = pd.get_dummies(data.Department)
# print(dummies)

# step: 5 merge dummies (dummy columns) with

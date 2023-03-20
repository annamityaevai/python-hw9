# Задача. В ячейке ниже представлен код генерирующий DataFrame, которая 
# состоит всего из 1 столбца. #Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head()

import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()
one_hot_dict = {value: [1 if value == x else 0 for x in unique_values] for value in unique_values}

for key in one_hot_dict:
    data[key] = data['whoAmI'].apply(lambda x: one_hot_dict[key][list(unique_values).index(x)])

data = data.drop('whoAmI', axis=1)

print(data.head())
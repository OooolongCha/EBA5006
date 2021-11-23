# import necessary packages - pandas, numpy
import pandas as pd
import numpy as np
# load json file
file = '/Users/Ivan Junqi Wu/Desktop/PlayStoreGameAppInfoReview 2.json'
data = pd.read_json(file)
# mark column into numbers from 1 to 170 representing each game
i = 1
for keys in data:
    data[i] = data.pop(keys)
    i = i + 1
# covert the data into dafaframe
data = pd.DataFrame(data)
# check reviews shape
reviews = data.iloc[1]
# extract reviews into a single dataframe
reviews = pd.DataFrame(reviews)
# transpose the dataframe
reviews = pd.DataFrame(reviews.T, index=reviews.columns, columns=reviews.index)
# check the shape of the reviews
i = 1
reviews_df = pd.DataFrame()
while i <= 170:
    reviews_select = reviews.iloc[0][i]
    for item in reviews_select:
        d = {'Game{}'.format(i):item}
        df = pd.DataFrame(d).T
        reviews_df = reviews_df.append(df)
        print(reviews_df)
    i = i+1#
print(reviews_df)
reviews_df.to_csv('reviews_df.csv')
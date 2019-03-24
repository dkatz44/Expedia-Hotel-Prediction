import pandas as pd
from sklearn import metrics
from sklearn.grid_search import GridSearchCV
import matplotlib.pylab as plt
get_ipython().magic(u'matplotlib inline')
from matplotlib.pylab import rcParams
from datetime import datetime
import numpy as np

#%%
#match_cols = ['user_location_country', 'user_location_region', 'user_location_city', 'hotel_market', 'orig_destination_distance']

def tsInMin(dataSet, dateCol, outputColName):
    
    timeSeries = pd.Series(dataSet[dateCol])
    timeSeries = pd.to_datetime(timeSeries)

    tsYearByMin = timeSeries.map(lambda x: ((int(x.strftime('%j')) * 60) * 60) + \
    (int(x.strftime('%H')) * 60) + int(x.strftime('%M')))

    dataSet[outputColName] = tsYearByMin.astype(int)

    return dataSet


# In[15]:

def dayOfYearFromTS(dataSet, dateCol, outputColName):
      
    timeSeries = pd.Series(dataSet[dateCol])
    timeSeries = pd.to_datetime(timeSeries, coerce=True)
   
    timeSeries = timeSeries.map(lambda x: int(x.strftime('%j')) if pd.notnull(x) else None)

    dataSet[outputColName] = timeSeries

    return dataSet 


# In[6]:

def dayOfYearFromDate(dataSet, dateCol, outputColName):

    timeSeries = pd.Series(dataSet[dateCol])
    timeSeries = pd.to_datetime(timeSeries, format='%Y-%m-%d', coerce=True)
    
    timeSeries = timeSeries.map(lambda x: int(x.strftime('%j')) if pd.notnull(x) else None)
    
    dataSet[outputColName] = timeSeries

    return dataSet 

def fill_nulls_with_median(frameToFill, fillByCol, fillWithCol, newColName):

    median_dist = np.zeros(len(frameToFill[fillByCol].unique()))

# Fill the array with the median values
    for i in range(len(frameToFill[fillByCol].unique())):
        median_dist[i] = frameToFill[(frameToFill[fillByCol] == i)][fillWithCol].dropna().median()

# Create a new col in the dataframe based on the old col
    frameToFill[newColName] = frameToFill[fillWithCol]

# Fill the nulls in the new col based on the values from the median array
    for i in range(len(frameToFill[fillByCol].unique())):
        frameToFill.loc[ (frameToFill[fillWithCol].isnull()) & (frameToFill[fillByCol]==i), newColName] = median_dist[i]
    
    return frameToFill


# In[8]:

def fill_nulls_by_level(frameToFill, fillWithCol, newColName):
    
    frameToFill = fill_nulls_with_median(frameToFill, 'user_location_city', fillWithCol, 'city_col')
    frameToFill = fill_nulls_with_median(frameToFill, 'user_location_country', 'city_col', 'country_col')
    frameToFill = fill_nulls_with_median(frameToFill, 'user_location_region', 'country_col', 'region_col')
    frameToFill = fill_nulls_with_median(frameToFill, 'posa_continent', 'region_col', newColName)
    
    frameToFill = frameToFill.drop(['city_col','country_col','region_col'],axis=1)
    
    return frameToFill
    


#%%

train = pd.read_csv('/Users/dkatz44/Downloads/train.csv',
                    dtype={'user_id': np.int32,
                           'is_booking':bool,
                           'srch_destination_id':np.int32, 
                           'hotel_cluster':np.int32,
                           'date_time': np.str_,
                           'user_location_country': np.int32,
                           'user_location_region': np.int32,
                           'user_location_city': np.int32,
                           'hotel_market': np.int32,
                           'orig_destination_distance': np.float64
                           }
                   )
#%%
# Training Set Formatting

# get time stamp in min
train = tsInMin(train, 'date_time', 'timeStamp_Min')


# In[16]:

# get srch_ci (check in date) as day of year
train = dayOfYearFromTS(train, 'srch_ci', 'srch_ci_DOY')
#train = dayOfYearFromDate(train, 'srch_ci', 'srch_ci_DOY')


# In[20]:

# get srch_co (check out date) as day of year
train = dayOfYearFromTS(train, 'srch_co', 'srch_co_DOY')
#train = dayOfYearFromDate(train, 'srch_co', 'srch_co_DOY')


# In[23]:

# Train Fill Missing

# Distance

train = fill_nulls_by_level(train, 'orig_destination_distance', 'new_dist_col')


# In[25]:

# srch_ci

train = fill_nulls_by_level(train, 'srch_ci_DOY', 'new_srch_ci_col')


# In[26]:

# srch_co

# want the median diff between srch_ci and srch_co... 3 days
train['temp_srch_co_col'] = train['new_srch_ci_col'].astype(int).map(lambda x: x + 3 if x + 3 <= 365                                                                         else ((x + 3) - 365))

train['new_srch_co_col'] = train['srch_co_DOY'].fillna(train['temp_srch_co_col'])

train = train.drop('temp_srch_co_col', axis=1)

#%%

train_ten = pd.read_csv('/Users/dkatz44/Downloads/formatted_ten_percent_train.csv',
                    dtype={'user_id': np.int32,
                           'is_booking':bool,
                           'srch_destination_id':np.int32, 
                           'hotel_cluster':np.int32,
                           'date_time': np.str_,
                           'user_location_country': np.int32,
                           'user_location_region': np.int32,
                           'user_location_city': np.int32,
                           'hotel_market': np.int32,
                           'orig_destination_distance': np.float64
                           }
                   )

#%%

train.to_csv('/Users/dkatz44/Desktop/Train_With_New_Cols.csv', sep=',', index_label='id')


# In[5]:

# Import Test Set

#ds = ws.datasets['Expedia_Test.csv']
ds = ws.datasets['formatted_test_2']
test = ds.to_dataframe()


# In[31]:

#test = test.drop(['new_srch_co_col', 'new_srch_ci_col', 'srch_ci_DOY', 'srch_co_DOY', \
#                    'city_col', 'country_col', 'region_col'], axis=1)


# In[32]:

# Test Set Formatting

# get time stamp in min
test = tsInMin(test, 'date_time', 'timeStamp_Min')

# get srch_ci (check in date) as day of year
test = dayOfYearFromDate(test, 'srch_ci', 'srch_ci_DOY')

# get srch_co (check out date) as day of year
test = dayOfYearFromDate(test, 'srch_co', 'srch_co_DOY')


# In[120]:

# Test Fill Missing

# Distance
test = fill_nulls_by_level(test, 'orig_destination_distance', 'new_dist_col')


# In[38]:

# srch_ci

test = fill_nulls_by_level(test, 'srch_ci_DOY', 'new_srch_ci_col')


# In[39]:

# srch_co

# want the median diff between srch_ci and srch_co... 3 days
test['temp_srch_co_col'] = test['new_srch_ci_col'].astype(int).map(lambda x: x + 3 if x + 3 <= 365                                                                         else ((x + 3) - 365))

test['new_srch_co_col'] = test['srch_co_DOY'].fillna(test['temp_srch_co_col'])

test = test.drop('temp_srch_co_col', axis=1)


# In[6]:

# Test drop unused columns
test = test.drop(['date_time','srch_ci','srch_co', 'user_id',                   'srch_co_DOY', 'srch_ci_DOY', 'orig_destination_distance'], axis=1)









#%%



import numpy as np
import pandas as pd

print("Reading train set")

train = pd.read_csv('/Users/dkatz44/Downloads/train.csv',
                    dtype={'user_id': np.int32,
                           'is_booking':bool,
                           'srch_destination_id':np.int32, 
                           'hotel_cluster':np.int32,
                           'date_time': np.str_,
                           'user_location_country': np.int32,
                           'user_location_region': np.int32,
                           'user_location_city': np.int32,
                           'hotel_market': np.int32,
                           'orig_destination_distance': np.float64
                           }
                           ,nrows=10000
                   )

print("Train set loaded")

print("Reading test set")

test = pd.read_csv('/Users/dkatz44/Downloads/formatted_test_2.csv',
                        dtype={'id': np.int32,
                               'user_id': np.int32,
                               'srch_destination_id':np.int32, 
                               'date_time': 'O',
                               'user_location_country': np.int32,
                               'user_location_region': np.int32,
                               'user_location_city': np.int32,
                               'hotel_market': np.int32,
                               'orig_destination_distance': np.float64
                               }
                        )

print("Test set loaded")

match_cols = ['user_location_country', 'user_location_region', 'user_location_city', 'hotel_market', 'orig_destination_distance']

groups = train.groupby(match_cols)
    
def generate_exact_matches(row, match_cols):
    index = tuple([row[t] for t in match_cols])
    try:
        group = groups.get_group(index)
    except Exception:
        return []
    clus = list(set(group.hotel_cluster))
    return clus

print("finding exact matches")

exact_matches = []
for i in range(test.shape[0]):
    exact_matches.append(generate_exact_matches(test.iloc[i], match_cols))

print("exact matches found")

exact_matches2 = pd.DataFrame(exact_matches)

#Read in the XGBoost Results

xgbPreds = pd.read_csv('/Users/dkatz44/Desktop/Expedia XGBoost Results 2.csv')

xgbPreds_df = pd.DataFrame(xgbPreds)

xgbPreds_df2 = xgbPreds_df['hotel_cluster'].str.split(expand=True)



#xgbPreds_df2.columns = ['zero', 'blankone', 'one', 'blanktwo', 'two', 'blankthree', 'three', 'blankfour', 'four']

xgbPreds_df2.columns = ['zero', 'one', 'two', 'three', 'four']

#xgbPreds_df2 = xgbPreds_df2.drop(['blankone', 'blanktwo', 'blankthree', 'blankfour'], axis=1)



#xgbPreds_df2


#df = pd.DataFrame(np.random.randn(10000,3))

#df.columns = ['ok', 'okok', 'okokok']



full_preds = pd.concat([exact_matches2, xgbPreds_df2], axis=1)



#full_preds = df.join(full_preds)

#%%

full_preds


#%%

full_preds.columns = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '1B', '2B', '3B', '4B', '5B']

full_preds['1A'] = full_preds['1A'].fillna(value=-999)
full_preds['2A'] = full_preds['2A'].fillna(value=-999)
full_preds['3A'] = full_preds['3A'].fillna(value=-999)
full_preds['4A'] = full_preds['4A'].fillna(value=-999)
full_preds['5A'] = full_preds['5A'].fillna(value=-999)
full_preds['6A'] = full_preds['6A'].fillna(value=-999)
full_preds['7A'] = full_preds['7A'].fillna(value=-999)
full_preds['8A'] = full_preds['8A'].fillna(value=-999)

full_preds['1A'] = full_preds['1A'].astype(int)
full_preds['2A'] = full_preds['2A'].astype(int)
full_preds['3A'] = full_preds['3A'].astype(int)
full_preds['4A'] = full_preds['4A'].astype(int)
full_preds['5A'] = full_preds['5A'].astype(int)
full_preds['6A'] = full_preds['6A'].astype(int)
full_preds['7A'] = full_preds['7A'].astype(int)
full_preds['8A'] = full_preds['8A'].astype(int)

#%%

full_preds['combined'] = full_preds['1A'].map(str) + ' ' + full_preds['2A'].map(str) + ' ' + \
                         full_preds['3A'].map(str) + ' ' + full_preds['4A'].map(str) + ' ' + \
                         full_preds['5A'].map(str) + ' ' + full_preds['6A'].map(str) + ' ' + \
                         full_preds['7A'].map(str) + ' ' + full_preds['8A'].map(str) + ' ' + \
                         full_preds['1B'].map(str) + ' ' + full_preds['2B'].map(str) + ' ' + \
                         full_preds['3B'].map(str) + ' ' + \
                         full_preds['4B'].map(str) + ' ' + full_preds['5B'].map(str)

full_preds_comb = full_preds.drop(['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '1B', '2B', '3B', '4B', '5B'], axis=1)

full_preds_comb['combined2'] = full_preds_comb['combined'].str.replace("-999", "")

full_preds_comb = full_preds_comb.drop('combined', axis=1)

full_preds_comb['combined3'] = full_preds_comb['combined2'].str.replace('     ', " ")

full_preds_comb = full_preds_comb.drop('combined2', axis=1)

full_preds_comb['combined4'] = full_preds_comb['combined3'].str.replace('    ', " ")

full_preds_comb = full_preds_comb.drop(['combined3'], axis=1)

full_preds2 = full_preds_comb['combined4'].str.split(expand=True)

full_preds2.columns = ['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '1B', '2B', '3B', '4B', '5B']

full_preds2['hotel_cluster'] = full_preds2['1A'].map(str) + ' ' + full_preds2['2A'].map(str) + ' ' + \
                               full_preds2['3A'].map(str) + ' ' + full_preds2['4A'].map(str) + ' ' + \
                               full_preds2['5A'].map(str)


full_preds2 = full_preds2.drop(['1A', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '1B', '2B', '3B', '4B', '5B'], axis=1)

full_preds2.to_csv('/Users/dkatz44/Desktop/Expedia Combined Results 2.csv', sep=',', index_label='id')

#%%

results = pd.read_csv('/Users/dkatz44/Desktop/Expedia Combined Results 2.csv', nrows=100)

#%%

results_head = results.head()

#%%

results_head

#%%
results_head['hotel_cluster'].unique()
#%%

def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

#%%

split_df = results_head['hotel_cluster'].str.split(expand=False)

#%%

split_df

#%%

split_df.columns = ['zero', 'one', 'two', 'three', 'four']

#%%

split_df[0:1]

#%%

ok = f5(split_df[2])

#%%

ok

#%%

list1 = pd.Series([91, 0, 91, 77, 48])
list2 = pd.Series([1, 2, 3, 4, 5])

#%%

list3 = pd.concat([list1, list2])

list3

#%%

okok = f5(pd.concat([list1, list2]))

#full_preds = [f5(exact_matches[p] + preds[p] + most_common_clusters)[:5] for p in range(len(preds))]

#%%

okok

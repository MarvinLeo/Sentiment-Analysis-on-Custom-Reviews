import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer


f = open('train.json', 'r')
train = json.load(f)
f.close()

colnames = train.keys()

train_data = pd.DataFrame()
print colnames
print train[colnames[2]].keys()

for name in colnames:

    df = pd.DataFrame.from_dict(train[name], 'index')
    if df.shape[1] == 1:
        df.columns = [name]
    else:
        df = pd.DataFrame(train[name].items())
        df.set_index(0, inplace=True)
    #print name, ":", df.shape
    if train_data is None:
        train_data = df
    train_data = pd.concat([train_data, df], axis=1)
#train_data.to_csv('train_data.csv', encoding='utf-8')

# for name in train_data.columns:
#     lack=sum(pd.isnull(train_data[name]))
#     print name, ":", lack
# print train_data['features_0'][:10]

#print train_data.head()
print "size of train data is:", train_data.shape
print "raw features are:",
for item in colnames:
    print item,
le = LabelEncoder()
train_data['label'] = le.fit_transform(train_data['interest_level'])
print "\n", len(set(train_data['building_id']))
#train_data.to_csv('train_data.csv', encoding='utf-8')
#print train_data
# for name in colnames:
#     train_data[name] = train[name]
#     print name, train[name]
#print train_data.head()
test_df=train_data['photos']
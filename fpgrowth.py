import pandas as pd
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

#data_set1 = pd.read_csv('data_fp.csv', sep=';')
data_set = pd.read_csv('data_fp-2.csv', sep=';')

#data_set1.drop([data_set1.columns[1]], inplace=True, axis=1)
#data_set1.drop([data_set1.columns[0]], inplace=True, axis=1)
data_set.drop([data_set.columns[0]], inplace=True, axis=1)

frequent_is = fpgrowth(data_set, min_support=0.03, use_colnames=True)
rules_fp = association_rules(frequent_is, metric="confidence", min_threshold=0.75)

rules_fp['consequents'].astype(str)
index_drop = []
for i in range(0, rules_fp.shape[0]):
    fs = list(rules_fp.iloc[i][1])
    if len(fs) > 1:
        index_drop.append(i)
    elif 'Suicide Rates High' in fs:
        print('found high')
    elif 'Suicide Rates Low' in fs:
        print('found low')
    else:
        index_drop.append(i)

rows = rules_fp.index[index_drop]
rules_fp.drop(rows, inplace=True)

rules_fp_sorted = rules_fp.sort_values(['support', 'confidence', 'lift', 'leverage', 'conviction'], ascending=False)
rules_fp_sorted = rules_fp_sorted.reset_index(drop=True)
rules_fp_sorted.drop(['antecedent support', 'consequent support'], inplace=True, axis=1)

rules_fp_sorted.drop([rules_fp_sorted.columns[5]], inplace=True, axis=1)
rules_fp_sorted.to_csv('data_association-rules.csv', index=False)
print()

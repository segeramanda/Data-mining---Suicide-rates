import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

col_list = ["Indicator", "Location", "Value"]
col_list1 = ["Indicator", "Location", "Period", "Value"]
col_list2 = ["Indicator", "Location", "Period", "Dim1ValueCode", "Value"]

data_UV = pd.read_csv('Data/UV-radiation.csv', usecols=col_list, decimal='.')
data_Social_workers = pd.read_csv('Data/Social workers working in mental health sector (per 100,000).csv',
                                  usecols=col_list1)
data_Raised_blood_pressure = pd.read_csv('Data/Raised blood pressure (SBP_=140 OR DBP_=90) (crude estimate).csv',
                                         usecols=col_list1)
data_Psychiatrists = pd.read_csv('Data/Psychiatrists working in mental health sector (per 100,000).csv',
                                 usecols=col_list1)
data_Women_Married = pd.read_csv(
    'Data/Proportion of women aged 20-24 years who were married or in a union by age 15 (_).csv', usecols=col_list1)
data_Out_Pocket = pd.read_csv(
    'Data/Out-of-pocket expenditure as percentage of current health expenditure (CHE) (_).csv', usecols=col_list1,
    decimal='.')
data_Nurse = pd.read_csv('Data/Nurses working in mental health sector (per 100,000).csv', usecols=col_list1)
data_Tobacco = pd.read_csv(
    'Data/Non-age-standardized estimates of daily tobacco use, tobacco smoking and cigarette smoking .csv',
    usecols=col_list2)
data_BMI = pd.read_csv('Data/MeanBMI(kg_m2)_(age-standardized_estimate).csv', usecols=col_list2)
data_Government_Expenditures = pd.read_csv(
    'Data/Government expenditures on mental health as a percentage of total government expenditures on health.csv',
    usecols=col_list1)
data_Alcohol_Total = pd.read_csv(
    'Data/Alcohol, total per capita (15+ years) consumption (in litres of pure alcohol).csv', usecols=col_list2)
data_Suicide_Rates = pd.read_csv('Data/age-standardized-suicide-rates-(per-100-population).csv', usecols=col_list2)
data_Young_Birth = pd.read_csv('Data/Adolescent birth rate (per 1000 women aged 15-19 years).csv', usecols=col_list1)
data_Alcohol_Youth = pd.read_csv('Data/13-15-years old any alcoholic beverage consumed in past 30 days, (_).csv',
                                 usecols=col_list2)
data_Mental_Hospital_Admissons = pd.read_csv('Data/Mental hospital admissions (per 100,000).csv', usecols=col_list1)

attribute_array = [data_Suicide_Rates, data_BMI, data_UV, data_Nurse, data_Young_Birth, data_Alcohol_Youth,
                   data_Alcohol_Total, data_Tobacco, data_Government_Expenditures, data_Psychiatrists,
                   data_Mental_Hospital_Admissons, data_Out_Pocket, data_Raised_blood_pressure, data_Social_workers,
                   data_Women_Married]

# Changing value to indicator
for x in attribute_array:
    x.rename(columns={'Value': x['Indicator'].iloc[0]}, inplace=True)

###
# UV-radiation
data_UV.drop(['Indicator'], inplace=True, axis=1)
data_UV[data_UV.columns[1]] = data_UV[data_UV.columns[1]].str.replace(',', '.')
data_UV[data_UV.columns[1]] = data_UV[data_UV.columns[1]].astype(float)
data_UV.at[190, 'UV radiation'] = None
###

###
# Social workers working in mental health sector (per 100,000)

data_Social_workers.drop(data_Social_workers.loc[data_Social_workers['Period'] <= 2014].index, inplace=True)
data_Social_workers_mean = data_Social_workers.groupby('Location', as_index=False)[
    data_Social_workers.columns[3]].mean()
###

###
# Raised blood pressure (SBP_=140 OR DBP_=90) (crude estimate)
data_Raised_blood_pressure = data_Raised_blood_pressure[data_Raised_blood_pressure["Period"] == 2015]
data_Raised_blood_pressure.drop(['Indicator', 'Period'], inplace=True, axis=1)
data_Raised_blood_pressure.drop(data_Raised_blood_pressure.loc[data_Raised_blood_pressure[
                                                                   data_Raised_blood_pressure.columns[
                                                                       1]] == 'No data'].index, inplace=True)
data_Raised_blood_pressure[data_Raised_blood_pressure.columns[1]] = \
    data_Raised_blood_pressure[data_Raised_blood_pressure.columns[1]].str.split('[').str[0]
data_Raised_blood_pressure[data_Raised_blood_pressure.columns[1]] = data_Raised_blood_pressure[
    data_Raised_blood_pressure.columns[1]].astype(float)
###

###
# Psychiatrists working in mental health

# data_Psychiatrists = data_Psychiatrists[data_Psychiatrists["Period"] == 2016]
data_Psychiatrists.drop(data_Psychiatrists.loc[data_Psychiatrists['Period'] <= 2014].index, inplace=True)
data_Psychiatrists_mean = data_Psychiatrists.groupby('Location', as_index=False)[data_Psychiatrists.columns[3]].mean()
###

###
# Proportion of women aged 20-24 years who were married or in a union by age 15
data_Women_Married.drop(['Indicator', 'Period'], inplace=True, axis=1)
###

###
# Out-of-pocket expenditure as percentage of current health expenditure
data_Out_Pocket.drop(data_Out_Pocket.loc[data_Out_Pocket['Period'] > 2017].index, inplace=True)
data_Out_Pocket.drop(data_Out_Pocket.loc[data_Out_Pocket['Period'] <= 2014].index, inplace=True)
data_Out_Pocket_mean = data_Out_Pocket.groupby('Location', as_index=False)[data_Out_Pocket.columns[3]].mean()

###

###
# Nurses working in mental health sector (per 100,000). 2015 - 2017 preprocess.
data_Nurse.drop(data_Nurse.loc[data_Nurse['Period'] < 2015].index, inplace=True)
data_Nurse_mean = data_Nurse.groupby('Location', as_index=False)[data_Nurse.columns[3]].mean()
###

###
# Non-age-standardized estimates of daily tobacco use, tobacco smoking and cigarette smoking
data_Tobacco = data_Tobacco[data_Tobacco["Dim1ValueCode"] == 'BTSX']
data_Tobacco.drop(data_Tobacco.loc[data_Tobacco['Period'] > 2017].index, inplace=True)
data_Tobacco.drop(data_Tobacco.loc[data_Tobacco['Period'] <= 2014].index, inplace=True)
data_Tobacco.drop(['Indicator', 'Period', 'Dim1ValueCode'], inplace=True, axis=1)
data_Tobacco[data_Tobacco.columns[1]] = data_Tobacco[data_Tobacco.columns[1]].str.split('[').str[0]
data_Tobacco[data_Tobacco.columns[1]] = data_Tobacco[data_Tobacco.columns[1]].astype(float)

###

###
# Mental hospital admissions (per 100,000). 2014 only.
data_Mental_Hospital_Admissons[data_Mental_Hospital_Admissons.columns[3]] = data_Mental_Hospital_Admissons[
    data_Mental_Hospital_Admissons.columns[3]].str.replace(',', '.')
data_Mental_Hospital_Admissons[data_Mental_Hospital_Admissons.columns[3]] = data_Mental_Hospital_Admissons[
    data_Mental_Hospital_Admissons.columns[3]].astype(float)
data_Mental_Hospital_Admissons.drop(['Indicator', 'Period'], inplace=True, axis=1)
###

###
# MeanBMI(kg_m2)_(age-standardized_estimate). 2015 and 2016 mean.
data_BMI = data_BMI[data_BMI['Dim1ValueCode'] == 'BTSX']
data_BMI.drop(data_BMI.loc[data_BMI['Period'] > 2017].index, inplace=True)
data_BMI.drop(data_BMI.loc[data_BMI['Period'] <= 2014].index, inplace=True)
data_BMI.drop(data_BMI.loc[data_BMI[data_BMI.columns[4]] == 'No data'].index, inplace=True)
data_BMI[data_BMI.columns[4]] = data_BMI[data_BMI.columns[4]].str.split('[').str[0]
data_BMI[data_BMI.columns[4]] = data_BMI[data_BMI.columns[4]].astype(float)
data_BMI.drop(['Indicator', 'Dim1ValueCode', 'Period'], inplace=True, axis=1)
data_BMI_mean = data_BMI.groupby('Location', as_index=False)[data_BMI.columns[1]].mean()
###

###
# Government expenditures on mental health as a percentage of total government expenditures on health
data_Government_Expenditures.drop(['Indicator', 'Period'], inplace=True, axis=1)

###

###
# Alcohol, total per capita (15+ years) consumption (in litres of pure alcohol)
data_Alcohol_Total = data_Alcohol_Total[data_Alcohol_Total["Dim1ValueCode"] == 'BTSX']
data_Alcohol_Total.drop(data_Alcohol_Total.loc[data_Alcohol_Total[data_Alcohol_Total.columns[4]] == '.'].index,
                        inplace=True)
data_Alcohol_Total[data_Alcohol_Total.columns[4]] = \
    data_Alcohol_Total[data_Alcohol_Total.columns[4]].str.split('[').str[0]
data_Alcohol_Total[data_Alcohol_Total.columns[4]] = data_Alcohol_Total[data_Alcohol_Total.columns[4]].astype(float)
data_Alcohol_Total.drop(['Indicator', 'Period', 'Dim1ValueCode'], inplace=True, axis=1)
###

###
# age-standardized-suicide-rates-(per-100-population)
data_Suicide_Rates = data_Suicide_Rates[data_Suicide_Rates["Dim1ValueCode"] == 'BTSX']
data_Suicide_Rates.drop(data_Suicide_Rates.loc[data_Suicide_Rates['Period'] > 2017].index, inplace=True)
data_Suicide_Rates.drop(data_Suicide_Rates.loc[data_Suicide_Rates['Period'] <= 2014].index, inplace=True)
data_Suicide_Rates[data_Suicide_Rates.columns[4]] = \
    data_Suicide_Rates[data_Suicide_Rates.columns[4]].str.split('[').str[0]
data_Suicide_Rates[data_Suicide_Rates.columns[4]] = data_Suicide_Rates[data_Suicide_Rates.columns[4]].astype(float)
data_Suicide_Rates_mean = data_Suicide_Rates.groupby('Location', as_index=False)[data_Suicide_Rates.columns[4]].mean()

###

###
# Adolescent birth rate (per 1000 women aged 15-19 years)
data_Young_Birth.drop(data_Young_Birth.loc[data_Young_Birth['Period'] > 2017].index, inplace=True)
data_Young_Birth.drop(data_Young_Birth.loc[data_Young_Birth['Period'] <= 2014].index, inplace=True)
data_Young_Birth_mean = data_Young_Birth.groupby('Location', as_index=False)[data_Young_Birth.columns[3]].mean()
###

###
# 13-15-years old any alcoholic beverage consumed in past 30 days
data_Alcohol_Youth = data_Alcohol_Youth[data_Alcohol_Youth["Dim1ValueCode"] == 'BTSX']
data_Alcohol_Youth.drop(data_Alcohol_Youth.loc[data_Alcohol_Youth['Period'] > 2017].index, inplace=True)
data_Alcohol_Youth.drop(data_Alcohol_Youth.loc[data_Alcohol_Youth['Period'] <= 2014].index, inplace=True)
data_Alcohol_Youth_mean = data_Alcohol_Youth.groupby('Location', as_index=False)[data_Alcohol_Youth.columns[4]].mean()

# for x in attribute_array:
#     x.drop(columns=['Indicator', 'Period'], inplace=True)
#     if 'Dim1ValueCode' in x.columns:
#         x.drop(["Dim1ValueCode"], axis=1, inplace=True)


attribute_array2 = [data_BMI_mean, data_UV, data_Nurse_mean, data_Young_Birth_mean, data_Alcohol_Youth_mean,
                    data_Alcohol_Total, data_Tobacco, data_Government_Expenditures, data_Psychiatrists_mean,
                    data_Mental_Hospital_Admissons, data_Out_Pocket_mean, data_Raised_blood_pressure,
                    data_Social_workers_mean,
                    data_Women_Married]

# Merge all dfs into one
for i in range(0, 14):
    y = attribute_array2[i]
    data_Suicide_Rates_mean = pd.merge(data_Suicide_Rates_mean, y, how='left', on=['Location']) #.fillna(-9999)

# Remove duplicates in df
data_Suicide_Rates_mean.drop_duplicates(subset='Location', keep='first', inplace=True)

print((data_Suicide_Rates_mean.isnull().sum(axis=0)/183)*100)
# Write df to CSV file
#
##Calculate quartiles
# for i in range(1, 16):
#     print(i)
#     print(data_Suicide_Rates_mean.columns[i])
#     print(pd.qcut(data_Suicide_Rates_mean[data_Suicide_Rates_mean.columns[i]], 4))
#
# data_Suicide_Rates_mean = data_Suicide_Rates_mean.reset_index(drop=True)
#
#
# data_Suicide_Rates_mean.plot(x=data_Suicide_Rates_mean.columns[0], y=data_Suicide_Rates_mean.columns[1], figsize=(180,5), grid=True)
# plt.locator_params(axis="x", nbins=10)
# plt.show()
# print()
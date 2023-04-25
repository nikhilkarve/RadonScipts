import os
import pandas as pd
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input_file', help='Input file name', required=True)
parser.add_argument('-o', '--output_file', help='Output file name', required=True)

args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file

xls = pd.ExcelFile(input_file)

df = {}
for num in xls.sheet_names:
    df[num] = pd.read_excel(xls, num)

for key in df:
    df[key]['SyncDate'] = pd.to_datetime(df[key]['SyncDate'])
    df[key].sort_values(by='SyncDate', ascending=True, inplace=True)
    df[key]['SyncDate'] = df[key]['SyncDate'].dt.floor('H')
    df[key] = df[key].resample('H', on = 'SyncDate').mean()
    df[key] = df[key].interpolate(method='linear', limit_direction='both')
    df[key].drop_duplicates(inplace=True)


# find the oldest dates in the dataset df
largest_len = 0
for key in df:
    if len(df[key]) > largest_len:
        largest_len = len(df[key])
        largest_key = key

df_radon = pd.DataFrame(index=df[largest_key].index)
for key in df:
    if key == 'classRoom':
        df_radon[key] = df[key]['Radon']
    else:
        df_radon['R'+key] = df[key]['Radon']

df_radon.to_excel(output_file, sheet_name='Combined')
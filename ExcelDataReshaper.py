import sys
import pandas as pd

def dataFormatter(filename, sheetname):
    print("-->Started formatting. Please Wait.")
    requiredData = pd.read_excel(filename, sheet_name=sheetname)
    df = requiredData
    df = df[::-1]
    df = df.reset_index().reset_index()
    df.drop('index', inplace=True, axis=1)
    df.rename({"level_0": "index"}, inplace=True, axis=1)
    df = df.set_index(['SyncDate', 'index'])
    df = df.stack().reset_index()
    df = df[["level_2", 0 , "SyncDate", "index"]]
    df.rename({"level_2": "Sensor ID", 0: "Radon Value", "index":"hour"}, axis=1, inplace=True)
    df.to_excel("output.xlsx", index=False)
    print("-->Formatting done.")

if __name__ == "__main__":
    filename = sys.argv[1]
    sheetname = sys.argv[2]
    dataFormatter(filename, sheetname)

import sys
import pandas as pd
def getHourlyData():
    all_weather_data_test = pd.read_excel("weather station.xlsx")
    temperature_data_test = all_weather_data_test[["Simple Date", "Hourly Rain (in/hr)", "Outdoor Temperature (Â°F)"]]
    temperature_data_test.rename({'Simple Date': 'SyncDate'}, inplace=True, axis=1)
    temperature_data_test["SyncDate"] = temperature_data_test["SyncDate"].dt.strftime('%Y/%m/%d %H')
    final_temp_test = temperature_data_test.groupby("SyncDate")["Outdoor Temperature (Â°F)", "Hourly Rain (in/hr)"].agg(['mean', 'std'])
    output_1 = pd.read_excel("output.xlsx")
    y = output_1
    y["SyncDate"] = y["SyncDate"].dt.strftime('%Y/%m/%d %H')
    matched_test = pd.merge(final_temp_test, output_1 , on=["SyncDate", "SyncDate"], how="inner")
    matched_test.to_excel("hourly_data.xlsx", index = False)
    
if __name__ == "__main__":
    getHourlyData()
    

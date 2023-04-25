import sys
import pandas as pd
def getDailyData(filename):
    output_1 = pd.read_excel(filename)
    y = output_1
    y["SyncDate"] = y["SyncDate"].dt.strftime('%Y/%m/%d')
    testing_data = y.groupby(["SyncDate", "Sensor ID"])["Radon Value"].agg(["mean", "std"])
    testing_dataframe = pd.DataFrame(testing_data)
    all_weather_data_test = pd.read_excel("weather station.xlsx")
    temperature_data_test = all_weather_data_test[["Simple Date", "Hourly Rain (in/hr)", "Outdoor Temperature (Â°F)", "Daily Rain (in)"]]
    temperature_data_test.rename({'Simple Date': 'SyncDate'}, inplace=True, axis=1)
    temperature_data_test["SyncDate"] = temperature_data_test["SyncDate"].dt.strftime('%Y/%m/%d')
    final_temp_test = temperature_data_test.groupby("SyncDate")["Outdoor Temperature (Â°F)", "Hourly Rain (in/hr)", "Daily Rain (in)"].agg(['mean', 'std'])
    z = testing_dataframe.reset_index()
    matched_test = pd.merge(final_temp_test, z , on="SyncDate", how="right")
    final_daily = matched_test[[                           'SyncDate',
       ('Outdoor Temperature (Â°F)', 'mean'),
        ('Outdoor Temperature (Â°F)', 'std'),
                 ('Daily Rain (in)', 'mean'),
                  ('Daily Rain (in)', 'std'),
                                 'Sensor ID',
                                      'mean',
                                       'std']]
    final_daily.to_excel("daily_data.xlsx", index = False)

if __name__ == "__main__":
    filename = sys.argv[1]
    getDailyData(filename)


import pandas as pd
import numpy
import csv

def write_csv_file(file_name, array):
    with open(file_name,"w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(array)


def get_search_interest_over_time(keyword_list, country_iso2, timeframe='today 5-y'):
    from pytrends.request import TrendReq
    pytrend = TrendReq()
    pytrend.build_payload(keyword_list, cat=0, timeframe=timeframe, geo=country_iso2, gprop='')
    res = pytrend.interest_over_time()
    array = res.to_numpy()

    # sum all scores for the past 5 years
    sum = array.sum(axis=0)[0]
    # count how many score points we have
    scoresCount = array.shape[0]

    avg = sum / scoresCount
    print(avg)

    list = [["Term", "Saudi Arabia"]]
    list.append(["good habits", "60"])

    write_csv_file("output.csv", list)


kw_list = ["good habits"]
get_search_interest_over_time(kw_list, 'SA')





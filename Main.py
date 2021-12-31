import json
import pandas as pd
import numpy
import csv
from Country import *
import argparse

def write_csv_file(file_name, array):
    with open(file_name, "w+") as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(array)

# get the data for the past 90 days
def get_search_interest_over_time(keyword_list, country_iso2, timeframe='today 3-m'):
    from pytrends.request import TrendReq
    pytrend = TrendReq()
    pytrend.build_payload(keyword_list, cat=0, timeframe=timeframe, geo=country_iso2, gprop='')
    res = pytrend.interest_over_time()
    array = res.to_numpy()

    # sum all scores for the past 5 years

    sum = array.sum(axis=0)[0] if (array.size > 0) else 0
    # count how many score points we have
    scoresCount = array.shape[0]

    avg = sum / scoresCount if (scoresCount != 0) else 0
    return avg

def gtrends_hyper_link(geo, query, cell_value):
    return f"=HYPERLINK(https://trends.google.com/trends/explore?geo={geo}&q={query}, {cell_value})"

def load_topics_list():
    file = open('topics.json')
    json_array = json.load(file)
    topics_list = []
    for item in json_array:
        topics_list.append(item)

    return topics_list

arg_parser = argparse.ArgumentParser(description='Get Search Intreset Over Time from Google Trends')
arg_parser.add_argument("-t", "--timeframe", help="Timeframe to run this searh for")
args = arg_parser.parse_args()
time_frame = args.timeframe or 'today 3-m'

topics_list = load_topics_list()

# 1 raw for the header & one row for the total
lastRow = len(arabic_countries) + 2

# set first column title
out = [["Country"]]
for topic in topics_list:
    # append the second column in the sheet (Topic)
    out[0].append(topic)
    countries_rows = 1
    # sum of all countries average scores
    score_sum = 0
    for country in arabic_countries:
        result = get_search_interest_over_time([topic], country.iso2, time_frame)
        score_sum = score_sum + result

        if countries_rows < len(out):
            out[countries_rows].append(result)
        else:
            out.append([country.name, result])
        countries_rows = countries_rows + 1

    # append the last row in the sheet which is the total of all countries averages
    if len(out) < lastRow:
        out.append(["Total", score_sum])
    else:
        out[lastRow - 1].append(score_sum)

write_csv_file("output.csv", out)

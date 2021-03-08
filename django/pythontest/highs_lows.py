import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
#    print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)
    dates, highs, lows = [], [], []

    highs = []
    for row in reader:
        # highs.append(high)
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            lows.append(low)
            highs.append(high)
            dates.append(current_date)
    # print(highs)

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates,highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # plt.plot(highs, c='red')
    plt.title("Daily high and low temperatures in 2014", fontsize=24)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=15)

    plt.tick_params(axis='both', which='major', labelsize=15)

    plt.show();
import pandas
import csv
import os
def sales_extractor(file_name):
    df = pandas.read_csv("./data/"+file_name)
    dic = {'Sales': [], 'Date': [], 'Region': []}
    with open("output.csv", 'a+', newline='') as csvfile:
        heading = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(csvfile, heading)
        writer.writeheader()
        for x in range(len(df['product'])):
            if df['product'][x] == 'pink morsel':
                sales = float(df['price'][x][1:]) * df['quantity'][x]
                writer.writerow({'Sales': sales, 'Date': df['date'][x], 'Region': df['region'][x]})




if __name__ == "__main__":
    for filename in os.listdir("./data"):
        sales_extractor(filename)

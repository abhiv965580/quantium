import pandas
import csv

def sales_extractor(file_name):
    df = pandas.read_csv(file_name)
    dic = {'Sales': [], 'Date': [], 'Region': []}
    with open("output.csv", 'w', newline='') as csvfile:
        heading = ['Sales', 'Date', 'Region']
        writer = csv.DictWriter(csvfile, heading)
        writer.writeheader()
        for x in range(len(df['product'])):
            if df['product'][x] == 'pink morsel':
                sales = float(df['price'][x][1:]) * df['quantity'][x]
                writer.writerow({'Sales': sales, 'Date': df['date'][x], 'Region': df['region'][x]})




if __name__ == "__main__":
    file1 = "daily_sales_data_0.csv"
    file2 = "daily_sales_data_1.csv"
    file3 = "daily_sales_data_2.csv"
    sales_extractor(file1)
    sales_extractor(file2)
    sales_extractor(file3)

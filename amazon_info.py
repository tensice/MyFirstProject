import csv
from datetime import datetime
path = 'data/amazon.csv'
with open(path) as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [i for i in reader]
def question1():
    max_stock_price = 0
    stock_date = None
    for i in data:
        value = i[4]
        value2 = value[2:]
        stock_price = float(value2)
        if stock_price > max_stock_price:
            max_stock_price = stock_price
            stock_date = i[0].strip()
    return stock_date,max_stock_price


def question2():
    lowest = 100000000
    stock_date = None
    for i in data:
        value = i[5]
        value2 = value[2:]
        value_float = float(value2)
        if value_float < lowest:
            lowest = value_float
            stock_date = i[0].strip()
    return stock_date,lowest

def mean():
    amazon_mean = []
    for i in data:
        value = i[1]
        value2 = value[2:]
        value_float = float(value2)
        amazon_mean.append(value_float)
    mean1 = (sum(amazon_mean)) / len(amazon_mean)
    return mean1

def median():
    amazon_median = []
    for i in data:
        value = i[1]
        value2 = value[2:]
        value_float = float(value2)
        amazon_median.append(value_float)
    amazon_median.sort()
    middle = (len(amazon_median) - 1) // 2
    print(amazon_median)
    print(amazon_median[middle])

    # amazon = []
    # for d in data:
    #     value = d[4]
    #     value2 = value[2:]
    #     value_float = float(value2)
    #     amazon.append(value_float)
    #     num = []
    #     num.append(value_float)
    # for x,y in zip(num,d[0]):
    #     if x == max(amazon):
    #         print(y)


    #print(max(amazon))




#print(question1())
#print(question2())
#print(mean())
median()
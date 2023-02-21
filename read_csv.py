#Native module to read csv files
import csv

#Generic function to read csv file
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #delimiter referst to what delimite each data.
        #Read row by row
        for row in reader:
            print('***' * 5)
            print(row)

#Execute with data.csv file
if __name__ == '__main__':
    read_csv('./data.csv')#

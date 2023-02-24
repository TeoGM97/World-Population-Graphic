#Native module to read csv files
import csv

#Generic function to read csv file
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') #delimiter referst to what delimite each data.
        # initially it is a list with the values. We need to do a dictionary.
        # Arrayy with names of columns
        header = next(reader)
        #Empty list to be filled by dictionaries below
        data = []
        #Read row by row
        for row in reader:
            #Header + row. Convert header and row into array of tuples. 1 Column 2 row
            iterable = zip(header, row)
            #Generate dictionart with dictionary comprehension:
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

#Execute with data.csv file
if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data[0])

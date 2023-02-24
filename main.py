import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./data.csv')
    #Only South American Countries
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    #All the countries
    countries = list(map(lambda x: x['Country/Territory'], data))
    #Percentage per country
    percentages = list(map(lambda x: ['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)


'''
country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)

        charts.generate_bar_chart(labels, values)
'''

if __name__ == '__main__':
    run()
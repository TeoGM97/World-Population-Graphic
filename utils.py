#Cualquier archivo .py puede considerarse un modulo y se puede importar desde otro archivo justo como
# se hace con random y demas modulos importables por defecto en Python.

#Los archivos donde se crean utilidades y se importan desde el princial
# suelen tener solo funciones

#Metemos todo dentro de run porque, si se importa desde otro archivo, se ejecutara completamente este
# y solo necesitamos que se ejecuten algunas cosas
# de esta manera, podr[iamos importar cada una de las funciones de utils por separado


def get_population(country_dict):
    #Dictionary with population
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population']),
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values

def population_by_country(data, country):
    #result will be a list of dictionaries. filter will give me specific data from a country
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result
#Cualquier archivo .py puede considerarse un modulo y se puede importar desde otro archivo justo como
# se hace con random y demas modulos importables por defecto en Python.

#Los archivos donde se crean utilidades y se importan desde el princial
# suelen tener solo funciones

#Metemos todo dentro de run porque, si se importa desde otro archivo, se ejecutara completamente este
# y solo necesitamos que se ejecuten algunas cosas
# de esta manera, podr[iamos importar cada una de las funciones de utils por separado

def run():
    def get_population(country_dict):
        #Dictionary with population
        population_dict = {
            '2022': country_dict['2022 Population'],
            '2020': country_dict['2020 Population'],
            '2015': country_dict['2015 Population'],
            '2010': country_dict['2010 Population'],
            '2000': country_dict['2000 Population'],
            '1990': country_dict['1990 Population'],
            '1980': country_dict['1980 Population'],
            '1970': country_dict['1970 Population'],
        }
        labels = population_dict.keys()
        values = population_dict.values()
        return labels, values

    def population_by_country(data, country): #data estara en el main
        #Result sera una lista de diccionarios. Filter me da los datos especificos de un pais
        result = list(filter(lambda item: item['Country'] == country, data))
        return result

#Este if es para tener la dualidad de lo que se dice arriba. Si quisiera ejecutar todo el archivo desde la 
#  terminal como un script. Este if me permite poder hacerlo
if __name__ == '__main__':
    run() #Si se ejecuta desde la terminal, ejecutarlo el run,
        #    pero si se corre desde otro archivo, no.

import utils
import read_csv
import charts
import pandas as pd




def run():

    '''
    data = read_csv.read_csv('world_population.csv')

    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country/Territory'], data))

    percentages = list(map(lambda x: x['World Population Percentage'], data))

    charts.generate_pie_chart(countries,percentages)
    '''
    df = pd.read_csv('world_population.csv')
    df = df[df['Continent']=='North America']
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries,percentages)
    data = read_csv.read_csv('world_population.csv')
    

    country = input('Ingresa el Pais: ')

    main_result = utils.get_population_by_country(data, country)

    if len(main_result) > 0:
        country = main_result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'],labels, values)





if __name__ == '__main__':
    run()
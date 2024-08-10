"""Esse algorirmo consome a API do The Movie Data Base. Mais de 1 milhão de títulos, extraindo Títulos Originais
e Sinopses, armazenando em um arquivo CSV para treinar um algoritmo de análise de sentimento. 
"""

import requests
import json
import pandas as pd
import random

def search_synopses(id):
    request = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=2b0225a8bab83e2a45825d2344fcec9d')
    arrays = request.json()

    return arrays

def several_dictionaries(start, end):
    list_dictionary = []

    for i in range(start, end):
        ids = random.randrange(1, 1000000)
        dictionary = search_synopses(ids)
        list_dictionary.append(dictionary)
    
    return list_dictionary

#print(list_dictionary)

def synopses_and_title(parameter1, parameter2):
    list_synopses = []
    number = 0

    for dictionary in several_dictionaries(parameter1, parameter2):
        try:
            write_title = dictionary['original_title']
            write_overview = dictionary['overview']
            number += 1

            string_synopse = f'#Número {number}, Título do filme: {write_title}, Sinopse: {write_overview}'
            list_synopses.append(string_synopse)

        except:
            number += 1

            if not dictionary['success'] == True:
                print(f'Número: {number}.', dictionary['status_message'])
            else:
                print(f'Número: {number}. Houve um erro na requisição.')

    return list_synopses

def saving_csv(start, end):
    data = synopses_and_title(start, end)
    file_csv = pd.DataFrame(data)
    file_csv.to_csv(f'lista_de_sinopses{start}-{end}.csv', index=False)

    return print("Arquivo CSV salvo com sucesso.")

def execute():
    start = int(input("Digite o Start para a consulta: "))
    end = int(input("Digite o End para a consulta: "))

    saving_csv(start, end)
    #print(synopses_and_title(start, end))
    return 

execute()

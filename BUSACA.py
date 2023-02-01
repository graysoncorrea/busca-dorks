#tld: domínio de nível superior em google.com ou google.in
#num: número de resultados que mostrados
#stop: último resultado a recuperar. Use Nenhum para continuar pesquisando para sempre.
#pause: lapso de espera entre as solicitações HTTP. 

import random
import time
import requests
from googlesearch import search

class SearchEngine:
    def __init__(self, query, num_results=10, tld='co.in'):
        self.query = query
        self.num_results = num_results
        self.tld = tld
        self.results = []
        
    def search(self):
        for url in search(self.query, tld=self.tld, num=self.num_results):
            time.sleep(random.randint(5, 10))
            self.results.append(url)
        
    def save_results(self, file_path):
        with open(file_path, 'w') as file:
            for result in self.results:
                file.write(result + '\n')
                
    def filter_results(self, keyword):
        self.results = [result for result in self.results if keyword in result]
        
    def get_results(self):
        return self.results

# Usando
query = input("Enter your dork: ")
se = SearchEngine(query)
se.search()
print(se.get_results())
se.filter_results('python')
print(se.get_results())
se.save_results('resultados.txt')

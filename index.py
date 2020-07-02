import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
from Universidade import Universidade

wiki = 'https://pt.wikipedia.org/wiki/Lista_de_universidades_federais_do_Brasil'
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page, 'html.parser')
all_table = soup.find_all('table')
table = soup.find('table', class_='wikitable sortable')

# gerando a lista em colunas
A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in table.findAll("tr"):  # para tudo que estiver em <tr>
    cells = row.findAll('td')  # variável para encontrar <td>
    if len(cells) == 8:  # número de colunas
        link = "https://pt.wikipedia.org" + \
            cells[3].find('a').get('href') if cells[3].find(
                'a') != None else "-"
        name = cells[3].find(text=True)
        A.append(cells[1].find(text=True).replace('\n', ''))
        B.append(name)
        C.append(cells[3].find(text=True))
        D.append(cells[4].find(text=True))
        E.append(cells[5].find(text=True).replace('\n', ''))
        F.append(cells[7].find(text=True).replace('\n', ''))
        G.append(link)

        # criando univ
        if(link != ""):
            univ = Universidade(link, name)
            univ.csv()

# importe o pandas para converter a lista em uma planilha

df = pd.DataFrame()

df['Região'] = A
df['UF'] = B
df['Nome'] = C
df['Sigla'] = D
df['Discentes'] = E
df['Fundação'] = F
df['Site'] = G

df.to_csv('wikipedia/univ_federais.csv')

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup


class Universidade:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def csv(self):
        try:
            page = urllib.request.urlopen(self.url)
            soup = BeautifulSoup(page, 'html.parser')
            all_table = soup.find_all('table')
            table = soup.find('table', class_='infobox_v2')

            df = pd.DataFrame()
            excep = ["Campus", "Cores da escola", "Afiliações", "Localização"]
            var = ""

            for row in table.findAll("tr"):  # para tudo que estiver em <tr>
                cells = row.findAll('td')  # variável para encontrar <td>
                if len(cells) == 2:  # número de colunas
                    if(str(cells[0].find(text=True)).replace('\n', '') in excep):
                        for x in cells[1].findAll('a'):
                            if len(x.text) != 0:
                                var += str(x.text).strip()+"\n"
                        df[str(cells[0].find(text=True)).replace('\n', '')] = var
                        var = ""
                    else:
                        df[str(cells[0].find(text=True)).replace('\n', '')] = [
                            str(cells[1].find(text=True)).strip()]

            df.to_csv("wikipedia/"+self.name.title().replace(" ", "")+".csv")
        except Exception:
            print("Erro: ", self.name, "\n")
            print("Possível causa: Não possui dado referente")
            print(table)

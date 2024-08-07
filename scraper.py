from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.tbs-sct.canada.ca/ap/list-liste/cio-dpi-eng.asp'

request = requests.get(url)
content = request.content

soup = BeautifulSoup(content.decode('utf-8','ignore'), features = 'html.parser')

untidy_insts = soup.find_all('dt')
untidy_cios = soup.find_all('dd')

# remove unwanted data
untidy_insts.pop()
untidy_cios.pop()

insts = [inst.text for inst in untidy_insts]
cios = [cio.text.strip() for cio in untidy_cios]

data = []
for i in range(0, len(insts)):
    temp = [insts[i], cios[i]]
    data.append(temp)

df = pd.DataFrame(columns = ['Institution', 'CIO'], data = data)

df.to_csv(r'scraped-goc-cio-data.csv')
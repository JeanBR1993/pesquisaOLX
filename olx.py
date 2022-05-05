from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#interface usuário
print('Escreva o termo a ser procurado na OLX:')
query = input()
print('Escreva o dígito da região onde quer procurar:')
list = ['DDD 11 - São Paulo e região', 'DDD 12 - V. do Paraíba e Litoral Norte', 'DDD 13 - Baixada Santista e Litoral Sul',
        'DDD 14 - Bauru, Marília e região','DDD 15 - Sorocaba e região','DDD 16 - Ribeirão Preto e região',
        'DDD 17 - S. José do Rio Preto e região', 'DDD 18 - Presidente Prudente e região', 'DDD 19 - Grande Campinas']
for x in range(len(list)):
    print(x,'-', list[x])
query2 = input()
print('Qual ordem de pesquisa? (0 - mais recente, 1 - relevancia ou 2 - mais barato?')
query3 = input()
listordem = ['.ja3zle-9:nth-child(1)', '.ja3zle-9:nth-child(2)', '.ja3zle-9:nth-child(3)']

#controle de regiao e ordem de pesquisa
try:
    query2 = int(query2)
    query3 = int(query3)
    if query2 < 0 or query2 > (len(list)-1):
        print('Número de regiao inválido')
        quit()
    if query3 < 0 or query2 > 2:
        print('Opção de ordem inválido')
        quit()
except:
    print('Opção em formato inválido')
    quit()


navegador = webdriver.Chrome()
navegador.get('https://www.olx.com.br/')

#pesquisa
try:
    search = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.ID, "searchtext")))
    search.click()
    search.send_keys(query)
    submit = WebDriverWait(navegador, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".searchSubmitBtn > svg")))
    submit.click()
except:
    print('Erro na primeira página de pesquisa')
    quit()

#seleção dos filtros
try:
    regiao = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.LINK_TEXT, list[query2])))
    regiao.click()
    if query3 == 0 or query3 == 2:
        ordem = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, listordem[query3])))
        ordem.click()
except:
    print('Erro nos filtros')
    quit()

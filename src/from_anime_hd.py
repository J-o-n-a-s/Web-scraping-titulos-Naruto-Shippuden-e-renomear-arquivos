from csv import writer
from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def web_scraping_anime_hd() -> None:
    inicio = time()

    print('\nExecutando.\nPor gentileza, aguarde...')

    url = 'https://animehd.cc/anime/36256/'
    titulos = {}

    options = Options()
    options.add_argument('headless')  # Não abre o browser
    driver = webdriver.Edge(options=options)
    driver.get(url)

    sleep(2)

    for valor in range(1, 501):
        find = f'/html/body/div[3]/div/div[1]/div[4]/a[{valor}]'
        element = driver.find_elements(By.XPATH, find)
        posicao_inicial = element[0].text.find(':') + 2
        name = element[0].text[posicao_inicial:]
        sanitized_name = []
        for caractere in name:
            if caractere in '\\/:*?"<>|':
                sanitized_name.append('')
            else:
                sanitized_name.append(caractere)
        titulos[valor] = ''.join(sanitized_name)

    driver.quit()

    file = open(
        'Títulos Naruto Shippuden.csv', 'w', newline='', encoding='UTF-8'
    )
    write = writer(file)
    for chave, valor in titulos.items():
        write.writerow([chave, valor])

    file.close()

    print(
        f'\nProcesso finalizado.\nO tempo de execução foi {(time() - inicio):.2f} segundos.\n'
    )

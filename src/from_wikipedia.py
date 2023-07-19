from csv import writer
from time import sleep, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


def web_scraping_wikipedia() -> None:
    inicio = time()

    print('\nExecutando.\nPor gentileza, aguarde...')

    url = 'https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Naruto_Shippuden'
    temporadas = 20
    capitulos = [
        30,
        23,
        24,
        25,
        26,
        25,
        26,
        26,
        25,
        26,
        25,
        25,
        26,
        24,
        23,
        26,
        26,
        27,
        21,
        21,
    ]
    tabela = 2
    titulos = {}
    capitulos_sequencial = 0

    options = Options()
    options.add_argument('headless')  # Não abre o browser
    driver = webdriver.Edge(options=options)
    driver.get(url)

    sleep(2)

    for temporada in range(temporadas):
        tabela = tabela + 2
        posicao = 2
        for capitulo in range(capitulos[temporada]):
            find = f'//*[@id="mw-content-text"]/div[1]/table[{tabela}]/tbody/tr[{posicao}]/td[2]/i/b'
            posicao = posicao + 3
            element = driver.find_elements(By.XPATH, find)
            name = element[0].text
            sanitized_name = []
            for caractere in name:
                if caractere in '\\/:*?"<>|':
                    sanitized_name.append('')
                else:
                    sanitized_name.append(caractere)
            capitulos_sequencial = capitulos_sequencial + 1
            titulos[capitulos_sequencial] = ''.join(sanitized_name)

    driver.quit()

    file = open(
        'Títulos Naruto Shippuden.csv', 'w', newline='', encoding='utf-8'
    )
    write = writer(file)
    for chave, valor in titulos.items():
        write.writerow([chave, valor])

    file.close()

    print(
        f'\nProcesso finalizado.\nO tempo de execução foi {(time() - inicio):.2f} segundos.\n'
    )

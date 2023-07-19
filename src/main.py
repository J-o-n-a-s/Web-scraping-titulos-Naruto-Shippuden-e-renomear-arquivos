import os

from fix_file_names import fix_anime_file_names
from from_anime_hd import web_scraping_anime_hd
from from_wikipedia import web_scraping_wikipedia

if __name__ == '__main__':
    while True:
        print('\n')
        print(
            '*********************************************************************'
        )
        print(
            '*  Web scraping títulos Naruto Shippuden e renomeação de arquivos   *'
        )
        print(
            '*********************************************************************'
        )
        print('\n')
        selection = input(
            'Selecione a origem de onde deseja fazer o web scraping dos títulos:'
            + '\n1 - Anime HD;'
            + '\n2 - Wikipedia;'
            + '\n3 - Pular.'
            + '\n> '
        )
        match selection:
            case '1':
                web_scraping_anime_hd()
                break
            case '2':
                web_scraping_wikipedia()
                break
            case '3':
                break
            case _:
                print('\nA opção selecionada é inválida.\n')

    while True:
        selection = input('\nDeseja renomer os nomes dos arquivos (S/N):\n> ')

        match selection.upper():
            case 'S':
                fix_anime_file_names()
                break
            case 'N':
                break
            case _:
                print('\nA opção selecionada é inválida.\n')

    print('\nObrigado e até logo!\n')

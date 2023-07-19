import os
from time import time


def return_current_file_name(path: str, file_name: str) -> str:
    return path + file_name


def return_new_file_name(
    episodes: list, title: str, path: str, file_name: str
) -> str:
    for episode in episodes:
        episode = episode.strip().split(',')
        value1 = int(episode[0])
        value2 = int(title[0][1:])
        if value1 == value2:
            episode_title = episode[1].replace('"', '')
            break
    return (
        path + file_name.split('.')[0] + ' - ' + episode_title + '.' + title[1]
    )


def fix_anime_file_names() -> None:
    path_files = input(
        '\nPor gentileza, digite o caminho da pasta onde estão os arquivos:\n> '
    )

    inicio = time()

    if path_files and path_files[-1:] != '\\':
        path_files += '\\'

    current_path = os.getcwd() + '\\'
    file_with_anime_names = current_path + 'Títulos Naruto Shippuden.csv'

    if os.path.isfile(file_with_anime_names):
        file_with_titles = open(file_with_anime_names, 'r', encoding='utf-8')
        episode_titles = file_with_titles.readlines()
        file_with_titles.close()

        files = os.listdir(path_files)

        for file in files:
            title = file.split('.')
            if len(title) > 1:
                match file[0].upper():
                    case 'E':
                        current_file_name = return_current_file_name(
                            path_files, file
                        )
                        new_file_name = return_new_file_name(
                            episode_titles, title, path_files, file
                        )

                    case _:
                        print(
                            'Erro: Inicial do episódio não se enquadra em nenhum tipo conhecido.'
                        )

                os.rename(current_file_name, new_file_name)
    else:
        print(f'\nArquivo {file_with_anime_names} não encontrado!')

    print(
        f'\nProcesso finalizado.\nO tempo de execução foi {(time() - inicio):.2f} segundos.'
    )

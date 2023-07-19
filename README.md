# Web scraping dos títulos dos capítulos do Naruto Shippuden e renomeação de arquivos MP4 com episódios

**SEJA BEM-VINDO A ESTE REPOSITÓRIO!!!**

-------------

**Instruções**

 - *Fork* este repositório;
 - Clone seu repositório *forked*;
 - Adicione seus scripts;
 - *Commit & Push*;
 - Crie um *pull request*;
 - Dê uma estrela para este repositório;
 - Aguarde que o seu *pull request* solicitado vire um *merge*;
 - Comemore, seu primeiro passo para o mundo de código aberto e continue contribuindo.

## Introdução

Projeto para realizar a raspagem em sites (Wikipedia e/ou Anime HD) dos títulos dos episódios de todas as 20 temporadas do Naruto Shippuden, suprimir caracteres inválidos, para nome de arquivos no Windows, e adicionar ao nome dos arquivos MP4 existentes.

Inicialmente a raspagem dos dados foram realizadas no site Wikipedia, porém eu notei que lá não havia informações dos episódios que eram semi fillers e/ou fillers. Por conta disso, acabei adicionando e deixando selecionável a raspagem em um segundo site, Anime HD, onde esse sim existe as informações se os episódios são semi fillers, fillers ou normais.

## Motivação

Tudo começou com a dificuldade de saber quais episódios eu já havia assistido e quais os próximos e não só isso. Os arquivos estava nomeados apenas com a inicial "E" e os três dígitos do número do episódio, sende de 001 até 500.

Como os nomes do episódios não continham o nome do episódio eu sempre precisa consultar na internet e saber do que se tratava a histório do episódio. Eu tinha a opção de toda vez consultar o nome do episódio na internet ou então facilitar a vida incluindo o nome do episódio diretamente no nome do arquivo MP4.

Se eu fizesse isso de forma manual seria muito trabalhoso. Eu deveria copiar um título por vez, pressionar a tecla "F2" sobre o arquivo MP4 correto, adiciona " - " (espaço, hífen, espaço) e depois colar o título do episódio que colei da internet. Fora isso, os títulos dos capitulos contém caracteres que não são aceitos no nome dos arquivos e eu teria que fazer uma sanitização manual no nome dos arquivos, lembrando que esse processo deveria ser repetido 500 vezes.

Por conta do citado acima, eu decidi automatizar todo esse processo fazendo a programação em Python (raspagem dos dados e renomeação dos arquivos MP4).

## Descrição do projeto

O projeto foi desenvolvido em Python 3.11 e dividido em 4 (quatro) arquivos (fix_file_names.py, from_anime_hd.py, from_wikipedia.py, main.py). A seguir vou explanar um pouco sobre o conteúdo de cada arquivo.

### Arquivo "main.py"

Esse é o arquivo principal do projeto. Ele faz a importação dos demais 3 (três) arquivos e faz a orquestração do funcionamento do projeto.

Foi criado um laço onde o usuário recebe informações no console. O programa aguarda a entrada de uma seleção disponibilizada para usuário, caso seja incorreta, apresenta novamente as informações para a seleção do usuário. Com a seleção correta do usuário, o programação direcionará o fluxo do programa para a lógica selecionada. As opções são:

1. Anime HD;
2. Wikipedia;
3. Pular.



1. Faça o login em seu e-mail;
2. Clique sobre o seu nome e selecione "Configurações";

 ![Configuração](https://www.locaweb.com.br/ajuda/wp-content/uploads/2018/05/config_filtro_web_novo.jpg "Configuração")

3. Do lado esquerdo do navegador clique em "Filtros e Regras";
4. Emails Bloqueados ou Emails Liberados;

 ![Emails Bloqueados](https://www.locaweb.com.br/ajuda/wp-content/uploads/2020/06/emails_bloqueados-01.png "Emails Bloqueados")

 ![Emails Liberados](https://www.locaweb.com.br/ajuda/wp-content/uploads/2020/06/emails_liberados-02.png "Emails Liberados")

5. Inserir no campo o endereço de e-mail, ou do domínio que deseja bloquear, ou liberar;
6. Clique no botão "Adicionar";
7. Ao fim da inserção dos e-mails/domínios, clique no botão "Salvar".

### Inserção automatizada

Fundamentalmente a ideia da programação em Python é realizar os passos 5, 6 e 7 descritos acima, porém, de forma automatizada e a partir da leitura de um arquivo TXT contendo uma lista com todos os e-mails/domínios que desejamos adicionar. Importante salientar que em cada linha do arquivo TXT deve conter apenas um único e-mail ou domínio.

O arquivo TXT pode ser criado com o auxílio de uma planilha em Excel, que facilitará a variações dos e-mails com o ajuste de algumas células, colunas e funções. Futuramente posso pensar em adicionar um módulo no programa para realizar a criação do arquivo TXT sem a necessidade do auxílio de uma planilha no Excel.

#### Bibliotecas e recursos utilizados

 - PyAutoGUI -> Fundamental para posicionamento do cursor do mouse e simulação do pressionamento de teclas do teclado;
 - Time -> Para adição de tempo e registro do início, fim e duração do processo;
 - Sys -> Para retornar erros de leitura do arquivo TXT;
 - Ctypes -> Para ser possível realizar o bloqueio da máquina no fim da execução do processo de adição de e-mails/domínios. O usuário decide se a máquina será bloqueada ou não;
 - PyInstaller -> Para criação do arquivo executável. Facilitando a utilização do programa mesmo em máquinas que não possuem o Python instalado.

 ## Instalação e execução do projeto

 ...

 ## Licença

 MIT License

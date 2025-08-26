# Projeto Olimpiadas 

Análise de Medalhas Olímpicas
Este projeto realiza a análise de dados sobre as medalhas concedidas nos Jogos Olímpicos, utilizando um script em Python para processar um arquivo de dados em formato CSV.

Objetivo
O objetivo principal é extrair informações relevantes de um conjunto de dados brutos de medalhas para gerar dois relatórios específicos:
- O quadro geral de medalhas, exibindo a contagem de medalhas de ouro, prata e bronze para cada país participante. (Em ordem de peso de medalhas de ouro, prata, bronze) 
- Uma lista dos países que tiveram apenas atletas de um único gênero (masculino ou feminino) entre seus medalhistas.
 
Componentes do Projeto
- cod_olimp.py: O coração do projeto. Este script em Python é responsável por ler o arquivo de dados, processar cada entrada, realizar a contagem das medalhas por país e analisar a distribuição de gênero dos atletas premiados.

- medalhas_atualizado.csv: A fonte de dados. Este arquivo contém a listagem detalhada de cada medalha, incluindo informações como o tipo da medalha, o nome do atleta, gênero, modalidade e o país correspondente.
Como Funciona
O script cod_olimp.py é executado através da linha de comando, recebendo o nome do arquivo .csv como argumento. Ele lê os dados, seleciona as colunas de interesse (país, tipo de medalha e gênero) e realiza os cálculos necessários para apresentar os resultados finais de forma organizada no terminal.

Segue a demonstração gráfica do resultado esperado:
<img width="312" height="511" alt="image" src="https://github.com/user-attachments/assets/79d1c552-60d6-4b6d-9f60-84def84c617e" />

<img width="287" height="474" alt="image" src="https://github.com/user-attachments/assets/64f52782-0fe0-4675-9f52-f758d3d34d7f" />

OBS: para rodar o código, foi utilizado a ferramenta Vscode, com o seguinte comendo no teminal : 
python cod_olimp.py medalhas_atualizado.csv

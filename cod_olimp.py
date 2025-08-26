from dataclasses import dataclass
from enum import Enum, auto
import sys
sys.setrecursionlimit(10**4)


class Tipo_Medalha(Enum):
    MED_OURO = auto()
    MED_PRATA = auto()
    MED_BRONZE = auto()


class Genero(Enum):
    M = auto()
    W = auto()
    O = auto()
    X = auto()


@dataclass
class Contagem:
    PAIS: str
    GOLD: int = 0
    SILVER: int = 0
    BRONZE: int = 0
    TOTAL: int = 0


def selecao(tabela: list[list[str]]) -> list[list[str]]:
    nova_lista = []
    for i in tabela:
        pais = i[10]
        if i[0] == 'Gold Medal':
            medalha = Tipo_Medalha.MED_OURO
        elif i[0] == 'Silver Medal':
            medalha = Tipo_Medalha.MED_PRATA
        elif i[0] == 'Bronze Medal':
            medalha = Tipo_Medalha.MED_BRONZE
        if i[4] == 'M':
            genero = Genero.M
        elif i[4] == 'W':
            genero = Genero.W
        elif i[4] == 'O':
            genero = Genero.O
        elif i[4] == 'X':
            genero = Genero.X
        else:
            genero = Genero.X

        nova_lista.append([pais, medalha, genero])
    return nova_lista


def verif_paises(nova_lista: list[list[str]]) -> list[str]:
    pais_lista = []
    for dados in nova_lista:
        if dados[0] not in pais_lista:
            pais_lista.append(dados[0])
    return pais_lista


def contador(nova_lista: list[list[str]], pais_lista: list[str]) -> list[Contagem]:
    paises_medalhas = []
    for pais in pais_lista:
        contagem = Contagem(pais)
        for dados in nova_lista:
            if dados[0] == pais:
                if dados[1] == Tipo_Medalha.MED_OURO:
                    contagem.GOLD += 1
                elif dados[1] == Tipo_Medalha.MED_PRATA:
                    contagem.SILVER += 1
                elif dados[1] == Tipo_Medalha.MED_BRONZE:
                    contagem.BRONZE += 1
        contagem.TOTAL = contagem.GOLD + contagem.SILVER + contagem.BRONZE
        paises_medalhas.append(contagem)
    return ordenacao(paises_medalhas)


def ordenacao(paises_medalhas: list[Contagem]) -> list[Contagem]:
    for i in range(len(paises_medalhas)):
        minimo = i
        for j in range(i + 1, len(paises_medalhas)):
            if paises_medalhas[j].GOLD > paises_medalhas[minimo].GOLD:
                minimo = j
            elif paises_medalhas[j].GOLD == paises_medalhas[minimo].GOLD:
                if paises_medalhas[j].SILVER > paises_medalhas[minimo].SILVER:
                    minimo = j
                elif paises_medalhas[j].SILVER == paises_medalhas[minimo].SILVER:
                    if paises_medalhas[j].BRONZE > paises_medalhas[minimo].BRONZE:
                        minimo = j
        paises_medalhas[i], paises_medalhas[minimo] = paises_medalhas[minimo], paises_medalhas[i]
    return paises_medalhas


def resultados(paises_medalhas: list[Contagem]):
    """
    Imprime o quadro de medalhas dos países.

    >>> paises_medalhas = [
    ...     Contagem('USA', GOLD=10, SILVER=5, BRONZE=3, TOTAL=18),
    ...     Contagem('GER', GOLD=7, SILVER=6, BRONZE=4, TOTAL=17),
    ...     Contagem('CAN', GOLD=3, SILVER=2, BRONZE=1, TOTAL=6)
    ... ]
    >>> resultados(paises_medalhas)
    País       | Ouro | Prata | Bronze | Total
    ------------------------------------------
    USA        | 10   | 5     | 3      | 18   
    GER        | 7    | 6     | 4      | 17   
    CAN        | 3    | 2     | 1      | 6    
    """

    print('País       | Ouro | Prata | Bronze | Total')
    print('------------------------------------------')
    for pais in paises_medalhas:
        print(f'{pais.PAIS:<10} | {pais.GOLD:<4} | {pais.SILVER:<5} | {pais.BRONZE:<6} | {pais.TOTAL:<5}')

# ------------------------------------------------------------recursiva----------------------------------------------------------


def genero_unico(nova_lista: list[list[str]]):
    """
    Verifica e imprime os países que ganharam medalhas em um único gênero.

    >>> nova_lista = [
    ...     ['USA', Tipo_Medalha.MED_OURO, Genero.M],
    ...     ['USA', Tipo_Medalha.MED_PRATA, Genero.M],
    ...     ['CAN', Tipo_Medalha.MED_BRONZE, Genero.W],
    ...     ['GER', Tipo_Medalha.MED_OURO, Genero.M],
    ...     ['GER', Tipo_Medalha.MED_PRATA, Genero.W],
    ...     ['FRA', Tipo_Medalha.MED_OURO, Genero.W]
    ... ]
    >>> genero_unico(nova_lista)
    Países com medalhas de um único gênero:
    USA
    CAN
    FRA
    """
    def verificar_genero(paises: list[str], index: int, resultado: list[str]) -> list[str]:
        if index >= len(paises):
            return resultado

        pais_atual = paises[index]
        generos = []

        def verificar_pais(idx: int):
            if idx >= len(nova_lista):
                return
            dados = nova_lista[idx]
            if dados[0] == pais_atual and dados[2] in (Genero.M, Genero.W):
                if dados[2] not in generos:
                    generos.append(dados[2])
            verificar_pais(idx + 1)

        verificar_pais(0)

        if len(generos) == 1:
            resultado.append(pais_atual)

        return verificar_genero(paises, index + 1, resultado)

    paises = verif_paises(nova_lista)
    resultado = verificar_genero(paises, 0, [])
    print('Países com medalhas de um único gênero:')
    for pais in resultado:
        print(pais)

# ------------------------------------------------------------------cod prof---------------------------------------------


def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])
    nova_lista = selecao(tabela)
    pais_lista = verif_paises(nova_lista)
    paises_medalhas = contador(nova_lista, pais_lista)
    resultados(paises_medalhas)
    genero_unico(nova_lista)
    # TODO: computar e exibir o quadro de medalhas
    # TODO: computar e exibir os países que tiverem apenas
    #       atletas de um único gênero premiados


def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.

    Por exemplo, se o conteúdo do arquivo for

    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995

    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        sys.exit(1)


if __name__ == '__main__':
    main()


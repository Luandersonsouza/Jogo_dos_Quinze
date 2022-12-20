"""(Jogo dos 15)"""

#imports
import random
import typing
import time
from IPython.display import clear_output

#funções

def create_matrix() -> typing.List[typing.List[int]]:
    """
    Gera uma matriz 4x4 com elementos em posições aleatórias
    entre 0 e 15
    
    :return: matriz 4x4 com valores entre 0 e 15
    """
    matrix = list()
    new_list = list(range(16))
    for i in range(4):
      line = []
      for j in range(4):
        x = random.choice(new_list)
        line.append(x)
        new_list.remove(x)
      matrix.append(line)
    return matrix


def find_position_zero(matrix: typing.List[typing.List[int]]) -> int:
  """
  Função que irá procurar e devolver a posição do 0 da matriz (espaço vazio)

  :param matriz: matriz com os elementos do jogo
  :return: posição do elemento 0
  """
  for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
          return (i + 1) * 10 + j + 1


def show_game(matrix: typing.List[typing.List[int]]) ->None:
  """
  Imprime o atual estado do tabuleiro

  :param matrix: matriz com os elemento do jogo
  """

  for i in range(4):
    print("+------+------+------+------+")
    for j in range(4):
      print("+ %02d " % matrix[i][j], end=" ")
    print("+")
  print("+------+------+------+------+")


def change_element(pos1: int, pos2: int, matrix: typing.List[typing.List[int]]) -> None:
  """
  Função de troca de posições baseada nas coordenadas passadas das
  posições linha coluna.
  """

  element1 = matrix[pos1 // 10 - 1][pos1 % 10-1]
  element2 = matrix[pos2 // 10 - 1][pos2 % 10-1]
  matrix[pos1 // 10 - 1][pos1 % 10-1] = element2
  matrix[pos2 // 10 - 1][pos2 % 10-1] = element1



def verify_play(pos: int, zero_pos: int) ->bool:
  """
  Verifica se a jogada selecionada(pretendida) é válida

  :param pos: posição do elemento a ser trocado
  :param zero_pos: posição do elemento 0
  :return: True se a jogada é válida
  """

  line = pos // 10
  column = pos % 10

  line_zero = zero_pos // 10
  column_zero = zero_pos % 10


  if line < 1 or line > 4 or column < 1 or column > 4:
    return False

  else:
    return(
        (line == line_zero -1 and column == column_zero)
        or (line == line_zero and (column == column_zero-1) or column == column_zero +1)
        or (line == line_zero +1 and column == column_zero)
    )

def check_if_you_won(matrix: typing.List[typing.List[int]]) -> bool:
  """
  Verifica se o jogador ganhou o jogo

  :param matrix: matriz com os elementos do jogo
  :return: True se houve vitória
  """

  in_line = list()
  for i in matrix:
    in_line +=1

  return in_line == sorted(in_line)


def main() -> None:
  """
  Função principal do jogo
  """

  #starting game
  game = create_matrix()
  zero_pos = find_position_zero(game)
  playing = True
  won = False

  #criando o loop principal do jogin

  while playing:

    clear_output(wait = True)
    time.sleep(0.3)
    show_game(game)
    time.sleep(0.3)

    pos = int(input("Digite a posição do elemento que você deseja trocar: "))
    while not verify_play(pos, zero_pos):
      print("Entrada inválida. Digite novamente")
      pos = int(input("Digite a posição do elemento que você deseja trocar: "))
    change_element(pos, zero_pos, game)
    zero_pos = pos

    won = check_if_you_won(game)
    playing = not won

  if won :
    print("Parabens, você Venceu!!!")

  else:
    print("Obrigado por jogar.")

main()

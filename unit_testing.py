import unittest

#Função que processa as estatísticas da temporada a partir do placar
def adicionar_jogo(placar:int,lista:list):
    numero = lista[0]+1
    if placar < lista[2]:
        minimo = placar
        minimo_batido = lista[4]+1
    else:
        minimo = lista[2]
        minimo_batido = lista[4]
    
    if placar > lista[3]:
        maximo = placar
        maximo_batido = lista[5]+1
    else:
        maximo = lista[3]
        maximo_batido = lista[5]

    return [numero,placar,minimo,maximo,minimo_batido,maximo_batido]

#Lista com os valores "já registrados"
lista = [
    [1,12,12,12,0,0],
    [2,24,12,24,0,1],
    [3,10,10,24,1,1],
    [4,24,10,24,1,1]
        ]

#Classe e Método para fazer o teste unitário do método usado no web-app
class TestAdicionar(unittest.TestCase):
    def test_jogo(self):
        self.assertAlmostEqual(adicionar_jogo(25,lista[len(lista)-1]),[5, 25, 10, 25, 1, 2])
        self.assertAlmostEqual(adicionar_jogo(9,lista[len(lista)-1]),[5, 9, 9, 24, 2, 1])
        self.assertAlmostEqual(adicionar_jogo(30,lista[len(lista)-1]),[5, 30, 10, 30, 1, 2])
        
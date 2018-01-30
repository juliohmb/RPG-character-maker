#JUL10#M8
from time import sleep
from random import randint


class Personagem(object):
    def __init__(self):
        self.classe = None
        self.caminho = None
        self.raca = None
        self.sub_raca = None
        self.pv = None
        self.ca = None
        self.atrib_forca = None
        self.atrib_destreza = None
        self.atrib_constituicao = None
        self.atrib_inteligencia = None
        self.atrib_sabedoria = None
        self.atrib_carisma = None
        self.mod_forca = None
        self.mod_destreza = None
        self.mod_constituicao = None
        self.mod_inteligencia = None
        self.mod_sabedoria = None
        self.mod_carisma = None
        self.deslocamento = None
        self.idiomas = ''
        self.proficiencias = ''
        self.extras_r = ''
        self.extras_sr = ''
        self.equipamento = ''

    def Ca(self):
        self.ca = 'Sem armadura sua CA é {}(10 + mod. de Destreza)'.format(10 + self.mod_destreza)

    def raca_esc(self):
        sleep(0.4)
        lista = ['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato', 'Gnomo', 'Meio-Elfo', 'Tiefling', 'Meio-Orc']
        for n in range(9):
            print(lista[n] + ' = [{}]'.format(n+1))
        while True:
            esc = input('Digite o numero correspondente a raça escolhida: \n')
            if esc.isnumeric():
                esc = int(esc)
                if 0 < esc < 10:
                    break
                else:
                    print('Você precisa digitar um número possivel cara cara!!!')
            elif not esc.isdigit():
                print('Você precisa digitar um número possivel cara cara!!!')
        raca = lista[esc - 1]
        self.raca = raca

    def sub_raca_esc(self):
        sleep(0.4)
        print('-' * 20)
        print('Cada raça possui uma sub-raça, por isso deve escolher uma! Lembre de levar em conta sua classe')
        if self.raca == 'Anão':
            print('Sua raça é Anão, por isso tem as seguintes sub-raças')
            print('''
            [1]ANÃO DA COLINA:
             Ajuste de Atributo: +1 em Sabedoria.
             Resistência dos Anões: +1 de PV por
            nível.
            
            
            [2]ANÃO DA MONTANHA:
             Ajuste de Atributo: +2 em Força.
             Treino em Armaduras dos Anões:
            Proficiência em Armaduras leves e
            médias.
            ''')
            while True:
                esc = input('Digite a sua escolha: ')
                if esc.isnumeric():
                    esc = int(esc)
                    if 0 < esc < 3:
                        break
                    else:
                        print('Você precisa digitar um número possivel cara cara!!!')
                elif not esc.isdigit():
                    print('Você precisa digitar um número possivel cara cara!!!')
            if esc == 1:
                self.sub_raca = '''ANÃO DA COLINA'''
                self.atrib_sabedoria += 1
                self.pv += 1
            elif esc == 2:
                self.sub_raca = '''ANÃO DA MONTANHA'''
                self.atrib_forca += 2
                self.proficiencias += '\nProficiência em Armaduras leves e médias.'
        if self.raca == 'Elfo':
            print('Sua raça é Elfo, por isso tem as seguintes sub-raças')
            print('''           [1]ALTO ELFO:
             Ajuste de Atributo: +1 em Inteligência.
             Treinamento em Armas Élficas: Proficiência em Espada
            Longa, Espada Curta, Arco Longo e Arco Curto.
             Truque: Conhece um truque da lista de truques do mago.
            A Inteligência é o atributo usado para conjurar este truque.
             Idioma Adicional: Pode falar, ler e escrever um idioma
            adicional de sua escolha.


            [2]ELFO DA FLORESTA:
             Ajuste de Atributo: +1 em Sabedoria.
             Treinamento em Armas Élficas: Proficiência em Espada
            Longa, Espada Curta, Arco Longo e Arco Curto.
             Pés Ligeiros: O deslocamento aumenta para 10,5m (7
            quadrados).
             Máscara da natureza: Pode se esconder mesmo enquanto
            levemente estiver obscurecido por algum fenômeno natural
            (Folhagem, chuva forte, neve caindo, neblina, etc).
                        
                        
            [3]ELFO NEGRO (DROW):
             Ajuste de Atributo: +1 em Carisma.
             Sensibilidade à Luz solar: Desvantagem nas jogadas de
            ataque e testes de Sabedoria (Percepção) quando estiver
            diretamente na luz solar.
             Visão no Escuro Superior: Visão no escuro estendida para
            36m (24 quadrados).
             Magia Drow: Conhece o truque Globos de Luz. A partir
            do nível 3 pode usar Fogo das Fadas uma vez por dia. A
            partir do nível 5 também pode usar Escuridão uma vez por
            dia.
             Treinamento em armas drows: Você tem proficiência com
            sabre, espada curta e besta de mão.
            ''')
            while True:
                esc = input('Digite a sua escolha: ')
                if esc.isnumeric():
                    esc = int(esc)
                    if 0 < esc < 4:
                        break
                    else:
                        print('Você precisa digitar um número possivel cara cara!!!')
                elif not esc.isdigit():
                    print('Você precisa digitar um número possivel cara cara!!!')
            if esc == 1:
                self.sub_raca = '''ALTO ELFO'''
                self.atrib_inteligencia += 1
                self.proficiencias += ' \nProficiência em Espada Longa, Espada Curta, Arco Longo e Arco Curto.'
                self.extras_sr += 'Truque: Conhece um truque da lista de truques do mago. A Inteligência é o atributo' \
                                  ' usado para conjurar este truque.'
                self.idiomas += ' Idioma Adicional: Pode falar, ler e escrever um idioma adicional de sua escolha.'
            elif esc == 2:
                self.sub_raca = '''ELFO DA FLORESTA'''
                self.atrib_sabedoria += 1
                self.proficiencias += ' \nProficiência em Espada Longa, Espada Curta, Arco Longo e Arco Curto.'
                self.extras_sr += '''Pés Ligeiros: O deslocamento aumenta para 10,5m (7 quadrados).
Máscara da natureza: Pode se esconder mesmo enquanto
levemente estiver obscurecido por algum fenômeno natural
(Folhagem, chuva forte, neve caindo, neblina, etc).'''
            elif esc == 3:
                self.sub_raca = '''ELFO NEGRO (DROW)'''
                self.atrib_carisma += 1
                self.extras_sr += '''Sensibilidade à Luz solar: Desvantagem nas jogadas de
ataque e testes de Sabedoria (Percepção) quando estiver
diretamente na luz solar.
Visão no Escuro Superior: Visão no escuro estendida para
36m (24 quadrados).
Magia Drow: Conhece o truque Globos de Luz. A partir
do nível 3 pode usar Fogo das Fadas uma vez por dia. A
partir do nível 5 também pode usar Escuridão uma vez por
dia.'''
                self.proficiencias += '''\nVocê tem proficiência com sabre, espada curta e besta de mão.'''
        if self.raca == 'Halfling':
            print('Sua raça é Halfling, por isso tem as seguintes sub-raças')
            print('''
            [1]ROBUSTO:
             Atributo: +1 em Constituição.
             Resiliência: vantagem em testes de
            resistência contra veneno, e tem resistência
            contra dano venenoso


            [2]PÉS LEVES:
             Atributo: +1 em Carisma.
             Furtividade Natural: Pode tentar se esconder
            mesmo quando possui apenas a cobertura de
            uma criatura que seja, no mínimo, uma
            categoria de tamanho maior que a sua.
            ''')
            while True:
                esc = input('Digite a sua escolha: ')
                if esc.isnumeric():
                    esc = int(esc)
                    if 0 < esc < 3:
                        break
                    else:
                        print('Você precisa digitar um número possivel cara cara!!!')
                elif not esc.isdigit():
                    print('Você precisa digitar um número possivel cara cara!!!')
            if esc == 1:
                self.sub_raca = '''ROBUSTO'''
                self.atrib_constituicao += 1
                self.extras_sr += '''Resiliência: vantagem em testes de
resistência contra veneno, e tem resistência
contra dano venenoso'''
            elif esc == 2:
                self.sub_raca = '''PÉS LEVES'''
                self.atrib_carisma += 1
                self.extras_sr += '''Furtividade Natural: Pode tentar se esconder
mesmo quando possui apenas a cobertura de
uma criatura que seja, no mínimo, uma
categoria de tamanho maior que a sua.'''
        if self.raca == 'Humano':
            self.sub_raca = '''TRAÇOS RACIAIS ALTERNATIVOS'''
            self.proficiencias += '''\nAdquire proficiência em uma perícia de sua escolha.'''
            self.extras_sr += '''Ganha um talento de sua escolha.'''
            esc = int(input('Escolha um atributo que deseja adicionar +1 ao mesmo: \n[1]Força\n[2]Destreza\n'
                            '[3]Constituição\n[4]Inteligencia\n[5]Sabedoria\n[6]Carisma\n'))
            esc2 = int(input('Escolha outro atributo que deseja adicionar +1 ao mesmo: \n[1]Força\n[2]Destreza\n'
                             '[3]Constituição\n[4]Inteligencia\n[5]Sabedoria\n[6]Carisma\n'))
            if esc == 1:
                self.atrib_forca += 1
            if esc == 2:
                self.atrib_destreza += 1
            if esc == 3:
                self.atrib_constituicao += 1
            if esc == 4:
                self.atrib_inteligencia += 1
            if esc == 5:
                self.atrib_sabedoria += 1
            if esc == 6:
                self.atrib_carisma += 1
            if esc2 == 1:
                self.atrib_forca += 1
            if esc2 == 2:
                self.atrib_destreza += 1
            if esc2 == 3:
                self.atrib_constituicao += 1
            if esc2 == 4:
                self.atrib_inteligencia += 1
            if esc2 == 5:
                self.atrib_sabedoria += 1
            if esc2 == 6:
                self.atrib_carisma += 1
        if self.raca == 'Draconato':
            self.sub_raca = 'Consultar tabela do Draconato para saber qual o seu sopro, baseado no ancestral draconico'
        if self.raca == 'Gnomo':
            print('Sua raça é Gnomo, por isso tem as seguintes sub-raças')
            print('''
            [1]Gnomo da Floresta:
            Atributo: +1 em Destreza.
             Ilusionista Natural: Conhece o Truque Ilusão
            Menor.
             Falar com Feras Pequenas: Pode comunicar
            ideias simples para feras Pequenas ou menores.


            [2]Gnomo da Rocha:
             Atributo: +1 em Constituição.
             Conhecimento do Artífice: Adiciona dobro de
            proficiência para testes de História relacionados
            a itens mágicos, objetos alquímicos e
            tecnológicos.
            Engenhoca: Proficiente com Ferramentas de
            Engenhoqueiro. Com 10 po e uma hora de
            trabalho pode criar um dispositivo mecânico
            (CA 5, 1 PV) que funciona por até 24h ou até
            ser desmontado (recuperando os materiais).
            Você pode ter até três mecanismos ativos ao
            mesmo tempo. Ao criá-lo escolha uma das
            seguintes funções.
            -Brinquedo: Colocado no chão move-se 1,5m em
            uma direção aleatória. Faz sons apropriados
            para o formato.
            -Caixa de Música: Quando aberta toca uma
            música pré-determinada em volume moderado.
            -Isqueiro: Com uma ação produz uma chama
            miniatura que pode ser usada para acender
            outras coisas''')
            while True:
                esc = input('Digite a sua escolha: ')
                if esc.isnumeric():
                    esc = int(esc)
                    if 0 < esc < 10:
                        break
                    else:
                        print('Você precisa digitar um número possivel cara cara!!!')
                elif not esc.isdigit():
                    print('Você precisa digitar um número possivel cara cara!!!')
            if esc == 1:
                self.sub_raca = 'Gnomo da Floresta'
                self.atrib_destreza += 1
                self.extras_sr += '''Ilusionista Natural: Conhece o Truque Ilusão
Menor.
Falar com Feras Pequenas: Pode comunicar
ideias simples para feras Pequenas ou menores.'''
            elif esc == 2:
                self.sub_raca = 'Gnomo da Rocha'
                self.atrib_constituicao += 1
                self.proficiencias += '''\nAdiciona dobro de
proficiência para testes de História relacionados
a itens mágicos, objetos alquímicos e
tecnológicos.
Engenhoca: Proficiente com Ferramentas de
Engenhoqueiro.'''
                self.extras_sr += '''
Com 10 po e uma hora de
trabalho pode criar um dispositivo mecânico
(CA 5, 1 PV) que funciona por até 24h ou até
ser desmontado (recuperando os materiais).
Você pode ter até três mecanismos ativos ao
mesmo tempo. Ao criá-lo escolha uma das
seguintes funções.
-Brinquedo: Colocado no chão move-se 1,5m em
uma direção aleatória. Faz sons apropriados
para o formato.
-Caixa de Música: Quando aberta toca uma
música pré-determinada em volume moderado.
-Isqueiro: Com uma ação produz uma chama
miniatura que pode ser usada para acender
outras coisas'''
        if self.raca == 'Meio-Elfo':
            self.sub_raca = 'Não tem :('
        if self.raca == 'Tiefling':
            self.sub_raca = 'Não tem :('
        if self.raca == 'Meio-Orc':
            self.sub_raca = 'Não tem :('

    def classe_esc(self):
        sleep(0.4)
        print('-' * 20)
        lista = ['Bárbaro', 'Bardo', 'Bruxo', 'Clérigo', 'Druida', 'Feitiçeiro', 'Guerreiro', 'Ladino', 'Mago',
                 'Monge', 'Paladino', 'Ranger']
        for n in range(12):
            print(lista[n] + ' = [{}]'.format(n+1))
        while True:
            esc = input('Digite o número correspondente a classe escolhida: ')
            if esc.isnumeric():
                esc = int(esc)
                if 0 < esc < 13:
                    break
                else:
                    print('Você precisa digitar um número possivel cara cara!!!')
            elif not esc.isdigit():
                print('Você precisa digitar um número possivel cara cara!!!')
        classe = lista[esc-1]
        self.classe = classe

    def atributos(self):
        sleep(0.4)
        print('-' * 20)
        print('Existem varias maneiras de calcular os atributos de seu personagem,\n'
              'a primeira delas consiste em jogar 4d6 e em seguida retirar o pior\n'
              'resultado e efetuar a soma dos restantes. A outra maneira é admitir\n'
              'os seguintes valores (15, 14, 13, 12, 10, 8)')
        while True:
            esc = input('Qual sua escolha? 1 ou 2? \n')
            if esc.isnumeric():
                esc = int(esc)
                if 0 < esc < 3:
                    break
                else:
                    print('Você precisa digitar um número possivel cara cara!!!')
            elif not esc.isdigit():
                print('Você precisa digitar um número possivel cara cara!!!')
        if esc == 1:
            sleep(0.4)
            print('-' * 20)
            sub_lista = []
            lista_valores = []
            lista_atributos = ['Força', 'Destreza', 'Constituiçao', 'Inteligencia', 'Sabedoria', 'Carisma']
            lista_atributos_esc = []
            print('Agora vai precisar rolar 4d6 por vez! Se não tiver dados pode escolher a opção 2, se tiver, opção 1')
            while True:
                esc2 = input()
                if esc2.isnumeric():
                    esc2 = int(esc2)
                    if 0 < esc2 < 3:
                        break
                    else:
                        print('Você precisa digitar um número possivel cara cara!!!')
                elif not esc2.isdigit():
                    print('Você precisa digitar um número possivel cara cara!!!')

            if esc2 == 1:
                for n in range(6):
                    print('{}ª vez'.format(n + 1))
                    for i in range(4):
                        while True:
                            dado = input('Dado {}: '.format(i + 1))
                            if dado.isnumeric():
                                dado = int(dado)
                                if 0 < dado < 7:
                                    break
                                else:
                                    print('Você precisa digitar um número possivel cara cara!!!')
                            elif not dado.isdigit():
                                print('Você precisa digitar um número possivel cara cara!!!')
                        sub_lista.append(dado)
                    sub_lista.pop(sub_lista.index(min(sub_lista)))
                    lista_valores.append(sum(sub_lista))
                    sub_lista = []
                print('Agora você vai decidir em quais atributos deve colocar os valores,\n'
                      'lembre-se de escolher o que melhor atende sua classe')
                for n in range(len(lista_atributos)):
                    print(lista_valores)
                    atrib = int(input(lista_atributos[n] + ' = '))
                    lista_atributos_esc.append(atrib)
                    lista_valores.pop(lista_valores.index(atrib))
            if esc2 == 2:
                lista_valores_aleat = []
                sub_lista_aleat = []
                for i in range(6):
                    sub_lista_aleat = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
                    sub_lista_aleat.pop(sub_lista_aleat.index(min(sub_lista_aleat)))
                    lista_valores_aleat.append(sum(sub_lista_aleat))
                for n in range(3):
                    while True:
                        manter = input('Os valores gerados foram: {}\nDeseja manter?(1=sim|2=não) '
                                       'Só poderá tentar de novo mais {} vezes'.format(lista_valores_aleat, (3-n)))
                        if manter.isnumeric():
                            manter = int(manter)
                            if 0 < manter < 3:
                                break
                            else:
                                print('Você precisa digitar um número possivel cara cara!!!')
                        elif not manter.isdigit():
                            print('Você precisa digitar um número possivel cara cara!!!')
                    if manter == 1:
                        break
                    elif manter == 2:
                        lista_valores_aleat.clear()
                        for i in range(6):
                            sub_lista_aleat = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
                            sub_lista_aleat.pop(sub_lista_aleat.index(min(sub_lista_aleat)))
                            lista_valores_aleat.append(sum(sub_lista_aleat))
                print('Agora você vai decidir em quais atributos deve colocar os valores,\n'
                      'lembre-se de escolher o que melhor atende sua classe')
                for n in range(len(lista_atributos)):
                    print(lista_valores_aleat)
                    while True:
                        atrib = input(lista_atributos[n] + ' = ')
                        if atrib.isnumeric():
                            atrib = int(atrib)
                            if atrib in lista_valores_aleat:
                                break
                            else:
                                print('Você precisa digitar um número possivel cara cara!!!')
                        elif not atrib.isdigit():
                            print('Você precisa digitar um número possivel cara cara!!!')
                    lista_atributos_esc.append(atrib)
                    lista_valores_aleat.pop(lista_valores_aleat.index(atrib))
            self.atrib_forca = lista_atributos_esc[0]
            self.atrib_destreza = lista_atributos_esc[1]
            self.atrib_constituicao = lista_atributos_esc[2]
            self.atrib_inteligencia = lista_atributos_esc[3]
            self.atrib_sabedoria = lista_atributos_esc[4]
            self.atrib_carisma = lista_atributos_esc[5]
        if esc == 2:
            sleep(0.4)
            print('-' * 20)
            lista_atributos = ['Força', 'Destreza', 'Constituiçao', 'Inteligencia', 'Sabedoria', 'Carisma']
            lista_valores = [15, 14, 13, 12, 10, 8]
            lista_atributos_esc = []
            print('Agora você vai decidir em quais atributos deve colocar os valores,\n'
                  'lembre-se de escolher o que melhor atende sua classe')
            for n in range(len(lista_atributos)):
                print(lista_valores)
                while True:
                    atrib = input(lista_atributos[n] + ' = ')
                    if atrib.isnumeric():
                        atrib = int(atrib)
                        if atrib in lista_valores:
                            break
                        else:
                            print('Você precisa digitar um número possivel cara cara!!!')
                    elif not atrib.isdigit():
                        print('Você precisa digitar um número possivel cara cara!!!')
                lista_atributos_esc.append(atrib)
                lista_valores.pop(lista_valores.index(atrib))
            self.atrib_forca = lista_atributos_esc[0]
            self.atrib_destreza = lista_atributos_esc[1]
            self.atrib_constituicao = lista_atributos_esc[2]
            self.atrib_inteligencia = lista_atributos_esc[3]
            self.atrib_sabedoria = lista_atributos_esc[4]
            self.atrib_carisma = lista_atributos_esc[5]

    def ajuste_r(self):
        if self.raca == 'Anão':
            self.atrib_constituicao += 2
            self.deslocamento = '7.5 metros'
            self.extras_r = '''
Visão no Escuro: Trata escuridão a
18m (12quadrados) como penumbra e
penumbra como claridade.
Resiliência dos Anões: Resistência a
dano de veneno e Vantagem em testes
de resistência contra veneno.'''
            self.proficiencias = '''
Armas:
machado de guerra,
machadinha, martelo de arremesso,
martelo de guerra.
Ferramentas:
ferramentas
de Ferreiro, Pedreiro ou Cervejeiro.
Extras:
Dobro de proficiência em História
relacionado à origem de trabalhos de
pedra.'''
            self.idiomas = 'Comum e Anão.'
        if self.raca == 'Elfo':
            self.atrib_destreza += 2
            self.deslocamento = '9 metros'
            self.proficiencias = '''
Proficiência na perícia
Percepção.'''
            self.extras_r = '''
Visão no Escuro: Trata escuridão a 18m (12quadrados)
como penumbra e penumbra como claridade.
Ancestral Feérico: Vantagem contra ser Enfeitiçado,
imune a magias de sono
Transe: Não dorme. Descanso prolongado de apenas 4
horas'''
            self.idiomas = 'Comum e Élfico'
        if self.raca == 'Halfling':
            self.atrib_destreza += 2
            self.deslocamento = '7.5 metros'
            self.extras_r = '''
Sorte: Quando rolar um 1 natural em uma
jogada de ataque, a teste de atributo ou
resistência, ele pode jogar novamente o
dado mas deve utilizar a nova rolagem.
Bravo: Vantagem em resistência contra
ficar amedrontado.
Agilidade Halfling: Pode se mover pelo
espaço de criaturas maiores que o seu.'''
            self.idiomas = 'Comum e Halfling.'
        if self.raca == 'Humano':
            self.atrib_forca += 1
            self.atrib_destreza += 1
            self.atrib_constituicao += 1
            self.atrib_inteligencia += 1
            self.atrib_sabedoria += 1
            self.atrib_carisma += 1
            self.deslocamento = '9 metros'
            self.idiomas = 'comum e um outro idioma adicional da escolha do jogador.'
        if self.raca == 'Draconato':
            self.atrib_forca += 2
            self.atrib_carisma += 1
            self.deslocamento = '9 metros'
            self.extras_r = '''
Ancestral Dracônico: Escolha um ancestral
dracônico. Suas escamas são dessa cor, sua
resistência e sopro são de acordo com o elemento
ligado.
Resistência: Recebe resistência ao elemento de
seu ancestral.
Sopro: O draconato pode usar um sopro que
causa 2d6 (resistência reduz à metade, CD 8 +
Proficiência + CON). Esse dano aumenta em 1d6
aos níveis 6, 11 e 16. Depois de usar seu sopro,
você não pode usá-lo novamente até que você
completar um descanso curto ou longo.'''
            self.idiomas = 'Comum e Dracônico.'
        if self.raca == 'Gnomo':
            self.atrib_inteligencia += 2
            self.deslocamento = '7.5 metros'
            self.extras_r = '''
Esperteza Gnômica: Vantagem em testes de
resistência de Inteligência, Sabedoria ou
Carisma contra magias.
Visão no Escuro: Trata escuridão a 18m
(12quadrados) como penumbra e penumbra
como claridade.'''
            self.idiomas = 'Comum e Gnomo.'
        if self.raca == 'Meio-Elfo':
            self.atrib_carisma += 2
            esc = input('Digite o nome de um atributo que queira adicionar + 1 a ele').lower()
            esc2 = input('Digite o nome de um outro atributo que queira adicionar + 1 a ele').lower()
            if esc == 'força' or esc2 == 'força':
                self.atrib_forca += 1
            elif esc == 'destreza' or esc2 == 'destreza':
                self.atrib_destreza += 1
            elif esc == 'constituição' or esc2 == 'constituição':
                self.atrib_constituicao += 1
            elif esc == 'inteligencia' or esc2 == 'inteligencia':
                self.atrib_inteligencia += 1
            elif esc == 'sabedoria' or esc2 == 'sabedoria':
                self.atrib_sabedoria += 1
            elif esc == 'carisma' or esc2 == 'carisma':
                self.atrib_carisma += 1
            self.deslocamento = '9 metros'
            self.proficiencias = 'Proficiência em duas perícias à escolha'
            self.extras_r = '''
Ancestral Feérico: Vantagem contra ser
Enfeitiçado, imune a magias de sono.
Visão no Escuro: Trata escuridão a 18m
(12quadrados) como penumbra e penumbra
como claridade'''
            self.idiomas = 'Comum, Élfico e mais um idioma.'
        if self.raca == 'Tiefling':
            self.atrib_carisma += 2
            self.atrib_inteligencia += 1
            self.deslocamento = '9 metros'
            self.extras_r = '''
Legado Infernal: Conhece o Truque
Taumaturgia. A partir do nível 3 pode usar a
magia Repreensão Infernal uma vez por dia. A
partir do nível 5 também pode usar a magia
Escuridão uma vez por dia.
Resistência Diabólica: Resistência à Fogo.
Visão no Escuro: Trata escuridão a 18m
(12quadrados) como penumbra e penumbra
como claridade'''
            self.idiomas = 'Comum e Infernal.'
        if self.raca == 'Meio-Orc':
            self.atrib_forca += 2
            self.atrib_constituicao += 1
            self.deslocamento = '9 metros'
            self.proficiencias = 'Proficiência em Intimidar.'
            self.extras_r = '''
Ataques Selvagens: Quando consegue um
decisivo rola um dado extra de dano.
Tolerância Infindável: Uma vez por
descanso longo, ao cair a 0 sem morrer,
cai para 1 ao invés.
Visão no Escuro: Trata escuridão a 18m
(12quadrados) como penumbra e
penumbra como claridade'''
            self.idiomas = 'Orc e Comum.'

    def ajuste_c(self):
        if self.classe == 'Bárbaro':
            sleep(0.4)
            print('-' * 20)
            self.pv = 12 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves, médias e escudos; Armas simples e
marciais; 
Ferramentas: Nenhuma; Testes de Resistência:
Força e Constituição; 
Perícias: Escolha duas entre
Adestrar Animais, Atletismo, Intimidação, Natureza,
Percepção e Sobrevivência'''
            self.equipamento = '''
Equipamentos:
Você começa com o equipamento a seguir,
além do equipamento do seu antecedente:
(a) Um machado grande ou (b) qualquer
arma marcial corpo-a-corpo;
(a) Duas machadinhas ou (b) qualquer
arma simples;
Um pacote do explorador e quatro azagaias'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Berserk ou '
                            '[2]Guerreiro Totêmico ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Berserk'
                    break
                elif esc == 2:
                    self.caminho = 'Guerreiro Totêmico'
                    break
                elif esc == 0:
                    print('''
                        BERSERK
                    3º Nível – Frenezi
                    Pode entrar em Frenezi quando em fúria
                    e fazer um ataque corpo a corpo como
                    ação bônus. Quando terminar a fúria
                    sofre um nível de exaustão.
                    6º Nível – Fúria Inabalável
                    Não pode ser amedrontado ou encantado
                    quando em fúria. Se estiver amedrontado
                    ou encantado quando entrar em fúria o
                    efeito é suspenso pela duração da fúria.
                    10º Nível - Presença Intimidadora
                    Escolha uma criatura até 9 m de você. Se
                    ela puder vê-lo ou ouvi-lo, deve passar no
                    teste de resistência de Sabedoria (CD = 8
                    + bônus de proficiência + mod de
                    Carisma) ou fica amedrontada até o final
                    do seu próximo turno. Em outros turnos
                    você pode usar sua ação para prolongar o
                    efeito. O efeito acaba se a criatura
                    terminar o turno dela fora da linha de
                    visão ou a mais de 18 m de você. Se ela
                    obter êxito no teste de resistência, você
                    não pode afeta-la dessa maneira por 24
                    horas.
                    14º Nível – Retaliação
                    Quando sofrer dano de uma criatura à
                    1,5 m de você, pode usar sua reação para
                    fazer um ataque corpo a corpo contra
                    aquela criatura
                    
                        GUERREIRO TOTÊMICO
                    3º Nível
                    – Caçador Espiritual e Espírito
                    Totêmico
                    Pode conjurar as magias falar com animas e sentido animal, mas somente como
                    ritual.
                    Pode escolher qualquer um entre:
                    Urso: Quando em fúria fica resistente a
                    todos os tipos de dano, exceto psíquico.
                    Águia: Quando em fúria
                    e sem usar
                    armadura pesada, criaturas tem
                    desvantagem em ataques de
                    oportunidade contra você
                    e você pode
                    usar ação corrida como ação bônus.
                    Lobo: Quando em fúria, seus aliados têm
                    vantagem em ataque corpo
                    a corpo
                    contra criaturas inimigas
                    a 1,5 m de você.
                    6º Nível
                    – Aspecto da Fera
                    Pode escolher qualquer um entre:
                    Urso: Sua capacidade de carga (incluindo
                    carga máxima
                    e sustentação)
                    é dobrada e
                    você tem vantagem nos testes de Força
                    feitos para empurrar, puxar, erguer ou
                    quebrar objetos.
                    Águia: Consegue enxergar
                    1 milha(1,6 km) sem dificuldade, podendo ver
                    detalhes como se estiver olhando
                    a 30m.
                    A penumbra não impõe desvantagem nos
                    testes de Sabedoria (Percepção).
                    Lobo: Consegue rastrear criaturas
                    enquanto viaja rápido
                    e pode se mover
                    furtivamente enquanto viaja em ritmo
                    normal.
                    10º Nível
                    – Andarilho Espiritual
                    Consegue conjurar magia comunhão com
                    anatureza, como ritual. Uma versão
                    espiritual de um dos animais totêmicos
                    aparece para dar
                    a informação.
                    14º Nível
                    – Harmonização Totêmica
                    Pode escolher qualquer um entre:
                    Urso: Quando em fúria, inimigos
                    a 1,5 m de você tem desvantagem em ataques
                    contra alvos que não sejam você ou outra
                    pessoa com essa habilidade..
                    Águia: Quando em fúria, tem
                    deslocamento de voo igual seu
                    deslocamento em terra Caí se terminar
                    o turno no ar ou não ter algo lhe
                    sustentando.
                    Lobo: Quando em fúria, pode usar uma
                    ação bônus para derrubar uma criatura
                    Grande ou menor que você acertar com
                    um ataque corpo
                    a corpo.
                    ''')
        if self.classe == 'Bardo':
            sleep(0.4)
            print('-' * 20)
            self.pv = 8 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves; Armas simples, besta de mão, espada
curta, espada longa, rapieira; 
Ferramentas: Escolha três
instrumentos musicais; 
Testes de Resistência: Destreza e
Carisma; 
Perícias: Escolha três que quiser.'''
            self.equipamento = '''
Equipamentos:
Você começa com os seguintes equipamentos,
em adição ao equipamento concedido pelo seu
antecedente:
(a) Um florete, (b) Uma espada longa, ou (c)
qualquer arma simples
(a) Pacote do diplomata ou (b) Pacote do artista
(a) Um alaúde ou (b) qualquer outro
instrumento musical
 Corselete de couro e uma adaga.'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Colégio da '
                            'Bravura ou [2]Colégio do Saber ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Colégio da Bravura'
                    break
                elif esc == 2:
                    self.caminho = 'Colégio do Saber'
                    break
                elif esc == 0:
                    print('''
                        COLÉGIO DA BRAVURA
                    3º Nível – Proficiência Bônus e Inspiração
                    de Combate
                    Você ganha proficiência em armaduras
                    médias, escudos e armas marciais.
                    O alvo de uma Inspiração do Bardo pode
                    rolar o dado e adicionar ao dano da arma,
                    quando fizer um ataque.
                    Além disso, quando um ataque for feito
                    contra esta criatura ela usar sua própria
                    reação, rolar o dado de Inspiração e adicioná-
                    lo na sua CA após a rolagem, mas antes de
                    saber se o ataque acertou ou errou.
                    6º Nível – Ataque Extra
                    Quando usar ação Atacar, pode atacar duas
                    vezes.
                    14º Nível – Combatente Mágico
                    Ao conjurar uma magia de bardo, pode fazer
                    um ataque com sua arma com uma ação
                    bônus
                    
                        COLÉGIO DO SABER
                    3º Nível – Proficiência Bônus e Palavras
                    Cortantes
                    Você ganha proficiência em três perícias a sua
                    escolha.
                    Quando uma criatura a até 18 m que você
                    possa ver fizer um ataque, teste de atributo ou
                    rolagem de dano, você pode usar sua reação
                    gastando um uso de Inspiração de Bardo.
                    Role o dado e subtraia o valor da rolagem da
                    criatura. Pode ser feito após a rolagem, mas
                    antes de saber se a rolagem obteve sucesso ou
                    não, ou antes de ser rolado o dano. A criatura
                    fica imune a isso se não puder ouvi-lo ou for
                    imune a se encantada.
                    6º Nível – Segredos Mágicos Adicionais
                    Escolha duas magias de qualquer classe,
                    incluindo esta, e adicione às conhecidas.
                    Devem ser de um nível você possa conjurar.
                    Contam como magias de bardo e são incluídas
                    no numero de magias conhecidas.
                    14º Nível – Habilidade Inigualável
                    Quando fizer um teste de atributo, pode
                    gastar um uso de Inspiração de Bardo.
                    Role o dado e adicione o valor ao seu
                    teste. Pode optar fazer isso depois da
                    rolagem, mas antes de saber se a rolagem
                    obteve sucesso ou não.''')
        if self.classe == 'Bruxo':
            sleep(0.4)
            print('-' * 20)
            self.pv = 8 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves; Armas simples; 
Ferramentas:
Nenhuma; 
Testes de Resistência: Sabedoria e Carisma;
Perícias: Escolha duas entre Arcanismo, Enganação,
História, Intimidação, Investigação, Natureza e Religião.'''
            self.equipamento = '''
Equipamentos:
Você começa com o seguinte equipamento, em
adição ao equipamento concedido pelo seu
antecedente:
(a) uma besta leve e 20 virotes ou (b) qualquer
arma simples;
(a) uma bolsa de componentes ou (b) um foco
arcano;
(a) um pacote de estudioso ou (b) um pacote de
masmorra;
Corselete de couro, qualquer arma simples, e
duas adagas.'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]O Feérico ou [2]O '
                            'Infernal ou [3]O Grande Antigo ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'O Feérico'
                    break
                elif esc == 2:
                    self.caminho = 'O Infernal'
                    break
                elif esc == 3:
                    self.caminho = 'O Grande Antigo'
                    break
                elif esc == 0:
                    print('''
                        O FEÉRICO
                    Você pode escolher magias da lista de magias
                    expandidas do feérico.
                    1º Nível – Presença Feérica
                    Uma ação, criaturas em um cubo de 3
                    metros originando de você fazem teste de
                    resistência de Sabedoria. Se falharem estão
                    amedrontados ou encantadas (você escolhe)
                    até o final do seu próximo turno. Pode usar
                    uma vez por descanso curto ou longo.
                    6º Nível – Fuga Nebulosa
                    Ao levar dano, pode usar sua reação para
                    ficar invisível e se teleportar até 18 metros
                    em um espaço não ocupado que possa ver.
                    Fica invisível até seu próximo turno ou
                    atacar ou conjurar magia. Pode usar uma
                    vez por descanso curto ou longo.
                    10º Nível – Defesa Sedutora
                    Fica imune a ser encantado. Se tentarem
                    tentar encantar você, pode usar sua reação
                    para retornar o encantamento nesta
                    criatura. Ela faz um teste de resistência. Se
                    falhar fica amedrontada ou encantada (você
                    escolhe) por 1 minuto ou até sua
                    concentração ser quebrada (como se
                    estivesse concentrando uma magia). O
                    efeito termina antes se ela sofrer dano. Pode
                    usar uma vez por descanso curto ou longo.
                    14º Nível – Delírio Obscuro
                    Com uma ação, escolha uma criatura que
                    possa ver até 18 metros. Ela faz um teste
                    de resistência. Se falhar fica amedrontada
                    ou encantada (você escolhe) por 1 minuto
                    ou até sua concentração ser quebrada
                    (como se estivesse concentrando uma
                    magia). O efeito termina antes se a
                    criatura sofrer dano. Até a ilusão
                    terminar, ela pensa que esta perdida em
                    um reino de neblina, a aparência você
                    escolhe. Só pode ouvir ela mesma, você e
                    a ilusão. Pode usar uma vez por descanso
                    curto ou longo.
                    
                        O INFERNAL
                    Você pode escolher magias da lista de magias
                    expandidas do infernal.
                    1º Nível – Benção do Obscuro
                    Ao reduzir um inimigo a 0 PV, ganha PVs
                    temporários igual ao seu mod de Carisma +
                    seu nível de bruxo (mínimo 1).
                    6º Nível – Sorte do Obscuro
                    Ao fazer teste de atributo ou teste de
                    resistência, pode adicionar 1d10 na
                    rolagem. Pode fazer isso depois de ver a
                    rolagem inicial, mas antes de ocorrer
                    qualquer efeito da rolagem. Pode usar uma
                    vez por descanso curto ou longo.
                    10º Nível – Resistência Infernal
                    Escolha um tipo de dano ao terminar um
                    descanso curto ou longo. Ganha resistência
                    contra esse tipo de dano até escolher outro.
                    Danos de armas mágicas ou armas de prata
                    ignoram esta resistência.
                    14º Nível – Passeio pelo Inferno
                    Ao acertar uma criatura com um ataque,
                    pode instantaneamente transportar o alvo
                    através dos planos inferiores. Ao fim do seu
                    próximo turno o alvo retorna para o local
                    que estava, ou o mais próximo desocupado.
                    Se não for um infernal, leva 10d10 de dano
                    psíquico. Pode usar uma vez por descanso
                    longo
                    
                        O GRANDE ANTIGO
                    Você pode escolher magias da lista de magias
                    expandidas do grande antigo.
                    1º Nível – Mente Desperta
                    Pode se comunicar telepaticamente com
                    qualquer criatura que possa ver até 9
                    metros. Não precisar compartilhar o
                    mesmo idioma para se entender
                    telepaticamente, mas a criatura deve
                    compreender ao menos um idioma.
                    6º Nível – Proteção Entrópica
                    Quando uma criatura fizer um ataque
                    contra você, pode usar sua reação para
                    impor desvantagem naquela rolagem. Se
                    errar, sua próxima rolagem de ataque
                    contra ela tem vantagem se fizer antes do
                    fim do seu próximo turno. Pode usar uma
                    vez por descanso curto ou longo.
                    10º Nível – Escudo Mental
                    Seus pensamentos não podem ser lidos por
                    telepatia ou outros meios a menos que você
                    permita. Você também tem resistência a
                    dano psíquico, e sempre que uma criatura
                    causar dano psíquico em você ela toma a
                    mesma quantia de dano.
                    14º Nível – Criar Escravo
                    Com uma ação pode tocar um humanoide
                    incapacitado. Ele fica encantado por você
                    até que a magia remover maldição seja
                    conjurada nele, a condição encantado for
                    removido dele ou você usar esta
                    característica novamente. Você pode se
                    comunicar telepaticamente com a criatura
                    encantada desde que os dois estejam no
                    mesmo plano de existência.''')
        if self.classe == 'Clérigo':
            sleep(0.4)
            print('-' * 20)
            self.pv = 8 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves, médias e escudos; Armas simples;
Ferramentas: Nenhuma; 
Testes de Resistência: Sabedoria
e Carisma; 
Perícias: Escolha duas entre História, Intuição,
Medicina, Persuasão e Religião.'''
            self.equipamento = '''
Equipamentos:
Você começa com os seguintes equipamentos, em
adição ao equipamento concedido pelo seu
antecedente:
(a) Uma maça ou (b) Um machado de batalha (se
proficiente)
(a) Armadura de escamas, (b) Armadura de couro,
ou (c) Cota de malha (se proficiente);
(a) Uma besta leve e 20 virotes ou (b) Uma arma
simples
(a) Pacote de sacerdote ou (b) Pacote de explorador
Um escudo e um símbolo sagrado'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de \n[1]Domínio do Conhecimento'
                            ' ou [2]Domínio da Enganação ou [3]Domínio da Guerra ou [4]Domínio da Luz ou [5]Domínio'
                            ' da Natureza ou [6] Domínio da Tempestade ou [7]Domínio da Vida ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Domínio do Conhecimento'
                    break
                elif esc == 2:
                    self.caminho = 'Domínio da Enganação'
                    break
                elif esc == 3:
                    self.caminho = 'Domínio da Guerra'
                    break
                elif esc == 4:
                    self.caminho = 'Domínio da Luz'
                    break
                elif esc == 5:
                    self.caminho = 'Domínio da Natureza'
                    break
                elif esc == 6:
                    self.caminho = 'Domínio da Tempestade'
                    break
                elif esc == 7:
                    self.caminho = 'Domínio da Vida'
                    break
                elif esc == 0:
                    print('''
                        DOMÍNIO DO CONHECIMENTO
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de magias
                    preparadas por dia.
                    1º Nível – Benção do Conhecimento
                    Aprende dois idiomas à sua escolha. Torna-se
                    proficiente em duas das seguintes perícias:
                    Arcanismo, História, Natureza ou Religião. Seu
                    bônus de proficiência é dobrado em testes que
                    usem essas perícias.
                    2º Nível – Canalizar Divindade: Conhecimento
                    das Eras
                    Uma ação, escolha uma perícia ou ferramenta. Por
                    10 minutos tem proficiência na pericia ou
                    ferramenta escolhida.
                    6º Nível – Canalizar Divindade: Ler
                    Pensamentos
                    Uma ação, escolha uma criatura que possa ver até
                    18 metros. Ela faz um teste de resistência de
                    Sabedoria. Se ela passar, não pode usar essa
                    característica até terminar um descanso longo. Se
                    falhar, pode ler pensamentos superficiais (que
                    aparecem primeiro na mente, refletindo o estado
                    emocional atual e no que sua atenção está focada)
                    enquanto estiver a 18 m dela. Dura 1 minuto. Pode
                    usar uma ação e encerrar este efeito lançando
                    sugestão na criatura sem gastar espaço de magia. O
                    alvo falha automaticamente no TR da magia.
                    8º Nível – Conjuração Potente
                    Adicione seu mod de Sabedoria em rolagens de
                    dano de truques de clérigo.
                    17º Nível – Visões do Passado
                    Recebe vislumbres de ventos recentes. Pode
                    meditar um numero de minutos igual seu mod
                    de Sabedoria. Pode usar uma vez por descanso
                    curto ou longo.
                    Ler Objeto: Segurando o objeto, depois de 1 minuto
                    descobre como o dono o adquiriu e o perdeu, bem
                    como eventos recentes significantes envolvendo o
                    objeto e o dono. Se foi portado por outras criaturas
                    recentemente (número de dias igual seu valor de
                    Sabedoria), pode gastar 1 minuto adicional por
                    portador para aprender a mesma informação sobre
                    a criatura.
                    Ler Área: Eventos recentes nos arredor (até 15 m
                    cúbicos)., volta um numero de dias igual seu mod
                    de Sabedoria. Cada minuto meditando, descobre
                    um evento significativo, a partir do mais recente.
                    Eventos significativos são tipicamente emoções
                    poderosas, como batalhas e trações, casamentos e
                    assassinatos, nascimentos e funerais. Podem incluir
                    eventos mundanos relevantes para sua situação
                    atual.
                    
                        DOMÍNIO DA ENGANAÇÃO
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de
                    magias preparadas por dia.
                    1º Nível – Benção do Malandro
                    Com uma ação, pode tocar uma criatura viva
                    e dar a ela vantagem nos testes de Destreza
                    (Furtividade). Dura por 1 hora ou até você
                    usar essa característica de novo.
                    2º Nível – Canalizar Divindade: Invocar
                    Duplicidade
                    Com uma ação, cria uma ilusão perfeita de
                    você que dura 1 minuto ou até perder sua
                    concentração (como uma magia). Aparece em
                    espaço desocupado até 9 metros de você, pode
                    mover ela 9 metros com sua ação bônus até 36
                    metros de você. Pode lançar magias através
                    dela, mas usando seus próprios sentidos.
                    Quando estiver a 1,5 m dela de uma criatura
                    que possa ver a ilusão, você tem vantagem nos
                    ataques.
                    6º Nível – Canalizar Divindade: Manto
                    das Sombras
                    Com uma ação, fica invisível ate final do seu
                    próximo turno. Fica visível se atacar ou lançar
                    magia.
                    8º Nível – Ataque Divino
                    Uma vez por turno, quando acertar um ataque
                    com arma, pode adicionar ao dano 1d8 de
                    dano de veneno. No 14º nível aumenta para
                    2d8.
                    17º Nível – Duplicidade Aprimorada
                    Pode criar até 4 cópias de você ao usar
                    Invocar Duplicidade. Com uma ação
                    bônus no seu turno, pode movê-las 9
                    metros, até 36 metros longe de você.
                    
                        DOMÍNIO DA GUERRA
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de
                    magias preparadas por dia.
                    1º Nível – Proficiência Bônus e Sacerdote
                    da Guerra
                    Ganha proficiência em armas marciais e
                    armaduras pesadas.
                    Além disso, quando usar a ação Atacar, pode
                    fazer um ataque com arma como uma ação
                    bônus. Pode fazer isso um numero de vezes
                    igual seu mod de Sabedoria (mínimo 1) por
                    descanso longo.
                    2º Nível – Canalizar Divindade: Ataque
                    Guiado
                    Quando atacar, pode usar seu Canalizar
                    divindade para ganhar +10 na jogada. Pode
                    usar depois de ver o resultado, mas antes do
                    mestre dizer se você acertou ou errou.
                    6º Nível – Canalizar Divindade: Benção
                    do Deus da Guerra
                    Quando uma criatura até 9 metros de você
                    fizer um ataque, pode usar sua reação para
                    das +10 na jogada de ataque dela, usando
                    Canalizar Divindade. Pode usar depois de ver
                    o resultado, mas antes do mestre dizer se você
                    acertou ou errou.
                    8º Nível – Ataque Divino
                    Uma vez por turno, quando acertar um ataque
                    com arma, pode adicionar ao dano 1d8 de
                    dano do tipo da arma. No 14º nível aumenta
                    para 2d8.
                    17º Nível – Avatar da Guerra
                    Ganha resistência a dano de concussão,
                    cortante e perfurante de armas não
                    mágicas.
                    
                        DOMÍNIO DA LUZ
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de
                    magias preparadas por dia.
                    1º Nível – Truque Bônus e Brilho Protetor
                    Você ganha o truque luz, se já não o souber.
                    Ao ser atacado por um inimigo até 9 metros
                    de você, pode usar sua reação para impor
                    desvantagem no ataque. Alguém que não
                    pode ficar cego é imune a isso. Pode usar um
                    número de vezes igual seu mod de Sabedoria
                    (mínimo 1) por descanso longo.
                    2º Nível – Canalizar Divindade:
                    Resplendor do Amanhecer
                    Com uma ação, mostra seu símbolo sagrado e
                    qualquer escuridão mágica até 9 metros de
                    você é dissipada. Criaturas hostis até 9 metros
                    de você precisam fazer teste de resistência de
                    Constituição. Se falhar levam 2d10 + seu nível
                    de clérigo ou metade se obterem sucesso. Uma
                    criatura com cobertura total não é afetada.
                    6º Nível – Brilho Aprimorado
                    Pode usar sua característica Brilho Protetor
                    quando uma criatura até 9 metros atacar outra
                    criatura que não seja você.
                    8º Nível – Conjuração Potente
                    Adicione seu mod de Sabedoria em rolagens
                    de dano de truques de clérigo.
                    17º Nível – Coroa de Luz
                    Pode usar sua reação para ativer uma aura
                    de luz do sol que dura 1 minuto ou até ser
                    dispersada por você com uma ação. Emite
                    claridade em 18 m de raio e penumbra de
                    9 m depois. Inimigos dentro da claridade
                    tem desvantagem em testes de resistência
                    contra magias que causem dano de fogo
                    ou radiante
                    
                        DOMÍNIO DA NATUREZA
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de
                    magias preparadas por dia.
                    1º Nível – Acólito da Natureza e Proficiência
                    Bônus
                    Aprende um truque de druida a sua escolha.
                    Ganha proficiência em uma das seguintes
                    pericias a sua escolha: Adestrar Animais,
                    Natureza ou Sobrevivência.
                    Ganha proficiência com armadura pesada.
                    2º Nível – Canalizar Divindade: Encantar
                    Animais e Plantas
                    Com um ação, exiba seu símbolo sagrado e
                    invoque o nome de sua divindade. Cada besta
                    ou criatura tipo planta que puder ver você até 9
                    m, faz um teste de resistência de Sabedoria. Se
                    falhar, esta encantada por você por 1 minuto o
                    até sofrer dano. Enquanto encantada, é amigável
                    à você e as criaturas que você designar.
                    6º Nível – Amortecer Elementos
                    Quando você ou uma criatura até 9 metros de
                    você levar dano ácido, congelante, fogo, elétrico
                    ou sônico, você pode usar sua reação para
                    conceder resistência para a criatura contra o
                    dano naquele momento.
                    8º Nível – Ataque Divino
                    Uma vez por turno, quando acertar um ataque
                    com arma, pode adicionar ao dano 1d8 de dano
                    congelante, fogo ou elétrico (sua escolha). No
                    14º nível aumenta para 2d8.
                    17º Nível – Mestre da Natureza
                    Ganha a habilidade de comandar animais e
                    criaturas plantas. Enquanto as criaturas
                    estiverem encantadas pela sua habilidade de
                    Encantar Animas e Plantas, você pode usar
                    uma ação bônus no seu turno para
                    verbalmente comandar o que cada uma destas
                    criaturas farão em seus próximos turnos.
                    
                        DOMÍNIO DA TEMPESTADE
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de
                    magias preparadas por dia.
                    1º Nível – Proficiência Bônus e Fúria da
                    Tempestade
                    Ganha proficiência com armas marciais e
                    armaduras pesadas.
                    Quando uma criatura que você possa ver
                    estiver a 1,5 m de você e lhe acertar um
                    ataque, pode usar sua reação para fazer com
                    que ela faça um teste de resistência de
                    Destreza. Se falhar sofre 2d8 de dano elétrico
                    ou sônico (sua escolha) ou metade se passar.
                    Pode usar um número de vezes igual seu mod
                    de Sabedoria (mínimo 1) por descanso longo.
                    2º Nível – Canalizar Divindade: Fúria
                    Destruidora
                    Quando for rolar dano elétrico ou sônico,
                    pode usar seu Canalizar Divindade para dar o
                    dano máximo, ao invés de rolá-lo
                    6º Nível – Canalizar Divindade: Manto
                    das Sombras
                    Quando causar dano elétrico em uma criatura
                    Grande ou menos, pode também empurrá-la a
                    até 3 m longe de você.
                    8º Nível – Ataque Divino
                    Uma vez por turno, quando acertar um ataque
                    com arma, pode adicionar ao dano 1d8 de
                    dano sônico. No 14º nível aumenta para 2d8.
                    17º Nível – Duplicidade Aprimorada
                    Pode voar com o mesmo deslocamento
                    em terra, exceto em lugares subterrâneos
                    ou dentro de lugares fechados.
                    
                        DOMÍNIO DA VIDA
                    Ganha magias de domínio ao ganhar níveis de
                    clérigo, conforme a tabela, que estão sempre
                    preparadas e não contam para o número de
                    magias preparadas por dia.
                    1º Nível – Proficiência Bônus e Discípulo
                    da Vida
                    Ganha proficiência em armaduras pesadas.
                    Sempre que usar uma magia de cura para
                    restaurar pontos de vida, o alvo recupera um
                    adicional de 2 + nível da magia.
                    2º Nível – Canalizar Divindade: Preservar
                    a Vida
                    Com uma ação, com seu símbolo sagrado
                    invoque energia curativa para recuperar
                    pontos de vida em um total de 5 vezes seu
                    nível de clérigo. Escolha qualquer numero de
                    criaturas a até 9 m de você e divida estes
                    pontos entre elas. Só pode curar até metade de
                    seus pontos de vidas totais. Não pode ser
                    usada em mortos-vivos ou constructos.
                    6º Nível – Cura Abençoada
                    Quando usar uma magia de cura em outra
                    criatura, recupere pontos de vida iguais a 2 +
                    nível da magia.
                    8º Nível – Ataque Divino
                    Uma vez por turno, quando acertar um ataque
                    com arma, pode adicionar ao dano 1d8 de
                    dano radiante. No 14º nível aumenta para
                    2d8.
                    17º Nível – Cura Suprema
                    Quando rolar dados para restaurar pontos
                    de vida, use o máximo possível da
                    rolagem. Por exemplo, se fosse rolar 2d6
                    você cura 12.''')
        if self.classe == 'Druida':
            sleep(0.4)
            print('-' * 20)
            self.pv = 8 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves, médias e escudos (druidas não usam armadura ou
escudo de metal); 
Armas: Adagas, azagaias, bordões, cimitarras,
clavas, dardos, foices, funda, lanças, maças; 
Ferramentas: kit de
Herbalismo; 
Testes de Resistência: Inteligência e Sabedoria;
Perícias: Escolha duas entre Adestrar Animais, Arcanismo,
Intuição, Natureza, Medicina, Percepção, Religião e Sobrevivência.'''
            self.equipamento = '''
Equipamentos:
Você começa com os seguintes equipamentos,
em adição ao equipamento concedido pelo seu
antecedente:
(a) Um escudo de madeira ou (b) qualquer
arma simples
(a)Uma cimitarra ou (b) qualquer arma corpo a
corpo simples
Corselete de couro, pacote do explorador e um
foco druídico.
            '''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Círculo da Lua ou [2]Círculo do'
                            ' Solo ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Círculo da Lua'
                    break
                elif esc == 2:
                    self.caminho = 'Círculo do Solo'
                    break
                elif esc == 0:
                    print('''
                            CÍRCULO DA LUA
                    2º Nível – Forma Selvagem de Combate e
                    Formas de Círculo
                    Pode usar Forma Selvagem no seu turno como
                    uma ação bônus. Quando transformado pela
                    Forma Selvagem, pode usar uma ação bônus
                    para gastar um espaço de magia e recuperar
                    pontos de vida iguais a 1d8 por nível do espaço
                    gasto.
                    Pode se transformar em criaturas de ND até 1
                    (ignora a ND Máx. da tabela, mas mantem as
                    limitações). No 6º Nível, pode se transformar
                    em uma besta de ND igual a seu nível de druida
                    dividido por 3, arredondado para baixo.
                    6º Nível – Ataque Selvagem
                    Seus ataque na forma de besta contam como
                    mágico para propósitos de superar resistências e
                    imunidades à ataque e danos não mágicos.
                    10º Nível – Forma Selvagem Elemental
                    Pode gastas dois usos de Forma Selvagem ao
                    mesmo tempo para se transformar em um
                    elemental da água, um elemental do ar, um
                    elemental do fogo ou um elemental da terra.
                    14º Nível – Mil Formas
                    Pode conjurar a magia alterar-se sem limite.
                            
                            CÍRCULO DO SOLO
                    Magias de Círculo: Escolha um terreno entre
                    ártico, deserto, floresta, litoral, montanha,
                    pântano, planície ou Subterrâneo. Ganha
                    magias de acordo com o terreno escolhido.
                    Elas estão sempre preparadas e não contam
                    para o número de magias preparadas por dia.
                    2º Nível – Truque Bônus e Recuperação
                    Espontânea
                    Ganha um truque de druida a sua escolha.
                    Durante um descanso curto, pode recuperar
                    espaços de magia. Os espaços de magia
                    podem ter um nível combinado igual ou
                    menor a metade do seu nível de druida
                    (arredondado para cima) e nenhum pode ser
                    de 6º nível ou maior. Só pode usar isso uma
                    vez por descanso longo.
                    Exemplo: No 4º nível de druida, pode
                    recuperar dois níveis de espaços de magia.
                    Pode recuperar uma de 2º nível ou duas de 1º.
                    6º Nível – Passo Firme
                    Mover por terreno difícil não mágico não
                    custa deslocamento extra. Pode atravessar
                    plantas não mágicas sem andar mais devagar
                    ou tomar dano se elas causarem. Tem
                    vantagem nos testes de resistência contra
                    plantas criadas ou manipuladas por magia.
                    10º Nível – Proteção da Natureza
                    Não pode ser amedrontado ou encantado por
                    elementais ou feéricos, e é imune a veneno e
                    doença.
                    14º Nível – Santuário da Natureza
                    Quando uma besta ou plante lhe atacar,
                    ela faz um teste de resistência de
                    Sabedoria contra sua CD de magias. Se
                    falhar, a criatura escolhe outro alvo, ou o
                    ataque automaticamente falha. Com um
                    sucesso, a criatura fica imune a este efeito
                    por 24 horas.''')
        if self.classe == 'Feitiçeiro':
            sleep(0.4)
            print('-' * 20)
            self.pv = 6 + self.mod_constituicao
            self.proficiencias += '''
Armaduras nenhuma; 
Armas adaga, besta leve, cajado,
dardo e funda; 
Ferramentas: Nenhuma; 
Testes de Resistência: Constituição e Carisma; 
Perícias: Escolha
duas de Arcanismo, Enganação, Intimidação, Intuição,
Persuasão e Religião.'''
            self.equipamento = '''
Equipamentos:
Você começa com os seguintes
equipamentos, em adição ao equipamento
concedido pelo seu antecedente:
(a) Um besta leve e 20 virotes ou (b)
qualquer arma simples;
(a) Uma bolsa de componentes ou (b) um
foco arcano;
(a) Pacote de masmorra ou (b) um pacote
do explorador;
Duas adagas'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Linhagem Dracônica ou [2]Magia '
                            'Selvagem ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Linhagem Dracônica'
                    break
                elif esc == 2:
                    self.caminho = 'Magia Selvagem'
                    break
                elif esc == 0:
                    print('''
                        LINHAGEM DRACÔNICA
                    1º Nível –Ancestral Dragão e Resiliência
                    Dracônica
                    Escolha um ancestral dragão conforme a tabela.
                    Pode falar, ler e escrever em Dracônico. Sempre
                    que fizer um teste de Carisma ao interagir com
                    Dragões, seu bônus de proficiência é dobrado se
                    for aplicado ao teste.
                    Seus pontos de vida aumentam em 1 e você
                    ganha 1 a mais sempre que ganhar um nível nesta
                    classe. Sua pele é coberta por um tênue brilho de
                    escamas dracônicas. Quando não estiver vestindo
                    armadura sua CA é igual a 13 + mod de Destreza.
                    6º Nível – Afinidade Elemental
                    Ao conjurar uma magia que cause dano associado
                    ao seu ancestral dracônico, adicione seu mod de
                    Carisma no dano. Além disso, você pode gastar 1
                    ponto de feitiçaria para ganhar resistência a esse
                    tipo de dano por 1 hora.
                    14º Nível –Asas de Dragão
                    Pode criar asas de dragão das suas costas,
                    ganhando deslocamento de voo igual seu
                    deslocamento atual. Pode criá-las com uma ação
                    bônus. Duram até você as dispensar com uma
                    ação bônus. Não pode criá-las se estiver usando
                    armadura, a menos que a armadura seja feita para
                    acomoda-las, e roupa que não foi feita para
                    acomoda-las é destruída quando você as cria.
                    18º Nível – Presença Dracônica
                    Com uma ação, pode gastar 5 pontos de
                    feitiçaria para exalar uma aura de fascínio ou
                    medo (você escolhe) até uma distância de 18 m.
                    Por 1 minuto ou até você perder sua
                    concentração (como concentrando em uma
                    magia) cada criatura hostil que começar seu
                    turno na aura deve obter sucesso em um teste
                    de resistência de Sabedoria ou fica encantada
                    (se você escolheu fascínio) ou amedrontada (se
                    escolheu medo) até a aura encerrar. Quem obter
                    sucesso, fica imune a aura por 24 horas.
                    
                        MAGIA SELVAGEM
                    1º Nível – Pulso de Magia Selvagem e Maré do
                    Caos
                    Imediatamente após conjurar uma magia de
                    feiticeiro de 1º nível ou maior, o Mestre pede que
                    você role um d20. Se rolar 1, role na tabela de Pulso
                    de Magia Selvagem para ver o efeito aleatório.
                    Pode ganhar vantagem em um ataque, teste de
                    atributo ou teste de resistência. Só pode usar uma
                    vez por descanso longo. Qualquer momento antes de
                    recuperar o uso o Mestre pode solicitar para rolar na
                    tabela Pulso de Magia Selvagem depois de conjurar
                    uma magia de 1º nível ou mais. Você então recupera
                    o uso desta habilidade.
                    6º Nível – Dobrar a Sorte
                    Quando uma criatura que você possa ver fizer um
                    ataque, teste de atributo ou teste de resistência, você
                    pode gastar 2 pontos de feitiçaria e rolar 1d4
                    aplicando o valor rolado como bônus ou penalidade
                    (você escolhe) no teste dela. Pode fazer isso depois
                    da rolagem, mas antes de qualquer efeito da rolagem
                    ocorrer.
                    14º Nível –Caos Controlado
                    Sempre que rolar na tabela de Pulso de Magia
                    Selvagem, pode rolar 2 vezes e escolher qualquer
                    número.
                    18º Nível – Bombardeio de Magia
                    Ao rolar o dano para qualquer magia e rolar o
                    valor mais alto possível em qualquer um dos dado
                    de dano rolados, escolha um desses dados, role-o
                    novamente e adicione ao dano. Pode usar essa
                    característica uma vez por turno''')
        if self.classe == 'Guerreiro':
            sleep(0.4)
            print('-' * 20)
            self.pv = 10 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves, médias, pesadas e escudos; 
Armas simples e marciais; 
Ferramentas: Nenhuma; 
Testes de Resistência: Força e Constituição; 
Perícias: Escolha duas entre Acrobacia, Adestrar Animais, 
Atletismo, História, Intuição, Intimidação, Percepção 
e Sobrevivência.'''
            self.equipamento = '''
Equipamentos:
Você começa com os seguintes
equipamentos, em adição ao equipamento
dado pelo seu antecedente:
(a) Cota de malha ou (b) corselete de
couro, arco longo e 20 flechas;
(a) Uma arma marcial e um escudo ou (b)
duas armas marciais;
(a) Uma besta leve e 20 virotes ou (b) duas
machadinhas
(a) Um pacote de masmorra ou (b) um
pacote de explorador'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Campeão ou [2]Mestre de Batalha '
                            'ou [3]Cavaleiro Místico ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Campeão'
                    break
                elif esc == 2:
                    self.caminho = 'Mestre de Batalha'
                    break
                elif esc == 3:
                    self.caminho = 'Cavaleiro Místico'
                    break
                elif esc == 0:
                    print('''
                        CAMPEÃO
                    3º Nível - Crítico Aprimorado
                    Seus ataques com arma tem sucesso
                    crítico com rolagens de 19 e 20.
                    7º Nível - Atleta Renomado
                    Pode adicionar metade do bônus de
                    proficiência (arredondado para cima)
                    para qualquer teste de Força, Destreza ou
                    Constituição que ainda não use seu
                    bônus de proficiência.
                    10º Nível - Estilo de Combate Adicional
                    Pode escolher uma segunda opção da
                    característica de classe Estilo de Luta.
                    Não pode ser a mesma que escolheu no
                    nível 1.
                    15º Nível - Crítico Superior
                    Seus ataques com arma tem sucesso
                    crítico com rolagens de 18 à 20.
                    18º Nível – Sobrevivente
                    No começo do seu turno, você recuperar
                    PVs iguais a 5 + mod de Constituição se
                    estiver abaixo da metade dos seus PVs
                    máximos. Não ganha este beneficio se
                    tiver 0 PV
                    
                        MESTRE DE BATALHA
                    3º Nível - Estudante de Guerra e Superioridade
                    em Combate
                    Você ganha proficiência em uma ferramenta de
                    artesão a sua escolha.
                    Manobras: Aprenda 3 a sua escolha. Nos níveis
                    7, 10 e 15 aprende duas manobras e pode
                    substituir uma se quiser.
                    Dado de Superioridade: Possui 4 dados, que são
                    d8. Recupera todos quando completa um
                    descanso curto ou longo.
                    Teste de Resistência: A CD nos TR das
                    manobras que pedirem são:
                    CD = 8 + bônus proficiência + mod Força ou
                    Destreza (sua escolha).
                    7º Nível – Conheça seu Inimigo e +2 manobras
                    Se gastar 1 minuto observando ou interagindo
                    com uma criatura pode descobrir:
                    • Valor de Força, Destreza ou Constituição;
                    CA;
                    • PVs atuais;
                    • Níveis totais de Classe (se tiver)
                    • Níveis de Guerreiro (se tiver)
                    10º Nível – Superioridade em Combate
                    Aprimorada e +2 manobras
                    Dado de superioridade vira 1d10. No 18º nível
                    vira 1d12.
                    15º Nível – Implacável e +2 manobras
                    Quando for rolar iniciativa e não tiver dados de
                    superioridade, recupere 1 dado de superioridade
                    
                        CAVALEIRO MÍSTICO
                    Magias Conhecidas: Aprende da lista de
                    Mago. Começa com três magias de nível 1
                    à sua escolha, mas 2 devem ser de
                    Abjuração ou Evocação. As magias que
                    aprender devem ser também de Abjuração
                    ou Evocação, exceto nos níveis 8, 14 e 20.
                    Quando ganhar um nível nesta classe,
                    pode trocar uma magia conhecida por
                    outra, mas deve ser de Abjuração ou
                    Evocação, exceto se a magia foi ganha nos
                    níveis 8, 14 ou 20. Recupera todos os
                    espaços de magia com um descanso
                    longo.
                    Atributo de Conjuração: Inteligência é o
                    atributo de conjuração.
                    CD de resistência a magia = 8 + bônus de
                    proficiência + mod Inteligência.
                    Ataque com magia = bônus de
                    proficiência + mod Inteligência
                    3º Nível – Elo com Arma
                    Realiza um ritual com uma arma durante
                    1 hora, que pode ser feito durante um
                    descanso curto. Não pode ser desarmado
                    com essa arma, a menos que esteja
                    incapacitado. Se estiverem no mesmo
                    plano de existência, pode invocar a arma
                    com uma ação bônus no seu turno, ela
                    aparece instantaneamente na sua mão.
                    Pode ter no máximo dois elos com arma,
                    mas só pode invocar uma de cada vez. Se
                    fizer elo com uma terceira arma quebra o
                    elo com uma anterior.
                    7º Nível - Magia Bélica
                    Quando usar uma Ação para conjurar um
                    truque, pode fazer um ataque com arma
                    com uma ação bônus.
                    10º Nível – Golpe Místico
                    Quando acertar um alvo com uma arma,
                    o alvo tem desvantagem no próximo teste
                    de resistência com uma magia que você
                    conjurar até o final do seu próximo turno.
                    15º Nível – Investida Arcana
                    Pode se teleportar até 9 metros em um
                    local não ocupado que possa ver, quando
                    usar um Pulso de ação. Pode se teleportar
                    antes ou depois da ação adicional.
                    18º Nível – Magia Bélica Aprimorada
                    Quando usar uma Ação para conjurar
                    uma magia, pode fazer um ataque com
                    arma com uma ação bônus.''')
        if self.classe == 'Ladino':
            sleep(0.4)
            print('-' * 20)
            self.pv = 8 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves; 
Armas simples, besta de mão, espada curta,
espada longa, rapieira; 
Ferramentas: Ferramentas de ladino;
Testes de Resistência: Destreza e Inteligência; 
Perícias: Escolha quatro entre Acrobacia, 
Atletismo, Atuação, Enganação,
Furtividade, Intimidação, Intuição, Percepção, Persuasão e
Prestidigitação.'''
            self.equipamento = '''
Equipamentos:
(a) Uma rapiera ou (b) uma espada longa;
(a) Um arco curto e aljava com 20 flechas
ou (b) uma espada curta;
(a) Pacote de assaltante ou (b) Pacote de
masmorra ou (c) pacote de exploração
Corselete de couro, duas adagas e as
ferramentas de ladino.'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Assassino ou [2]Ladrão ou '
                            '[3]Trapaceiro Arcano ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Assassino'
                    break
                elif esc == 2:
                    self.caminho = 'Ladrão'
                    break
                elif esc == 3:
                    self.caminho = 'Trapaceiro Arcano'
                    break
                elif esc == 0:
                    print('''
                        ASSASSINO
                    3º Nível – Proficiência Bônus e Assassinato
                    Ganha proficiência com kit de disfarce e kit
                    do envenenador.
                    Tem vantagem em ataques contra
                    criaturas que não tiveram seu turno no
                    combate ainda. Além disso, qualquer
                    acerto contra uma criatura surpresa é um
                    acerto crítico.
                    9º Nível – Especialista em Infiltração
                    Pode criar identidades falsas para você sem
                    chance de falha. Deve gastar 7 dias e 25 po
                    para estabelecer uma história, profissão e
                    afiliações para esta identidade. Não pode
                    usar uma identidade de outra pessoa. Por
                    exemplo, pode adquirir roupa apropriada,
                    cartas de recomendação e um certificado
                    claramente oficial para se estabelecer como
                    um membro de uma casa mercante de uma
                    cidade remota, para então se introduzir
                    sutilmente na companhia de outros
                    comerciantes ricos.
                    13º Nível – Impostor
                    Pode imitar sem erros o modo de falar de
                    outra pessoa, sua escrita e até seu
                    comportamento. Deve gastar 3 horas
                    estudando estes três comportamento da
                    pessoa, ouvindo-a falar, examinado seu
                    modo de escrever e observando seus
                    modismo e peculiaridades. Este ardil não é
                    discernível para o observador casual. Se
                    uma criatura cautelosa suspeita que algo
                    esta errado, você tem vantagem em
                    qualquer teste de Carisma (Enganação) que
                    fizer para evitar detecção.
                    17º Nível – Ataque Mortal
                    Quando acertar uma criatura surpresa, ela
                    faz um teste de resistência de Constituição
                    (CD 8 + seu mod de Destreza + seu bônus
                    de proficiência). Se falhar, ela sofre o dobro
                    de dano do seu ataque
                    
                        LADRÃO
                    3º Nível – Proficiência Bônus e
                    Assassinato
                    Pode usar a ação bônus concedida pela
                    Ação Astuta para fazer um teste de
                    Destreza (Prestidigitação) usando as
                    ferramentas de ladino para desarmar
                    armadilhas, abrir uma fechadura ou a ação
                    Usar Objeto.
                    Escalar não custa movimento adicional.
                    Além disso, quando fizer um salto longo,
                    o alcance que pode saltar aumentar um
                    numero de metros iguais a 1,5 vezes seu
                    mod de Destreza.
                    9º Nível – Furtividade Suprema
                    Tem vantagem no teste de Destreza
                    (Furtividade) se não se mover mais do que
                    a metade do seu deslocamento em um
                    turno.
                    13º Nível – Usar Dispositivo Mágico
                    Você pode ignorar todas as classes, raças e
                    níveis exigidos para o uso de qualquer
                    item mágico.
                    17º Nível – Reflexos de Ladrão
                    Você pode realizar dois turnos durante a
                    primeira rodada de qualquer combate.
                    Você realiza seu primeiro turno na sua
                    iniciativa e depois realiza o segundo na
                    ordem de sua iniciativa menos 10. Não
                    pode usar esta habilidade se estiver
                    surpreso
                    
                        TRAPACEIRO ARCANO
                    Magias Conhecidas: Aprende da lista de
                    Mago. Você aprende 3 truques: mãos
                    mágicas e mais dois truques a sua
                    escolha da lista de mago. No nível 10
                    aprende outro truque a sua escolha.
                    Começa com três magias de nível 1 à
                    sua escolha, mas 2 devem ser de
                    Encantamento ou Ilusão. As magias que
                    aprender devem ser também de
                    Encantamento ou Ilusão, exceto nos
                    níveis 8, 14 e 20. Quando ganhar um
                    nível nesta classe, pode trocar uma
                    magia conhecida por outra, mas deve ser
                    de Encantamento ou Ilusão, exceto se a
                    magia foi ganha nos níveis 8, 14 ou 20.
                    Recupera todos os espaços de magia com
                    um descanso longo.
                    Atributo de Conjuração: Inteligência é o
                    atributo de conjuração.
                    CD de resistência a magia = 8 + bônus
                    de proficiência + mod Inteligência.
                    Ataque com magia = bônus de
                    proficiência + mod Inteligência
                    3º Nível – Mãos Mágicas Trapaceiras
                    Quando conjurar mão mágicas, pode
                    criar uma mão espectral invisível que
                    pode fazer as seguintes tarefas:
                    • Pode guardar um objeto que a mão
                    esta segurando em um compartimento
                    vestido ou carregado por outra
                    criatura.
                    • Pode retirar um objeto de
                    compartimento vestido ou carregado
                    por outra criatura.
                    • Pode usar as ferramentas de ladrão
                    para abrir fechaduras e desarmar
                    armadilha à distância.
                    Pode fazer uma destas tarefas sem ser
                    notado por uma criatura se obter sucesso
                    em um teste de Destreza (Prestidigitação)
                    contra um teste de Sabedoria (Percepção)
                    da criatura.
                    Além disso, pode usar a ação bônus da
                    Ação Astuta para controlar a mão.
                    9º Nível – Emboscada Mágica
                    Se estiver escondido quando conjurar
                    uma magias em uma criatura, ela tem
                    desvantagem em qualquer teste de
                    resistência contra a magia neste turno.''')
        if self.classe == 'Mago':
            sleep(0.4)
            print('-' * 20)
            self.pv = 6 + self.mod_constituicao
            self.proficiencias += '''
Armaduras nenhuma; 
Armas adaga, besta leve, cajado,
dardo e funda; 
Ferramentas: Nenhuma; 
Testes de Resistência: Inteligência e Sabedoria; 
Perícias: Escolha duas de Arcanismo, 
História, Intuição, Investigação,
Medicina e Religião.'''
            self.equipamento = '''
Equipamentos:
Você começa com os seguintes
equipamentos, em adição ao equipamento
concedido pelo seu antecedente:
(a) Um cajado ou (b) uma adaga;
(a) Uma bolsa de componentes (b) um foco
arcano;
(a) Pacote do estudioso ou (b) um pacote
do explorador;
Um grimório'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de \n[1]Escola da Advinhação ou '
                            '[2]Escola da Abjuração ou [3]Escola da Conjuração ou [4]Escola de encantamento ou [5]'
                            'Escola de Evocação ou [6]Escola de Ilusão ou [7]Escola de Necromancia ou [8]Escola '
                            'de Transmutação ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Escola da Advinhação'
                    break
                elif esc == 2:
                    self.caminho = 'Escola da Abjuração'
                    break
                elif esc == 3:
                    self.caminho = 'Escola da Conjuração'
                    break
                elif esc == 4:
                    self.caminho = 'Escola de encantamento'
                    break
                elif esc == 5:
                    self.caminho = 'Escola de Evocação'
                    break
                elif esc == 6:
                    self.caminho = 'Escola de Ilusão'
                    break
                elif esc == 7:
                    self.caminho = 'Escola de Necromancia'
                    break
                elif esc == 8:
                    self.caminho = 'Escola de Transmutação'
                    break
                elif esc == 0:
                    print('''   ESCOLA DA ABJURAÇÃO
                    2º Nível –Erudita da Abjuração e Defesa
                    Arcana
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de abjuração em seu grimório é
                    reduzido pela metade.
                    Quando conjurar uma magia de 1º nível ou
                    maior pode criar uma defesa mágica em você
                    que permanece ativa até terminar um descanso
                    longo. Ela tem pontos de vida iguais a duas
                    vezes seu nível de mago + seu mod de
                    Inteligência. Quando você sofrer dano, a defesa
                    absorve o dano antes. Se ela for reduzida a 0,
                    você sofre o dano remanescente e ela não poderá
                    absorver mais dano. Toda vez que lançar uma
                    magia de abjuração de 1º nível ou superior, a
                    defesa arcana recupera pontos de vida iguais a
                    duas vezes o nível da magia. Não pode criá-la de
                    novamente até terminar um descanso longo.
                    6º Nível – Defesa Projetada
                    Quando criatura que você possa ver à 9 m sofrer
                    dano, pode usar sua reação para fazer sua
                    Defesa Arcana absorver o dano. Se a defesa for
                    reduzida a 0 pontos de vida a criatura sofre o
                    dano remanescente.
                    10º Nível – Abjuração Aprimorada
                    Quando conjurar magia de abjuração que exige
                    que você faça um teste de atributo (como a
                    contra mágica dissipar magia) você adiciona seu
                    bônus de proficiência ao teste de atributo.
                    14º Nível – Resistência à Magia
                    Você tem nos teste de resistência contra
                    magia. Possui também resistência contra dano
                    causados por magias
                    
                        ESCOLA DA ADVINHAÇÃO
                    2º Nível –Erudita da Adivinhação e Presságio
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de adivinhação em seu grimório
                    é reduzido pela metade.
                    Ao terminar um descanso longo, jogue dois
                    d20 e anote os resultados. Pode usar estes
                    valores para substituir qualquer ataque, teste de
                    resistência ou teste de atributo feito por você ou
                    outra criatura que possa ver. Deve fazer isso
                    antes da rolagem e só pode substituir uma ver
                    por turno. Cada jogada predita só pode ser
                    usada uma vez. Quando terminar um descanso
                    longo perder qualquer jogada não usada.
                    6º Nível – Adivinho Especialista
                    Quando conjurar uma magia de adivinhação de
                    2º nível ou maior usando um espaço de magia,
                    recuperar um espaço de magia gasto. Ele deve
                    ser de um espaço menor do que você lançou e
                    não pode ser maior que o 5º nível.
                    10º Nível – O Terceiro Olho
                    Usando uma ação pode aumentar seus poderes
                    de percepção. Escolha um dos seguintes
                    benefícios, que duram até você ficar
                    incapacitado, terminar um descanso curto ou
                    longo. Só pode usar uma vez por descanso.
                    Visão no Escuro: Ganha visão no escuro 18 m.
                    Visão Etérea: Pode ver o Plano Etéreo 18m.
                    Compreensão Maior: Pode ler qualquer idioma.
                    Ver o Invisível: Pode ver criaturas e objetos
                    invisíveis até 3 m de você, desde que esteja na
                    sua linha de visão.
                    14º Nível – Presságio Maior
                    Pode rolar três d20 usando a característica
                    Presságio, ao invés de dois.
                    
                        ESCOLA DE CONJURAÇÃO
                    2º Nível –Erudita da Conjuração e
                    Conjuração Menor
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de conjuração em seu grimório
                    é reduzido pela metade.
                    Pode usar sua ação para conjurar um objeto
                    inanimado na sua mão ou chão, em um espaço
                    desocupado que possa ver até 3 metros. O objeto
                    não pode ser maior que 90 centímetros de lado e
                    não pode pesar mais que 4,5 quilos. Deve ter a
                    forma de um objeto não-mágico que já tenha
                    visto. O objeto é visivelmente mágico e irradia
                    uma penumbra de 1,5 metros de alcance. O
                    objeto desaparece depois de 1 hora, quando usar
                    esta característica novamente ou se o objeto
                    levar qualquer dano.
                    6º Nível – Transposição Benigna
                    Pode usar sua ação para se teleportar até 9
                    metros para um espaço desocupado que possa
                    ver. Alternativamente, pode escolher um espaço
                    ao alcance que esteja ocupado por uma criatura
                    Pequena ou Média. Se ela não resistir, vocês
                    dois trocam de lugar. Pode usar uma vez por
                    descanso curto ou se lançar uma magia de
                    conjuração de 1º nível ou maior.
                    10º Nível – Conjuração Focalizada
                    Enquanto estiver se concentrando em uma
                    magia de conjuração, sua concentração não
                    pode ser encerrada se sofrer dano.
                    14º Nível – Invocação Resistente
                    Qualquer criatura que você invocar ou criar
                    com uma magia de conjuração, possuirá 30
                    pontos de vidas temporários.
                    
                        ESCOLA DE ENCANTAMENTO
                    2º Nível –Erudita do Encantamento e Olhar
                    Hipnótico
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de encantamento em seu
                    grimório é reduzido pela metade.
                    Com uma ação, escolha uma criatura que
                    possa ver até 1,5 m de você. Se o alvo puder te
                    ver e ouvir, deve passar em um teste de
                    resistência de Sabedoria contra sua CD de magia
                    ou fica encantado até o final do seu próximo
                    turno. A criatura reduz seu deslocamento para 0,
                    e ela fica incapacitada e visivelmente tonta.
                    Nos turnos subsequentes, pode usar sua ação
                    para manter este efeito estendendo-o a duração
                    até o final do seu próximo turno. Entretanto, o
                    efeito termina se você se mover mais que 1,5 m
                    longe dela, se ela não puder mais te ver ou ouvir,
                    ou se ela sofrer dano. Só pode usar uma vez por
                    descanso longo.
                    6º Nível – Fascinação Instintiva
                    Se uma criatura que você possa ver até 9 metros
                    te atacar, você pode suar sua reação para desviar
                    o ataque para outra criatura ao alcance do
                    atacante. O atacante deve fazer um teste de
                    resistência de Sabedoria contra sua CD de
                    magias. Se falhar, ele deve mirar na criatura
                    mais próxima dele, exceto você e ele mesmo. Se
                    houver múltiplas criaturas, o atacante escolhe
                    uma delas. Se passar, você não pode usar isso de
                    novo no mesmo atacante até terminar um
                    descanso longo. Você deve usar essa
                    característica antes de saber se o ataque acertou
                    ou não. Criaturas que não podem ser encantadas
                    são imunes a este efeito.
                    10º Nível –Dividir Encantamento
                    Quando conjurar uma magia de encantamento
                    de 1º nível ou maior cujo alvo seja somente uma
                    criatura, pode ter como alvo uma segunda
                    criatura.
                    14º Nível – Alterar Memórias
                    Ao conjurar uma magia de encantamento
                    para encantar uma ou mais criaturas, pode
                    alterar a compreensão dela para que não
                    perceba que está sendo encantada. Além
                    disso, antes de magia terminar, pode usar sua
                    ação para tentar fazer com que ela esqueça um
                    tempo que passou encantada. Ela deve passar
                    em um teste de resistência de Inteligência
                    contra sua CD de magias, ou perderá um
                    numero de horas de sua memória igual a 1 +
                    seu mod de Carisma (mínimo 1). Você pode
                    fazer ela esquecer um tempo menor e o
                    máximo de tempo não pode exceder a
                    duração da magia de encantamento.
                    
                        ESCOLA DE EVOCAÇÃO
                    2º Nível –Erudita da Evocação e Magias
                    Esculpidas
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de evocação em seu grimório é
                    reduzido pela metade.
                    Ao lançar uma magia de evocação que afeta
                    outras criaturas que possa ver, pode escolher um
                    número de criaturas igual a 1 + o nível da
                    magia. As criaturas escolhidas passam
                    automaticamente nos testes de resistência contra
                    magia lançada e não sofrem dano se fossem
                    sofre metade com um sucesso no teste de
                    resistência.
                    6º Nível – Truque Potente
                    Quando uma criatura passar no teste de
                    resistência de um truque seu, ela sofre metade do
                    dano (se houver), mas nenhum efeito adicional.
                    10º Nível – Evocação Potencializada
                    Pode adicionar seu mod de Inteligência no dano
                    de qualquer magia de evocação que conjurar.
                    14º Nível – Intensificação Poderosa
                    Quando lançar uma magia de 5º nível ou
                    menor que cause dano, ela causa dano
                    máximo. A primeira vez que fizer isso não
                    sofrerá nenhum efeito. Porém, se usar de novo
                    isso antes de terminar um descanso longo,
                    sofrerá 2d12 de dano necrótico para cada nível
                    da magia, imediatamente após lançá-la. Cada
                    vez que usar isso sem terminar um descanso
                    longo, o dano necrótico sofrido aumenta em
                    1d12 por nível. Este dano ignora qualquer
                    resistência ou imunidade.
                        ESCOLA DE ILUSÃO
                    2º Nível –Erudita da Ilusão e Ilusão Menor
                    Aprimorada
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de ilusão em seu grimório é
                    reduzido pela metade.
                    Você aprende o truque ilusão menor. Se já
                    conhecer, aprende outro truque à sua escolha.
                    Ele não conta para sua lista de truques
                    conhecidos. Quando conjurar a magia ilusão
                    menor, pode criar som e imagem com uma única
                    conjuração.
                    6º Nível – Ilusões Maleáveis
                    Quando conjurar uma magia de ilusão que
                    possui duração de 1 minuto ou mais, pode usar
                    sua ação para mudar a natureza desta ilusão
                    (usando os parâmetros normais da magia para a
                    ilusão), desde que possa ver a ilusão criada.
                    10º Nível –Ilusão Própria
                    Quando uma criatura acertar um ataque em
                    você, pode usar sua reação para criar uma
                    duplicata ilusória sua entre o atacante você. O
                    ataque falha automaticamente e então a ilusão
                    some. Só pode usar uma vez por descanso curto
                    ou longo.
                    14º Nível – Realidade Ilusória
                    Quando conjurar uma magia de ilusão de 1º
                    nível ou maior, pode escolher um objeto
                    inanimado e não mágico que faça parte da
                    ilusão e torna-lo real. Pode fazer isso com
                    uma ação bônus no seu turno, enquanto a
                    magia está ativa. O objeto fica real por 1
                    minuto. Por exemplo, pode criar a ilusão de
                    uma ponte sobre um abismo e torna-la real
                    tempo suficiente para seus aliados passarem
                    por ela. O objeto não pode causar dano ou
                    machucar alguém diretamente, de nenhuma
                    forma.
                    
                        ESCOLA DE NECROMANCIA
                    2º Nível –Erudita da Necromancia e Colheita
                    Macabra
                    O dinheiro e tempo gastos para copiar uma
                    magia da escola de necromancia em seu
                    grimório é reduzido pela metade.
                    Um vez por turno ao matar uma ou mais
                    criatura com uma magia de 1º nível ou maior,
                    você recupera pontos de vida igual a duas vezes
                    o nível da magia ou três vezes se a magia
                    pertencer a Escola da Necromancia. Não ganha
                    este benefício quando matar constructos ou
                    mortos-vivos.
                    6º Nível – Vassalos Mortos-Vivos
                    Adicione a magia animar os mortos, se não a
                    tiver. Quando conjurar a magia animar os mortos,
                    pode incluir um corpo ou pilha de ossos
                    adicional como alvo da magia, criando outro
                    zumbi ou esqueleto.
                    Sempre que criar um morto-vivo usando uma
                    magia de necromancia, ele terá os seguintes
                    benefícios:
                    • Os pontos de vida da criatura são
                    aumentados em um numero igual seu nível
                    de mago.
                    • A criatura adiciona o seu bônus de
                    proficiência nas jogadas de dano com armas.
                    10º Nível – Habituado aos Mortos-Vivos
                    Adquire resistência a dano necrótico e seus
                    pontos de vida máximos não podem ser
                    reduzidos.
                    14º Nível – Comandar Mortos-Vivos
                    Com uma ação, pode escolher um morto-vivo
                    que possa ver até 18 m. Ele faz um teste de
                    resistência de Carisma contra sua CD de
                    magias. Se passar, não pode usar essa
                    característica de novo. Se falhar, torna-se
                    amigável e obedece seus comandos até você
                    usar essa característica de novo.
                    Se o alvo possuir um valor de Inteligência de 8
                    ou mais, possui vantagem no teste de
                    resistência. Se falhar no teste e possuir
                    Inteligência igual a 12 ou mais, pode repetir o
                    teste de resistência no final de cada hora, até
                    passar no teste e ficar livre do seu controle.
                    
                        ESCOLA DE TRANSMUTAÇÃO
                    2º Nível –Erudita da Transmutação e Alquimia
                    Menor
                    O dinheiro e tempo gastos para copiar uma magia
                    da escola de transmutação em seu grimório é
                    reduzido pela metade.
                    Você executa um procedimento alquímico na
                    composição do objeto, podendo ser madeira, pedra
                    (não gemas), ferro, cobre ou prata. Transforma o
                    objeto em um destes materiais. A cada 10 minutos
                    gastos executando este procedimento, pode
                    transformar 30 centímetro cúbicos de material.
                    Após 1 hora ou até você perder sua concentração
                    (como se estivesse concentrando uma magia), o
                    material volta a ser a sua substancia original.
                    6º Nível – Pedra de Transmutação
                    Pode gastar 8 horas criando uma pedra e
                    transmutação. Você pode usá-la ou dá-la para outra
                    criatura. Ela ganha um benefício a sua escolha,
                    desde que esteja com a pedra. Quando criar a
                    pedra escolha um entre:
                    • Visão no escuro 18 m.
                    • Aumento de deslocamento em 3 m, enquanto
                    estiver desimpedido.
                    • Proficiência em testes de resistência de
                    Constituição.
                    • Resistência a dano de ácido, congelante, fogo,
                    eletricidade ou sônico (você escolhe).
                    Quando você lançar uma magia de 1º nível ou
                    maior, pode alterar o efeito da pedra se estiver em
                    sua posse. Se criar outra pedra, a anterior para de
                    funcionar.
                    10º Nível –Metamorfo
                    Adiciona a magia metamorfose, se não tiver. Pode
                    conjurar metamorfose sem gastar espaço de magia.
                    Quando o fizer, somente você ode ser o alvo e só
                    pode se transformar em uma besta de ND 1 ou
                    menor. Só pode usar desta forma uma vez por
                    descanso curto ou longo.
                    14º Nível – Transmutador Mestre
                    Pode quebra sua Pedra de Transmutação e
                    escolher entre (só pode se refeita quando você
                    terminar um descanso longo):
                    Transformação Maior: Pode transformar objeto
                    não-mágico – de até 1,5 m cúbicos – em outro
                    objeto não-mágico de tamanho e massa similar,
                    de mesmo valor ou inferior. Deve gastar 10
                    minutos segurando-o para isso
                    Panaceia: Remove todas as maldições, doenças e
                    venenos que afetam a criatura que você tocar. Ela
                    também recuperar todos seus pontos de vida.
                    Restaurar Vida: Pode conjurar reviver os mortos na
                    criatura que tocar com a pedra, sem gastar espaço
                    de magia e sem ter ela no se grimório.
                    Restaurar Juventude: Toca uma criatura com a
                    pedra e a idade aparente dela é reduzida em 3d10
                    anos, no mínimo 13 anos. Não estende o tempo
                    de vida da criatura.''')
        if self.classe == 'Monge':
            sleep(0.4)
            print('-' * 20)
            self.pv = 8 + self.mod_constituicao
            self.proficiencias += '''
Armaduras nenhuma; 
Armas simples e espada curta;
Ferramentas: Escolha entre ferramentas do artesão ou um
instrumento musical; 
Testes de Resistência: Força e Destreza; 
Perícias: Escolha duas entre Acrobacia,
Atletismo, História, Intuição, Religião e Furtividade'''
            self.equipamento = '''
 Equipamentos:
Você começa com os seguintes
equipamentos, em adição aos
equipamentos concedidos pelo seu
antecedente:
(a) Uma espada curta ou (b) qualquer arma
simples;
(a) Pacote de masmorra ou (b) pacote de
explorador;
10 dardos'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Caminho da Máo Aberta ou'
                            ' [2]Caminho das Sombras ou [3]Caminho dos Quatro Elementos ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Caminho da Máo Aberta'
                    break
                elif esc == 2:
                    self.caminho = 'Caminho das Sombras'
                    break
                elif esc == 3:
                    self.caminho = 'Caminho dos Quatro Elementos'
                    break
                elif esc == 0:
                    print('''CAMINHO DA MÃO ABERTA
                    3º Nível –Técnica da Mão Aberta
                    Sempre que atingir uma criatura com sua
                    Rajada de Golpes, pode impor um dos
                    seguintes efeitos:
                    • O alvo deve passar em um teste de
                    resistência de Destreza ou ficará derrubado.
                    • O alvo deve passar em um teste de
                    resistência de Força, se falhar você pode
                    empurrá-lo 5 metros de distância.
                    • O alo não pode realizar nenhuma reação
                    até o final do seu próximo turno.
                    6º Nível – Controle do Corpo
                    Com uma ação, pode recuperar pontos de
                    vida iguais a três vezes seu nível de monge. Só
                    pode fazer isso uma vez por descanso longo.
                    11º Nível – Tranquilidade
                    No final de um descanso longo, ganha o efeito
                    da magia santuário que dura até o inicio do seu
                    próximo descanso longo (a magia pode
                    terminar antes normalmente). A CD para o
                    teste de resistência é igual a 8 + mod de
                    Sabedoria + seu bônus de proficiência.
                    17º Nível – Mão Vibrante
                    Ao acertar uma criatura com um ataque
                    desarmado pode gastar 3 pontos de Ki
                    para desencadear vibrações
                    imperceptíveis, que duram por um numero
                    de dias iguais ao seu nível de monge. São
                    inofensivas até que você use uma ação
                    para finalizá-las. O alvo deve estar no
                    mesmo plano de existência. Ao realizar
                    essa ação, a criatura faz um teste de
                    resistência de Constituição. Se falhar, fica
                    com 0 pontos de vida. Se for bem
                    sucedida, leva 10d10 de dano necrótico.
                    Só pode ter um alvo sob efeito desta
                    característica por ver. Pode cancelar o
                    efeito dessas vibrações de modo inofensivo
                    sem gastar uma ação.
                    
                        CAMINHO DAS SOMBRAS
                    3º Nível –Artes das Sombras
                    Com uma ação, pode gastar 2 pontos de Ki
                    para conjurar escuridão, coroa da loucura, passos
                    sem pegadas ou silêncio, sem precisar de
                    componentes materiais. Além disso, ganha o
                    truque ilusão menor se não o tiver.
                    6º Nível – Passo das Sombras
                    Quando estiver sob penumbra ou escuridão,
                    pode com uma ação bônus para se teleportar a
                    até 18 m para um espaço vazio que possa ver e
                    também esteja na penumbra ou escuridão.
                    Ganha vantagem no primeiro ataque corpo a
                    corpo que fizer até o final do turno.
                    11º Nível – Manto das Sombras
                    Quando estiver sob penumbra ou escuridão,
                    pode com uma ação para ficar invisível.
                    Permanece invisível até que ataque, conjurar
                    uma magia ou fique em uma área iluminada.
                    17º Nível – Oportunista
                    Sempre que uma criatura até 1,5 m de
                    você for acertada por um ataque feito por
                    outra criatura que não você, pode usar sua
                    reação para fazer um ataque corpo a corpo
                    contra aquela criatura.
                    
                        CAMINHO DOS QUATRO
                        ELEMENTOS
                    3º Nível –Discípulo dos Elementos e
                    Disciplinas Elementais
                    Aprende disciplinas que requerem que você
                    gaste pontos de Ki quando for usá-la. Você
                    aprende Sintonia Elemental e uma outra
                    disciplina elemental a sua escolha. Não precisa
                    de componentes materiais. Pode gastar Ki
                    adicional para aumentar o nível da magia. O
                    nível da magia aumenta em 1 para cada ponto
                    de Ki adicional gasto. Exemplo: Se for um
                    monge de 5º nível e usar Varredura das Cinzas
                    para conjurar mãos flamejantes, pode gastar 3 de
                    Ki e conjurá-la como 2º nível (base 2 de Ki mais
                    1).
                    6º Nível – Nova Disciplina Elemental
                    Aprende uma nova disciplina elemental. Pode
                    substitui uma que já conhece por outra.
                    11º Nível – Nova Disciplina Elemental
                    Aprende uma nova disciplina elemental. Pode
                    substitui uma que já conhece por outra.
                    17º Nível – Nova Disciplina Elemental
                    Aprende uma nova disciplina elemental. Pode
                    substitui uma que já conhece por outra''')
        if self.classe == 'Paladino':
            sleep(0.4)
            print('-' * 20)
            self.pv = 10 + self.mod_constituicao
            self.proficiencias += '''
Armaduras leves, médias, pesadas e escudos; 
Armas simples e marciais; 
Ferramentas: Nenhuma; 
Testes de Resistência: Sabedoria e Carisma; 
Perícias: Escolha duas entre Atletismo, 
Intimidação, Medicina, Percepção,
Persuasão e Religião.'''
            self.equipamento = '''
 Equipamentos:
 Começa-se com o seguinte equipamento,
para além o equipamento concedido pelo
seu antecedente:
 (a) uma arma marcial e um escudo ou (b)
duas armas marciais.
 (a) cinco dardos ou (b) qualquer arma
branca simples.
 (a) Pacote de um sacerdote ou (b) a pacote
de explorador
 Cota de malha e um símbolo sagrado'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Juramento de Devoção ou'
                            ' [2]Juramento dos Anciões ou [3]Juramento da Vingança ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Juramento de Devoção'
                    break
                elif esc == 2:
                    self.caminho = 'Juramento dos Anciões'
                    break
                elif esc == 3:
                    self.caminho = 'Juramento da Vingança'
                    break
                elif esc == 0:
                    print('''   JURAMENTO DA DEVOÇÃO
                    Princípios da Devoção
                    Honestidade: Não mentir ou enganar.
                    Coragem: Nunca temer para agir, porém é
                    sábio ser cauteloso.
                    Compaixão: Ajudar os outros, proteger os
                    fracos e punir quem os ameaça. Mostrar
                    misericórdia aos inimigos, mas usando
                    de sabedoria.
                    Honra: Tratar os outros com justiça, fazer
                    o máximo de bem com o mínimo de
                    danos.
                    Dever: Ser responsável com suas ações e
                    suas consequências, proteger quem lhe
                    foi confiado e obedecer quem tem
                    autoridade sobre você.
                    Magias de Juramento
                    Ganha magias em níveis mostrado na
                    tabela. Elas sempre estão preparadas.
                    Não contam para o numero de magias
                    que você pode preparar por dia
                    3º Nível - Canalizar Divindade
                    Você ganha as duas seguintes opções de
                    Canalizar Divindade. Só pode usar uma
                    delas por descanso curto ou longo.
                    Arma Sagrada: Imbua uma arma com
                    energia sagrada. Por 1 minuto, adicione
                    seu mod de Carisma nas rolagens de
                    ataque com aquela arma (mínimo 1). Ela
                    também emite claridade de 6 m de raio e
                    penumbra 6 m após. Se a arma não for
                    mágica, se torna pela duração.
                    Pode terminar este efeito como parte de
                    outra ação. Se não estiver segurando a
                    arma ou ficar inconsciente, o efeito
                    encerra
                    Expulsar o Profano: Com uma ação,
                    mostre seu símbolo sagrado e cada
                    infernal ou morto-vivo que possa lhe ver
                    ou ouvir à 9 metros de você deve fazer
                    um teste de resistência de Sabedoria. Se
                    falhar, fica expulsado por 1 minuto ou
                    até levar dano. Uma criatura expulsada
                    deve gastar seus turno tentar se mover
                    para longe de você, e não pode entrar
                    voluntariamente em um espaço a 9
                    metros de você. Não pode fazer reações.
                    Em suas ações só pode usar a ação
                    Correr ou tentar escapar de um efeito que
                    impeça o movimento. Se não houver
                    local para se mover, a criatura usa a ação
                    Esquivar.
                    7º Nível - Aura da Devoção
                    Você e aliados dentro de 9 metros de você
                    não podem ser encantados enquanto você
                    estiver consciente. No 18º nível esta aura
                    aumenta para 18 metros.
                    15º Nível – Pureza de Espírito
                    Você sempre esta sob efeito da magia proteção
                    contra o bem e o mal.
                    20º Nível – Auréola Sagrada
                    Com uma ação, por 1 minuto luz brilhante
                    emana de você em um raio de 9 metros e luz
                    fraca emana por outros 9 metros. Sempre
                    que um inimigo iniciar seu turno na luz
                    brilhante, a criatura leva 10 de dano
                    radiante. Além disso, por esta duração você
                    tem vantagem no testes de resistência contra
                    magias conjuradas por infernais ou mortosvivos.
                    Só por usar uma vez por descanso
                    longo.
                    
                        JURAMENTO DOS ANCIÕES
                    Princípios dos Anciões
                    Acender a Luz: Através de atos de piedade,
                    bondade e perdão, acenda a luz de
                    esperança no mundo.
                    Abrigo da Luz: Onde houver bem, beleza,
                    amor e alegria no mundo, se imponha
                    contra a perversidade que tente o destruir.
                    Preserve sua Própria Luz: Encante-se com
                    musicas e risadas, na beleza e nas artes. Se
                    permitir a luz morrer no seu coração, não
                    poderá a preservar no mundo.
                    Seja a Luz: Se um farol glorioso para todos
                    que vivem em aflição. Deixa sua luz brilhar
                    em todas suas tarefas.
                    Magias de Juramento
                    Ganha magias em níveis mostrado na
                    tabela. Elas sempre estão preparadas. Não
                    contam para o numero de magias que você
                    pode preparar por dia
                    3º Nível - Canalizar Divindade
                    Você ganha as duas seguintes opções de
                    Canalizar Divindade. Só pode usar uma
                    delas por descanso curto ou longo.
                    Fúria da Natureza: Com uma ação, pode
                    fazer cipós espectrais surgirem e
                    alcançarem uma criatura até 9 metros que
                    você possa ver. Ela deve obter sucesso em
                    um teste de resistência de Força ou
                    Destreza (escolha dela) ou fica presa.
                    Enquanto presa pelos cipós, ela repte o
                    teste no fim de seus turnos, se soltando com
                    um sucesso e os cipós desaparecem.
                    Expulsar os Infiéis: Com uma ação, mostre
                    seu símbolo sagrado e cada feérico ou
                    infernal que possa lhe ouvir à 9 metros de
                    você deve fazer um teste de resistência de
                    Sabedoria. Se falhar, fica expulsado por 1
                    minuto ou até levar dano. Uma criatura
                    expulsada deve gastar seus turno tentar se
                    mover para longe de você, e não pode
                    entrar voluntariamente em um espaço a 9
                    metros de você. Não pode fazer reações.
                    Em suas ações só pode usar a ação Correr
                    ou tentar escapar de um efeito que impeça
                    o movimento. Se não houver local para se
                    mover, a criatura usa a ação Esquivar. Se a
                    verdadeira forma da criatura estiver oculta
                    por uma ilusão, metamorfose, ou outro
                    efeito, a forma é revelada enquanto estiver
                    expulsa.
                    7º Nível - Aura da Defesa
                    Você e aliados dentro de 9 metros de você
                    tem resistência contra dano de magias. No
                    18º nível esta aura aumenta para 18 metros.
                    15º Nível – Sentinela Imortal
                    Quando reduzido a 0 pontos de vida, mas
                    não for morto, você pode escolher ficar com
                    1 ponto de vida no lugar. Só por usar uma
                    vez por descanso longo.
                    20º Nível – Campeão Ancião
                    Assume a forma de uma antiga força da
                    natureza, você escolhe a aparência. Por
                    exemplo, a pele pode ficar verde ou uma
                    textura de casca de árvore, o cabelo virar
                    folhas ou musgo.
                    Usando sua ação, você entra na
                    transformação. Por 1 minuto ganha os
                    seguintes benefícios:
                    • No início do turno, recupera 10 PV
                    • Sempre que conjurar uma magia de
                    paladino que tenha tempo de conjuração
                    de 1 ação, pode conjurar com uma ação
                    bônus.
                    • Inimigos dentro de 9 metros de você tem
                    desvantagem em testes de resistência
                    contra suas magias de paladino e opções
                    de Canalizar Divindade.
                    Só por usar uma vez por descanso longo.
                    
                        JURAMENTO DA VINGAÇA
                    Princípios da Vingança
                    Combater o Mau Maior: Tendo de
                    escolher entre lutar contra meu inimigos
                    jurados ou males menores, escolho o
                    mau maior
                    Sem Misericórdia para os Ímpios: Inimigos
                    comuns podem ter minha piedade, mas
                    meus inimigos jurados não.
                    Por Qualquer Meio Necessário: Meus
                    escrúpulos não podem entra no caminho
                    de exterminar meus inimigos.
                    Reparação: Se meus inimigos causaram a
                    ruína do mundo, é porque não consegui
                    detê-los. Devo ajudar os afetados por
                    estes atos.
                    Magias de Juramento
                    Ganha magias em níveis mostrado na
                    tabela. Elas sempre estão preparadas.
                    Não contam para o numero de magias
                    que você pode preparar por dia
                    3º Nível - Canalizar Divindade
                    Você ganha as duas seguintes opções de
                    Canalizar Divindade. Só pode usar uma
                    delas por descanso curto ou longo.
                    Repudiar Inimigo: Com uma ação, mostre
                    seu símbolo sagrado e use Canalizar
                    Divindade. Escolha uma criatura até 18
                    metros que você possa ver. A criatura
                    deve fazer um teste de resistência de
                    Sabedoria, a menos que seja imune a ser
                    amedrontada. Infernais e mortos-vivos
                    tem desvantagem neste teste.
                    Se falhar, fica amedrontado por 1 minuto
                    ou até levar dano. Enquanto
                    amedrontada, seu deslocamento é 0 e
                    não pode se beneficiar de nenhum bônus
                    no deslocamento.
                    Em um teste bem sucedido, o
                    deslocamento da criatura cai pela metade
                    por 1 minuto ou até levar dano.
                    Voto de Hostilidade: Com uma ação
                    bônus, pode proferir um voto contra uma
                    criatura que possa ver até 9 metros. Você
                    ganha vantagem nas rolagens de ataque
                    contra a criatura por 1 minuto ou até ela
                    ficar com 0 pontos de vida ou ficar
                    inconsciente.
                    7º Nível – Vingador Implacável
                    Quando acertar uma criatura com um
                    ataque de oportunidade, pode se mover
                    metade do seu deslocamento logo após o
                    ataque e como parte da mesma reação. Esse
                    movimento não provoca ataque de
                    oportunidade.
                    15º Nível – Espírito da Vingança
                    Quando uma criatura sob o efeito do seu
                    Voto de Hostilidade fizer um ataque, você
                    pode usar sua reação para fazer um ataque
                    contra a criatura se ela estiver ao alcance.
                    20º Nível – Anjo Vingador
                    Assume a forma de um vingador angelical.
                    Usando sua ação, entra na transformação.
                    Por 1 hora, ganha os seguintes benefícios:
                    • Asas saem das suas costas e lhe dão
                    deslocamento de voo 18 metros.
                    • Você emana uma aura de ameaça em um
                    raio de 18 metros. A primeira vez que
                    um inimigo entrar na aura ou começar
                    seu turno dentro dela durante a batalha,
                    a criatura deve obter sucesso em um teste
                    de resistência de Sabedoria ou fica
                    amedrontada por 1 minuto ou até levar
                    dano. Rolagens de ataque contra a
                    criatura amedrontada tem vantagem.
                    Só por usar uma vez por descanso longo.''')
        if self.classe == 'Ranger':
            sleep(0.4)
            print('-' * 20)
            self.pv = 10 + self.mod_constituicao
            self.proficiencias += '''
 Armaduras leves, médias e escudos; 
 Armas simples e marciais; 
 Ferramentas: Nenhuma; 
 Testes de Resistência: Força e Destreza; 
 Perícias: Escolha três entre Adestrar
Animais, Atletismo, Furtividade, Intimidação, Intuição,
Natureza, Percepção e Sobrevivência.'''
            self.equipamento = '''
Equipamentos:
 Você começa com os seguintes
equipamentos, em adição aos
equipamentos concedidos pelo seu
antecedente:
 (a) brunea ou (b) corselete de couro
 (a) duas espadas curtas ou (b) duas armas
corpo a corpo simples
 (a) um pacote de masmorra ou (b) um
pacote de exploração
 Um arco longo e uma aljava com 20
flechas'''
            while True:
                esc = input('Com a classe escolhida voce pode escolher o caminho de [1]Caçador ou [2]Mestre das'
                            ' Feras ou [0]Para uma descrição')
                if esc.isnumeric():
                    esc = int(esc)
                else:
                    print('Valor invalido!!!')
                    continue
                if esc == 1:
                    self.caminho = 'Caçador'
                    break
                elif esc == 2:
                    self.caminho = 'Mestre das Feras'
                    break
                elif esc == 0:
                    print('''CAÇADOR
                    3º Nível – Presa do Caçador
                    Escolha um entre:
                    Matador de Colossos: Ao acertar uma criatura
                    com uma arma, ela leva 1d8 de dano extra se
                    estiver abaixo de seus pontos de vida
                    máximos. Só pode causar este dano extra uma
                    vez por turno.
                    Assassino de Gigantes: Quando uma criatura
                    Grande ou maior até 1,5 m de você lhe acertar
                    ou errar um ataque, pode usar sua reação para
                    atacar aquela criatura imediatamente após seu
                    ataque, desde que possa ver a criatura.
                    Destruidor de Horda: Um vez por turno,
                    quando fizer um ataque, pode fazer outro com
                    a mesma arma contra uma criatura diferente
                    que esteja a 1,5 m do alvo original e dentro do
                    alcance da sua arma.
                    7º Nível – Táticas Defensivas
                    Escolha um entre:
                    Escapar da Horda: Ataques de oportunidade
                    contra você são feitos com desvantagem.
                    Defesa contra Ataques Múltiplos: Quando
                    uma criatura acertar você com um ataque,
                    você ganha +4 na CA contra todos os
                    ataques subsequentes feitos por aquela
                    criatura pelo resto do turno.
                    Vontade de Aço: Você tem vantagem em
                    testes de resistência contra ser amedrontado.
                    11º Nível – Ataque Múltiplo
                    Escolha um entre:
                    Rajada: Com uma ação, faz um ataque à
                    distância contra quaisquer número de
                    criaturas dentro de 3 metros de um ponto
                    que possa ver dentro do alcance da sua
                    arma. Deve ter munição para cada alvo e faz
                    uma rolagem de ataque separada para cada
                    um dos alvos.
                    Ataque Redemoinho: Pode usar sua ação
                    para fazer um ataque corpo a corpo contra
                    qualquer numero de criaturas à 1,5 de você,
                    com uma rolagem de ataque separada para
                    cada um dos alvos.
                    15º Nível – Defesa Superior do Caçador
                    Escolha um entre:
                    Evasão: Quando fizer um teste de resistência
                    de Destreza para tomar metade do dano, ao
                    invés disso não toma dano se passar no teste
                    e somente metade se falhar.
                    Ficar Contra a Maré: Quando um inimigo
                    errar um ataque corpo a corpo contra você,
                    você pode usar sua reação para forçar aquela
                    criatura a repetir o mesmo ataque contra
                    outro alvo (que não seja ela mesma) à sua
                    escolha.
                    Esquiva Sobrenatural: Quando um inimigo
                    lhe acertar com um ataque, pode usar sua
                    reação para reduzir pela metade o dano.
                    
                        MESTRE DAS FERAS
                    3
                    º Nível
                    – Companheiro do Ranger
                    Você ganha uma besta companheira
                    .
                    Escolha uma que não seja maior do que
                    Médio
                    e tenha nível de desafio de
                    ¼ ou
                    menos
                    . Adicione
                    o seu bônus de proficiência
                    na CA da besta, rolagens de ataque
                    e dano,
                    bem como em quaisquer testes de resistência e perícias que ela seja proficiente. Os pontos
                    de vida máximos dela são iguais
                    a seu
                    máximo normal ou quatro vezes
                    o seu nível
                    de ranger,
                    o que for maior
                    .
                    A besta obedece seus comandos da melhor
                    forma que puder
                    . Tem seus turnos na ordem
                    de iniciativa do ranger
                    . No seu turno, você
                    pode verbalmente comandar
                    a besta para se
                    mover, ser gastar ação
                    . Pode usar sua ação
                    para verbalmente comandar ela para usar
                    a
                    ação de Atacar, Investir, Desengajar,
                    Esquivar, ou Ajudar
                    . Quando tiver
                    a
                    característica de Ataque Extra, pode fazer
                    um ataque quando comandar
                    a besta
                    à fazer
                    uma ação de Ataque
                    .
                    Quando viajando pelo seu terreno favorito
                    somente com
                    a besta, pode se mover
                    furtivamente com deslocamento normal
                    .
                    Se
                    a besta morrer, pode obter outra ao gastar
                    8 horas se conectando magicamente com
                    outra besta que não seja hostil
                    a você, sendo
                    do mesmo tipo da besta anterior ou um
                    diferente
                    .
                    7
                    º Nível
                    – Treinamento Excepcional
                    No seu turno, quando
                    a besta companheira
                    não atacar, pode gastar uma ação bônus
                    para mandar ela fazer uma ação de Investir,
                    Desengajar, Esquivar ou Ajudar neste turno
                    .
                    11
                    º Nível
                    – Fúria Bestial
                    Sua besta companheira pode fazer dois
                    ataques quando você
                    a comanda para usar
                    a
                    ação de Ataque
                    .
                    15
                    º Nível
                    – Compartilhar Magia
                    Quando você conjurar uma magia eu tenha
                    você como alvo, pode afetar sua besta
                    companheira com
                    a magia também se ela
                    estiver
                    a até
                    9 metros de você''')

    def modificadores(self):
        self.mod_forca = int((self.atrib_forca - 10) / 2)
        self.mod_destreza = int((self.atrib_destreza - 10) / 2)
        self.mod_constituicao = int((self.atrib_constituicao - 10) / 2)
        self.mod_inteligencia = int((self.atrib_inteligencia - 10) / 2)
        self.mod_sabedoria = int((self.atrib_sabedoria - 10) / 2)
        self.mod_carisma = int((self.atrib_carisma - 10) / 2)


def main():
    personagem = Personagem()
    personagem.raca_esc()
    personagem.classe_esc()
    personagem.atributos()
    personagem.ajuste_r()
    personagem.modificadores()
    personagem.ajuste_c()
    personagem.sub_raca_esc()
    personagem.modificadores()
    personagem.Ca()
    ficha = open('Ficha.txt', 'w')
    ficha.write('Classe = {} | Caminho  = {}\n'.format(personagem.classe, personagem.caminho))
    ficha.write('Raça   = {} | Sub-Raça = {}\n'.format(personagem.raca, personagem.sub_raca))
    ficha.write('\n\nAtributos:\nForça        = {}({})\nDestreza     = {}({})\nConstituição = {}({})\nInteligencia ='
                ' {}({})\nSabedoria    = {}({})\nCarisma      = {}({})\n'.format(personagem.atrib_forca,
                                                                                 personagem.mod_forca,
                                                                                 personagem.atrib_destreza,
                                                                                 personagem.mod_destreza,
                                                                                 personagem.atrib_constituicao,
                                                                                 personagem.mod_constituicao,
                                                                                 personagem.atrib_inteligencia,
                                                                                 personagem.mod_inteligencia,
                                                                                 personagem.atrib_sabedoria,
                                                                                 personagem.mod_sabedoria,
                                                                                 personagem.atrib_carisma,
                                                                                 personagem.mod_carisma))
    ficha.write('\n\nCA = {}\nPV = {}\nDeslocamento'
                ' = {}\n'.format(personagem.ca, personagem.pv, personagem.deslocamento))
    ficha.write('\n{}\n'.format(personagem.equipamento))
    ficha.write('\n\nIdiomas: {}\n'.format(personagem.idiomas))
    ficha.write('\n\nProficiencias:\n{}\n'.format(personagem.proficiencias))
    ficha.write('\n\nExtras:\n{}\n {}'.format(personagem.extras_r, personagem.extras_sr))
    ficha.close()


main()

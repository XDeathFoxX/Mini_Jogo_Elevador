# Crie uma classe denomidada Elevador para armazenar as informações de um elevador,
# dentro de um prédio.A Classe deve armazenar o andar atual (térreo=0),total de 
# andares no prédio ,excluindo o térreo,capacidade do elevador,e quantas pessoas
# estão presentes nele.
"""
A Classe também deve disponibilizar os seguintes métodos:
inicializa:que deve receber como parâmetros a capacidade do elevador e o total de 
andares no prédio(os elevadores começam no térreo e vazio)

entra:para acrescentar uma pessoa no elevador(só deve acrescentar se tiver espaço)

sai:para remover uma pessoa do elevador(só deve remover se tiver alguém dentro)

sobe:para subir um andar(não deve subir se já estiver no último andar)

desce:para descer um andar(não deve descer se estiver no térreo)

encapsular todos os atributos da classe
"""
from xml.sax.handler import property_interning_dict


acao=''
class Elevador:
    elevador = 0
    def __init__(self,andarat,andares,capacidade,pessoas):
        self.__andarat = andarat
        self.__andares = andares
        self.__capacidade = capacidade
        self.__pessoas = pessoas
    
    @property
    def capacidade(self):
        return self.__capacidade
    
    
    def inicializa(self):
        return f'O elevador tem {self.capacidade} de capacidade e o prédio tem {self.__andares} andares'

    def entra(self):
        if self.__pessoas < self.capacidade:
            self.__pessoas = self.__pessoas+1
            print('Passageiro entrando...')
            print(f'Temos {self.__pessoas} passageiro(s) no elevador')
        else:
            print('Não é possível entrar mais passageiros')
    
    def sai(self):
        if self.__pessoas >= 1:
            self.__pessoas = self.__pessoas-1
            print('Passageiro saindo...')
            print(f'Temos {self.__pessoas} passageiro(s) no elevador')
        else:
            print('Não tem passageiro(s) para sair')

    def subir(self):
        if self.__andarat < self.__andares:
            self.__andarat = self.__andarat+1
            print('Subindo de andar...')
            print(f'Agora estamos no andar {self.__andarat}')
        else:
            print('Não é possível subir mais,estamos no último andar!')

    def desce(self):
        if self.__andarat <= 0:
            print('Não é possível descer mais,já estamos no térro!')
        else:
            self.__andarat = self.__andarat-1
            print('Descendo de andar...')
            if self.__andarat == 0:
                print('Agora estamos no térro')
            else:    
                print(f'Agora estamos no andar {self.__andarat}')
    
    def terreo(self):
        if self.__andarat > 0:
            while self.__andarat > 0:
                self.__andarat = self.__andarat - 1
                if self.__andarat == 0:
                    print('Estamos no térreo...')
        else:
            print('Não é possível descer mais,já estamos no térreo!')

    def cobertura(self):
        if self.__andarat < self.__andares:
            while self.__andarat < self.__andares:
                self.__andarat = self.__andarat + 1
                if self.__andarat == self.__andares:
                    print('Estamos na cobertura...')
        else:
            print('Não é possível subir mais,já estamos na cobertura! ')

elevador1=Elevador(0,8,6,0)
print(elevador1.inicializa())

while acao != 'fechar':
    acoes='entra','sai','subir','descer','fechar','terreo','cobertura'
    acao = input('Digite uma ação (Entra, Sai, Subir, Descer, Fechar, Terreo, Cobertura): ').lower().strip()
    if acao == 'entra':
        elevador1.entra()
    elif acao == 'sai':
        elevador1.sai()
    elif acao == 'subir':
        elevador1.subir()
    elif acao == 'descer':
        elevador1.desce()
    elif acao == 'terreo':
        elevador1.terreo()
    elif acao == 'cobertura':
        elevador1.cobertura()
    elif acao == 'fechar':
        exit()
    elif acao not in acoes:
        while acao not in acoes:
            print('Ação inválida,digite uma ação entre ("Entra, Sai, Subir, Descer, Terreo, Cobertura, Fechar")')
            acao = input('Digite uma ação: ').lower().strip()
        else:
            if acao =='entra':
                elevador1.entra()
            elif acao == 'sai':
                elevador1.sai()
            elif acao == 'subir':
                elevador1.subir()
            elif acao == 'descer':
                elevador1.desce()


class Plano_cartesiano():
    
   """ Resposta: que coincidencia professor, foi exatamente o que eu fiz hehe :D"""

    contador = 0

    def __init__(self):
        self.formas = {}

    def inserir_forma(self, forma: object):

        Plano_cartesiano.contador += 1
        self.formas[f"{forma.get_type}{forma.n}"] = forma

    def remover_forma(self, forma):

        del self.formas[f"{forma.get_type}{forma.n}"]

    def mostrar_formas(self):

        print('\nEste plano cartesiano possui as seguintes formas:\n')
        for n, forma in enumerate(self.formas.keys()):
            print(f"{self.formas[forma]}", end=", " if n > Plano_cartesiano.contador else "\n")

    def print_detalhe(self):

        for key in self.formas.keys():
            print(f"{key}: {self.formas[key].atributos()}\n")

    def get_forma(self, key):
        print(key, self.formas[key].atributos())
        return self.formas[key]

    #foram feitos os devidos testes

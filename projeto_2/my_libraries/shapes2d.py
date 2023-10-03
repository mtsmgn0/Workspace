from math import sqrt, pi


class Ponto:
    contador = 0

    def __init__(self, x, y):

        Ponto.contador += 1
        self.n = Ponto.contador
        self.x = x
        self.y = y

    def quadrante(self):

        if self.x == 0 and self.y == 0:
            return "Origem"
        elif self.x == 0 or self.y == 0:
            return "Eixo"
        elif self.y > 0:
            return "Primeiro quadrante" if self.x > 0 else "Segundo quadrante"
        else:
            return "Terceiro quadrante" if self.x < 0 else "Quarto quadrante"

    def get_type(self):
        return "Ponto"


class Reta:

    contador = 0

    def __init__(self, ponto1: Ponto, ponto2: Ponto):

        Reta.contador += 1 * self.verificar(ponto1, ponto2)
        self.ponto1 = ponto1 if self.verificar(ponto1, ponto2) else None
        self.ponto2 = ponto2 if self.verificar(ponto1, ponto2) else None
        self.n = Reta.contador if self.verificar(ponto1, ponto2) else None

        print("Inisira dois pontos validos" * (not self.verificar(ponto1, ponto2)))

    def coeficiente_angular(self):
        # Se x1 e x2 são iguais, a reta é vertical e o coeficiente angular é indefinido
        if self.ponto1.x != self.ponto2.x:
            return (self.ponto1.y - self.ponto2.y) / (self.ponto1.x - self.ponto2.x)
        else:
            return None

    def comprimento(self):
        # Calcula o comprimento da linha usando o teorema de Pitágoras
        comprimento = sqrt((self.ponto1.y - self.ponto2.y) ** 2 + (self.ponto1.x - self.ponto2.x) ** 2)
        return comprimento

    def verificar_ponto_reta(self, ponto):

        # verifica se o ponto dado esta na classe ponto
        if not isinstance(ponto, Ponto):
            return None

        # Verifica se o ponto está na reta
        if self.ponto1.x == self.ponto2.x:
            return ponto.x == self.ponto1.x
        else:
            equacao_reta = self.ponto1.y + self.coeficiente_angular() * (ponto.x - self.ponto1.x)
            return ponto.y == equacao_reta

    def encontrar_centro(self):
        # Calculando as coordenadas x e y do centro
        centro_x = (self.ponto1.x + self.ponto2.x) / 2
        centro_y = (self.ponto1.y + self.ponto2.y) / 2

        # Criando um novo ponto para representar o centro
        centro = Ponto(centro_x, centro_y)

        return centro

    def verificar(self, ponto1, ponto2):
        return isinstance(ponto1, Ponto) and isinstance(ponto2, Ponto) and not (ponto1.x == ponto2.x and ponto1.y == ponto2.y)

    def get_type(self):
        return "Reta"


class Triangulo:
    contador = 0

    def __init__(self, base: Reta, topo: Ponto):

        self.base = base if isinstance(base, Reta) else None
        self.topo = topo if isinstance(topo, Ponto) else None
        self.lados_ordenados()
        Triangulo.contador += 1 * self.validar_triangulo()
        self.n = Triangulo.contador if self.validar_triangulo() else None
        print("O triangulo não existe" * (self.n is None))

    def validar_triangulo(self):

        if self.base is None or self.topo is None or self.base.verificar_ponto_reta(self.topo):
            self.base = None
            self.topo = None
            return False
        return True

    def calcular_area_triangulo(self):
        if not self.validar_triangulo():
            return "O triângulo não existe"

        lados = self.lados_ordenados()
        a, b, c = lados[0], lados[1], lados[2]
        p = (a + b + c) / 2

        return sqrt(p * (p - a) * (p - b) * (p - c))

    def calcular_altura(self):
        area = self.calcular_area_triangulo()
        altura = (2 * area) / self.base.comprimento()
        return altura

    def lados_ordenados(self):

        lados = [self.base.comprimento()]
        self.lado1 = Reta(self.topo, self.base.ponto1)
        self.lado2 = Reta(self.topo, self.base.ponto2)

        lados.append(self.lado1.comprimento())
        lados.append(self.lado2.comprimento())

        return sorted(lados)

    def is_retangulo(self):
        lados_ordenados = self.lados_ordenados()
        return lados_ordenados[0] ** 2 + lados_ordenados[1] ** 2 == lados_ordenados[2] ** 2

    def get_type(self):
        return "Triangulo"


class Quadrilatero:

    contador = 0

    def __init__(self, base: Reta, altura):
        self.base = base if isinstance(base, Reta) else None
        self.altura = altura
        Quadrilatero.contador += 1 * (self.base is not None)
        self.n = Quadrilatero.contador if self.base is not None else None
        print("Selecione uma reta para ser a base" * (self.base is None))

    def area_quadrilatero(self):
        return self.base.comprimento() * self.altura

    def is_quadrado(self):
        return self.base.comprimento() == self.altura

    def ponto_dentro_quadrilatero(self, ponto):
        if isinstance(ponto, Ponto):
            return True if self.base.ponto1.x < ponto.x < self.base.ponto2.x and self.base.ponto1.y < ponto.y < self.base.ponto1.y + self.altura else False

    def get_type(self):
        return "Quadrilatero"


class Circulo:

    contador = 0

    def __init__(self, centro: Ponto, raio):
        self.centro = centro if isinstance(centro, Ponto) else None
        self.raio = raio
        Circulo.contador += 1 * (self.centro is not None)
        self.n = Circulo.contador if self.centro is not None else None
        print("Selecione um Ponto para ser o centro" * (self.centro is None))
        self.circunferencia = self.calcular_circunferencia()
        self.area = self.area_do_circulo()



    def calcular_circunferencia(self):
        return 2 * pi * self.raio

    def ponto_na_circunferencia(self, ponto: Ponto):

        if ponto.x == self.centro.x and ponto.y == self.centro.y:
            return "O ponto é o centro da circunferência"

        linha = Reta(ponto, self.centro)
        if linha.comprimento() == self.raio:
            return "O ponto faz parte da circunferência"
        elif linha.comprimento() > self.raio:
            return "O ponto está fora da circunferência"
        else:
            return "O ponto está dentro da circunferência"

    def area_do_circulo(self):
        return pi * (self.raio ** 2)

    def get_type(self):
        return "Circulo"



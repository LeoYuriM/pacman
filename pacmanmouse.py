import pygame

pygame.init()

screen = pygame.display.set_mode((800,600), 0)

AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0, 0, 255)
VELOCIDADE = 1

class Cenario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [
            [2, 2, 2, 2, 2],
            [2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2],
            [2, 2, 2, 2, 2],
        ]


    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            pygame.draw.rect(tela, AZUL, (x, y, self.tamanho, self.tamanho), 0)

    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)

class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho // 2

    def calcular_regras(self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)



    def pintar(self, tela):
            # desenhar o corpo do pacman
            pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

            # Desenho da boca do Pacman
            canto_boca = (self.centro_x, self.centro_y)
            labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
            labio_inferior = (self.centro_x + self.raio, self.centro_y)
            pontos = [canto_boca, labio_superior, labio_inferior]

            pygame.draw.polygon(tela, PRETO, pontos, 0)

            # Desenho do olho do Pacman

            olho_x = int(self.centro_x + self.raio / 4)
            olho_y = int(self.centro_y - self.raio * 0.7)
            olho_raio = int(self.raio / 10)

            pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif event.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE
                elif event.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                elif event.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif event.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif event.key == pygame.K_UP:
                    self.vel_y = 0
                elif event.key == pygame.K_DOWN:
                    self.vel_y = 0

    def processar_eventos_mouse(self, eventos):
        delay = 100
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) // delay
                self.linha = (mouse_y - self.centro_y) // delay


if __name__ == '__main__':
    pac = Pacman()
    cenario = Cenario(600 // 30)
    while True:
        # Calcular as regras
        pac.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pac.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Captura os eventos
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                exit()
        pac.processar_eventos_mouse(eventos)
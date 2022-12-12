

import pygame

def afficher_sudoku(grille):
    pygame.init()
    taille_case = 50
    écran = pygame.display.set_mode((taille_case * 9, taille_case * 9))
    fond = pygame.Surface(écran.get_size())
    fond = fond.convert()
    fond.fill((250, 250, 250))

    # Dessine les lignes
    for x in range(0, taille_case * 9, taille_case):  # Lignes horizontales
        pygame.draw.line(fond, (0,0,0), (x,0), (x,taille_case * 9))
    for y in range(0, taille_case * 9, taille_case):  # Lignes verticales
        pygame.draw.line(fond, (0,0,0), (0,y), (taille_case * 9, y))

    # Dessine les blocs
    for x in range(0, taille_case * 9, taille_case * 3):
        for y in range(0, taille_case * 9, taille_case * 3):
            pygame.draw.rect(fond, (0, 0, 0), (x, y, taille_case * 3, taille_case * 3), 2)

    écran.blit(fond, (0, 0))

    # Affiche les chiffres
    font = pygame.font.Font(None, 40)
    for y, ligne in enumerate(grille):
        for x, chiffre in enumerate(ligne):
            if chiffre != 0:
                text = font.render(str(chiffre), 1, (0, 0, 0))
                écran.blit(text, (x * taille_case + 15, y * taille_case + 15))

    pygame.display.flip()

# Boucle de jeu
grille = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

afficher_sudoku(grille)

# Boucle d'événements
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((700, 700))

pygame.mixer.init()
air = "F:\!Python\cosmomedley\Medley-Air.ogg"
charango = "F:\!Python\cosmomedley\Medley-Charango.ogg"
drums = "F:\!Python\cosmomedley\Medley-Drums.ogg"
flute = "F:\!Python\cosmomedley\Medley-Flute.ogg"
horn = "F:\!Python\cosmomedley\Medley-Horn.ogg"


pygame.mixer.Channel(0).set_volume(0)
pygame.mixer.Channel(1).set_volume(0)
pygame.mixer.Channel(2).set_volume(0)
pygame.mixer.Channel(3).set_volume(0)
pygame.mixer.Channel(4).set_volume(0)

pygame.mixer.Channel(3).play(pygame.mixer.Sound(flute), -1)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(air), -1)
pygame.mixer.Channel(1).play(pygame.mixer.Sound(charango), -1)
pygame.mixer.Channel(2).play(pygame.mixer.Sound(drums), -1)
pygame.mixer.Channel(4).play(pygame.mixer.Sound(horn), -1)

def button(screen, position, text, size, colors="white on blue"):
    fg, bg = colors.split(" on ")
    font = pygame.font.SysFont("Times New Roman", size)
    text_render = font.render(text, 1, fg)
    x, y, w , h = text_render.get_rect()
    x, y = position
    
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg, (x, y, w , h))
    print(screen.blit(text_render, (x, y)))
    return screen.blit(text_render, (x, y)) 
 
def play_air():
    pygame.mixer.Channel(0).set_volume(0.5)

def play_charingo():
    pygame.mixer.Channel(1).set_volume(0.5)

def play_drums():
    pygame.mixer.Channel(2).set_volume(0.5)

def play_flute():
    pygame.mixer.Channel(3).set_volume(0.5)

def play_horn():
    pygame.mixer.Channel(4).set_volume(0.5)

def stop_air():
    pygame.mixer.Channel(0).set_volume(0)

def stop_charingo():
    pygame.mixer.Channel(1).set_volume(0)

def stop_drums():
    pygame.mixer.Channel(2).set_volume(0)

def stop_flute():
    pygame.mixer.Channel(3).set_volume(0)

def stop_horn():
    pygame.mixer.Channel(4).set_volume(0)

def menu():
    # b0 contains the rect coordinates of the button
    b0 = button(screen, (10, 10), "Here comes the buttons", 55, "white on blue")
    quit_b = button(screen, (300, 300), "Quit", 50, "white on blue")
    air_b_on = button(screen, (100, 100), "Air", 50, "white on blue")
    charango_b_on = button(screen, (100, 200), "Charango", 50, "white on blue")
    drums_b_on = button(screen, (200, 100), "Drums", 50, "white on blue")
    flute_b_on = button(screen, (400, 200), "Flute", 50, "white on blue")
    horn_b_on = button(screen, (400, 100), "Horn", 50, "white on blue")
    air_b_off = button(screen, (700, 700), "Air", 50, "white on blue")
    charango_b_off = button(screen, (700, 700), "Charango", 50, "white on blue")
    drums_b_off = button(screen, (700, 700), "Drums", 50, "white on blue")
    flute_b_off = button(screen, (700, 700), "Flute", 50, "white on blue")
    horn_b_off = button(screen, (700, 700), "Horn", 50, "white on blue")

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check when you click if the coordinates of the pointer are in the rectangle of the buttons
                if quit_b.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
# Start section
                elif air_b_on.collidepoint(pygame.mouse.get_pos()):
                    play_air()
                    air_b_on = button(screen, (700, 700), "Air", 50, "white on blue")
                    air_b_off = button(screen, (100, 100), "Air", 50, "blue on white")
                elif air_b_off.collidepoint(pygame.mouse.get_pos()):
                    stop_air()
                    air_b_on = button(screen, (100, 100), "Air", 50, "white on blue")
                    air_b_off = button(screen, (700, 700), "Air", 50, "white on blue")
                elif charango_b_on.collidepoint(pygame.mouse.get_pos()):
                    play_charingo()
                    charango_b_on = button(screen, (700, 700), "Charango", 50, "white on blue")
                    charango_b_off = button(screen, (100, 200), "Charango", 50, "blue on white")
                elif charango_b_off.collidepoint(pygame.mouse.get_pos()):
                    stop_charingo()
                    charango_b_on = button(screen, (100, 200), "Charango", 50, "white on blue")
                    charango_b_off = button(screen, (700, 700), "Charango", 50, "white on blue")
                elif drums_b_on.collidepoint(pygame.mouse.get_pos()):
                    play_drums()
                    drums_b_on = button(screen, (700, 700), "Drums", 50, "white on blue")
                    drums_b_off = button(screen, (200, 100), "Drums", 50, "blue on white")
                elif drums_b_off.collidepoint(pygame.mouse.get_pos()):
                    stop_drums()
                    drums_b_on = button(screen, (200, 100), "Drums", 50, "white on blue")
                    drums_b_off = button(screen, (700, 700), "Drums", 50, "white on blue")
                elif flute_b_on.collidepoint(pygame.mouse.get_pos()):
                    play_flute()
                    flute_b_on = button(screen, (700, 700), "Flute", 50, "white on blue")
                    flute_b_off = button(screen, (400, 200), "Flute", 50, "blue on white")
                elif flute_b_off.collidepoint(pygame.mouse.get_pos()):
                    stop_flute()
                    flute_b_on = button(screen, (400, 200), "Flute", 50, "white on blue")
                    flute_b_off = button(screen, (700, 700), "Flute", 50, "white on blue")
                elif horn_b_on.collidepoint(pygame.mouse.get_pos()):
                    play_horn()
                    horn_b_on = button(screen, (700, 700), "Horn", 50, "white on blue")
                    horn_b_off = button(screen, (400, 100), "Horn", 50, "blue on white")
                elif horn_b_off.collidepoint(pygame.mouse.get_pos()):
                    stop_horn()
                    horn_b_on = button(screen, (400, 100), "Horn", 50, "white on blue")
                    horn_b_off = button(screen, (700, 700), "Horn", 50, "white on blue")
        pygame.display.update()
    pygame.quit()
 
menu()

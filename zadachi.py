import pygame
import math

def main():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((800, 800), 0, 32)
    screen.fill(BLACK)
    clock = pygame.time.Clock()
    min_score = 100

    min_distance = float('inf')
    max_distance = 0

    while True:
        pos = pygame.mouse.get_pos()
        pygame.draw.rect(
            screen, "White",
            (400, 390,
             20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  # Left mouse button down.
                    if pos[0] > 350 and pos[0] < 470 and pos[1] > 350 and pos[1] < 470:
                        f1 = pygame.font.Font(None, 36)
                        text1 = f1.render('Слишком близко к точке', True,
                                          (180, 0, 0))
                        screen.blit(text1, (10, 50))
                    else:
                        last = (event.pos[0]-event.rel[0], event.pos[1]-event.rel[1])
                        if min_score > 70:
                            pygame.draw.line(screen, "GREEN", last, event.pos, 1)
                        distance = round(math.sqrt(((pos[0] - 400) ** 2) + ((pos[1] - 400) ** 2)))
                        min_distance = min(min_distance, distance)
                        max_distance = max(max_distance, distance)
                        print(round((min_distance / max_distance)*100))
                        min_score = round((min_distance / max_distance)*100)
                        if min_score > 40 and min_score<= 70:
                            pygame.draw.line(screen, "YELLOW", last, event.pos, 1)
                        if min_score <= 40:
                            pygame.draw.line(screen, "RED", last, event.pos, 1)




            elif event.type == pygame.MOUSEBUTTONUP:
                f2 = pygame.font.Font(None, 36)
                if (round((min_distance / max_distance)*100) + 15) <= 100:
                    text2 = f2.render((str(round((min_distance / max_distance)*100) + 15)) + "%", True,
                                      (180, 0, 0))
                    screen.blit(text2, (400, 700))
                else:
                    text2 = f2.render((str(round((min_distance / max_distance) * 100) + 15)) + "%", True,
                                      (180, 0, 0))
                    screen.blit(text2, (400, 700))
        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 30 FPS.


if __name__ == "__main__":
    main()
import random
import pygame
import pygame as pg


# Размер экрана
WSIZE = (720, 480)

screen = pg.display.set_mode(WSIZE)

clock = pygame.time.Clock()
fps = 5
# Размер кубика(клетки)
TSIDE = 30

MSIZE = WSIZE[0] // TSIDE, WSIZE[1] // TSIDE

start_pos = MSIZE[0] // 2, MSIZE[1] // 2
snake = [start_pos]
# жива ли змейка?
alive = True
# направление snake
direction = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# то самое красное яблоко
apple = random.randint(0, MSIZE[0]), random.randint(0, MSIZE[1])

# Шрифт для очков
pg.font.init()
font_score = pg.font.SysFont("Arial", 23 )
font_gameover = pg.font.SysFont("Arial", 43 )
font_space = pg.font.SysFont("Arial", 18 )


running = True
while running:
    clock.tick(fps)
    # Событие QUIT означает, что пользователь нажал X, чтобы закрыть окно.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # проверка на нажатии кнопок
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT and direction != 2:
                direction = 0
            if event.key == pg.K_DOWN and direction != 3:
                direction = 1
            if event.key == pg.K_LEFT and direction != 0:
                direction = 2
            if event.key == pg.K_UP and direction != 1:
                direction = 3

    # залейте экран цветом
    screen.fill("black")

    # draw - мудуль для рисовки фигур
    [pg.draw.rect(screen, 'green', (x * TSIDE, y * TSIDE, TSIDE - 1, TSIDE - 1)) for x, y in snake]
    pg.draw.rect(screen, 'red', (apple[0] * TSIDE, apple[1] * TSIDE, TSIDE - 1, TSIDE - 1))

    #елси мы живы
    if alive:
        new_pos = snake[0][0] + directions[direction][0], snake[0][1] + directions[direction][1]
        # проверка за бардюр , проверка не в сами мы в себе
        if not (0 <= new_pos[0] < MSIZE[0] and 0 <= new_pos[1] < MSIZE[1]) or \
            new_pos in snake:
            alive = False
        else:
            snake.insert(0, new_pos)
            if new_pos == apple:
                fps += 1
                apple = random.randint(0, MSIZE[0]), random.randint(0, MSIZE[1])
            else:
                snake.pop(-1)
    else:
        text = font_gameover.render(f"GAME OVER", True, "red")
        screen.blit(text, (WSIZE[0] // 2 - text.get_width() // 2, WSIZE[1] // 2 - 50))
        text = font_space.render(f"Press SPACE for restart ", True, "yellow")
        screen.blit(text, (WSIZE[0] // 2 - text.get_width() // 2, WSIZE[1] // 2 + 50))


    screen.blit(font_score.render(f'Очки: {len(snake)}', True, 'yellow'), (5, 5))
# flip() для отображения вашей работы на экране
    pygame.display.flip()


pygame.quit()

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

apple = random.randint(0, MSIZE[0]), random.randint(0, MSIZE[1])

running = True
while running:
    clock.tick(fps)
    # Событие QUIT означает, что пользователь нажал X, чтобы закрыть окно.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # проверка на нажатии кнопок
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                direction = 0
            if event.key == pg.K_DOWN:
                direction = 1
            if event.key == pg.K_LEFT:
                direction = 2
            if event.key == pg.K_UP:
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

    # flip() для отображения вашей работы на экране
    pygame.display.flip()




pygame.quit()

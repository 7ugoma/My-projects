import pygame
import math

# Инициализация Pygame
pygame.init()

# Установка размера окна
size = (1200, 700)
screen = pygame.display.set_mode(size)

# Установка названия окна
pygame.display.set_caption("Дерево Пифагора")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Рекурсивная функция для рисования дерева
def draw_tree(x1, y1, angle, depth, y):
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        pygame.draw.line(screen, white, (x1, y1), (x2, y2), 2)
        draw_tree(x2, y2, angle -y, depth - 1, y)
        draw_tree(x2, y2, angle +y, depth - 1, y)


# Главный цикл игры
done = False
clock = pygame.time.Clock()
a = int(input("Введите угол"))
b = int(input("Введите глубину рекурсии"))
y = int(input("Введите угол между ветвями"))
while not done:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Очистка экрана
    screen.fill(black)

    # Рисование дерева
    draw_tree(size[0]/2, size[1]/2+350, -a, b, y)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(10)

# Выход из программы
pygame.quit()

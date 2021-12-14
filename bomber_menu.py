import pygame


display_width = 900
display_height = 476
show = True
pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((display_width, display_height))


def print_text(message, x, y, font_color=(0, 0, 0), font_type='PingPong.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


class Button:
    def __init__(self, width, height, type):
        self.width = width
        self.height = height
        self.clr = (23, 204, 58)
        self.type = type

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x+self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(display, self.clr, (x, y, self.width, self.height))
                if click[0] == 1 and self.type == 'settings':
                    show_settings()
                elif click[0] == 1 and self.type == 'start':
                    return True
        print_text(message, x+10, y+10)


def show_settings():
    menu_bckgr = pygame.image.load('menu.png')
    hard_btn = Button(100, 50, 'settings')
    veryhard_btn = Button(190, 50, 'settings')
    show_set = True
    while show_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        hard_btn.draw(50, 50, 'HARD')
        veryhard_btn.draw(50, 100, 'VERY HARD')

        pygame.display.update()
        clock.tick(60)


def show_menu():
    menu_bckgr = pygame.image.load('menu.png')

    start_btn = Button(100, 50,'start')
    settings_btn = Button(140, 50,'settings')
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        if start_btn.draw(50, 50, 'START'):
            show = False
        settings_btn.draw(50, 100, 'SETTINGS')



        pygame.display.update()
        clock.tick(60)


show_menu()


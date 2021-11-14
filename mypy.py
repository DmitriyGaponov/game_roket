import pygame
import random
pygame.init()

dis_w = 1000
dis_h = 500


display = pygame.display.set_mode((dis_w, dis_h))
icon = pygame.image.load("arblr-o704c-001.ico")
pygame.display.set_icon(icon)
rok = [pygame.image.load('pix1.png'), pygame.image.load('pix2.png'), pygame.image.load('pix3.png')]
rokgg = pygame.image.load('pixgg.png')
kotey1 = pygame.image.load('kotey1.2.png')
kotey2 = pygame.image.load('kotey2.png')
kotey3 = pygame.image.load('kotey3.png')
kotey4 = pygame.image.load('kotey4.png')


class Boll:
    def __init__(self, x, y, wid, hei, speed, roket_h, image):
        self.roket_h = roket_h
        self.wid = wid
        self.hei = hei
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
    def move(self):
        if self.x > -self.wid:
            #display.blit(self.image, (self.x, self.y))

            if (self.roket_h == True) and self.x > usr_x:
                if usr_y > self.y:
                    self.y += 2
                elif usr_y < self.y:
                    self.y -= 2
                else:
                    self.y = usr_y


            #pygame.draw.rect(display, (0, 200, 0), ())
            display.blit(self.image, (self.x, self.y))


            self.x -= self.speed
            return True
        else:
            self.x = dis_w + 50 + random.randrange(-50, 5000)
            self.y = dis_h - 200 + random.randrange(-250, 200)
            return False

        #if (self.x + 32) == (usr_x + 66) and (self.y + 32) == (usr_y + 28):

usr_h = 28
usr_w = 66
usr_x = dis_w/5
usr_y = dis_h - usr_h - 40
fr = 0
clock = pygame.time.Clock()
make_jump = False
jump_counter = 8
tm = 0

def run_game():
    global game
    game = True
    global make_jump
    boll_arr = []
    gen_boll(boll_arr)
    cosmo = pygame.image.load('wallpaperbetter.jpg')
    global tm
    global t
    t = 0

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(cosmo, (0, 0))
        draw_array(boll_arr)
        t = t + 0.1
        t = round(t, 1)
        print_txt(str(t), 880, 10)

        #pygame.draw.rect(display, (198, 150, 70), (usr_x, usr_y, usr_w, usr_h))
        global fr
        if fr + 1 >= 60:
            fr = 0
        if ch_stlk(boll_arr):
            display.blit(rokgg, (usr_x, usr_y))
            game = False
            if tm < t:
                tm = t

        else:
            display.blit(rok[fr // 20], (usr_x, usr_y))
        fr += 5
        print_txt('The Best:' + str(tm), 700, 50)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            jump()
        else:
            fall()



        pygame.display.update()
        clock.tick(60)
    return game_over()

def jump():
    global usr_y, jump_counter
    if usr_y > 0:
        usr_y -= jump_counter


def fall():
    global usr_y, jump_counter
    if usr_y <= dis_h - usr_h - 75:
        usr_y += jump_counter/2

def gen_boll(array):
    array.append(Boll(dis_w + 1300, dis_h, 48, 34, 5, 1, kotey2))
    array.append(Boll(dis_w + 500, dis_h, 48, 34, 7, 0, kotey2))
    array.append(Boll(dis_w + 5000, dis_h, 48, 34, 7, 0, kotey2))
    array.append(Boll(dis_w + 5000, dis_h, 48, 34, 9, 1, kotey2))
    array.append(Boll(dis_w + 70, dis_h, 28, 29, 9, 0, kotey1))
    array.append(Boll(dis_w + 70, dis_h, 28, 29, 11, 0, kotey1))
    array.append(Boll(dis_w + 70, dis_h - 300, 28, 29, 8, 0, kotey1))
    array.append(Boll(dis_w + 60, dis_h, 28, 29, 12, 1, kotey1))
    array.append(Boll(dis_w + 1440, dis_h, 41, 35, 3, 0, kotey3))
    array.append(Boll(dis_w + 2380, dis_h, 41, 35, 4, 0, kotey3))
    array.append(Boll(dis_w + 105, dis_h, 41, 35, 7, 1, kotey3))
    array.append(Boll(dis_w + 27, dis_h, 47, 32, 6, 0, kotey4))
    array.append(Boll(dis_w + 27, dis_h, 47, 32, 6, 0, kotey4))
    array.append(Boll(dis_w + 27, dis_h, 47, 32, 12, 0, kotey4))
    array.append(Boll(dis_w + 27, dis_h, 47, 32, 10, 0, kotey4))

 #if (self.x + 32)     == (usr_x + 66) and (self.y + 32) == (usr_y + 28):
# def ch_stlk(barriers):
#     for barrier in barriers:
#         if usr_x + usr_w == barrier.x + barrier.wid:
#             if usr_y + usr_h == barrier.y + barrier.hei:
#                 return True
#     return False
#             if barrier.x <= usr_x <= barrier.x + barrier.wid:
#                 return True
#             elif barrier.x <= usr_x + usr_w <= barrier.x + barrier.wid:
#                 return True

def ch_stlk(barriers):
    for barrier in barriers:
        if usr_x + usr_w - 3 >= barrier.x and usr_x <= barrier.x + barrier.wid:
            if barrier.y < usr_y <= barrier.y + barrier.hei - 8:
                return True
            elif usr_y < barrier.y <= usr_y + usr_h - 8:
                 return True
            elif usr_y >= barrier.y and usr_y + usr_h < barrier.y + barrier.hei:
                return True
    return False

def draw_array(array):
    for boll in array:
        boll.move()


def print_txt(message, x, y, front_color = (0, 255, 255), front_type = '18965.ttf', front_size = 30):
    front_type = pygame.font.Font(front_type, front_size)
    text = front_type.render(message, True, front_color)
    display.blit(text, (x, y))


# if usr_x + usr_w >= barrier.x and usr_x <= barrier.x + barrier.wid:
#     if barrier.y < usr_y >= barrier.y + barrier.hei:
#         return True
#
#

def game_over():
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_txt('КАНЕЦ.', 450, 200)
        print_txt('Кнопай ENTER и Начнешь с начала', 200, 250)
        print_txt('ESCAPE - если надоело ', 300, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(60)



while run_game():
    pass
pygame.quit()
quit()

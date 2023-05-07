from constantes import *
def bar_spawn(bar_sprites, i):
    coord = [200, 250, 300, 350] 
    random.shuffle(coord)
    for i in range(3):
        b = Bar(bar, sc, coord[i], 50)
        bar_sprites.append(b)

FPS = 120
W = 800
H = 1000
WHITE = (255, 255, 255)

bar = ('bar.png')
pg.init()
sc = pg.display.set_mode((W, H))
clock = pg.time.Clock() 
# координата x будет случайна
fly = Fly('fly.png', sc)
space1 = Space('space.png', sc, (W - 200) // 2, 0)
space2 = Space('space.png', sc, (W - 200) // 2, - H)
bullet = Bullet('bullet.png', sc)
bar_sprites = []
meteor_filename_list = ['bar.png']
meteor_image_list = []
for filename in meteor_filename_list:
    meteor_image = pg

coord = [200, 300, 400, 500] 
for i in range(3):
    random.shuffle(coord)
    b = Bar(bar, sc, coord[i], 50)
    bar_sprites
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button== 1:
            bullet = Bullet(fly.rect.centerx, fly.rect.top, sc)
          
    space1.update()
    space2.update()
    bullet.update()
    fly.update()
    for i in range(len(bar_sprites)):
        bar_sprites[i].update()
        if bar_sprites[i].rect.y > H:
            bar_sprites1.clear()
            bar_spawn(bar_sprites1, 0)
    space1.draw()
    space2.draw()
    bullet.draw()
    fly.draw()
    pg.display.flip
    clock.tick(FPS)
    pg.display.update()

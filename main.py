import os
import pygame
import sys
import traceback
import myplane
from pygame import *
import enemy
import bullets
os.chdir(r'F:\BaiduNetdiskDownload\096Pygame：飞机大战7\课堂演示')

pygame.init()
pygame.mixer.init()
bg_size = width,height = 480,700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战')

background =pygame.image.load('images/background.png').convert()
# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

def small_enemy_add(group1,group2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)
def mid_enemy_add(group1,group2,num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)
def big_enemy_add(group1,group2,num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def main():
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    #image1 image2 switch
    sw_image = True
    #Delay
    delay = 50
    me = myplane.Myplane(bg_size)
    # Total Enemy
    total_enemy = pygame.sprite.Group()
    # Samll Enemy
    small_enemy = pygame.sprite.Group()
    small_enemy_add(total_enemy, small_enemy, 15)
    # Mid Enemy
    mid_enemy = pygame.sprite.Group()
    mid_enemy_add(total_enemy, mid_enemy, 5)
    # Big Enemy
    big_enemy = pygame.sprite.Group()
    big_enemy_add(total_enemy, big_enemy, 2)
    # Bullet
    bullet1=[]
    bullet1_num = 8
    bullet1_index = 0
    for i in range(bullet1_num):
        bullet1.append(bullets.Bullet1(me.rect.midtop))

    # Destroy index
    small_flight_index = 0
    mid_flight_index = 0
    big_flight_index = 0
    me_flight_index = 0



    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            me.moveup()
        if key_pressed[K_DOWN]:
            me.movedown()
        if key_pressed[K_LEFT]:
            me.moveleft()
        if key_pressed[K_RIGHT]:
            me.moveright()
        screen.blit(background,(0,0))
        if not (delay % 10):
            bullet1[bullet1_index].reset4(me.rect.midtop)
            bullet1_index = (bullet1_index + 1) % bullet1_num

        for b in bullet1:
            if b.active:
                b.move()
                screen.blit(b.img,b.rect)
                enemy_hit = pygame.sprite.spritecollide(b,total_enemy,False,pygame.sprite.collide_mask)
                if enemy_hit:
                    b.active = False
                    for e in enemy_hit:
                        e.destory = True

        if not me.destory:
            if sw_image:
                screen.blit(me.image1,me.rect)
            else:
                screen.blit(me.image2,me.rect)
        else:
            if me_flight_index ==1:
                me_down_sound.play()
            if not (delay % 5):
                screen.blit(each.destory_images[me_flight_index], each.rect)
                me_flight_index+=1
                if me_flight_index == 4:
                    me_flight_index = 0
                    me.reset()

        if not (delay%10):
            sw_image = not sw_image
            delay -=1
        elif delay ==0:
            delay = 50
        else:
            delay -=1
        enemy_down = pygame.sprite.spritecollide(me,total_enemy,False,pygame.sprite.collide_mask)
        if enemy_down:
            me.destory = True
            for e in enemy_down:
                e.destory = True

        for each in big_enemy:
            each.move()
            if not each.destory:
                if sw_image:
                    screen.blit(each.image1,each.rect)
                else:
                    screen.blit(each.image2, each.rect)
                if each.rect.bottom == -50:
                    enemy3_fly_sound.play()
            else:
                if big_flight_index ==1:
                    enemy3_down_sound.play()
                if not (delay % 5):
                    screen.blit(each.destory_images[big_flight_index],each.rect)
                    big_flight_index +=1
                    if big_flight_index == 6:
                        enemy3_fly_sound.stop()
                        big_flight_index = 0
                        each.reset3()

        for each in mid_enemy:
            each.move()
            if not each.destory:
                screen.blit(each.image,each.rect)
            else:
                if mid_flight_index == 1:
                    enemy2_down_sound.play()
                if not (delay % 5):
                    screen.blit(each.destory_images[mid_flight_index], each.rect)
                    mid_flight_index += 1
                    if mid_flight_index == 4:
                        mid_flight_index = 0
                        each.reset2()

        for each in small_enemy:
            each.move()
            if not each.destory:
                screen.blit(each.image,each.rect)
            else:
                if small_flight_index == 1:
                    enemy1_down_sound.play()
                if not (delay % 5):
                    screen.blit(each.destory_images[small_flight_index], each.rect)
                    small_flight_index += 1
                    if small_flight_index == 4:
                        small_flight_index = 0
                        each.reset1()

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        input()




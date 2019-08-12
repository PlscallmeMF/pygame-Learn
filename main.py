import os
os.chdir(r'D:\pygame\flight_game')
import pygame
import sys
import traceback
import myplane
from pygame import *
import enemy
import bullet
import supply
from random import *

pygame.init()
pygame.mixer.init()
bg_size = width,height = 480,700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战')

BLACK =(0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

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
    delay = 1800
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
    big_enemy_add(total_enemy, big_enemy, 3)
    # Bullet
    bullet1=[]
    bullet1_num = 8
    bullet1_index = 0
    for i in range(bullet1_num):
        bullet1.append(bullet.Bullet1(me.rect.midtop))
    # Super Bullet
    bullet2 = []
    bullet2_num = 12
    bullet2_index = 0
    for i in range(bullet2_num//3):
        bullet2.append(bullet.Bullet2((me.rect.centerx,me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx-33,me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30,me.rect.centery)))
    # Destroy index
    small_flight_index = 0
    mid_flight_index = 0
    big_flight_index = 0
    me_flight_index = 0
    # Score record
    score = 0
    score_font = pygame.font.Font('font/font.ttf',36)
    # Level
    level = 1
    #Bomb
    bomb_image =  pygame.image.load('images/bomb.png').convert_alpha()
    bomb_rect  = bomb_image.get_rect()
    bomb_font = pygame.font.Font('font/font.ttf',40)
    bomb_num = 3
    # Supplies
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    #Pause or Unpause
    pause = False
    pause_nor_image =pygame.image.load('images/pause_nor.png').convert_alpha()
    pause_pressed_image = pygame.image.load('images/pause_pressed.png').convert_alpha()
    resume_nor_image = pygame.image.load('images/resume_nor.png').convert_alpha()
    resume_pressed_image = pygame.image.load('images/resume_pressed.png').convert_alpha()
    pause_rect = pause_nor_image.get_rect()
    pause_rect.left, pause_rect.top = width - pause_rect.width, 10
    pause_img = pause_nor_image
    # Super bullet time
    timerecord = False
    #Life number
    life_image = pygame.image.load('images/life.png').convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3
    #invincible time
    invincible_time = 180
    #gameover
    gameover = False
    # 游戏结束画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button ==1 and pause_rect.collidepoint(event.pos):
                    pause = not pause
                    if pause:
                        pause_img = resume_nor_image
                    else:
                        pause_img = pause_nor_image
            elif event.type == MOUSEMOTION:
                if pause_rect.collidepoint(event.pos):
                    if pause:
                        pause_img = resume_pressed_image
                    else:
                        pause_img = pause_pressed_image
                else:
                    if pause:
                        pause_img = resume_nor_image
                    else:
                        pause_img = pause_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -=1
                        bomb_sound.play()
                        for each in total_enemy:
                            if each.rect.bottom >0:
                                each.destory = True



        screen.blit(background, (0, 0))
        if life_num and not pause:
            pygame.mixer.music.unpause()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_UP]:
                me.moveup()
            if key_pressed[K_DOWN]:
                me.movedown()
            if key_pressed[K_LEFT]:
                me.moveleft()
            if key_pressed[K_RIGHT]:
                me.moveright()
                

            if not (delay % 10):
                if timerecord:
                    bullets = bullet2
                    bullets[bullet2_index].reset4((me.rect.centerx-33,me.rect.centery))
                    bullets[bullet2_index+1].reset4((me.rect.centerx+33,me.rect.centery))
                    bullets[bullet2_index+2].reset4((me.rect.centerx,me.rect.centery))
                    bullet2_index = (bullet2_index+3) % bullet2_num
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset4(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % bullet1_num

            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.img,b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b,total_enemy,False,pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            if e in mid_enemy or e in big_enemy:
                                e.hit = True
                                e.energy -=1
                                if e.energy ==0:
                                    e.destory = True
                            else:
                                e.destory = True

            if me.invincible:
                me.destory = False
                invincible_time -= 1
                if invincible_time ==0:
                    me.invincible = False
                    invincible_time = 180


            if not me.destory:
                if sw_image:
                    screen.blit(me.image1,me.rect)
                else:
                    screen.blit(me.image2,me.rect)
            else:
                if me_flight_index ==1:
                    me_down_sound.play()
                if not (delay % 2):
                    screen.blit(each.destory_images[me_flight_index], each.rect)
                    me_flight_index+=1
                    if me_flight_index == 4:
                        me_flight_index = 0
                        life_num -= 1
                        me.reset()
                        
                    


            if not (delay % 10):
                sw_image = not sw_image
                delay -= 1
            elif delay == 0:
                delay = 1800
            else:
                delay -= 1
            enemy_down = pygame.sprite.spritecollide(me, total_enemy, False, pygame.sprite.collide_mask)
            if enemy_down:
                me.destory = True
                for e in enemy_down:
                    e.destory = True

            for each in big_enemy:
                if not each.destory:
                    each.move()
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if not each.destory:
                            if sw_image:
                                screen.blit(each.image1, each.rect)
                            else:
                                screen.blit(each.image2, each.rect)
                    pygame.draw.line(screen, BLACK,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     2)
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain,
                                      each.rect.top - 5), 2)


                else:
                    if big_flight_index == 1:
                        enemy3_down_sound.play()
                    if not (delay % 2):
                        screen.blit(each.destory_images[big_flight_index], each.rect)
                        big_flight_index += 1
                        if big_flight_index == 6:
                            enemy3_fly_sound.stop()
                            big_flight_index = 0
                            score += 10000
                            each.reset3()



            for each in mid_enemy:
                if not each.destory:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit, each.rect)
                        each.hit = False
                    else:
                        if not each.destory:
                            screen.blit(each.image, each.rect)
                    pygame.draw.line(screen, BLACK,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.right, each.rect.top - 5),
                                     2)
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color,
                                     (each.rect.left, each.rect.top - 5),
                                     (each.rect.left + each.rect.width * energy_remain,
                                      each.rect.top - 5), 2)
                else:
                    if mid_flight_index == 1:
                        enemy2_down_sound.play()
                    if not (delay % 2):
                        screen.blit(each.destory_images[mid_flight_index], each.rect)
                        mid_flight_index += 1
                        if mid_flight_index == 4:
                            mid_flight_index = 0
                            score += 5000
                            each.reset2()

            for each in small_enemy:
                each.move()
                if not each.destory:
                    screen.blit(each.image, each.rect)
                else:
                    if small_flight_index == 1:
                        enemy1_down_sound.play()
                    if not (delay % 2):
                        screen.blit(each.destory_images[small_flight_index], each.rect)
                        small_flight_index += 1
                        if small_flight_index == 4:
                            small_flight_index = 0
                            score += 1000
                            each.reset1()

            if not (delay % (20 * 60)):
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, me):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, me):
                    get_bullet_sound.play()
                    lefttime = 10 * 60
                    timerecord = True
                    bullet_supply.active = False
            if timerecord:
                lefttime -=1
                if lefttime == 0:
                    timerecord = False
                        

            #Bomb
            bomb_text = bomb_font.render('X %d'%bomb_num,True,WHITE)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image,(10,height-10-bomb_rect.height))
            screen.blit(bomb_text,(20+bomb_rect.width,height-5-text_rect.height))
            #Life
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,(width-10-(i+1)*life_rect.width,height-10-life_rect.height))

            score_text = score_font.render('Score: %s' %str(score),True, WHITE)
            screen.blit(score_text,(10,5))
            level_text = score_font.render('Level: %s' %str(level),True, WHITE)
            screen.blit(level_text,(width//2+60,5))
        
        elif life_num ==0:
            pygame.mixer_music.stop()
            pygame.mixer.stop()
            delay = 0
            
            if not gameover:
                gameover = True
            # Highest score
                with open('record.txt','r') as f:
                    record_score = int(f.read())
                    
                if score > record_score:
                    record_score = score
                    with open('record.txt','w') as f:
                        f.write(str(score))  


            # Gameover
            record_score_text = score_font.render("Best : %d" % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))
            
            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top =(width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)
            
            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = (width - gameover_text2_rect.width) // 2, gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top =(width - again_rect.width) // 2, gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = (width - again_rect.width) // 2,again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    main()
                # 如果用户点击“结束游戏”            
                elif gameover_rect.left < pos[0] < gameover_rect.right and gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()      

            
            
        elif pause:
            pygame.mixer.music.pause()
            pause_font = pygame.font.Font('font/font.ttf',60)
            pause_text = pause_font.render('Pause...',True, RED)
            pause_text_rect = pause_text.get_rect()
            screen.blit(pause_text,((width - pause_text_rect.width)//2,(height-pause_text_rect.height)//2))

            
        # Pause image
        screen.blit(pause_img,pause_rect)
        pygame.display.flip()
        clock.tick(60)
        #Level increase
        if score > 20000 and score<=80000:
            if level ==1:
                level = 2
                level_up = True
        elif score > 80000 and score <= 200000:
            if level ==2:
                level = 3
                level_up = True
        elif score >200000 and score <=400000:
            if level ==3:
                level = 4
                level_up = True
        elif score > 400000:
            if level ==4:
                level = 5
                level_up = True
        if level == 2 and level_up:
            small_enemy_add(total_enemy, small_enemy, 5)
            mid_enemy_add(total_enemy, mid_enemy, 3)
            for each in small_enemy:
                each.speed = 3
            level_up = False
        elif level == 3 and level_up:
            small_enemy_add(total_enemy, small_enemy, 4)
            mid_enemy_add(total_enemy, mid_enemy, 2)
            for each in small_enemy:
                each.speed = 4
            level_up = False
        elif level == 4 and level_up:
            small_enemy_add(total_enemy, small_enemy, 3)
            mid_enemy_add(total_enemy, mid_enemy, 1)
            for each in small_enemy:
                each.speed = 5
            level_up = False
        elif level == 5 and level_up:
            small_enemy_add(total_enemy, small_enemy, 2)
            mid_enemy_add(total_enemy, mid_enemy, 1)
            for each in small_enemy:
                each.speed = 6
            level_up = False


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        input()




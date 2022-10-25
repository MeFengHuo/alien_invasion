
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    #设置背景色
    # bg_color = (230,230,230)

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组和一个外星人编组
    bullets = Group()
    aliens = Group()

    #创建一个外星人
    alien = Alien(ai_settings,screen)

    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #创建一个用于存储游戏统计信息的实例,并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #开始游戏的主循环
    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            bullets.update()

            #删除已消失的子弹
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
            """
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            # print(len(bullets))  """

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        '''
        # #监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()
        '''
run_game()


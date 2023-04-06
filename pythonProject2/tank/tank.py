#坦克大战
import time,random,pygame
__display = pygame.display
import random
random.randint(1,6)
class MainGame():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    window = None
    P_TANK = None
    Enemy_tank_list = []
    enum_tank_count = 5
    bullet_list = []
    enemy_bullet_list = []
    explode_list = []
    wall_list = []

    def startGame(self):
        pygame.display.init()
        # 创建窗口面板
        MainGame.window = pygame.display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        pygame.display.set_caption('孔万三的坦克大战')
        MainGame.P_TANK = Tank(400,450)

        self.createEnemyTank()
        self.createWall()
        while True:
            MainGame.window.fill(pygame.Color(0,0,0))
            # MainGame.P_TANK.move()
            self.getEvent()
            # 将带有文字的surface绘制到窗口中
            MainGame.window.blit(self.drawText('剩余敌方坦克%d辆' % len(MainGame.Enemy_tank_list)), (5, 5))

            self.show_wall()
            self.show_P_Tank()
            self.show_enemy_tank()
            self.show_bullet()
            self.show_enemy_bullet()

            self.play_bgm()

            self.show_explode()

            # 刷新屏幕
            pygame.display.update()
            time.sleep(0.01)
    def play_bgm(self):
        m = Musice('./img/start.wav')
        m.paly_music()

    def createWall(self):
        for i in range(6):
            wall = Wall(130*i,350)
            MainGame.wall_list.append(wall)

    def show_wall(self):
        for wall in MainGame.wall_list:
            wall.display_wall()

    def createEnemyTank(self):
        for i in range(MainGame.enum_tank_count):
            random_left = random.randint(1,8)
            enemy_tank = EnemyTank(random_left*100,150)
            MainGame.Enemy_tank_list.append(enemy_tank)
    def show_explode(self):
        for explode in MainGame.explode_list:
            if explode.live:
                explode.display_explode()
            else:
                MainGame.explode_list.remove(explode)

    def show_P_Tank(self):
        if MainGame.P_TANK and MainGame.P_TANK.live:
            MainGame.P_TANK.display_tank()
            if not MainGame.P_TANK.stop:
                MainGame.P_TANK.move()
                MainGame.P_TANK.hit_wall()
        else:
            del MainGame.P_TANK
            MainGame.P_TANK = None

    def show_enemy_tank(self):
        for eTank in MainGame.Enemy_tank_list:
            eTank.display_enemy_tank()
            if eTank.live:
                eTank.display_enemy_tank()
                eTank.random_move()
                eTank.hit_wall()
            else:
                MainGame.Enemy_tank_list.remove(eTank)
                liveCount = 1
                if len(MainGame.Enemy_tank_list) < 1:
                    self.createEnemyTank()
                    self.P_TANK.speed = liveCount * 1.3
                    EnemyTank.speed = liveCount * 1.1

            ebullet = eTank.random_fire()
            if ebullet:
                MainGame.enemy_bullet_list.append(ebullet)

    def show_bullet(self):
        for bullet in MainGame.bullet_list:
            bullet.bullet_move()
            if bullet.live:
                bullet.displey_bullet()
                bullet.hit_tank()
                bullet.hit_wall()
            else:
                MainGame.bullet_list.remove(bullet)

    def show_enemy_bullet(self):
        for ebullet in MainGame.enemy_bullet_list:
            ebullet.bullet_move()
            if ebullet.live:
                ebullet.displey_bullet()
                ebullet.hit_my_tank()
                ebullet.hit_wall()
            else:
                MainGame.enemy_bullet_list.remove(ebullet)

    # 事件处理方法
    def getEvent(self):
        eventList = pygame.event.get() #获取所有事件
        for event in eventList:
            if event.type == pygame.QUIT:
                print('游戏结束')
                self.gameOver()
            elif event.type == pygame.KEYDOWN:
                if MainGame.P_TANK and MainGame.P_TANK.live:
                    if event.key == pygame.K_LEFT:
                        print('向左移动')
                        MainGame.P_TANK.direction = 'L'
                        MainGame.P_TANK.stop = False
                        # if MainGame.P_TANK.rect.left > 0:
                        #     MainGame.P_TANK.rect.left -= MainGame.P_TANK.speed
                        # MainGame.P_TANK.move()
                    elif event.key == pygame.K_RIGHT:
                        print('向右移动')
                        MainGame.P_TANK.direction = 'R'
                        MainGame.P_TANK.stop = False
                        # if MainGame.P_TANK.rect.left < MainGame.SCREEN_WIDTH-MainGame.P_TANK.rect.height:
                        #     MainGame.P_TANK.rect.left += MainGame.P_TANK.speed
                        # MainGame.P_TANK.move()
                    elif event.key == pygame.K_UP:
                        print("向上移动")
                        MainGame.P_TANK.direction = 'U'
                        MainGame.P_TANK.stop = False
                        # if MainGame.P_TANK.rect.top > 0 :
                        #     MainGame.P_TANK.rect.top -= MainGame.P_TANK.speed
                        # MainGame.P_TANK.move()
                    elif event.key == pygame.K_DOWN:
                        print("向下移动")
                        MainGame.P_TANK.direction = 'D'
                        MainGame.P_TANK.stop = False
                        # if MainGame.P_TANK.rect.top <= MainGame.SCREEN_HEIGHT-MainGame.P_TANK.rect.height:
                        #     MainGame.P_TANK.rect.top += MainGame.P_TANK.speed
                        # MainGame.P_TANK.move()
                    elif event.key == pygame.K_SPACE and MainGame.P_TANK:
                        print('开枪%d' % len(MainGame.bullet_list))
                        if len(MainGame.bullet_list) < 6:
                            bullet = MainGame.P_TANK.fire()
                            MainGame.bullet_list.append(bullet)
                elif event.key == pygame.K_ESCAPE:
                    print('重新开始')
                    MainGame.P_TANK = Tank(400,450)

            elif event.type == pygame.KEYUP:
                # MainGame.P_TANK.stop = True
                if event.key != pygame.K_SPACE and MainGame.P_TANK and MainGame.P_TANK.live:
                    MainGame.P_TANK.stop = True

    #给一个字符串
    def drawText(self,content):
        #字体模块初始化
        pygame.font.init()
        #创建字体对象
        font = pygame.font.SysFont('kaiti',20)
        # fonts_list = pygame.font.get_fonts()
        # print(fonts_list)
        #使用字体渲染内容
        text_sf = font.render(content,True,pygame.Color(255,0,0))
        #返回包含内容的surface
        return text_sf
    def gameOver(self):
        exit()

#继承精灵类的类,共其他类继承
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Tank(BaseItem):
    def __init__(self,left,top):
        self.images = {
            'U':pygame.image.load('./img/p1tankU.gif'),
            'D':pygame.image.load('./img/p1tankD.gif'),
            'L':pygame.image.load('./img/p1tankL.gif'),
            'R':pygame.image.load('./img/p1tankR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect() #区域
        self.rect.left = left
        self.rect.top = top
        self.speed = 1
        #用来控制坦克是否应该移动的开关
        self.stop = True
        self.live = True
        self.old_left = 0
        self.old_top = 0

    def display_tank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)

    def move(self):
        #修改tank的坐标，取决于坦克的方向
        self.old_top = self.rect.top
        self.old_left = self.rect.left
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT-self.rect.height:
                self.rect.top += self.speed
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH-self.rect.width:
                self.rect.left += self.speed

    def fire(self):
        bullet = Bullet(self)
        # MainGame.bullet_list.append(bullet)
        return  bullet

    def stay(self):
        self.rect.left = self.old_left
        self.rect.top = self.old_top
    def hit_wall(self):
        for wall in MainGame.wall_list:
            result = pygame.sprite.collide_rect(wall,self)
            if result:
                self.stay()


class Bullet(BaseItem):
    def __init__(self,Tank):
        self.image = pygame.image.load('./img/bullet.gif')
        self.direction = Tank.direction
        self.speed = 1 * 3
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = Tank.rect.left + Tank.rect.width/2 - self.rect.width/2
            self.rect.top = Tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = Tank.rect.left + Tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = Tank.rect.top + Tank.rect.height
        elif self.direction == 'L':
            self.rect.left = Tank.rect.left - self.rect.width
            self.rect.top = Tank.rect.top +  Tank.rect.height/2 - self.rect.height/2
        elif self.direction == 'R':
            self.rect.left = Tank.rect.left + Tank.rect.width
            self.rect.top = Tank.rect.top + Tank.rect.height / 2 - self.rect.height / 2
        self.live = True

    def displey_bullet(self):
        MainGame.window.blit(self.image,self.rect)

    def hit_tank(self):
        for eTank in MainGame.Enemy_tank_list:
            result = pygame.sprite.collide_rect(eTank,self)
            if result:
                self.live = False
                eTank.live = False
                explode = Explode(eTank.rect)
                MainGame.explode_list.append(explode)

    def hit_wall(self):
        for wall in MainGame.wall_list:
            result = pygame.sprite.collide_rect(wall,self)
            if result:
               self.live = False


    def bullet_move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False

    def hit_my_tank(self):
        for eBullet in MainGame.enemy_bullet_list:
            if MainGame.P_TANK and MainGame.P_TANK.live:
                result = pygame.sprite.collide_rect(eBullet, MainGame.P_TANK)
                if result:
                    explode = Explode(self.rect)
                    MainGame.explode_list.append(explode)
                    eBullet.live = False
                    MainGame.P_TANK.live = False
            else:
                break


class EnemyTank(Tank):
    def __init__(self,left,top):
        self.images = {
            'U': pygame.image.load('./img/enemy1U.gif'),
            'D': pygame.image.load('./img/enemy1D.gif'),
            'L': pygame.image.load('./img/enemy1L.gif'),
            'R': pygame.image.load('./img/enemy1R.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()  # 区域
        self.rect.left = left
        self.rect.top = top
        self.speed = 1
        # 用来控制坦克是否应该移动的开关
        self.stop = False
        self.step = 10
        self.live = True

    def random_directon(self):
        num = random.randint(1,4)
        if num ==1:
            self.direction = 'U'
        elif num == 2:
            self.direction = 'D'
        elif num == 3:
            self.direction = 'L'
        elif num == '4':
            self.direction = 'R'
        return self.direction

    def random_move(self):
        if self.step == 0:
            self.random_directon()
            self.step = 50
        else:
            self.move()
            self.step -= 1

    def display_enemy_tank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)

    def random_fire(self):
        num = random.randint(1,100)
        if num == 3:
            ebullet = self.fire()
            return  ebullet

class Wall(BaseItem):
    def __init__(self,left,top):
        self.image = pygame.image.load('./img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
    def display_wall(self):
        MainGame.window.blit(self.image,self.rect)

class  Explode(BaseItem):
    def __init__(self,rect):
        self.images = [
            pygame.image.load('./img/blast0.gif'),
            pygame.image.load('./img/blast1.gif'),
            pygame.image.load('./img/blast2.gif'),
            pygame.image.load('./img/blast3.gif'),
            pygame.image.load('./img/blast4.gif'),
            pygame.image.load('./img/blast5.gif'),
            pygame.image.load('./img/blast6.gif'),
            pygame.image.load('./img/blast7.gif'),
        ]
        self.rect = rect
        self.image = self.images[0]
        self.live = True
        self.step = 0
    def display_explode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0

class Musice():
    def __init__(self,music):
        pygame.mixer.init()
        self.music = music
        pygame.mixer.music.load(self.music)
    def paly_music(self):
        pygame.mixer.music.play(-1)


if __name__ == "__main__":
    games = MainGame()
    # games.drawText('1')
    games.startGame()
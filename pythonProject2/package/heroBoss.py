import random
import time


class Hero():
    def __init__(self, name, hp, damage, skillQ):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.skillQ = skillQ

    # 英雄攻击boss的方法，boss做参数，传进来
    def attack_boss(self, boss):

        rand_num = random.randint(1, 10)
        if rand_num == 1 or rand_num == 2:
            # 调用暴击伤害
            self.attack2_boss(boss)
        elif rand_num == 3:
            # 调用技能伤害
            self.attack3_boss(boss)
        else:
            # 调用普通伤害
            self.attack1_boss(boss)

    # 普通伤害
    def attack1_boss(self, boss):
        # 伤害值增加随机浮动伤害值
        rand_damge = random.randint(1, 99)
        boss.hp -= (self.damage + rand_damge)
        print("英雄:%s 攻击Boss:%s 伤害值:%d Boss剩余生命值:%d"
              % (self.name, boss.name, self.damage + rand_damge, boss.hp))

    # 暴击伤害
    def attack2_boss(self, boss):
        # 伤害值增加随机浮动伤害值
        rand_damge = random.randint(1, 99)
        boss.hp -= (self.damage + rand_damge) * 2
        print("英雄:%s 攻击Boss:%s \033[1;31m暴击伤害值:%d\033[0m Boss剩余生命值:%d"
              % (self.name, boss.name, (self.damage + rand_damge) * 2, boss.hp))

    # 技能伤害
    def attack3_boss(self, boss):
        boss.hp -= self.skillQ.skillDamage
        print("英雄:%s 攻击Boss:%s \033[1;34m技能伤害值:%d\033[0m Boss剩余生命值:%d"
              % (self.name, boss.name, self.skillQ.skillDamage, boss.hp))


class Boss():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # 英雄攻击boss的方法，boss做参数，传进来
    def attack_hero(self, hero):
        rand_damge = random.randint(1, 50)
        hero.hp -= (self.damage + rand_damge)
        print("Boss:%s 攻击英雄:%s 伤害值:%d 英雄剩余生命值:%d"
              % (self.name, hero.name, self.damage + rand_damge, hero.hp))


# 创建技能类
class Skill():
    def __init__(self, skillName, skillDamage):
        self.skillName = skillName
        self.skillDamage = skillDamage

if __name__ == '__main__':
    count = 1

    # 创建技能对象
    skillQ = Skill('当头一棒', 100)
    # 创建英雄
    hero1 = Hero('至尊宝', 100, 20, skillQ)
    # 创建Boss
    boss1 = Boss('白晶晶', 300, 5)
    while True:
        print("------------------【round%d】-----------------" % count)
        if hero1.hp > 0:
            hero1.attack_boss(boss1)
            if boss1.hp <= 0:
                print("至尊宝获胜")
                break
        if boss1.hp > 0:
            boss1.attack_hero(hero1)
            if hero1.hp <= 0:
                print("晶晶获胜")
                break
        count += 1
        time.sleep(0.8)
        print('\n' * 1)

#coding:gbk
"""
第一个小项目：完成RPSLS游戏
作者：王紫鑫
2019.11.20
"""

import random

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4

        

def number_to_name(number):
    """
    将整数对应到游戏的不同对象
    """

    if number==0:
        return "石头"
    elif number==1:
        return "史波克"
    elif number==2:
        return "纸"
    elif number==3:
        return "蜥蜴"
    elif number==4:
        return "剪刀"
		

def rpsls(choice_name):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """

    print("----------------")
    print("您的选择为:",choice_name)
        
    player_choice_number=name_to_number(choice_name)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    
    print("计算机的选择为:",comp_choice)
    
    d=player_choice_number-comp_number 
    if d==1 or d==2 or d==-4 or d==-3:
        print("您赢了")
    elif d==0:
        print("您和计算机出的一样呢")
    elif d==-1 or d==-2 or d==4 or d==3:
        print("计算机赢了")
   

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()

if choice_name in ["石头","史波克","纸","剪刀","蜥蜴"]:
	rpsls(choice_name)
else:
	print("Error: No Correct Name")

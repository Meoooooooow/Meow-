#coding:gbk
"""
��һ��С��Ŀ�����RPSLS��Ϸ
���ߣ�������
2019.11.20
"""

import random

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4

        

def number_to_name(number):
    """
    ��������Ӧ����Ϸ�Ĳ�ͬ����
    """

    if number==0:
        return "ʯͷ"
    elif number==1:
        return "ʷ����"
    elif number==2:
        return "ֽ"
    elif number==3:
        return "����"
    elif number==4:
        return "����"
		

def rpsls(choice_name):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """

    print("----------------")
    print("����ѡ��Ϊ:",choice_name)
        
    player_choice_number=name_to_number(choice_name)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    
    print("�������ѡ��Ϊ:",comp_choice)
    
    d=player_choice_number-comp_number 
    if d==1 or d==2 or d==-4 or d==-3:
        print("��Ӯ��")
    elif d==0:
        print("���ͼ��������һ����")
    elif d==-1 or d==-2 or d==4 or d==3:
        print("�����Ӯ��")
   

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()

if choice_name in ["ʯͷ","ʷ����","ֽ","����","����"]:
	rpsls(choice_name)
else:
	print("Error: No Correct Name")

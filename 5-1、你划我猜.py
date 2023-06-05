import random
"""
你划我猜 （不可跳过）
"""
'''
str1 = "金枪鱼、鸵鸟、牦牛、考拉、穿山甲、藏羚羊、熊猫、企鹅、海豚、鲸鱼、老鹰、长颈鹿、刺猬、鳄鱼、猴子、孔雀"
str2 = "亡羊补牢、颠三倒四、拔苗助长、画蛇添足、顺手牵羊、三长两短、坐井观天、眼高手低、目瞪口呆、盲人摸象、画龙点睛、走马观花、眉飞色舞、自言自语 、手舞足蹈"
str3 = "黄焖鸡米饭、开水白菜、西红柿炒番茄、干锅土豆、佛跳墙、羊肉串、火腿蛋炒饭、蚂蚁上树、夫妻肺片、糖油果子、豆汁儿、剁椒鱼头、黄瓜皮蛋汤、章鱼烧、张飞牛肉"
no_1 = str1.split("、")
no_2 = str2.split("、")
no_3 = str3.split("、")
category = ["动物类", "成语类", "食物类"]
score = [0, 0, 0]
seq = 1
print("======你划我猜游戏======")
print("温馨提示：每组15个词，限时2分钟。")
while seq < 4:
    count = 1
    num = input("请第%d组选择主题（1：动物类，2：成语类，3：食物类）:" % seq)
    num = int(num)
    if num == 1:
        list1 = no_1
    elif num == 2:
        list1 = no_2
    else:
        list1 = no_3
    print("第%d组选择了%s" % (seq, category[num - 1]))
    input("请按任意键继续！")
    while count < 16:
        index = random.randint(0, len(list1)-1)
        str_pop = list1.pop(index)
        is_quit = input("(q:退出，其他:继续)\n第%d个词【%s】" % (count, str_pop))
        if is_quit == "q":
            break
        score[seq - 1] = count
        count += 1
    seq += 1
print(score)
'''
"""
你划我猜 （可跳过）
"""
# '''
str1 = "金枪鱼、鸵鸟、牦牛、考拉、穿山甲、藏羚羊、熊猫、企鹅、海豚、鲸鱼、老鹰、长颈鹿、刺猬、鳄鱼、猴子、孔雀"
str2 = "亡羊补牢、颠三倒四、拔苗助长、画蛇添足、顺手牵羊、三长两短、坐井观天、眼高手低、目瞪口呆、盲人摸象、画龙点睛、走马观花、眉飞色舞、自言自语 、手舞足蹈"
str3 = "黄焖鸡米饭、开水白菜、西红柿炒番茄、干锅土豆、佛跳墙、羊肉串、火腿蛋炒饭、蚂蚁上树、夫妻肺片、糖油果子、豆汁儿、剁椒鱼头、黄瓜皮蛋汤、章鱼烧、张飞牛肉"
no_1 = str1.split("、")
no_2 = str2.split("、")
no_3 = str3.split("、")
category = ["动物类", "成语类", "食物类"]
score = [0, 0, 0]
seq = 1
print("======你划我猜游戏======")
print("温馨提示：每组15个词，限时2分钟。")
while seq < 4:
    count = 1
    num = input("请第%d组选择主题（1：动物类，2：成语类，3：食物类）:" % seq)
    num = int(num)
    if num == 1:
        list1 = no_1
    elif num == 2:
        list1 = no_2
    else:
        list1 = no_3
    print("第%d组选择了%s" % (seq, category[num - 1]))
    input("请按任意键继续！")
    while count < 16:
        index = random.randint(0, len(list1)-1)
        str_pop = list1.pop(index)
        is_quit = input("(q:退出，1:计分，0:跳过)\n第%d个词【%s】" % (count, str_pop))
        if is_quit == "q":
            break
        score[seq - 1] += int(is_quit)
        count += 1
    seq += 1
print(score)
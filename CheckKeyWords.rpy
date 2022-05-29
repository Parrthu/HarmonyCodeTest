#开始运行python代码
init python:
#写出关键词列表
    klist1 = ["你好","早上好","下午好","晚上好","中午好"]
    klist2 = ["dave","主角","名字","来源"]
define qqq = ""
label QnA3:
    $ qqq = renpy.input("输入内容")
    $ qqq = qqq.strip()
#也可以使用in语句，in语句更为简单
#if qqq in klist1:
    if klist1.count(qqq) > 0:
        "你好啊。"
    elif klist2.count(qqq) > 0:
            "这一切都大有来头。"
            "主角Dave的名字，事实上来源于PasswordTheVN"
            "他也是那个游戏中的主角。"
    else:
        "嗯，你或许应该问点别的。"
        menu:
            "好啊。":
                jump QnA3
            "就到这里吧。":
                jump AfterQnA3
menu:
    "继续？"
    "好":
        jump QnA3
    "不了":
        jump AfterQnA3

label AfterQnA3:
    "谢天谢地，提问环节结束了。"

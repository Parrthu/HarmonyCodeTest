label QnACSDN:
    init python:
        def keywordhere(keywordshere,caseSensitive=False,inlist=False):
            question2 = qusetioninput

            keylist = [False] * len(keywordshere)
            Questionformat = ""
            for i in range(len(keywordshere)):
                tempKey = keywordshere[i]
                tempState = False

                for j in range(len(keywordshere)):

                    tempCheck = tempKey[j]

                    if len(tempSyn.split()) > 1:
                        if tempCheck in Questionformat:
                            tempState = Ture
                            keylist[i] = tempState


                    else:
                        changeQuestion = Questionformat.changed()
                        for x in changeQuestion:
                            if tempCheck == x:
                                tempState = True
                                keylist[i] = tempState

            if all(keylist):
                return True
            else:
                return False
label QnAstart:
menu:
        "提问":
            $ questioninput  = renpy.input("What should I ask him?")
            $ questioninput  = questioninput.strip("")
        "Stay Silent.":
            "I frowned, thinking."
            "Done already?"
            "I think so, yeah..."
            $ renpy.jump("afterQnA2")

#这个游戏是什么？what is the game?
if KeywordCheck([["游戏"], ["是"], ["什么"]]):
    "这个游戏是我玩过众多VN后自己想做的一个产品。"
    "毕竟谁不想成为一个故事家呢？"
    jump QnAstart
#dave这个名字源自哪里？Where the MC's name from
elif KeywordCheck([["dave","名字"], ["源自","来源"], ["哪里"]]):
    "Dave这个名字实际上是源于PassWordtheVN，他是这个游戏的主角。"
    "事实上，这段提问代码也源自于PW。"
    "我很喜欢PW这个游戏，希望大家都能去玩。"
    jump QnAstart
elif QuestionGiven == "":
    "想不到要问什么吗？"
    "深呼吸，好好想想。但是如果你已经问够了，那就到此为止吧。"
else:
    label Iwillnotanwser2:
    $ thenQError += 1
    if thenQError == 3:
        jump thenResponseHelp1
    else:
        $ renpy.jump("thenmyanswer" + str(renpy.random.randint(1, 5)))
jump QnAstart

label thenmyanswer1:
    "啊，或许你可以提出别的问题。"
    jump QnAstart
label thenmyanswer2:
    "我是不会回答这个问题的。"
    jump QnAstart
label thenmyanswer3:
    "你可以提出这个问题，但是恕我不会回答。"
    jump QnAstart
label thenmyanswer4:
    "作者眨了眨眼睛，保持沉默。"
    "应该要提出更有价值的话题。"

    jump QnAstart
label thenmyanswer5:
    "是吗？你就想问这个？"
    "那我建议你换一个问题。"
    jump QnAstart
label thenResponseHelp1:
    "你难道不好奇我喜欢什么吗？"
    "或者这个游戏是什么？"
    "或者主角的名字的来历？"
    "请务必用小写的英文提问。"
    $ thenQError == 0
    jump QnAstart

label afterQnA2:
    "谢天谢地，提问环节结束了。"

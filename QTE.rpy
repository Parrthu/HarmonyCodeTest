label qtedefine:
#button,button是QTE按钮，bar是QTE时间条，thumb是滑动槽。将他们都放入images文件夹。
init -1 image qte_button:
    "button.png"
    pause 0.2
    "button2.png"
    pause 0.2
    repeat

init -1 image qte_bar:
    "left.png"

init -1 image qte_thumb:
    "thumb.png"

# 滑动块不带参的变换
transform qte_thumb_trans:
    xpos 0
    linear 2.0 xpos 400

init python:
    class QTE:
        #对象初始化时对各个参数赋值
        def __init__(self, qte_button=None, qte_bar=None , qte_thumb=None):
            #三个基础部件，按钮、时间条、滑动槽
            self.qte_button=qte_button
            self.qte_bar=qte_bar
            self.qte_thumb=qte_thumb

            self.qte_button_trans = None
            self.qte_bar_trans = None
            self.qte_thumb_trans = None

        def set_button(self, qte_button=None, trans=None):
            self.qte_button = qte_button
            self.qte_button_trans = trans

        def set_bar(self, qte_bar=None, trans=None):
            self.qte_bar = qte_bar
            self.qte_bar_trans = trans

        def set_thumb(self, qte_thumb=None, trans=None):
            self.qte_thumb = qte_thumb
            self.qte_thumb_trans = trans

        def add_qte(self, offset, sv, sv_value, sv_all=None, sv_all_value=None):
            action = [SetScreenVariable(sv,sv_value-1)]
            if sv_all != None:
                action.append(SetScreenVariable(sv_all, sv_all_value-1))

            ui.fixed()
            if self.qte_button != None:
                if self.qte_button_trans == None:
                    ui.imagebutton(idle=self.qte_button, offset=offset, action=action)
                else:
                    ui.imagebutton(idle=self.qte_button, offset=offset, action=action, at=self.qte_button_trans)

            if self.qte_bar != None:
                if self.qte_bar_trans == None:
                    ui.add(self.qte_bar, offset=offset)
                else:
                    ui.add(self.qte_bar, offset=offset, at=self.qte_bar_trans)

            if self.qte_thumb != None:
                if self.qte_thumb_trans == None:
                    ui.add(self.qte_thumb, offset=offset)
                else:
                    ui.add(self.qte_thumb, offset=offset, at=self.qte_thumb_trans)
            ui.close()

screen QTE():
    #首先需要创建QTE生成器的对象
    python:
        qte = QTE("qte_button", "qte_bar", "qte_thumb")
        qte.set_thumb("qte_thumb", qte_thumb_trans)

    default qte1=1
    default qte2=2
    default qte_all=6
    if qte1:
        $ qte.add_qte((0,0), "qte1", qte1, "qte_all", qte_all)

    if qte2:
        $ qte.add_qte((200,200), "qte2", qte2, "qte_all", qte_all)

    default qte3=3
    if qte3:
        $ qte.add_qte((400,400), "qte3", qte3, "qte_all", qte_all)

    #总体的计时器，时间到了就返回False，gg
    timer 3.5 action Return(False)

    #每过一段时间检测是否当前所有按钮已按下，全按了则返回True
    #如果与总体的计时器同时到了时间，目前看来这个 计时器更先判定，但不排除风险可能
    timer 0.5:
        if qte_all:
            action NullAction()
        else:
            action Return(True)
        repeat True
        
#在主线中使用
label main:
   "一堆剑飞过来了！！"
   call screen QTE()
   if _return = True:
      "躲过去了。"
   else:
      "失败了。"

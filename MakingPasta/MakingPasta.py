from bangtal import *

setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene1 = Scene('스파게티 게임', 'Images/food-1932466_1920.jpg')
scene2 = Scene('요리사 킹카의 설명!', 'Images/wood-2142241_1920.jpg')
scene3 = Scene('마트에 도착했어!', 'Images/123.png')
scene4 = Scene('마트에 도착했어!', 'Images/123.png')
scene5 = Scene('마트에 도착했어!', 'Images/123.png')
scene6 = Scene('마트에 도착했어!', 'Images/123.png')
scene7 = Scene('마트에 도착했어!', 'Images/123.png')
scene8 = Scene('계산을 할거야!!', 'Images/apples-1841132_1920.jpg')
scene9 = Scene('집에 도착했어!!', 'Images/kitchen-2165756_1920.jpg')
scene10 = Scene('완성했어!!', 'Images/spaghetti-1392266_1920.jpg')

sound1 = Sound("Audios/namnam.mp3")
sound2 = Sound("Audios/Tales.mp3")

sound2.play(loop = True)

startButton = Object('Images/pngegg.png')
startButton.setScale(0.5)
startButton.locate(scene1, 50, 80)
startButton.show()

soundon = Object('Images/soundon.png')
soundon.setScale(0.3)
soundon.locate(scene1,1070,220)
soundon.show()

soundoff = Object('Images/soundoff.png')
soundoff.setScale(0.2)
soundoff.locate(scene1,1070,190)



FLAG = Object('Images/게임!.png')
FLAG.locate(scene1, 590, 20)
FLAG.show()

Daddy = Object('Images/5-1.png')
Daddy.locate(scene1, 50, 150)
Daddy.show()

KINGKA = Object('Images/5-2.png')
KINGKA.locate(scene2,0,100)
KINGKA.show()

NINGKA = Object('Images/5-4.png')
NINGKA.locate(scene9,0,100)
NINGKA.show()

QueenKA = Object('Images/5-3.png')
QueenKA.setScale(1.5)
QueenKA.locate(scene8,150,10)
QueenKA.show()

tomatoma = Object('Images/1.png')
tomatoma.setScale(1.0)
tomatoma.locate(scene9,500,300)

knife = Object('Images/hiclipart.png')
knife.setScale(1.0)
knife.locate(scene9, 300, 250)

Saying = Object('Images/323123.png')
Saying.locate(scene2,470,50)
Saying.show()

NextButton = Object('Images/clipart529527.png')
NextButton.setScale(0.1)
NextButton.locate(scene2,1120,20)
NextButton.show()

NextButton2 = Object('Images/clipart529527.png')
NextButton2.setScale(0.1)
NextButton2.locate(scene3,1120,20)
NextButton2.show()

NextButton3 = Object('Images/clipart529527.png')
NextButton3.setScale(0.1)
NextButton3.locate(scene4,1120,20)
NextButton3.show()

NextButton4 = Object('Images/clipart529527.png')
NextButton4.setScale(0.1)
NextButton4.locate(scene5,1120,20)
NextButton4.show()

NextButton5 = Object('Images/clipart529527.png')
NextButton5.setScale(0.1)
NextButton5.locate(scene6,1120,20)
NextButton5.show()

NextButton6 = Object('Images/clipart529527.png')
NextButton6.setScale(0.1)
NextButton6.locate(scene7,1120,20)
NextButton6.show()

Noodle = Object('Images/6.png')
Noodle.setScale(0.4)
Noodle.locate(scene3,330,290)
Noodle.show()

Soy = Object('Images/7.png')
Soy.setScale(0.6)
Soy.locate(scene3,530,245)
Soy.show()

Garlic = Object('Images/8.png')
Garlic.setScale(0.7)
Garlic.locate(scene3,810,195)
Garlic.show()

Meat = Object('Images/9.png')
Meat.setScale(0.4)
Meat.locate(scene4,270,265)
Meat.show()

Bananakick = Object('Images/10.png')
Bananakick.setScale(0.4)
Bananakick.locate(scene4,610,265)
Bananakick.show()

godung = Object('Images/11.png')
godung.setScale(0.5)
godung.locate(scene4,790,230)
godung.show()

nam = Object('Images/nam.png')
nam.setScale(1.0)
nam.locate(scene9,300,0)

Mush = Object('Images/12.png')
Mush.setScale(0.2)
Mush.locate(scene5,270,265)
Mush.show()

Oil = Object('Images/13.png')
Oil.setScale(0.2)
Oil.locate(scene5,610,275)
Oil.show()

Onion = Object('Images/14.png')
Onion.setScale(0.2)
Onion.locate(scene5,800,265)
Onion.show()

Salt = Object('Images/15.png')
Salt.setScale(0.2)
Salt.locate(scene6,270,265)
Salt.show()

Tomato1 = Object('Images/16.png')
Tomato1.setScale(0.5)
Tomato1.locate(scene9, 570, 245)

chocolate = Object('Images/pngwingcom.png')
chocolate.setScale(0.15)
chocolate.locate(scene6,610,275)
chocolate.show()

tomato = Object('Images/16.png')
tomato.setScale(0.19)
tomato.locate(scene6,850,265)
tomato.show()

Bacon = Object('Images/17.png')
Bacon.setScale(0.4)
Bacon.locate(scene7,270,265)
Bacon.show()

ket = Object('Images/023.png')
ket.setScale(0.4)
ket.locate(scene7,610,275)
ket.show()

Butter = Object('Images/19.png')
Butter.setScale(0.5)
Butter.locate(scene7,850,265)
Butter.show()

Price = Object('Images/28000원.png')
Price.setScale(0.7)
Price.locate(scene8,100,150)
Price.show()

Price2 = Object('Images/29000원.png')
Price2.setScale(0.7)
Price2.locate(scene8,100,300)
Price2.show()

Price3 = Object('Images/30000원.png')
Price3.setScale(0.7)
Price3.locate(scene8,100,450)
Price3.show()

Price4 = Object('Images/31000원.png')
Price4.setScale(0.7)
Price4.locate(scene8,800,150)
Price4.show()

Price5 = Object('Images/32000원.png')
Price5.setScale(0.7)
Price5.locate(scene8,800,300)
Price5.show()

Price6 = Object('Images/33000원.png')
Price6.setScale(0.7)
Price6.locate(scene8,800,450)
Price6.show()

NoNo = Object('Images/22.png')
NoNo.setScale(0.8)
NoNo.locate(scene9,330,90)

hey = 0
hed = 0
gray = 1
totomama=0
total=0

timer = Timer(10.)

pot = Object('Images/nana.png')
pot.setScale(1.0)
pot.locate(scene9,450,90)

def soundon_onMouseAction(x,y,action):
    sound2.stop()
    soundon.hide()
    soundoff.show()
soundon.onMouseAction = soundon_onMouseAction

def soundoff_onMouseAction(x,y,action):
    sound2.play()
    soundon.show()
    soundoff.hide()
soundoff.onMouseAction = soundoff_onMouseAction

def pot_onMouseAction(x,y,action):
    global total
    if NoNo.inHand():
        NoNo.drop()
        NoNo.hide()
        total = total + 1
    if tomatoma.inHand():
        tomatoma.drop()
        tomatoma.hide()
        total = total + 1
    if knife.inHand():
        showMessage('칼도 넣으려고?ㅋㅋ')
    if Butter.inHand():
        Butter.drop()
        Butter.hide()
        total = total + 1
    if ket.inHand():
        ket.drop()
        ket.hide()
        total = total + 1
    if Bacon.inHand():
        Bacon.drop()
        Bacon.hide()
        total = total + 1
    if Salt.inHand():
        Salt.drop()
        Salt.hide()
        total = total + 1
    if Onion.inHand():
        Onion.drop()
        Onion.hide()
        total = total + 1
    if Oil.inHand():
        Oil.drop()
        Oil.hide()
        total = total + 1
    if Mush.inHand():
        Mush.drop()
        Mush.hide()
        total = total + 1
    if Garlic.inHand():
        Garlic.drop()
        Garlic.hide()
        total = total + 1
    if total == 10:
        global hed
        hed = hed + 1
        timer.set(20.)
        sound1.play(True)
        timer.start()
pot.onMouseAction = pot_onMouseAction

def nam_onMouseAction(x,y,action):
    if Noodle.inHand():
        sound1.play(True)
        Noodle.drop()
        Noodle.hide()
        NoNo.show()
        showTimer(timer)
        timer.set(10.)
        timer.start()
        global hey
        hey=hey + 1
nam.onMouseAction = nam_onMouseAction

def timer_onTimeout():
    global hey
    global hed
    if hey == 1:
        showMessage('면이 다 끓었어! 면을 꺼내주자')
        sound1.stop()
        global gray
        gray=gray-1
        hey=False
    if hed == 1:
        sound1.stop()
        showMessage('스파게티가 완성되었어! 맛있게 먹자!')
        scene10.enter()
timer.onTimeout = timer_onTimeout

def NoNo_onMouseAction(x,y,action):
    if gray==0:
        NoNo.pick()
        nam.hide()
        pot.show()
        showMessage('이제 남은 재료들을 다 use item 해서 냄비에 넣자!')
NoNo.onMouseAction = NoNo_onMouseAction
def tomatoma_onMouseAction(x,y,action):
    tomatoma.pick()
    nam.show()
    showMessage('이제 사온 면을 Use item하고 팬에 넣자!')
tomatoma.onMouseAction = tomatoma_onMouseAction

def Tomato1_onMouseAction(x,y,action):
    if knife.inHand():
        global totomama
        totomama = totomama +1
        if totomama==10:
            tomato.drop()
            tomato.hide()
            Tomato1.hide()
            tomatoma.show()
            showMessage('잘했어! 이제 토마토를 집어')
Tomato1.onMouseAction = Tomato1_onMouseAction

def knife_onMouseAction(x,y,action):
    knife.pick()
    showMessage('칼을들고 토마토를 연타하면 다져질거야')
knife.onMouseAction = knife_onMouseAction

def Price_onMouseAction(x, y, action):
    showMessage('틀렸습니다!')
Price.onMouseAction = Price_onMouseAction

def Price2_onMouseAction(x, y, action):
    showMessage('틀렸습니다!')
Price2.onMouseAction = Price2_onMouseAction

def Price3_onMouseAction(x, y, action):
    showMessage('틀렸습니다!')
Price3.onMouseAction = Price3_onMouseAction

def Price5_onMouseAction(x, y, action):
    showMessage('틀렸습니다!')
Price5.onMouseAction = Price5_onMouseAction

def Price6_onMouseAction(x, y, action):
    showMessage('틀렸습니다!')
Price6.onMouseAction = Price6_onMouseAction

def Price4_onMouseAction(x, y, action):
    scene9.enter()
    showMessage('정답입니다! 집에 도착!')
Price4.onMouseAction = Price4_onMouseAction

def startButton_onMouseAction(x,y,action):
    scene2.enter()
startButton.onMouseAction = startButton_onMouseAction

def NextButton_onMouseAction(x,y,action):
    scene3.enter()
NextButton.onMouseAction = NextButton_onMouseAction

def Noodle_onMouseAction(x, y, action):
    Noodle.pick()
    Noodle.picked=True
    showMessage('스파게티 면은 2000원이야!')
Noodle.onMouseAction = Noodle_onMouseAction

def Soy_onMouseAction(x, y, action):
    showMessage('토마토 스파게티에 간장...? 별난친구네')
Soy.onMouseAction = Soy_onMouseAction

def Bananakick_onMouseAction(x, y, action):
    showMessage('토마토 스파게티에 바나나킥...? 별난친구네')
Bananakick.onMouseAction = Bananakick_onMouseAction

def Meat_onMouseAction(x, y, action):
    showMessage('토마토 스파게티에 목살...? 별난친구네')
Meat.onMouseAction = Meat_onMouseAction

def godung_onMouseAction(x, y, action):
    showMessage('토마토 스파게티에 고등어...? 별난친구네')
godung.onMouseAction = godung_onMouseAction

def chocolate_onMouseAction(x, y, action):
    showMessage('토마토 스파게티에 초콜릿...? 별난친구네')
chocolate.onMouseAction = chocolate_onMouseAction

def Garlic_onMouseAction(x, y, action):
    Garlic.pick()
    Garlic.picked=True
    showMessage('다진마늘은 1500원이야!')
Garlic.onMouseAction = Garlic_onMouseAction

def Mush_onMouseAction(x, y, action):
    Mush.pick()
    Mush.picked=True
    showMessage('버섯은 1500원이야!')
Mush.onMouseAction = Mush_onMouseAction

NINGKA.picked=False
def NINGKA_onMouseAction(x, y, action):
    if NINGKA.picked==False:
        showMessage('요리를 시작할거야! 칼을 사용해서 토마토를 다져봐!')
        Tomato1.show()
        knife.show()
        NINGKA.picked=True
NINGKA.onMouseAction = NINGKA_onMouseAction

def Oil_onMouseAction(x, y, action):
    Oil.pick()
    Oil.picked=True
    showMessage('올리브오일은 9500원이야!')
Oil.onMouseAction = Oil_onMouseAction

def Onion_onMouseAction(x, y, action):
    Onion.pick()
    Onion.picked=True
    showMessage('양파는 1500원이야!')
Onion.onMouseAction = Onion_onMouseAction

def Salt_onMouseAction(x, y, action):
    Salt.pick()
    Salt.picked=True
    showMessage('소금는 1500원이야!')
Salt.onMouseAction = Salt_onMouseAction

def tomato_onMouseAction(x, y, action):
    tomato.pick()
    tomato.picked=True
    showMessage('토마토는 4500원이야!')
tomato.onMouseAction = tomato_onMouseAction

def Butter_onMouseAction(x, y, action):
    Butter.pick()
    Butter.picked=True
    showMessage('버터는 3500원이야!')
Butter.onMouseAction = Butter_onMouseAction

def Bacon_onMouseAction(x, y, action):
    Bacon.pick()
    Bacon.picked=True
    showMessage('베이컨은 4000원이야!')
Bacon.onMouseAction = Bacon_onMouseAction

def ket_onMouseAction(x, y, action):
    ket.pick()
    ket.picked=True
    showMessage('케첩은 1500원이야!')
ket.onMouseAction = ket_onMouseAction

def NextButton_onMouseAction(x,y,action):
    scene3.enter()
NextButton.onMouseAction = NextButton_onMouseAction

def NextButton2_onMouseAction(x,y,action):
    if Noodle.picked==True and Garlic.picked==True:
        scene4.enter()
    else:
        showMessage('필요한걸 아직 사지 않았어!')
NextButton2.onMouseAction = NextButton2_onMouseAction

def NextButton3_onMouseAction(x,y,action):
    scene5.enter()
NextButton3.onMouseAction = NextButton3_onMouseAction

def NextButton4_onMouseAction(x,y,action):
    if Mush.picked==True and Oil.picked==True and Onion.picked==True:
        scene6.enter()
    else:
        showMessage('필요한걸 아직 사지 않았어!')
NextButton4.onMouseAction = NextButton4_onMouseAction

def NextButton5_onMouseAction(x,y,action):
    if Salt.picked==True and tomato.picked==True:
        scene7.enter()
    else:
        showMessage('필요한걸 아직 사지 않았어!')
NextButton5.onMouseAction = NextButton5_onMouseAction

def NextButton6_onMouseAction(x,y,action):
    if Butter.picked==True and Bacon.picked==True and ket.picked==True:
        scene8.enter()
        showMessage('산 물건을 계산할거에요! 자 얼마죠?')
    else:
        showMessage('필요한걸 아직 사지 않았어!')
NextButton6.onMouseAction = NextButton6_onMouseAction

startGame(scene1)


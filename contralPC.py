import pyautogui as auto
import time,socket
auto.FAILSAFE=True


print(auto.size())
width,height=auto.size()
print(width,height)

auto.hotkey('winleft','i')
time.sleep(2)
auto.hotkey('winleft','up')
# currentMouseX,currentMouseY=auto.position()
# print(currentMouseX,currentMouseY)
#
auto.click(952,222,clicks=1,interval=0.0,button='left',duration=0.0,tween=auto.linear)
time.sleep(2)
print('1111111111')
# auto.click(1159,477,clicks=1,interval=0.0,button='left',duration=0.0,tween=auto.linear)
# time.sleep(2)
# print('2222222')
# auto.click(459,139,clicks=1,interval=0.0,button='left',duration=0.0,tween=auto.linear)
# currentMouseX,currentMouseY=auto.position()

# print(currentMouseX,currentMouseY)
# time.sleep(5)
# print('3333')
# auto.click(1126,535,clicks=1,interval=0.0,button='left',duration=0.0,tween=auto.linear)
# currentMouseX,currentMouseY=auto.position()
# print(currentMouseX,currentMouseY)
# time.sleep(10)
# # pic_1=auto.screenshot()
# # pic_2=auto.screenshot('blueteethname.png')
# # devices=auto.locateOnScreen('blueteethname.png')
# # print(devices)
# # X=devices[2]
# # Y=devices[3]
# # print(X,Y)
# # auto.click(X,Y,clicks=2)
# # print('44444444444444')
# # X1,Y1=auto.center('blueteethname.png')
# # auto.click(devices)
# # auto.click(X1,Y1)
# # auto.locateOnScreen('blueteethname.png',grayscale=False)
# # time.sleep(5)
# # tupian=auto.locateOnScreen('lianjie.png')
# # auto.click(tupian)
# # print(tupian)
# while True:
# 	dev=auto.locateCenterOnScreen(r'H:\CloudMusic\blueteethname.png',grayscale=False)
# 	print(dev)
# 	auto.click(dev)
#
# 	time.sleep(5)
# 	dev1=auto.locateCenterOnScreen(r'H:\CloudMusic\lianjie.png',grayscale=False)
# 	print(dev1)
# 	auto.click(dev1)
# 	break
# time.sleep(5)
# dev2=auto.locateCenterOnScreen(r'H:\CloudMusic\finish.png',grayscale=False)
# print(dev2)
# auto.click(dev2)
time.sleep(2)
dev3=auto.locateCenterOnScreen(r'H:\CloudMusic\deldevice.png',grayscale=False)
print(dev3)
auto.click(dev3)
time.sleep(2)

dev4=auto.locateCenterOnScreen(r'H:\CloudMusic\deleet.png',grayscale=False)
print(dev4)
auto.click(dev4)
time.sleep(2)
dev5=auto.locateCenterOnScreen(r'H:\CloudMusic\queding.png',grayscale=False)
print('777777777777777')
print(dev5)
auto.click(dev5,clicks=2)


# auto.hotkey('return')
# auto.hotkey('return')
time.sleep(2)
auto.hotkey('Alt','f4')
# auto.hotkey('Alt','f4')

print('結束')
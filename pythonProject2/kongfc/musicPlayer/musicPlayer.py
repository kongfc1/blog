import os
import time
import tkinter
import threading
import tkinter.filedialog
import pygame

root = tkinter.Tk(); # 创建窗口
root.title('孔万三音乐播放器') # 设置窗口标题
# 调整窗口大小和位置，单位是像素
width,height = 460,600
x,y=500,100
# root.geometry('800x600+100+100')
root.geometry(f'{width}x{height}+{x}+{y}')
root.config(bg='#cccccc')


folder =''
res = []
num = 0
now_music = ''

def buttonChooseClick():
    global folder
    global res
    if not folder:
        folder = tkinter.filedialog.askdirectory()
        musics = [folder + '\\' + music
                  for music in os.listdir(folder) \
\
                  if music.endswith(('.mp3','.wav'))]
        ret = []
        for i in musics:
            ret.append(i.split('\\')[1:])
            ret.append(i.replace('\\','/'))

        var2 = tkinter.StringVar()
        var2.set(ret)
        lb = tkinter.Listbox(root, listvariable=var2)
        lb.place(x=50, y=100, width=260, height=300)
    if not folder:
        return

    global playing
    playing = True
    buttonPlay = 'normal'
    buttonStop = 'normal'

    # buttonPlay['state'] = 'normal'
    # buttonStop['state'] = 'normal'
    # pause_resume.set('播放')

def play():
    if len(res):
        pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                nextMusic = res[num]
                print(nextMusic)
                print(num)
                pygame.mixer.music.load(nextMusic.encode())
                pygame.mixer.music.play(1)
                if len(res) - 1 == num:
                    num = 0
                else:
                    num = num + 1
                nextMusic = nextMusic.split('\\')[1:]
                musicName.set('playing...' + ''.join(nextMusic))
            else:
                time.sleep(0.1)

def buttonPlayClick():
    pass

def buttonStopClick():
    pass

def buttonNextClick():
    pass

def closeWindow():
    pass

def control_voice(value=0.5):
    pass

def buttonPrevClick():
    pass


root.protocol('WM_DELETE_WINDOW',closeWindow)

buttonChoose = tkinter.Button(root,text='添加',command=buttonChooseClick())
buttonChoose.place(x=50,y=10,width=50,height=20)

pause_resume = tkinter.StringVar(root,value='播放')
buttonPlay = tkinter.Button(root,textvariable=pause_resume,command=buttonPlayClick())
buttonPlay.place(x=190,y=10,width=50,height=20)
buttonPlay['state'] = 'disabled'

buttonStop = tkinter.Button(root,text='停止')
buttonStop.place(x=120,y=10,width=50,height=20)
buttonStop['state'] = 'disabled'

buttonNext = tkinter.Button(root,text='下一首')
buttonNext.place(x=260,y=10,width=50,height=20)
buttonNext['state'] = 'disabled'

buttonNext = tkinter.Button(root,text='上一首')
buttonNext.place(x=330,y=10,width=50,height=20)
buttonNext['state'] = 'disabled'

musicName = tkinter.StringVar(root,value='稍等，请添加音乐。。。')
lableName = tkinter.Label(root,textvariable=musicName)
lableName.place(x=10,y=30,width=260,height=20)

s = tkinter.Scale(root,label='音量',from_=0,to=1,orient=tkinter.HORIZONTAL,length=240,showvalue=0,tickinterval=2,resolution=0.1)
s.place(x=50,y=50,width=200)

#生成窗口
root.mainloop()

























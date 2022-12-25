import pygame, sys
import random
sys.path.append("/Users/akashkesani/Desktop/projects/V8_game_engine")

from engine.play.entity import gamelooper,frameviewer
from engine.play.action import display,terminate,loop


GM = gamelooper.GameLooper()
FV = frameviewer.FrameViewer((1280,720))

display = display.Display()
terminate = terminate.Terminate()
loop = loop.Loop()


FV.insert_action(display)
FV.insert_action(terminate)
GM.insert_action(loop)

GM.loopActions.append(display)
GM.eventActions.append(terminate)

loop.act()




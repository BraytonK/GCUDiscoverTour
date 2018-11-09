#By: Brayton Kerekffy
from mcpi.minecraft import Minecraft
import RPi.GPIO as GPIO
import random
import time
mc = Minecraft.create()

goldOre = 14
sandBlock = 12
lava = 8
greenLight = 14
onTriggerBlock = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(greenLight,GPIO.OUT)
def createBoard():
    x,y,z = mc.player.getPos()
    mc.setBlocks(x+3,y,goldOre)
    mc.postToChat("yooyoyoyoyo")
    
def lightBlink():
    #print('blink')
    GPIO.output(greenLight, True)
    time.sleep(0.25)
    GPIO.output(greenLight, False)
    time.sleep(0.25)

def diamondDetecter():
    try:
        while True:
            x,y,z = mc.player.getPos()
            for i in range(15):
                #print('in range')
                if mc.getBlock(x,y-i,z) == 56:
                    #print('made it')
                    lightBlink()
    except KeyboardInterrupt:
        GPIO.cleanup()
        
def onHoverCraftMaterial():
    #createBoard()
    while True:
        x,y,z = mc.player.getPos()
        block_under_player = mc.getBlock(x,y - 1,z)
        if block_under_player == goldOre:
            #random_time = random.uniform(0.1, 1.5)
            #time.sleep(random_time);
            mc.player.setPos(x,y+50, z)
            x,y,z = mc.player.getPos()
            #mc.setBlock(x,y-1,z,sandBlock)
            onTriggerBlock = True
            while(onTriggerBlock == True):
                if(y<15):
                    onTriggerBlock = False
                x,y,z = mc.player.getPos()
                mc.setBlock(x,y-2,z,sandBlock)
        
            
            #mc.postToChat("RUN!")
    
onHoverCraftMaterial()


    
    


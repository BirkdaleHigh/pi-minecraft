from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()

mc.setBlock(0,30,0,
            block.MELON)
starttime=time.time()
while time.time()-starttime<30:
    mc.postToChat("Time left: " + str(30-(time.time()-starttime)) [0:2])


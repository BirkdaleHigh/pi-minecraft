from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()
while True:
    xyz=mc.player.getPos()
    stoodOn=mc.getBlock(xyz.x,xyz.y-1,xyz.z)
    mc.postToChat('You are stood on'+str(stoodOn)) 

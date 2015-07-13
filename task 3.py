from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()

while True:
    xyz=mc.player.getPos()
    if xyz.y<5:
        mc.player.setPos(xyz.x,50,xyz.z)

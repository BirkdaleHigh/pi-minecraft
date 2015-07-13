from mcpi import minecraft
from mcpi import block
import time

mc = minecraft.Minecraft.create()

xyz=mc.player.getPos()
for countUp in range(0,10):
    mc.setBlock(xyz.x+5,xyz.y+countUp,xyz.z,block.WOOL.id, 3)

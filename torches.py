from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()
mc.player.setPos(0,20,0)
red=block.WOOL.id, 14
for countUp in range(0,200):
    mc.setBlock(0,countUp,0,red)
mc=minecraft.Minecraft.create()
mc.player.setPos(0,20,0)
red=block.WOOL.id, 14
for countUp in range(0,200):
    mc.setBlock(1,countUp,0,red)

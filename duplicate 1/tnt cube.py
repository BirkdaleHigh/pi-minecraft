from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()
tnt=46
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)
mc.setBlocks(x-2, y-2, z-2, x-12, y-12, z-12, tnt, 1)

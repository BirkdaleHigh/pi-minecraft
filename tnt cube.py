from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()
obsidian=49
x, y, z = mc.player.getPos()
mc.setBlocks(-121.5+1, 6.0+1, 73.7+1, -121.5+11, 6.0+11, 73.7+11, obsidian, 1)
mc.setBlocks(-121.5-2, 6.0-2, 73.7-2, -121.5-12, 6.0-12, 73.7-12, obsidian, 1)

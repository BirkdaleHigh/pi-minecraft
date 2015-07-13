from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()
while True:
    xyz=mc.player.getPos()
    mc.postToChat(xyz)


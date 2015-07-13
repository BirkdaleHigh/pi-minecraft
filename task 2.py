from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()

while True:
    time.sleep(5)
    mc.player.setPos(0,50,0)

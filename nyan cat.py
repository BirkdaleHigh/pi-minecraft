from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()
while True:
    xyz=mc.player.getPos()
    mc.setBlock(xyz.x-3,xyz.y,xyz.z, block.WOOL.id, 1)
    mc.setBlock(xyz.x-3,xyz.y+1,xyz.z, block.WOOL.id, 2)
    mc.setBlock(xyz.x-3,xyz.y+2,xyz.z, block.WOOL.id, 5)
    mc.setBlock(xyz.x-3,xyz.y+3,xyz.z, block.WOOL.id, 6)

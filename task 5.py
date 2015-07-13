from mcpi import minecraft
from mcpi import block
import time

mc=minecraft.Minecraft.create()

xyz=mc.player.getPos()
mc.setBlock(xyz.x,xyz.y,xyz.z-2, block.WOOL.id, 5)
mc.setBlock(xyz.x,xyz.y,xyz.z+2, block.WOOL.id, 10)

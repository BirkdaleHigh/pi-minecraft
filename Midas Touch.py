from mcpi import minecraft
import time
mc = minecraft.Minecraft.create()

flower = [37,38]
water = 9
air = 0

while True:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y, pos.x)
    if blockBelow == air:
        mc.setBlock(pos.x, pos.y, pos.z, flower)
        time.sleep(0.1)


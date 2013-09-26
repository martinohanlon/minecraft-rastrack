import math

gridRef = "SO878900"

#get numeric value of letter reference A->0, B->1, C->2, etc
letter1 = ord(gridRef[0:1])-65
letter2 = ord(gridRef[1:2])-65
#shuffle down letters after 'I' [since 'I' is not used in grid]
if letter1 > 7: letter1 -= 1
if letter2 > 7: letter2 -= 1

print letter1
print letter2

#convert grid letters into 100km-square indexes from false origin (grid square SV)
ea = ((letter1 - 2) % 5) * 5 + (letter2 % 5)
no = (19 - math.floor(letter1 / 5) * 5) - math.floor(letter2 / 5)
tp_ea = ea * 2000
tp_no = 28000 - (no * 2000)

# skip grid letters to get numeric part of ref
gridRefNos = gridRef[2:]
ea = gridRefNos[:len(gridRefNos)/2]
no = gridRefNos[len(gridRefNos)/2:]

print gridRefNos
print ea
print no

# normalise to 1m grid, rounding up to centre of grid square
#  100m (three-figure)
if len(gridRefNos) == 6: multiplier = 2
#  1000m (two figure
if len(gridRefNos) == 4: multiplier = 20
tp_ea = tp_ea + (int(ea) * multiplier)
tp_no = tp_no - (int(no) * multiplier)

print tp_ea
print tp_no

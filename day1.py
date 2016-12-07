heading = 90
y = 0
x = 0
history =[]


d ="R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1"
#d = "R8, R4, R4, R8"
directions = d.split(', ')
end = len(directions)

match = False
for i in range(0, end):
    movement = directions[i]
    stop = len(movement)
    forward = movement[1:stop]
    if movement[0] == 'R':
        heading = (heading - 90) % 360
    else:
        heading = (heading + 90) % 360

    if heading == 0:
        for j in range(1, int(forward)+1):
            coord = x+j, y
            if coord in history:
                if match == False:
                    match = coord
            history.append(coord)
        x = x + int(forward)
    elif heading == 90:
        for j in range(1, int(forward)+1):
            coord = x, y+j
            if coord in history:
                if match == False:
                    match = coord
            history.append(coord)
        y = y + int(forward)
    elif heading == 180:
        for j in range(1, int(forward)+1):
            coord = x-j, y
            if coord in history:
                if match == False:
                    match = coord
            history.append(coord)
        x = x - int(forward)
    else:
        for j in range(1, int(forward)+1):
            coord = x, y-j
            if coord in history:
                if match == False:
                    match = coord
            history.append(coord)
        y = y - int(forward)

print "x's:", x
print "y's:", y

if x < 0:
    x = x * (-1)
if y < 0:
    y = y * (-1)

print heading
print 'actual bunny:', match

distance = x + y
print distance

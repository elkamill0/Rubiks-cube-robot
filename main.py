from functions import set_digts
def start():
    global up, left, front, right, back, down
    up =    [0,0,0,0,0,0,0,0,0]
    left =  [0,0,0,0,0,0,0,0,0]
    front = [0,0,0,0,0,0,0,0,0]
    right = [0,0,0,0,0,0,0,0,0]
    back =  [0,0,0,0,0,0,0,0,0]
    down =  [0,0,0,0,0,0,0,0,0]
start()

def scramble(word):
    global ret
    counter = 0
    word1 = word.split(" ")
    global scramble_move
    for scramble_move in word1:
        if scramble_move == 'R':
            ret = R(right)
        elif scramble_move == "R'":
            ret = Rp(right)
        elif scramble_move == 'R2':
            ret = double(right, R, Rp)
        elif scramble_move == "L":
            ret = L(left)
        elif scramble_move == "L'":
            ret = Lp(left)
        elif scramble_move == "L2":
            ret = double(left, L, Lp)
        elif scramble_move == "U":
            ret = U(up)
        elif scramble_move == "U'":
            ret = Up(up)
        elif scramble_move == "U2":
            ret = double(up, U, Up)
        elif scramble_move == "D":
            ret = D(down)
        elif scramble_move == "D'":
            ret = Dp(down)
        elif scramble_move == "D2":
            ret = double(down, D, Dp)
        elif scramble_move == "F":
            ret = F(front)
        elif scramble_move == "F'":
            ret = Fp(front)
        elif scramble_move == "F2":
            ret = double(front, F, Fp)
        elif scramble_move == "B":
            ret = B(back)
        elif scramble_move == "B'":
            ret = Bp(back)
        elif scramble_move == "B2":
            ret = double(back, B, Bp)
        if ret:
            ret = False
            return counter
        counter += 1
    return counter

def new_arms(slots):
    new_arms_tab = []
    new_faces_tab = []
    for i in range(4):
        x = slots[i]
        if i == 0:
            if x[1] == 'X' or x[1] == 'x':
                new_arms_tab.append('UB')
                if x[1] == 'x':
                    new_faces_tab.append('U')
                else:
                    new_faces_tab.append('B')
            if x[3] == 'X' or x[3] == 'x':
                new_arms_tab.append('UL')
                if x[3] == 'x':
                    new_faces_tab.append('U')
                else:
                    new_faces_tab.append('L')
            if x[5] == 'X' or x[5] == 'x':
                new_arms_tab.append('UR')
                if x[5] == 'x':
                    new_faces_tab.append('U')
                else:
                    new_faces_tab.append('R')
            if x[7] == 'X' or x[7] == 'x':
                new_arms_tab.append('UF')
                if x[7] == 'x':
                    new_faces_tab.append('U')
                else:
                    new_faces_tab.append('F')
        elif i == 1:
            if x[1] == 'X' or x[1] == 'x':
                new_arms_tab.append('DF')
                if x[1] == 'x':
                    new_faces_tab.append('D')
                else:
                    new_faces_tab.append('F')
            if x[3] == 'X' or x[3] == 'x':
                new_arms_tab.append('DL')
                if x[3] == 'x':
                    new_faces_tab.append('D')
                else:
                    new_faces_tab.append('L')
            if x[5] == 'X' or x[5] == 'x':
                new_arms_tab.append('DR')
                if x[5] == 'x':
                    new_faces_tab.append('D')
                else:
                    new_faces_tab.append('R')
            if x[7] == 'X' or x[7] == 'x':
                new_arms_tab.append('DB')
                if x[7] == 'x':
                    new_faces_tab.append('D')
                else:
                    new_faces_tab.append('B')
        elif i == 2:
            if x[5] == 'X' or x[5] == 'x':
                new_arms_tab.append('FR')
                if x[5] == 'x':
                    new_faces_tab.append('F')
                else:
                    new_faces_tab.append('R')
            if x[3] == 'X' or x[3] == 'x':
                new_arms_tab.append('FL')
                if x[3] == 'x':
                    new_faces_tab.append('F')
                else:
                    new_faces_tab.append('L')
        elif i == 3:
            if x[5] == 'X' or x[5] == 'x':
                new_arms_tab.append('BL')
                if x[5] == 'x':
                    new_faces_tab.append('B')
                else:
                    new_faces_tab.append('L')
            if x[3] == 'X' or x[3] == 'x':
                new_arms_tab.append('BR')
                if x[3] == 'x':
                    new_faces_tab.append('B')
                else:
                    new_faces_tab.append('R')
    return new_arms_tab, new_faces_tab

def main(max, word, second_sequence, stop):
    cases = []
    faces = []
    cases1 = ['UB', 'UR', 'UF', 'UL', 'DB', 'DR', 'DF', 'DL', 'BL', 'BR', 'FR', 'FL']
    counter1 = 0
    if second_sequence is not None:
        n = new_arms(second_sequence)
        print("n:",n[0])
        print("m:   ",n[1])
        #result(up, left, front, right, back, down)

    counting = 0
    for i in range(63, 4033): #63-4033
        b = str(set_digts(i, 12))
        count = 0
        for j in b:
            if j == "1":
                count+=1
            if count > 6:
                break
        if count == 6:
            tab = []
            tab1 = []
            counter = 0
            for i in b:
                if i == "1":
                    tab.append(cases1[counter])
                counter += 1

            for i in range(64):
                end = False
                a = str(set_digts(i, 6))
                for j in range(len(tab)):
                    actual = tab[j][int(a[j])]
                    if actual in tab1:
                        tab1 = []
                        break
                    else:
                        tab1.append(tab[j][int(a[j])])
                        if len(tab1) == 6:
                            end = True
                            break
                if end:
                    counting += 1
                    #print(tab)
                    #print(tab1)
                    cases.append(tab)
                    faces.append(tab1)
                    set_arms(tab, tab1)
                    counter1 += 1

                    #result(up, left, front, right, back, down)
                    moves = scramble(word)
                    if moves >= max:
                        print("tab:", tab)
                        print("tab1:  ", tab1)
                        print("moves:", moves)
                        #result(up, left, front, right, back, down)
                        max = moves

                        s = [up, down, front, back]
                        #print("new:",new_arms(s))
                        #print()
                        #print(new_arms(s))
                        #return 0
                        if max >= len(word.split(" ")):
                            return 0
                    start()
                    break
    #print(counting)
    word = " ".join(word.split(" ")[max:])
    print(word)
    print("""

     """)

    main(0, word, s, True)

def set_arms(x, y):
    def arms_orientation(first, num1, second, num2):
        if y[i] == x[i][0]:
            first[num1] = 'x'
            second[num2] = 'X'
        else:
            first[num1] = 'X'
            second[num2] = 'x'
    for i in range(6):
        if x[i] == 'UB':
            arms_orientation(up,1,back,1)
        elif x[i] == 'UR':
            arms_orientation(up,5,right,1)
        elif x[i] == 'UF':
            arms_orientation(up,7,front,1)
        elif x[i] == 'UL':
            arms_orientation(up,3,left,1)
        elif x[i] == 'DB':
            arms_orientation(down,7,back,7)
        elif x[i] == 'DR':
            arms_orientation(down,5,right,7)
        elif x[i] == 'DF':
            arms_orientation(down,1,front,7)
        elif x[i] == 'DL':
            arms_orientation(down,3,left,7)
        elif x[i] == 'BL':
            arms_orientation(back,5,left,3)
        elif x[i] == 'BR':
            arms_orientation(back,3,right,5)
        elif x[i] == 'FR':
            arms_orientation(front,5,right,3)
        elif x[i] == 'FL':
            arms_orientation(front,3,left,5)
def result(up, left, front, right, back, down):
    print(f"    {up[0]}{up[1]}{up[2]}")
    print(f"    {up[3]}{up[4]}{up[5]}")
    print(f"    {up[6]}{up[7]}{up[8]}")
    print(f"    ---")
    print(f"{left[0]}{left[1]}{left[2]}|{front[0]}{front[1]}{front[2]}|{right[0]}{right[1]}{right[2]}|{back[0]}{back[1]}{back[2]}")
    print(f"{left[3]}{left[4]}{left[5]}|{front[3]}{front[4]}{front[5]}|{right[3]}{right[4]}{right[5]}|{back[3]}{back[4]}{back[5]}")
    print(f"{left[6]}{left[7]}{left[8]}|{front[6]}{front[7]}{front[8]}|{right[6]}{right[7]}{right[8]}|{back[6]}{back[7]}{back[8]}")
    print(f"    ---")
    print(f"    {down[0]}{down[1]}{down[2]}")
    print(f"    {down[3]}{down[4]}{down[5]}")
    print(f"    {down[6]}{down[7]}{down[8]}")
def flipp(name_layer):

    if name_layer[1] == 'x':
        name_layer[1], name_layer[3] = name_layer[3], name_layer[1]
    elif name_layer[5] == 'x':
        name_layer[5], name_layer[1] = name_layer[1], name_layer[5]
    elif name_layer[7] == 'x':
        name_layer[7], name_layer[5] = name_layer[5], name_layer[7]
    elif name_layer[3] == 'x':
        name_layer[3], name_layer[7] = name_layer[7], name_layer[3]
def flip(name_layer):
   if name_layer[1] == 'x':
       name_layer[1], name_layer[5] = name_layer[5], name_layer[1]
   elif name_layer[5] == 'x':
       name_layer[5], name_layer[7] = name_layer[7], name_layer[5]
   elif name_layer[7] == 'x':
       name_layer[7], name_layer[3] = name_layer[3], name_layer[7]
   elif name_layer[3] == 'x':
       name_layer[3], name_layer[1] = name_layer[1], name_layer[3]

def R(layer):
    crash = False
    if up[5] == "X":
        if back[3] == "x":
            crash = True
        else:
            up[5], back[3] = back[3], up[5]
    elif back[3] == "X":
        if down[5] == "x":
            crash = True
        else:
            back[3], down[5] = down[5], back[3]
    elif down[5] == "X":
        if front[5] == "x":
            crash = True
        else:
            down[5], front[5] = front[5], down[5]
    elif front[5] == "X":
        if up[5] == "x":
            crash = True
        else:
            front[5], up[5] = up[5], front[5]
    if crash:
        return True
    flip(layer)
    return False
def Rp(layer):
    crash = False
    if up[5] == "X":
        if front[5] == "x":
            crash = True
        else:
            up[5], front[5] = front[5], up[5]
    elif back[3] == "X":
        if up[5] == "x":
            crash = True
        else:
            back[3], up[5] = up[5], back[3]
    elif down[5] == "X":
        if back[3] == "x":
            crash = True
        else:
            down[5], back[3] = back[3], down[5]
    elif front[5] == "X":
        if down[5] == "x":
            crash = True
        else:
            front[5], down[5] = down[5], front[5]
    if crash:
        return True

    flipp(layer)
    return False
def L(layer):
    crash = False
    if up[3] == "X":
        if front[3] == "x":
            crash = True
        else:
            up[3], front[3] = front[3], up[3]
    elif back[5] == "X":
        if up[3] == "x":
            crash = True
        else:
            back[5], up[3] = up[3], back[5]
    elif down[3] == "X":
        if back[5] == "x":
            crash = True
        else:
            down[3], back[5] = back[5], down[3]
    elif front[3] == "X":
        if down[3] == "x":
            crash = True
        else:
            front[3], down[3] = down[3], front[3]
    if crash:
        return True

    flip(layer)
    return False
def Lp(layer):
    crash = False
    if up[3] == "X":
        if back[5] == "x":
            crash = True
        else:
            up[3], back[5] = back[5], up[3]
    elif back[5] == "X":
        if down[3] == "x":
            crash = True
        else:
            back[5], down[3] = down[3], back[5]
    elif down[3] == "X":
        if front[3] == "x":
            crash = True
        else:
            down[3], front[3] = front[3], down[3]
    elif front[3] == "X":
        if up[3] == "x":
            crash = True
        else:
            front[3], up[3] = up[3], front[3]
    if crash:
        return True

    flipp(layer)
    return False
def U(layer):
    crash = False
    if back[1] == "X":
        if right[1] == "x":
            crash = True
        else:
            back[1], right[1] = right[1], back[1]
    elif right[1] == "X":
        if front[1] == "x":
            crash = True
        else:
            right[1], front[1] = front[1], right[1]
    elif front[1] == "X":
        if left[1] == "x":
            crash = True
        else:
            front[1], left[1] = left[1], front[1]
    elif left[1] == "X":
        if back[1] == "x":
            crash = True
        else:
            left[1], back[1] = back[1], left[1]
    if crash:
        return True

    flip(layer)
    return False
def Up(layer):
    crash = False
    if back[1] == "X":
        if left[1] == "x":
            crash = True
        else:
            back[1], left[1] = left[1], back[1]
    elif left[1] == "X":
        if front[1] == "x":
            crash = True
        else:
            left[1], front[1] = front[1], left[1]
    elif front[1] == "X":
        if right[1] == "x":
            crash = True
        else:
            front[1], right[1] = right[1], front[1]
    elif right[1] == "X":
        if back[1] == "x":
            crash = True
        else:
            right[1], back[1] = back[1], right[1]
    if crash:
        return True

    flipp(layer)
    return False
def D(layer):
    crash = False
    if back[7] == "X":
        if left[7] == "x":
            crash = True
        else:
            back[7], left[7] = left[7], back[7]
    elif left[7] == "X":
        if front[7] == "x":
            crash = True
        else:
            left[7], front[7] = front[7], left[7]
    elif front[7] == "X":
        if right[7] == "x":
            crash = True
        else:
            front[7], right[7] = right[7], front[7]
    elif right[7] == "X":
        if back[7] == "x":
            crash = True
        else:
            right[7], back[7] = back[7], right[7]
    if crash:
        return True

    flip(layer)
    return False
def Dp(layer):
    crash = False
    if back[7] == "X":
        if right[7] == "x":
            crash = True
        else:
            back[7], right[7] = right[7], back[7]
    elif right[7] == "X":
        if front[7] == "x":
            crash = True
        else:
            right[7], front[7] = front[7], right[7]
    elif front[7] == "X":
        if left[7] == "x":
            crash = True
        else:
            front[7], left[7] = left[7], front[7]
    elif left[7] == "X":
        if back[7] == "x":
            crash = True
        else:
            left[7], back[7] = back[7], left[7]
    if crash:
        return True

    flipp(layer)
    return False
def F(layer):
    crash = False
    if up[7] == "X":
        if right[3] == "x":
            crash = True
        else:
            up[7], right[3] = right[3], up[7]
    elif right[3] == "X":
        if down[1] == "x":
            crash = True
        else:
            right[3], down[1] = down[1], right[3]
    elif down[1] == "X":
        if left[5] == "x":
            crash = True
        else:
            down[1], left[5] = left[5], down[1]
    elif left[5] == "X":
        if up[7] == "x":
            crash = True
        else:
            left[5], up[7] = up[7], left[5]
    if crash:
        return True

    flip(layer)
    return False
def Fp(layer):
    crash = False
    if up[7] == "X":
        if left[5] == "x":
            crash = True
        else:
            up[7], left[5] = left[5], up[7]
    elif left[5] == "X":
        if down[1] == "x":
            crash = True
        else:
            left[5], down[1] = down[1], left[5]
    elif down[1] == "X":
        if right[3] == "x":
            crash = True
        else:
            down[1], right[3] = right[3], down[1]
    elif right[3] == "X":
        if up[7] == "x":
            crash = True
        else:
            right[3], up[7] = up[7], right[3]
    if crash:
        return True

    flipp(layer)
    return False
def B(layer):
    crash = False
    if up[1] == "X":
        if left[3] == "x":
            crash = True
        else:
            up[1], left[3] = left[3], up[1]
    elif left[3] == "X":
        if down[7] == "x":
            crash = True
        else:
            left[3], down[7] = down[7], left[3]
    elif down[7] == "X":
        if right[5] == "x":
            crash = True
        else:
            down[7], right[5] = right[5], down[7]
    elif right[5] == "X":
        if up[1] == "x":
            crash = True
        else:
            right[5], up[1] = up[1], right[5]
    if crash:
        return True

    flip(layer)
    return False
def Bp(layer):
    crash = False
    if up[1] == "X":
        if right[5] == "x":
            crash = True
        else:
            up[1], right[5] = right[5], up[1]
    elif right[5] == "X":
        if down[7] == "x":
            crash = True
        else:
            right[5], down[7] = down[7], right[5]
    elif down[7] == "X":
        if left[3] == "x":
            crash = True
        else:
            down[7], left[3] = left[3], down[7]
    elif left[3] == "X":
        if up[1] == "x":
            crash = True
        else:
            left[3], up[1] = up[1], left[3]
    if crash:
        return True

    flipp(layer)
    return False
def double(layer ,move, reverse):
    if move(layer):
        if reverse(layer):
            return True
        else:
            if reverse(layer):
                return True
            else:
                return False

    else:
        if move(layer):
            return True
        else:
            return False
word = "L2 R F' L2 B2 F' L2 B U2 D F L2 B2 U' R D2 B2"
main(0, word, None, False)
print(len(word.split(" ")))

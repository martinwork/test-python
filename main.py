def Update():
    global row1str, row2str
    if time > -1:
        
        #Wow big :3
        A = B
        B = C
        C = D
        D = E
        E = F
        F = G
        G = H
        H = I
        I = J
        J = K
        K = L
        L = M
        M = N
        N = O
        O = P


        # read notes list and deal with row1
        if notes[time] == 1:
            P = ["1","0"]
        if notes[time] == 2:
            P = ["0","1"]
        if notes[time] == 0:
            P = ["0","0"]
        
        print(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P)
        # Button sound test
        if not (CheckB == 1):
            music.ring_tone(262)
        else:
            music.rest(1)
        row1str = ""
        row2str = "CONSTRUCTION"
        music.set_volume(40)
        makerbit.show_string_on_lcd1602(A[0]+B[0]+C[0]+D[0]+E[0]+F[0]+G[0]+H[0]+I[0]+J[0]+K[0]+L[0]+M[0]+N[0]+O[0]+P[0], makerbit.position1602(LcdPosition1602.POS1), 16)
        makerbit.show_string_on_lcd1602(row2str, makerbit.position1602(LcdPosition1602.POS17), 16)
Button = 0
Y_joy = 0
X_joy = 0
row2str = ""
row1str = ""
CheckB = 0
notes: List[number] = []
time = 0
row1: List[number] = []
pressed_last_tick = 0
A = ["0","0"]
B = ["0","0"]   
C = ["0","0"]
D = ["0","0"]
E = ["0","0"]
F = ["0","0"]
G = ["0","0"]
H = ["0","0"]
I = ["0","0"]
J = ["0","0"]
K = ["0","0"]
L = ["0","0"]
M = ["0","0"]
N = ["0","0"]
O = ["0","0"]
P = ["0","0"]

makerbit.connect_lcd(39)
time = -2
once = True
notes = [0,
    1,
    2,
    2,
    1,
    0,
    1,
    0,
    2,
    1,
    2,
    0,
    2,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0]
bpm = 60
tbb = 25 / bpm

def on_forever():
    global X, Y, B, CheckB
    # Joystick test
    if X_joy > 700:
        led.plot(2, 2)
    else:
        led.unplot(2, 2)
    X_joy = pins.analog_read_pin(AnalogPin.P1)
    Y_joy = pins.analog_read_pin(AnalogPin.P0)
    Button = pins.analog_read_pin(AnalogPin.P2)
    CheckB = pins.digital_read_pin(DigitalPin.P5)
    if CheckB == 1:
        led.unplot(1, 1)
        pressed_last_tick == 0
    else:
        led.plot(1, 1)
        pressed_last_tick == 1
    led.plot(3,3)

    if X_joy > 700 and (not Button == 1) and A[1] == "1":
        A[1] = "0"

basic.forever(on_forever)

def on_every_interval():
    global time
    time += 1
    Update()
loops.every_interval(tbb * 1000, on_every_interval)

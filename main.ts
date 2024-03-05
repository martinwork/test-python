function Update() {
    let row16: number[];
    let row15: number[];
    let row14: number[];
    let row13: number[];
    let row12: number[];
    let row11: number[];
    let row10: number[];
    let row9: number[];
    let row8: number[];
    let row7: number[];
    let row6: number[];
    let row5: number[];
    let row4: number[];
    let row3: number[];
    let row2: number[];
    
    if (time > -1) {
        //  read notes list and deal with row1
        row16 = row15
        row15 = row14
        row14 = row13
        row13 = row12
        row12 = row11
        row11 = row10
        row10 = row9
        row9 = row8
        row8 = row7
        row7 = row6
        row6 = row5
        row5 = row4
        row4 = row3
        row3 = row2
        row2 = row1
        if (notes[time] == 1) {
            
        }
        
        if (notes[time] == 2) {
            
        }
        
        if (notes[time] == 0) {
            
        }
        
        //  Button sound test
        if (!(CheckB == 1)) {
            music.ringTone(262)
        } else {
            music.rest(1)
        }
        
        row1str = "UNDER"
        row2str = "CONSTRUCTION"
        music.setVolume(40)
        makerbit.showStringOnLcd1602(row1str, makerbit.position1602(LcdPosition1602.Pos1), 16)
        makerbit.showStringOnLcd1602(row2str, makerbit.position1602(LcdPosition1602.Pos17), 16)
    }
    
}

let B = 0
let Y = 0
let X = 0
let row2str = ""
let row1str = ""
let CheckB = 0
let notes : number[] = []
let time = 0
let row1 : number[] = []
let pressed_last_tick = 0
let A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
A = [0, 0]
makerbit.connectLcd(39)
time = -2
let once = true
notes = [0, 1, 2, 2, 1, 0, 1, 0, 2, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
let bpm = 60
let tbb = 25 / bpm
basic.forever(function on_forever() {
    
    //  Joystick test
    if (X > 700) {
        led.plot(2, 2)
    } else {
        led.unplot(2, 2)
    }
    
    let X_joy = pins.analogReadPin(AnalogPin.P1)
    let Y_joy = pins.analogReadPin(AnalogPin.P0)
    B = pins.analogReadPin(AnalogPin.P2)
    CheckB = pins.digitalReadPin(DigitalPin.P5)
    if (CheckB == 1) {
        led.unplot(1, 1)
        pressed_last_tick == 0
    } else {
        led.plot(1, 1)
        pressed_last_tick == 1
    }
    
})
loops.everyInterval(tbb * 1000, function on_every_interval() {
    
    time += 1
    Update()
})

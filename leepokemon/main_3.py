import array, time, random, rp2
from machine import Pin

'''
Button activated LED neopixel ring
'''


# Config WS2812 LEDs
NUM_LEDS = 24
brightness = 0.05

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLUE, WHITE) 

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x,1).side(0)[T3-1]
    jmp(not_x,"do_zero").side(1)[T1-1]
    jmp("bitloop").side(1)[T2-1]
    label("do_zero")
    nop().side(0)[T2-1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8000000, sideset_base=Pin(6))
sm2 = rp2.StateMachine(1, ws2812, freq=8000000, sideset_base=Pin(14))

# Start StateMachine, it will wait for data on its FIFO
sm.active(1)
sm2.active(1)

# Display a pattern on LEDs via an array of LED RGB values
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

def pixels_show(state_machine):
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g << 12) + (r << 8) + b
    state_machine.put(dimmer_ar, 8)
                
def pixels_set(i, color):
    ar[i] = (color[1] << 12) + (color[0] << 8) + color[2]
    
def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)
    
def color_chase(color, wait, sm):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        pixels_show(sm)
        time.sleep_ms(wait)
   
# Button IO
pin_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
            
# Button IO
while True:
    print("Loop")
    time.sleep_ms(100)
    print(pin_button.value())
    
    if pin_button.value() == 1:
        for n in range(5):
            pixels_fill(WHITE)
            pixels_show(sm2)
            for color in COLORS:
                pixels_fill(color)
                pixels_show(sm)
            for color in COLORS:
                color_chase(color, 50, sm)       
    else:
        pixels_fill(BLACK)
        pixels_show(sm)
        pixels_show(sm2)    

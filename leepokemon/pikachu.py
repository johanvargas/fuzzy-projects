import array, time, random
from machine import Pin
import rp2

# Config WS2812 LEDs
NUM_LEDS = 24
PIN_NUM = 6
brightness = 0.02

#BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (0, 255, 255)
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
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start StateMachine, it will wait for data on its FIFO
sm.active(1)

# Display a pattern on LEDs via an array of LED RGB values
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g << 12) + (r << 8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(1)
                
def pixels_set(i, color):
    ar[i] = (color[1] << 12) + (color[0] << 8) + color[2]
    
def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)
    
def color_chase(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        time.sleep(wait)
        pixels_show()
    time.sleep(0.01)
 
while True:
    print("pika" + str(random.randrange(1000)))
    print("fills")
    for color in COLORS:
        pixels_fill(color)
        pixels_show()
        #time.sleep(0.2)

    print("chases")
    for color in COLORS:
        color_chase(color, 0.01)

    print("chu!")
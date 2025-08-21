import sensor, time
from pyb import UART, LED

# -------- DEBUG FLAG --------
DEBUG = True  # Enable to print messages

# -------- Camera & Sensor Setup --------
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
sensor.set_auto_exposure(False, exposure_us=11000)
sensor.skip_frames(time=2000)

clock = time.clock()

# -------- UART & LED Setup --------
uart = UART(3, 115200)
red_led   = LED(1)
green_led = LED(2)
blue_led  = LED(3)

# Blink yellow to indicate qualification mode
green_led.on(); red_led.on()
time.sleep(0.5)
red_led.off(); green_led.off(); blue_led.off()
time.sleep(0.5)

# -------- Color Thresholds (LAB Space) --------
red_threshold    = [(32, 54, 40, 67, 17, 63)]
green_threshold  = [(36, 69, -56, -21, -19, 32)]
blue_threshold   = [(9, 76, -45, 27, -57, -8)]
orange_threshold = [(38, 77, -15, 34, 14, 55)]
black_threshold  = [(0, 37, -26, 7, -17, 11)]

# -------- Regions of Interest (ROI) --------
img_h = sensor.height()
img_w = sensor.width()
cubes_roi = (0, int(img_h * 0.5), img_w, int(img_h * 0.5))
lines_roi = (5, int(img_h * 0.5), img_w - 10, int(img_h * 0.4))
wall_roi  = (50, int(img_h * 0.5 - 18), img_w - 100, int(img_h * 0.2 - 10))

# -------- Blob Filtering Parameters --------
min_cube_size       = 100
min_line_size       = 1000
min_area            = 10
min_valid_cube_area = 450
black_wall_min_area = 7000
min_black_height    = 37

# -------- PD Parameters for Cube Following --------
kp_cube = 0.21
kd_cube = 2.8
pid_error = 0.0
pid_last_error = 0.0
follow_threshold = 4205
direction = 0

# -------- Helper Functions --------
def get_largest_blob(blobs):
    return max(blobs, key=lambda b: b.area(), default=None)

def is_invalid_orange(orange_blob, red_blobs):
    if orange_blob.h() > orange_blob.w():
        return "ignore_orange"
    for r in red_blobs:
        if (r.x() < orange_blob.x()+orange_blob.w() and
            r.x()+r.w() > orange_blob.x() and
            r.y() < orange_blob.y()+orange_blob.h() and
            r.y()+r.h() > orange_blob.y()):
            ra, oa = r.area(), orange_blob.area()
            if ra >= oa * 1.5:
                return "ignore_orange"
            elif oa >= ra * 0.1:
                return "ignore_red"
    return None

# -------- Main Loop --------
while True:
    clock.tick()
    img = sensor.snapshot()
    target_x = img_w // 2

    # ---- Detect Blobs ----
    red_blobs    = img.find_blobs(red_threshold, roi=cubes_roi, pixels_threshold=min_cube_size, area_threshold=min_cube_size, merge=True)
    green_blobs  = img.find_blobs(green_threshold, roi=cubes_roi, pixels_threshold=min_cube_size, area_threshold=min_cube_size, merge=True)
    blue_blobs   = img.find_blobs(blue_threshold, roi=lines_roi, pixels_threshold=min_line_size, area_threshold=min_line_size, merge=True)
    orange_blobs = img.find_blobs(orange_threshold, roi=lines_roi, pixels_threshold=min_line_size, area_threshold=min_line_size, merge=True)
    black_blobs  = img.find_blobs(black_threshold, roi=wall_roi, pixels_threshold=black_wall_min_area, area_threshold=black_wall_min_area, merge=True)

    red_cube    = get_largest_blob([b for b in red_blobs   if b.area() >= min_valid_cube_area])
    green_cube  = get_largest_blob([b for b in green_blobs if b.area() >= min_valid_cube_area])
    blue_line   = get_largest_blob([b for b in blue_blobs  if b.area() >= min_area])
    orange_line = get_largest_blob([b for b in orange_blobs if b.area() >= min_area])
    black_blob  = get_largest_blob(black_blobs)

    # ---- Black Wall ----
    if black_blob and black_blob.h() >= min_black_height and black_blob.area() >= black_wall_min_area:
        img.draw_rectangle(black_blob.rect(), color=(0,0,0))  # draw black wall
        uart.write("BLACK\n".encode())
        if DEBUG: print("Sent to Arduino: BLACK")

    # ---- Cube ----
    candidates = []
    if red_cube:   candidates.append(('R', red_cube))
    if green_cube: candidates.append(('G', green_cube))

    if candidates:
        color_char, cube = max(candidates, key=lambda x: x[1].area())
        area = cube.area()
        error = (cube.cx() - target_x) / float(target_x)
        pid_error = kp_cube * error + kd_cube * (error - pid_last_error)
        pid_last_error = error

        # Draw cube
        color_val = (255,0,0) if color_char=='R' else (0,255,0)
        img.draw_rectangle(cube.rect(), color=color_val)
        img.draw_cross(cube.cx(), cube.cy(), color=color_val)

        if area < follow_threshold:
            uart.write(("S{:+.3f}\n".format(error)).encode())
            if DEBUG: print("Sent to Arduino: S{:+.3f}".format(error))
        else:
            uart.write((color_char + "\n").encode())
            if DEBUG: print("Sent to Arduino:", color_char)

    # ---- Line Following ----
    valid_orange = None
    if orange_line and not is_invalid_orange(orange_line, red_blobs):
        valid_orange = orange_line

    chosen_line, chosen_color = None, None
    if blue_line and valid_orange:
        chosen_line, chosen_color = (blue_line, "BLUE") if blue_line.area() > valid_orange.area() else (valid_orange, "ORANGE")
    elif blue_line:
        chosen_line, chosen_color = blue_line, "BLUE"
    elif valid_orange:
        chosen_line, chosen_color = valid_orange, "ORANGE"

    if chosen_line:
        img.draw_rectangle(chosen_line.rect(), color=(0,0,255) if chosen_color=="BLUE" else (255,165,0))
        uart.write((chosen_color + "\n").encode())
        if DEBUG: print("Sent to Arduino:", chosen_color)
        if direction == 0:
            direction = 1 if chosen_color=="BLUE" else 2

    # ---- Optional: send direction ----
    # uart.write((str(direction) + "\n").encode())

    time.sleep(0.05)

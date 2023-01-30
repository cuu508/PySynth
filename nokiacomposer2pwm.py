""" Play tunes on a buzzer hooked up to PWM GPIO pins. """

import re

PITCHHZ = {}
keys_s = ("a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#")
for k in range(88):
    freq = 27.5 * 2.0 ** (k / 12.0)
    oct = (k + 9) // 12
    note = "%s%u" % (keys_s[k % 12], oct)
    PITCHHZ[note] = freq


def parse_ringtone(tune_str):
    tune = []
    pattern = "([0-9]+)(\.?)(#?)([\w-])([0-9]?)"
    for duration, dotted, sharp, pitch, octave in re.findall(pattern, tune_str):
        if pitch == "-":
            pitch = "r"

        duration = -int(duration) if dotted else int(duration)

        tune.append((pitch + sharp + octave, int(duration)))

    return tune


# eiffel_65_im_blue"
TEMPO = 160
DATA = "4a1 4#a1 8g1 8#a1 8c2 8f1 8a1 4#a1 8g1 8#a1 8d2 4#d2 8d2 8c2 4#a1 8g1 8#a1 8c2 8f1 8a1 4#a1 8g1 8#a1 8d2 4#d2 8d2 8c2 4#a1 8g1 8#a1 8c2 8f1 8a1 4#a1 8g1 8#a1 8d2 4#d2 8d2 8c2 4#a1 8g1 8#a1 8a1 8f1 8f1 2g1"

# eminem_slim_shady
TEMPO = 160
DATA = "8c2 8#d2 8g1 8#g1 4c2 8- 8#g1 4g1 8- 8#g1 16g1 16#g1 8g1 8#f1 8g1 8c2 8#d2 8g1 8#g1 4c2 8- 8#g1 4g1 8- 8#g1 16g1 16#g1 8g1 8#f1 8g1 8c2 8#d2 8g1 8#g1 4c2 8- 8#g1 4g1 8- 8#g1 16g1 16#g1 8g1 8#f1 8g1"

# michael_jackson_smooth_criminal
TEMPO = 100
DATA = "8a1 16a1 16a1 16g1 16a1 8b1 8b1 8- 16a1 16b1 8c2 8c2 8- 16b1 16c2 8b1 4g1 8a1 8- 8a1 16a1 16a1 16g1 16a1 8b1 8b1 8- 16a1 16b1 8c2 8c2 8- 16b1 16c2 8b1 4g1"

# fur_elise.wav
TEMPO = 160
DATA = "8e2 8#d2 8e2 8#d2 8e2 8b1 8d2 8c2 4a1 8- 8c1 8e1 8a1 4b1 8- 8e1 8#g1 8b1 4c2 8- 8e1 8e2 8#d2 8e2 8#d2 8e2 8b1 8d2 8c2 4a1 8- 8c1 8e1 8a1 4b1 8- 8e1 8c2 8b1 4a1"

# southpark_uncle_fucka.wav
TEMPO = 160
DATA = "8e2 8e2 8e2 8e2 4e2 8d2 8c2 8a1 2c2 8- 8c2 8d2 8e2 8e2 8e2 8e2 8e2 8e2 8d2 8c2 8a1 2c2 8- 8c2 8c2 8d2 8d2 8d2 8b1 8c2 8d2 8e2 16- 16e2 16f2 16f2 8e2 8d2 8c2 8b1 8c2 8d2"

# lose_yourself
TEMPO = 250
DATA = "4a2 8- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 4f2 8- 8d1 4- 8d1 4- 8d1 4- 4g2 8- 8d1 4- 4c3 8#a2 4a2 8g2 4a2 8- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 8d1 4- 4f2 8- 8d1 4- 8d1 4- 8d1 4- 4g2 8- 8d1 4- 4c3 8#a2 4a2 8g2 4a2"

# sandstorm
TEMPO = 90
DATA = "16e2 16e2 16e2 16e2 8e2 16e2 16e2 16a2 16a2 16a2 16a2 16g2 16g2 16g2 16d2 16e2 16e2 16e2 16e2 8e2 16e2 16a2 16e2 16e2 16e2 16e2 8e2 16e2 16d2 16e2 16e2 16e2 16e2 16e2 8e2 16e2 16e2 16a2 16a2 16a2 16a2 16g2 16g2 16g2 16d2 16e2 16e2 16e2 16e2 8e2 16e2 16a2 16e2 16e2 16e2 16e2 8e2 16e2 16d2 16e2 16e2 16e2 16e2 16e2 8e2 16e2 16e2 16a2 16a2 16a2 16a2 16g2 16g2 16g2 16d2 16e2 16e2 16e2 16e2 8e2 16e2 16a2 16e2 16e2 16e2 16e2 8e2 16e2 16d2 16e2"

# light_my_fire
TEMPO = 120
DATA = "8b2 16g2 16a2 8b2 8d3 8c3 8b2 8a2 8g2 8a2 16f2 16a2 8c3 8f3 16d3 16c3 16#a2 16g2 8#g2 8g2 8#g2 16g2 16a2 8b2 8#c3 16b2 16a2 16g2 16f2 8e2 8f2 1a2 4a2"


full_note = 200.0 / TEMPO
print("DIR=/sys/devices/platform/soc/ff800000.bus/ff807000.pwm/pwm/pwmchip2/pwm0")
for note_pitch, note_duration in parse_ringtone(DATA):
    # note_duration is 1, 2, 4, 8, ... and actually means 1, 1/2, 1/4, ...
    duration = full_note / note_duration

    if note_pitch == "r":
        print("sleep %.2f" % duration)
    else:
        freq = PITCHHZ[note_pitch]
        freq *= 2**4
        period = int(1000000 * 2000 / freq)

        print("echo %d > $DIR/period" % period)
        print("echo 1 > $DIR/enable; sleep %.2f; echo 0 > $DIR/enable" % duration)

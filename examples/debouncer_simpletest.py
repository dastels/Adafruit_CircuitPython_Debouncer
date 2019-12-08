"""
The MIT License (MIT)

Copyright (c) 2019 Dave Astels for Adafruit Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# pylint: disable=invalid-name

import board
import digitalio
from adafruit_debouncer import Debouncer

pin = digitalio.DigitalInOut(board.D11)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
switch1 = Debouncer(pin)

switch2 = Debouncer(board.D12)

while True:
    switch1.update()
    switch2.update()
    if switch1.fell:
        print('Just pressed 1')
    if switch1.rose:
        print('Just released 1')
    if switch1.value:
        print('not pressed 1')
    else:
        print('pressed 1')

    if switch2.fell:
        print('Just pressed 2')
    if switch2.rose:
        print('Just released 2')
    if switch2.value:
        print('not pressed 2')
    else:
        print('pressed 2')

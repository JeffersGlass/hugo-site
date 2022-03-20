# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import digitalio
import neopixel
from time import sleep

from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K, SNMR_UDP, SNSR_SOCK_UDP
import adafruit_wiznet5k.adafruit_wiznet5k_socket as socket
import adafruit_requests as requests


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

targetMACs = [
    [0x54, 0xB2, 0x03, 0x93, 0xED, 0x13], #Flock Table NW
    [0x54, 0xB2, 0x03, 0x93, 0xED, 0x12], #Flock Table NW
    [0x54, 0xB2, 0x03, 0x93, 0xFB, 0x52], #Flock Table SW
    [0x54, 0xB2, 0x03, 0x93, 0xFB, 0x54], #Flock Table SW
    [0x54, 0xB2, 0x03, 0x94, 0x0B, 0x72], #Flock Table NE
    [0x54, 0xB2, 0x03, 0x94, 0x0B, 0x73], #Flock Table NE
    [0x54, 0xB2, 0x03, 0x94, 0x41, 0xDF], #Flock Table SE
    [0x54, 0xB2, 0x03, 0x94, 0x41, 0xE0], #Flock Table SE
    [0x54, 0xB2, 0x03, 0x93, 0xF8, 0xA3], #Flight Aware W
    [0x54, 0xB2, 0x03, 0x93, 0xF8, 0xA4], #Flight Aware W
    [0x54, 0xB2, 0x03, 0x93, 0xFD, 0xD0], #Flight Aware E
    [0x54, 0xB2, 0x03, 0x93, 0xFD, 0xD1], #Flight Aware E
    ]

cs = digitalio.DigitalInOut(board.D10)
spi_bus = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize ethernet interface with DHCP
eth = WIZNET5K(spi_bus, cs, is_dhcp=False)

ip = eth.unpretty_ip("172.16.0.10")
subnet_mask = eth.unpretty_ip("255.255.0.0")
gateway = eth.unpretty_ip("172.16.0.10")
dns = eth.unpretty_ip("172.16.0.10")
eth.ifconfig = (ip, subnet_mask, gateway, dns)
#eth.ifconfig = (ip, subnet_mask, None, None)

print(eth.pretty_ip(eth.ip_address))
pixel[0] = (255,0,255)

retry = True
while retry:
    try:
        eth.socket_connect(0, eth.unpretty_ip('172.16.255.255'), 556, conn_mode=SNMR_UDP)
    except AssertionError as err:
        print(str(err) + ", retrying in 10 Seconds")
        sleep(10)
    else:
        retry = False

status = eth.socket_status(0)
if [int(b) for b in status] == [SNSR_SOCK_UDP]:
    print("Socket 0 connected as UDP")
else:
    print(f"Socket not connected, status is {status}")

pixel[0] = (0,0,255)
sleep(5)

while True:
    pixel[0] = (0,255,0)
    for i, target in enumerate(targetMACs):
        led.value = True
        fullPacket = bytearray([0xFF] * 6 + target * 16)
        print(f"Sending WoL packet to computer {i} with mac address {eth.pretty_mac(target)}")
        eth.socket_write(0, fullPacket, 1)
        led.value = False
        sleep(.1)

    pixel[0] = (0,0,255)
    sleep(5)

eth.socket_close(0)

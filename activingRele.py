# -*- coding: utf-8 -*-

# Import RPi.GPIO module
import RPi.GPIO as GPIO
# Import module for delay
from time import sleep
# Import module progress bar
from tqdm import tqdm

try:
	# Disable message warnings
	GPIO.setwarnings(False)

	# Set pin specification mode choose BCM or BOARD
	GPIO.setmode(GPIO.BOARD)

	# Set GPIO port as an output
	GPIO.setup(18, GPIO.OUT)

	# Set GPIO port to False or True
	GPIO.output(18, False)

	# Print terminal
	print("Activating port")

	# Progress bar
	for i in tqdm(range(60)):
		sleep(1)

	# Print terminal
	print("Disabling port")

	# Set GPIO port to False or True
	GPIO.output(18, True)

# CTRL+C keyboard interrupt
except KeyboardInterrupt:

	# Reset GPIO port used
	GPIO.cleanup()

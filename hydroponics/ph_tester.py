<<<<<<< HEAD
import time
import RPi.GPIO as GPIO
import spidev
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 250000
calibration = 21.25

def poll_sensor(channel):
	assert 0 <= channel <= 1, 'ADC channel must be 0 or 1'

	if channel:
		cbyte = 0b11000000
	else:
		cbyte = 0b10000000

	r = spi.xfer2([1,cbyte,0])
	return ((r[1] & 31) << 6) + (r[2] >> 2)


def get_ph():
    total = 0.0
    count = 6
    try:
        for x in range(count):
            channel = 0
            channeldata = poll_sensor(channel)
            voltage = round(((channeldata * 5000) / 1024),0)
            ph = -5.70 * (voltage / 1000) + calibration
            total = total + ph
    except Exception as e:
        total = -1.0
        count = 1
        print("An exception has occured in get_ph")
        print(e)
    finally:
        spi.close()
        return total/count

=======
import time
import RPi.GPIO as GPIO
import spidev
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 250000
calibration = 21.25

def poll_sensor(channel):
	assert 0 <= channel <= 1, 'ADC channel must be 0 or 1'

	if channel:
		cbyte = 0b11000000
	else:
		cbyte = 0b10000000

	r = spi.xfer2([1,cbyte,0])
	return ((r[1] & 31) << 6) + (r[2] >> 2)


def get_ph():
    total = 0.0
    count = 6
    try:
        for x in range(count):
            channel = 0
            channeldata = poll_sensor(channel)
            voltage = round(((channeldata * 5000) / 1024),0)
            ph = -5.70 * (voltage / 1000) + calibration
            total = total + ph
    except:
        total = -1.0
        count = 1
        print("An exception has occured in get_ph")
    finally:
        spi.close()
        return total/count
>>>>>>> refs/remotes/origin/main

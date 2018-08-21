# RasPi Camera Sync
This is an experiment in synchronizing and stitching/manipulating photos from two Raspberry Pi cameras attached
to two separate Raspberry Pis. A remote host uses the pigpio python library to toggle a pin on each Pi between
high and low. A change in the pin triggers the cameras on each Pi to take a photo. OpenCV will then be used to
stitch the photos together and transform them in other ways.

## Setup
### Requirements
* Two Raspberry Pis
* Two Raspberry Pi camera modules
* Python3
* pigpiod

### Installation
Install [pigpiod on both Pis](http://abyz.me.uk/rpi/pigpio/pigpiod.html) via apt: `sudo apt-get install pigpiod`
Start it with `sudo pigpiod`; don't start it as a service as it will only bind to localhost and not expose the port.
Verify that you can communicate with the default port (8888) externally, or at least between the two Pis.

Clone this repository onto both Pis and ensure the camera modules are both detected and enabled. Make sure that
nothing else is using the cameras.

Install the python requirements using pip and requirements.txt. Start the listener on each Pi:

`python listen.py`

Wait for the camera to warm up and for the script to begin listening to the GPIO pin on both Pis. Then,
run the trigger script:

`python main.py`

*Note*: You main run into some permissions errors related to access to /dev/mem, in which case add
your user to the gpio group with `sudo usermod -aG gpio username` and optionally change permissions on /dev/gpiomem:

`sudo chown root:gpio /dev/gpiomem`

`sudo chmod g+rw /dev/gpiomem`

This will toggle pin 11 between high and low, and on each trigger it should call the camera to take a photo.
It will also print the current time in ms to give you some idea of the delay between photos. This is especially
beneficial if one Pi is synced to a remote NTP time source and acts as the sole time source of the other.

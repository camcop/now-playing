# Now Playing

![demo](/static/demo.gif)

Now Playing is a pocket-sized device to show you the currently playing track from a specific Last.fm user.
 
## Hardware

- [Raspberry Pi Zero WH](https://thepihut.com/products/raspberry-pi-zero-wh-with-pre-soldered-header)
- (Optional but recommended) [Heatsink for RPi](https://thepihut.com/products/heatsink-for-raspberry-pi-zero-2)
- [Waveshare 2.13" e-ink screen v2](https://www.waveshare.com/product/displays/e-paper/2.13inch-e-paper-hat.htm) [(alternative)](https://thepihut.com/products/eink-display-phat-2-13-250x122)
- (Optional) [Pi Zero Case for Waveshare 2.13" eInk Display](https://thepihut.com/products/pi-zero-case-for-waveshare-2-13-eink-display)
- Micro-USB cable for power
 

## Installation

- Uses waveshare's [example repo](https://github.com/waveshareteam/e-Paper) for e-ink displays
- Uses code from [music-screen-api](https://github.com/hankhank10/music-screen-api/tree/master) repo but adapts it to use the waveshare e-ink screen
 
### Hardware setup
  
  1. Attach heatsink to Pi (if using)
  2. Attach e-ink screen to Pi using the GPIO header
  3. Build and insert into case (if using)

### Installation steps
    
1.  Install "Raspberry Pi OS (Legacy, 32 bit) Lite" to SD card using [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
    
    > Note:  Set up WiFi and allow SSH access at this step

2. Insert SD card into Pi
3. Connect to Pi via SSH with [Putty](https://www.putty.org/) (locate IP address via router)
4. Download this repo as a zip file
5. Extract to zip to device (e.g. user's home directory recommended)
6. Create .env file in extracted directory containing `LAST_FM_USERNAME=<username>`
7. Create entry in crontab to run script on device start:
   1. `crontab -e`
   2. Add `@reboot sleep 10 && cd /path/to/home/now-playing && python3 nowplaying.py > /path/to/home/now-playing/log.txt 2>&1`
8. Unplug device and plug in again
9. Enjoy!
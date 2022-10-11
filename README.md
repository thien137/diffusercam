# Diffusercam with ESP32 Cam
This repository includes embedded repositories to set up the ESP32 Camera for DiffuserCam applications.
* DiffuserCam (https://github.com/Waller-Lab/DiffuserCam-Tutorial)
* ESP32 MicroPython Firmware (https://github.com/lemariva/micropython-camera-driver)
* ESP32 MicroPython WiFi LiveStreaming (https://github.com/lemariva/uPyCam)

## ESP32 Camera Setup
### ESP32 Firmware
Before you can start streaming from the ESP32 Camera, you first need to flash the firmware into the device.
Connect the ESP32 to your computer via micro-USB and then run the following:
```sh
git clone https://github.com/lemariva/micropython-camera-driver
cd micropython-camera-driver/firmware
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 micropython_camera_feeeb5ea3_esp32_idf4_4.bin
```
#### Notes on Firmware Installation
- Note 1: You will need to replace '/dev/ttyUSB0/' with the appropriate port of your device
  - Windows: Device Manager -> COM#
  - Unix: Run `ls /dev/tty*` and find the correct port
- Note 2: If unable to find serial connection with ESP32:
  - While flashing, hold IO0 button and then RST button (if there are two reset buttons, press both)
### ESP32 MicroPython WiFi LiveStreaming
Now that we have the firmware, we need to upload MicroPython code for the ESP32 to run.
Download this code from the aforementioned repository by running the following code.
```sh
git clone https://github.com/lemariva/uPyCam
cd uPyCam
```

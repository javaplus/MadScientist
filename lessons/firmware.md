# Prepare Pico for MicroPython

In order to use Python on a new Pico, you need to update the firmware to enable MicroPython.

I've found the easiest way to do this is to use Thonny. 

[Download Thonny](https://thonny.org/)

Open Thonny and then get ready to connect the Pico via a USB cable.  As you connect the Pico via a USB cable hold the "BOOTSEL" button on top of the Pico as you plug the Pico in.  

You may hear your computer detect a new device and maybe even open a file explorer like view.  If so, close this and just go back to Thonny.  

In Thonny, go to the `Tools` menu and choose `Options`:

![Thonny Options](/lessons/images/ThonnyOptions.PNG)

In the Thonny Options screen, select `MicroPython (Raspberry Pi Pico)` as the interpreter in the dropdown at the top. 

Next, click the `Install or update MicroPython` link at the bottom right:

![Thonny Options Popup](/lessons/images/ThonnyOptionsPopup.PNG)

In the "Install or update MicroPython" popup window, choose the "RPI-***" device in the `Target volume` drop down.

The `variant` should be "Pico W / Pico WH".

![Thonny Firmware](/lessons/images/ThonnyFirmware.PNG)

Once the target volume and variant is set properly, click install.

It may take a minute or two to install and your computer may detect a new device during this process.

When it's done, close the pop up windows in Thonny to get back to the main Thonny screen.

Now go to the very bottom right to select your MicroPython enabled device from the drop down:

Note: Your COM port number may be different.
![Thonny Device](/lessons/images/ThonnyChoosePico.PNG)

Once you've selected your device, you should see the Shell change to show the version of MicroPython installed on your Pico.

![Thonny done](/lessons/images/ThonnyFinal.PNG)


### Install picozero library

Go to this link and follow just the few steps to [install the pico zero library.](https://picozero.readthedocs.io/en/latest/gettingstarted.html#install-picozero-from-pypi-in-thonny)


Now you should be good to go!!!

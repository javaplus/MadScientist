# Prepare Pico for MicroPython

In order to use Python on a new Pico, you need to update the firmware to enable MicroPython.

I've found the easiest way to do this is to use Thonny.

[Download Thonny](https://thonny.org/)

Open Thonny and then get ready to connect the Pico via a micro USB cable.  Hold the "BOOTSEL" button on top of the Pico as you plug the Pico in.

<img alt="Pico WH Bootsel button" src="/lessons/images/pico_wh_bootsel.png" width="500"/>

You may hear your computer detect a new device and maybe even open a file explorer like View.  If so, close this and just go back to Thonny.

In Thonny, go to the `Tools` menu and choose `Options`:

![Thonny Options](/lessons/images/ThonnyOptions.PNG)

In the Thonny `Options` screen, select `MicroPython (Raspberry Pi Pico)` as the interpreter in the dropdown at the top. 

Next, click the `Install or update MicroPython` link at the bottom right:

![Thonny Options Popup](/lessons/images/ThonnyOptionsPopup.PNG)

In the `Install or update MicroPython` popup window, choose the "RPI-***" device in the `Target volume` drop down.

The `variant` should be `Pico W / Pico WH`. Be sure to pick `Pico W` and not the normal `Pico` the `W` is important!

![Thonny Firmware](/lessons/images/ThonnyFirmware.PNG)

Once the target volume and variant are set properly, click Install.

It may take a minute or two to install and your computer may detect a new device during this process.

When it's done, close the pop up windows in Thonny to get back to the main Thonny screen.

Now go to the very bottom right to select your MicroPython enabled device from the drop down.

Note: Your COM port number may be different.

![Thonny Device](/lessons/images/ThonnyChoosePico.PNG)

Once you've selected your device, you should see the Shell change to show the version of MicroPython installed on your Pico.

![Thonny done](/lessons/images/ThonnyFinal.PNG)   

NOTE: Your exact version of MicroPython may be slightly different than the screenshot above, but be sure you see `Raspberry Pi Pico W` in the output.  Again, the `W` is important!

### Operating System Qwirks

If you're running Thonny with Flatpak on Linux, you may need to add yourself to the `dialout` group:

1. `sudo usermod -aG disk,dialout $USER`

On some operating systems, like Fedora Atomic setups, you may need to allow the `dialup` group
be to assignable first:

1. `grep -E '^dialout:' /usr/lib/group | sudo tee -a /etc/group`
2. ensure it's added with `cat /etc/group | grep dialout`
3. now run `sudo usermod -aG disk,dialout $USER`

### Install picozero library

Go to this link and follow just the few steps to [install the picozero library.](https://picozero.readthedocs.io/en/latest/gettingstarted.html#install-picozero-from-pypi-in-thonny)


Now you should be good to go!!!

# Mad Scientist Labs

Fun learning with Electronics and Raspberry Pi Pico

This is kind of V2.0 of the Mad Scientist lab.  The original shark with laser game and more gentle introduction to electronics and the Pico can be found here: https://github.com/javaplus/PicoProjects


## The Grab

 Using Raspberry Pi Pico microcontrollers, Python, electric motors, 3D printed parts, and your ingenuity, you will construct a rover ready to conquer Mars! This vehicle will be capable of traversing rough surfaces like those of the red planet and will be programmable to handle out of this world challenges. Remember those mechanical sharks with freakin' lasers on their heads? Well HONEY WE BLEW UP THE SHARKS and will be using those shark parts to transform these rovers into the ULTIMATE MAD SCIENTIST vehicles to fend off any threats you may encounter in this extra-planetary conquest.
Once you've built your functioning rover in our lab, if you choose, you will have the opportunity to battle test your vehicle against other rovers to see whose design reigns supreme! Join us in this epic quest and learn to meld software and hardware together to accomplish our goal of bringing Sharks to Mars!

## Description

This is a tutorial for building a JAWS Rover.  A JAWS Rover is just like it sounds... a mix between a shark and a Mars-like rover.  

Nearly all the plastic parts are 3D printed and the brain is a Raspberry Pi Pico.  You will assemble the plastic bits and install the Pico, the motors, wires, and other electronics to make a functioning autonomous rover.
We will use Python as the programming language for the Pico microcontroller, but all code will be provided.


# Overview/Agenda

- Verify parts from parts kit (link goes here to parts list and pictures)
- Assemble tank treads
- Snap wheels on body
- Add motors (Maybe connect wires to motors)
- Connect motor controller to motors
- Connect motor controller to Pico
- Connect 5V regulator to battery connector
- Connect battery power to Pico
- Connect laser to Pico
- Connect photoresistor to Pico

# Prepare Pico

To prepare the Pico, you need to flash it to support MicroPython.
Here are the instructions to [flash the Pico for MicroPython](/lessons/firmware.md).

# Lessons

The links in this section are to labs which walk you through working with the various components that will ultimately make up your rover. These labs will give you a better understanding of the individual parts and code that go into making the rover work.  However, these lessons do not actually get into building the rover, but are just for learning how the components work.  They are hands-on labs that actually have you working with the electronics and code, but do not include assembly of the rover.  The assembly is in its own section.  So, if you don't care to learn how the individual components work and want to skip straight to building the rover, then skip this section.


[Blink Demo](/lessons/blink.md)  
(May not be in your kit)[Simple LED](/lessons/Led.md)  
(May not be in your kit)[LED PWM](/lessons/led_pwm.md)  
[Working with Electric Motors](/lessons/SimpleMotor.md)  
[Motor Controller](/lessons/MotorController.md)  


# Assembly

[Pico Plate](/lessons/assembly/plate.md)  
[Chassis Motors](/lessons/assembly/chassis.md)  
[Wheels and Tracks](/lessons/assembly/wheels.md)  
[Power Components](/lessons/assembly/power.md)  
[Pico and Chassis Together](/lessons/assembly/plate_chassis.md)  
[RGB Leds](/lessons/assembly/rgb.md)  
[Tail Tip/Photoresistor](/lessons/assembly/tail.md)


# Install the Code

[Install Code](/lessons/assembly/code_install.md)

# Customize the Code

[Custom Game Modes](/lessons/game_mode_coding.md)


# BlueTooth Remote

https://javaplus.github.io/MadScientist/
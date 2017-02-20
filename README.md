# artoo
Raspberry Pi R2D2

Start with a Raspberry Pi with the latest Raspbian image, update and upgrade.
``` 
sudo apt-get update
sudo apt-get upgrade
```

Download and run pip
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```

## Snowboy
We will use Snowboy Hotword Detection by [KITT.AI](http://kitt.ai).
Snowboy is a customizable hotword detection engine for you to create your own
hotword like "OK Google" or "Alexa". It is powered by deep neural networks and
has the following properties:
* **highly customizable**: you can freely define your own magic phrase here –
let it be “open sesame”, “garage door open”, or “hello dreamhouse”, you name it.

* **always listening** but protects your privacy: Snowboy does not use Internet
and does *not* stream your voice to the cloud.

* light-weight and **embedded**: it even runs on a Raspberry Pi and consumes
less than 10% CPU on the weakest Pi (single-core 700MHz ARMv6).

* Apache licensed!

Create a directory named snowboy and download the latest snowboy code.
[Snowboy Home Page](https://snowboy.kitt.ai)
[Snowboy Documentation](http://docs.kitt.ai/snowboy)
Unzip the contents, move it up a level, and delete the compressed file and the folder.
Example below:
```
mkdir snowboy
cd snowboy
wget https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.0.tar.bz2
tar -vxjf rpi-arm-raspbian-8.0-1.1.0.tar.bz2
mv rpi-arm-raspbian-8.0-1.1.0/* .
rmdir rpi-arm-raspbian-8.0-1.1.0/
rm rpi-arm-raspbian-8.0-1.1.0.tar.bz2
```

Adding a note here for later.  I want R2 to welcome me when my phone gets in range.  
R2D2 will be looking for my bluetooth signal.
```
sudo hcitool info 00:00:00:00:00:00 <your bluetooth MAC address>
```

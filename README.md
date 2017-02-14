# artoo
Raspberry Pi R2D2

Start with a Raspberry Pi with the latest Raspbian image, update and upgrade:
``` 
sudo apt-get update
sudo apt-get upgrade
```

Create a directory named snowboy and download the latest snowboy code (http://docs.kitt.ai/snowboy/).  Then unzip the contents, move it up a level, and delete the compressed file and the folder.  Example below:
```
mkdir snowboy
cd snowboy
wget https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.0.tar.bz2
tar -vxjf rpi-arm-raspbian-8.0-1.1.0.tar.bz2
mv rpi-arm-raspbian-8.0-1.1.0/* .
rmdir rpi-arm-raspbian-8.0-1.1.0/
```

Adding a note here for later.  I want R2 to welcome me when my phone gets in range.  He will be looking for my bluetooth signal.
```
sudo hcitool info 00:00:00:00:00:00 <your bluetooth MAC address>
```

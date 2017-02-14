# artoo
Raspberry Pi R2D2

Start with a Raspberry Pi with the latest Raspbian image, update and upgrade:
``` 
sudo apt-get update
sudo apt-get upgrade
```

Adding a note here for later.  I want R2 to welcome me when my phone gets in range.  He will be looking for my bluetooth signal.
```
sudo hcitool info 00:00:00:00:00:00 <your bluetooth MAC address>
```

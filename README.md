# TgBotSendingTool
Tool for sending advertising or any other announcements to the id-database in your telegram bot

## What was this utility written for?
The main need for this application is that not all backend telegram bots support effective sending alerts to users. This software allows you to make a sending alerts to your bot user base in a format convenient for you.

<details> <summary>Example of message that could be sent by this tool</summary>
<div align="center">
    <img src="images/preview.png" />
</div></details> 

<details> <summary>Screenshot of working log</summary>
<div align="center">
    <img src="images/log.png" />
</div></details> 

## What is needed to launch?

### 1) Clone repo and change work dirictory
```
git clone https://github.com/g0sha1337/TgBotSendingTool.git && cd TgBotSendingTool
```
### 2) Install requirements.txt
```
pip install -r requirements.txt
```
### 3) Put token of your bot in config.py
```
TelegramBotToken = 'Your_secret_tg_token' #from @BotFather
```
### 4) Extract telegram ids from your database and put it in database txt file
### 5) Prepare your text message file, image and inline buttons
All data format exaples in files ids.txt, inline.txt, msg.txt and image.png.


# Usage

```
python sender.py --database ids.txt --text msg.txt --image image.png --inline inline.txt
```
- `--database ids.txt`  Database with telegram-IDs of users your bot. It is nessessory file to run this tool. [Example](https://github.com/g0sha1337/TgBotSendingTool/blob/main/ids.txt) 
- `--text msg.txt` Main text of your message. Should be writtent on markdown (links and etc) [Example](https://github.com/g0sha1337/TgBotSendingTool/blob/main/msg.txt) 
- `--image img.png` Image, that will be sent with your text 
- `--gif gif.gif` Gif, that will be sent with your text
- `--inline inline.txt` List of inline buttons in format ButtonName, Link [Example](https://github.com/g0sha1337/TgBotSendingTool/blob/main/inline.txt) 



#### !TODO Multithreading, procentage with all statisctics
Also, you can merge it and develop this soft together 

## Give star, if this tool was helpfull for you ⭐️

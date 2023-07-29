# EncoderRobot 

An anime themed telegram bot which can encode videos with many advanced features.

### Special Features 
• Advanced progress bar which shows

```
  • Encoding Progress in %
  
  
  • Encoded Size
  
  
  • Estimated Size 
  
  
  • Time Left
```
  
• Modes which are 

```
  • Normal_mode - This mode enables to encode any sent file.
  
  
  • Manual_mode - This mode disables the normal mode and you can use other features which don't require normal mode.
```
  
  
• EvalPy which can be used to execute python cmds.


```
Ex: /eval print(Config.AUTH_USERS)
```

• Download to download replied file to perform certain tasks.


```
Ex: /dl (reply to any telegram media)
```


• Upload to upload any downloaded or processed file.


```
Ex: /ul path (path = name of the downloaded file)
```


• Bash to execute shell cmds.


```
Ex: /bash ffmpeg -h
```


• Settings to see ffmpeg variables.


```
Ex: /settings
```


• Cmds to change ffmpeg variables


```
• /crf 


Ex: /crf 28


• /quality


Ex: /quality 800x400


• /speed


Ex: /speed fast


• /audio


Ex: /audio 40k


/codec 


Ex: /codec libx265
```


### Deploy
• Preferred deploying place is either (ab)use workflows or vps.


• Workflows

```
• Clone https://github.com/Parth-Senpai/AutoHost


• Clone this repo and make private


• Add environmental variables in config.py


• In AutoHost repo, add secrets such as

GH_TOKEN (github token with all permissions)

GitHubName (github name)

GithubMail (github mail)


• In AutoHost repo, add your repo link and in line cd, replace the next text with ur repo username.


• After this, you are advised to trigger a workflow_dispatch and voila, bot will start working.
```


### Anime Group

<a href="https://t.me/Anime_ChatClub"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>


### Follow On

• [Github](https://github.com/StrawHat-Network)


• [Telegram](http://t.me/Animes_Encoded)

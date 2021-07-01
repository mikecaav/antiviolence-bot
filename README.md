# Anti-Violence Discord.py Bot
Welcome, this is the repository to the Anti-Violence bot which
was created to avoid violence in discord servers. This bot uses emotion analysis to detect when a message is being violent
and then sends to a private channel the message to the moderators to
review the message and decide if the user is going to be banned or not.

## Add this to your discord server
If you'd like to add this bot to your discord server you just need to
<a href='https://discord.com/api/oauth2/authorize?client_id=859471254703833099&permissions=8&scope=bot'>click here</a>


## Installation
### Docker
To run this bot with the dockerized image you can 
```
docker run anti-violence-bot
```

### Python
To run this bot on your own and add some modifications you need to: <br/>
Clone this repo:
```
git clone https://github.com/mikecaav/antiviolence-bot.git
cd antiviolence-bot
```

#### Create a virtual environment
Install virtualenv
```
pip install virtualenv
```
Crate the virtual environment
```
virtualenv env
```
Activate your environment
##### Linux
```
source venv/bin/activate
```
##### Windows
```
.\env\Scripts\activate.bat
```

#### Install the python requirements

```
pip install -r requirements.txt
```

Download the weights and configuration files of the emotion analysis model
```
git lfs install
git clone https://huggingface.co/cardiffnlp/twitter-roberta-base-emotion
```
It is important that you wait the weights files to be downloaded, as long
as the files are heavy they may not be downloaded immediately.


## Run
To run the bot and make it work you'll need to add a variable called 
<i>ANTI-VIOLENCE-TOKEN</i> to your environment variables with the token of your
discord application. For more information about how to create your
own discord application, please check. 
<a href='https://www.freecodecamp.org/news/create-a-discord-bot-with-python/'>this blog</a>.
</br>
One you've followed the installation process you can finally run:
```
python bot.py
```

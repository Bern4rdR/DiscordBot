# DiscordBot
A discord bot built in python, on the discord API


### Table of contents
* Project description
* Todo
* Requirements
* Installation
* Testrun
* Issue tracker
* Code conventions
* Contribution
* Citing
* Contact
* Changelog


### Project description
This project is going to be an automated Discord bot that can respond to members of a server. 
A member will type a command in a channel and recieve a responce from the bot.
Functions will include a rock-paper-scissors game that keeps track of the score as well as a scoreboard. 
Other functions will be to play 8ball or maybe even music. The prefix used to activate the bot will default to `?` 
but anyone with access to the code will be able to change it.

**Note:**  Code will have to be adapted, for example every bot has a unique token. 
Strings that requre additonal information are surrounded by two angle brackets `<< >>`, 
information can be found in the Discord [developer portal](https://discord.com/developers/applications).

Here is a UML diagram of the class used in this project, you can find it in the `user.py` file:

![image](https://user-images.githubusercontent.com/96416409/155847726-61b6544d-ab42-4f44-a8b2-5eb41a8d58c4.png)



### Todo
- [x] Store user information
- [x] Rock-paper-scissors
- [x] 8ball
- [x] Dice
- [x] Message history
- [ ] Scoreboard
- [ ] Play music


### Requirements
- python 3.5+
- discord.py module
- requests module


### Installation
The latest versoin of **Python** is available [here](https://www.python.org/downloads/).

To install the `discord.py` package in the command prompt using the command `pip install discord.py`. 
For a guidde on the installation, click [here](https://pypi.org/project/discord.py/). 
Note that discord.py only works with **Python 3.5+**.

For the requests package, type `pip install requests` into your command prompt.
  
To create your own bot, first you need to create an application in the [developer portal](https://discord.com/developers/applications).


### Example run
Teminal:
```
Beep. Boop. . Bot is Ready
```

Discord channel:
```
>>> ?commands
dice + sides (optional) --> roll a die
8ball + question --> ask the magic 8ball a question
rps + choice --> play rock-paper-sissors against the bot
log --> log the last 50 messages in chat
hist + ammount --> show your fist messages

>>> ? rps rock
ROCK vs PAPER
You LOOSE!

>>> ?dice
6

>>> ?8ball Will it rain today?
Most likely
```


### Issue tracker
- `interact.py` --> Adding member: not automated
- `main.py` --> Does not permanently store users
- music requres module, not an API
- sometimes adding people doesn't work (above my pay grade)


### Code conventions
#### File organizing
Code is split up in to different files, by order of functions, for easier interaction and to facilitate contributions.

**Commenting:**  1-line comments are written above the code line to explain its purpose.

**Naming:**  All files use **snake_case** for variable names as in standard PEP8.


### Contributors
This is a scool project and it will get a faling grade if someone other than me (the creator). 
After the grading, pull requests will gladly be accepted and new features would be appreciated.

- WIP


### Citing
Paste this text into the top of your main file:

"All or part of this project uses code that was written by Bern4rdR

Repository: https://github.com/Bern4rdR/DiscordBot"


### Contact
**Author:**  Bernard R [Bern4rdR]

**Mail:**  [rumarbernard@gmail.com](mailto:rumarbernard@gmail.com)

**Discord:**  BernHard#6216


### Changelog
**v0.1**
  
  Added:
  - Manualy add a user through the bot
  
**v0.2**
  
  Added:
  - MINIGAME: Rock paper sissors
  
**v0.3**
  
  Added:
  - MINIGAME: dice
  - MINIGAME: magic 8ball
  
  Fixed:
  - RPS not running if it creats new user

**v0.4**
  
  Added:
  - FEATURE: log the last 50 messages
  - FEATURE: recieve your first messages
  - FEATURE: help command
  
**v0.5**

  Fixed:
  - Can now add user trough command


### Licence
[MIT](https://choosealicense.com/licenses/mit/)

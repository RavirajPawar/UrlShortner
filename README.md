# URLShortner
## _Web app gives you short URL_

## Features

- Simple User Interface
- No need to log in or sign up
- Easy to use


URLShortner is 'flask' web app which uses 'cuttly' for generating short url.
You can get 'docker' image also from here.



## Technologies
- Bootstrap
- Python
- Flask
- Docker 

## Installation

You need to install python first then go for dependencies like flask, request which are already included in requirement.txt 

```sh
python install -r requirements.txt
```

then you need docker as an installed app. You can pull my image using following command.

```sh
sudo docker pull pawarraviraj/urlshortner:latest
```

Once you pulled images you will get IMAGE_ID for that image. Which is visible after entring 

```sh
sudo docker images
```

once you get image in local you need to enter next command. For flask app 5000 is default port exposed. -p stannds for port command says expose host machine's 5000 for docker image in which 5000 port our app is running.
```sh
sudo docker run -p 5000:5000 IMAGE_ID
```



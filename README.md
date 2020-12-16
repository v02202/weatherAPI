# weatherAPI
WeatherAPI is a simple website for looking for weather data. 

## Technologies
Project is created with:
* Python 3.8.6
* Django 3.1.4
* Django-environ 0.4.5
* Docker 19.03.13
* AWS EC2

## Setup
To run this project, install it locally using `git clone https://github.com/v02202/weatherAPI.git`

#### Please add an .env file and specify the following
* SECRET_KEY: please contact me. 

For example:
```
ENV=dev
SECRET_KEY ='YOUR_SECRET_KEY'
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,13.112.174.169
```
#### Use the development mode: RUN ```docker-compose build``` and then RUN ```docker-compose up```
You can connect to your local url: http://127.0.0.1:8000/

#### Check the website: http://13.112.174.169/ 

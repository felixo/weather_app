#Weather api

##Requirements: 
1. docker 

##Configuration:
1. git clone git@github.com:felixo/weather_app.git
2. vim {dir_with_project}/weather_app/weather_app/settings_local.py (Will send in mail)

##Run
./run_weather

###requests:
1. http://0.0.0.0:8081/weather/?city=саратов or http://0.0.0.0:8081/weather/?city=moscow
2. http://0.0.0.0:8081/history/ check history
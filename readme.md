# Weather api

## Requirements: 
- docker 

## Configuration:
- Clone project:
```bash
git clone git@github.com:felixo/weather_app.git
```
- Add private keys (Will send you in mail):
```bash
vim {dir_with_project}/weather_app/weather_app/settings_local.py
```
## Runing
For convenience, the launch of the project is placed in a script run_weather.sh
```bash
cd {/dir/with/project}
./run_weather
```
### Requests:
- Get weather of city in browser: http://0.0.0.0:8081/weather/?city=саратов or 
```bash
curl http://0.0.0.0:8081/weather/?city=moscow
```
- Look history: http://0.0.0.0:8081/history/ or
```bash
curl http://0.0.0.0:8081/history/
```

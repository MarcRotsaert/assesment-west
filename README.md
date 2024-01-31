# Assesment-west

## Startup
### Local start
- Clone the git repository to server
- create python virtual environment

`pip install -r requirements.txt venv` 

- activate  python virtual environment venv
- startup script

 `. start_lowest_local.sh`

Webpage should open, ready for use

### Docker start 
- clone the git repository to server
- install Docker on the server
- setup Docker an activate engine.
- build docker image 

 `. build_docker_img.sh`

- startup docker container with 

 `. start_lowest_container.sh`

Webpage should open, ready for use

## External access
- open port on firewall of the server
- add Ip adress of partner in settings.py, variable \<Allowed-host\>
- make connection to url:

`http://<ipadreshost>:8080/algoritm`

## Unittest
- perform (**from map  src/django_west**):

 `python manage.py test`



# assesment-west

## Local start
- Clone the git repository to 
- startup with start_lowest_local.sh
Webpage should be opened

## Docker start
- Clone the git repository to 
- Download Docker
- build image with build_docker_img.sh
- startup with start_lowest_container.sh


## External access
For access open port on firewall 
Add Ip adress of partner in settings.py, variable Allowed-host

Make connection to url:
http://<ipadreshost>:8080/algoritm

## Unittest
python manage.py test
- activate from map  src/django_west


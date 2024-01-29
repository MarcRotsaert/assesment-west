# remove west docker
container_name=westassesment
image_name=westassesment
# docker ps -f name=kean_mclaren
# docker kill "$(docker container ls -f name=${container_name} -q)"
docker images -f reference=${image_name}
docker rmi "$(docker images -f reference=${image_name} -q)"

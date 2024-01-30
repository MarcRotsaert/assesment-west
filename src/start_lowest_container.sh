container="westassesment"
version="0.1"
west_image="${container}:${version}"
echo "${west_image}"

docker run --rm -idt -p 8080:8080 --name "${container}" "${west_image}"
sleep 10
python3 -m webbrowser -t "http://127.0.0.1:8080/algoritm"

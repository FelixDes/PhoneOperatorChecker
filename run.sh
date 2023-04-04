docker network create backend-internal

docker-compose down --remove-orphans
docker-compose rm -f
docker-compose pull
docker-compose up --build -d
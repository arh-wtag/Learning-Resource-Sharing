# docker run --name learning \
#   -e DB_HOST=postgres \
#   -e DB_USER=postgres \
#   -e POSTGRES_PASSWORD=12345678 \
#   -e DB_NAME=resources \
#   -e DB_PORT=5432 \
#   -p 8000:8000 \
#   -d learning-application

# docker run --name postgres \
#   -e POSTGRES_USER=postgres \
#   -e POSTGRES_PASSWORD=12345678 \
#   -e POSTGRES_DB=resources \
#   -p 5433:5432 \
#   -d postgres

# docker network create my_network


# docker run --name learning \
#   --network my_network \
#   -e DB_HOST=postgres \
#   -e DB_USER=postgres \
#   -e POSTGRES_PASSWORD=12345678 \
#   -e DB_NAME=resources \
#   -e DB_PORT=5432 \
#   -p 8000:8000 \
#   -d learning-application


# docker run --name postgres \
#   --network my_network \
#   -e POSTGRES_USER=postgres \
#   -e POSTGRES_PASSWORD=12345678 \
#   -e POSTGRES_DB=resources \
#   -p 5433:5432 \
#   -d postgres
# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db
```

### Seed the volume (via Docker Desktop)

```bash
i did it with docker desktop
```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 . 
```

### Run the container

```bash
docker run -it --name server1_c -v fastapi-db:/app/db -p 8000:8000 shopping-server1:v1
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -it --name server2_c -v fastapi-db:/app/db -p 8001:8000 shopping-server2:v1 
```
###  create Bind Mount for bakup

```bash
docker stop srever2_c
docker rm server2_c
docker run -it --name server2_c -v ./data/backup_shopping_list.json:/app/bakup -v fastapi-db:/app/db -p 8001:8000 shopping-server2:v1 
```

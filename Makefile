# Makefile
.PHONY: build up logs stop clean

build:
	sudo docker compose up --build

up:
	sudo docker compose up --build -d

logs:
	sudo docker compose logs --tail=100 -f

stop:
	sudo docker compose down

clean:
	sudo docker compose down -v

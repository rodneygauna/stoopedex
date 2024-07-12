# Makefile
.PHONY: build run up stop clean logs shell seed test-env restart

# Docker-related variables
DOCKER_COMPOSE = docker compose

# Build the Docker image
build:
	$(DOCKER_COMPOSE) build

# Run the Docker container
run:
	$(DOCKER_COMPOSE) up

# Build and run the Docker container
up:
	$(DOCKER_COMPOSE) up --build -d

# Stop and remove the Docker container
stop:
	$(DOCKER_COMPOSE) down

# Clean up Docker images and volumes
clean:
	$(DOCKER_COMPOSE) down -v --rmi local

# View the logs
logs:
	$(DOCKER_COMPOSE) logs --tail=100 -f

# Container shell
shell:
	$(DOCKER_COMPOSE) exec app sh

# Seed the database with test data
seed_users:
	$(DOCKER_COMPOSE) exec app flask commands seed_users

seed_events:
	$(DOCKER_COMPOSE) exec app flask commands seed_events

seed_attendees:
	$(DOCKER_COMPOSE) exec app flask commands seed_attendees

seed: seed_users seed_events seed_attendees

# Test environment
test-env: clean up seed logs

# Quick restrat
restart: stop up logs

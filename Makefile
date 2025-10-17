.PHONY: up down restart clean logs rebuild help check-env

# Default target
.DEFAULT_GOAL := help

# Environment file validation
check-env:
	@if [ ! -f .env ]; then \
		echo "❌ Error: .env file not found!"; \
		echo ""; \
		echo "📋 To create the .env file:"; \
		echo "   cp .env.template .env"; \
		echo ""; \
		echo "⚙️ Then edit .env and configure:"; \
		echo "   - LOCAL_PORT (default: 8080)"; \
		echo "   - ENVIRONMENT (local/staging/production)"; \
		echo "   - BASE_URL (localhost:port for local dev)"; \
		echo ""; \
		echo "📖 Example for local development:"; \
		echo "   LOCAL_PORT=8080"; \
		echo "   ENVIRONMENT=local"; \
		echo "   BASE_URL=http://localhost:8080/"; \
		exit 1; \
	fi

up: check-env ## Start all Docker services for local development
	docker compose -f docker-compose.yml -f docker-compose.local.yml up -d

down: ## Stop and remove all containers
	docker compose -f docker-compose.yml -f docker-compose.local.yml down

restart: down up ## Restart all containers (stop and start)

clean: down ## Complete cleanup: remove containers, images, and volumes
	docker compose -f docker-compose.yml -f docker-compose.local.yml down -v --rmi all
	docker system prune -f

logs: ## Show logs from all services
	docker compose -f docker-compose.yml -f docker-compose.local.yml logs -f

rebuild: clean ## Force rebuild all Docker images
	docker compose -f docker-compose.yml -f docker-compose.local.yml build --no-cache
	docker compose -f docker-compose.yml -f docker-compose.local.yml up -d

help: ## Show this help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: up down clean logs rebuild help check-env

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
		echo "   - BASE_URL (your local IP:port for local dev)"; \
		echo ""; \
		echo "📖 Example for local development:"; \
		echo "   LOCAL_PORT=8080"; \
		echo "   ENVIRONMENT=local"; \
		echo "   BASE_URL=http://192.168.1.100:8080/"; \
		exit 1; \
	fi

up: check-env ## Start all Docker services
	docker-compose --profile local up -d

down: ## Stop and remove all containers
	docker-compose --profile local down

clean: down ## Complete cleanup: remove containers, images, and volumes
	docker-compose down -v --rmi all
	docker system prune -f

logs: ## Show logs from all services
	docker-compose --profile local logs -f

rebuild: clean ## Force rebuild all Docker images
	docker-compose --profile local build --no-cache
	docker-compose --profile local up -d

help: ## Show this help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
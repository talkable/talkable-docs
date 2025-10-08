# =============================================================================
# Talkable Documentation - Local Development Makefile
# =============================================================================

# Default values (will be overridden by .env file if it exists)
ENVIRONMENT ?= local
LOCAL_PORT ?= 8080

# Docker Compose configuration
COMPOSE_FILE := docker-compose-local.yml
CONTAINER_NAME := docs-$(ENVIRONMENT)

# Check if .env file exists and load it
ifneq (,$(wildcard .env))
    include .env
    ENV_FILE_EXISTS = true
else
    ENV_FILE_EXISTS = false
endif

# Validate required environment variables
ifeq ($(ENV_FILE_EXISTS),false)
    ENV_ERROR = .env file not found
else ifeq ($(ENVIRONMENT),)
    ENV_ERROR = ENVIRONMENT variable not defined in .env file
else ifeq ($(LOCAL_PORT),)
    ENV_ERROR = LOCAL_PORT variable not defined in .env file
else
    ENV_ERROR = 
endif

# Default target
.PHONY: help
help: ## Show available commands
	@echo "Talkable Documentation - Local Development"
	@echo "=========================================="
	@echo ""
	@if [ "$(ENV_ERROR)" != "" ]; then \
		echo "❌ Configuration Error: $(ENV_ERROR)"; \
		echo ""; \
		echo "To fix this issue:"; \
		echo "1. Copy the template: cp .env.template .env"; \
		echo "2. Edit .env file and ensure these variables are set:"; \
		echo "   - ENVIRONMENT=local"; \
		echo "   - LOCAL_PORT=8080"; \
		echo ""; \
	else \
		echo "✅ Configuration loaded from .env file"; \
		echo ""; \
		echo "Available commands:"; \
		echo "  make setup     Create .env file from template"; \
		echo "  make up        Start local development server"; \
		echo "  make down      Stop local development server"; \
		echo "  make clean     Remove containers and clean up residuals"; \
		echo "  make logs      View development server logs"; \
		echo "  make status    Check container status"; \
		echo "  make start     Quick setup and start (alias for setup + up)"; \
		echo "  make stop      Quick stop and cleanup (alias for down + clean)"; \
		echo ""; \
		echo "Environment: $(ENVIRONMENT)"; \
		echo "Port: $(LOCAL_PORT)"; \
		echo "Access: http://localhost:$(LOCAL_PORT)"; \
	fi

# =============================================================================
# Core Development Targets
# =============================================================================

.PHONY: up
up: ## Start local development server
	@if [ "$(ENV_ERROR)" != "" ]; then \
		echo "❌ Cannot start: $(ENV_ERROR)"; \
		echo "Run 'make help' for instructions on how to fix this."; \
		exit 1; \
	fi
	@echo "Starting local development server..."
	@echo "Environment: $(ENVIRONMENT)"
	@echo "Port: $(LOCAL_PORT)"
	@echo "Access: http://localhost:$(LOCAL_PORT)"
	@echo ""
	docker compose -f $(COMPOSE_FILE) up --build -d

.PHONY: down
down: ## Stop local development server
	@echo "Stopping local development server..."
	docker compose -f $(COMPOSE_FILE) down

# =============================================================================
# Cleanup Targets
# =============================================================================

.PHONY: clean
clean: ## Remove containers and clean up all residuals
	@echo "Cleaning up all residuals..."
	@echo "Stopping containers..."
	docker compose -f $(COMPOSE_FILE) down -v
	@echo "Removing container images..."
	docker rmi $(CONTAINER_NAME) 2>/dev/null || true
	@echo "Removing unused Docker objects..."
	docker system prune -f
	@echo "Cleanup complete!"

# =============================================================================
# Utility Targets
# =============================================================================

.PHONY: logs
logs: ## View development server logs
	@if [ "$(ENV_ERROR)" != "" ]; then \
		echo "❌ Cannot view logs: $(ENV_ERROR)"; \
		echo "Run 'make help' for instructions on how to fix this."; \
		exit 1; \
	fi
	@echo "Following logs for $(CONTAINER_NAME)..."
	docker compose -f $(COMPOSE_FILE) logs -f

.PHONY: status
status: ## Check container status
	@echo "Container status:"
	docker compose -f $(COMPOSE_FILE) ps

# =============================================================================
# Environment Setup Target
# =============================================================================

.PHONY: setup
setup: ## Create .env file from template if it doesn't exist
	@if [ ! -f .env ]; then \
		echo "Creating .env file from template..."; \
		cp .env.template .env; \
		echo "✅ .env file created successfully"; \
		echo "   You can now run 'make help' to see available commands"; \
	else \
		echo "ℹ️  .env file already exists"; \
	fi

# =============================================================================
# Quick Start Target
# =============================================================================

.PHONY: start
start: setup up ## Quick setup and start

.PHONY: stop
stop: down clean ## Quick stop and cleanup

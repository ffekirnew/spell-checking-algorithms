.phony: test-run wagner-fischer

test-run:
	@echo "Loading the words dictionary..."
	@python3 src/main.py

test:
	@echo "Running tests..."
	@python3 -m test src/**/*_test.py

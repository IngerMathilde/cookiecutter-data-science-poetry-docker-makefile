.PHONY: clean data lint install docker push format

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = {{ cookiecutter.s3_bucket }}
PROFILE = {{ cookiecutter.aws_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
SRC_DIR = {{ cookiecutter.source_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################
ifeq ($(OS),Windows_NT)
VENV_BIN = .venv/Script
else
VENV_BIN = .venv/bin
endif


## Set up python interpreter environment
create_environment:
	@echo ">>> Creating environment"
	$(PYTHON_INTERPRETER) -m pip install --upgrade pip
	$(PYTHON_INTERPRETER) -m pip install -U poetry
	$(PYTHON_INTERPRETER) -m poetry config virtualenvs.create true
	$(PYTHON_INTERPRETER) -m poetry config virtualenvs.in-project true

## Install Python Dependencies
install: create_environment
	@echo ">>> Installing python dependencies"
	$(PYTHON_INTERPRETER) -m poetry update --lock # ensures all dependencies are as up-to-date as possible
	$(PYTHON_INTERPRETER) -m poetry install --no-root

	@echo ">>> Activate virtual environment for windows and posix"
	@echo "$(shell pwd) $(PWD) $(VENV_BIN)"
	. $(VENV_BIN)/activate && exec bash



## Make Dataset
data:
	@echo ">>> Making dataset"
	PYTHONPATH=$(SRC_DIR) $(PYTHON_INTERPRETER) $(SRC_DIR)/data/make_dataset.py data

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 $(SRC_DIR)

## Format using black
format:
	black $(SRC_DIR)

## Run bandit security test
bandit:
	poetry run bandit -n 3 -r $(SRC_DIR)

test:
	PYTHONPATH=$(SRC_DIR) poetry run pytest

## Building docker repos
docker:
	docker-compose build

## Pushing docker repos
push: docker
	docker-compose up

## Upload Data to S3
sync_data_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync data/ s3://$(BUCKET)/data/
else
	aws s3 sync data/ s3://$(BUCKET)/data/ --profile $(PROFILE)
endif

## Download Data from S3
sync_data_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/data/ data/
else
	aws s3 sync s3://$(BUCKET)/data/ data/ --profile $(PROFILE)
endif

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')

# Remove compiled bytecode of source files
dev-clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*.pytest_cache' -exec rm -fr {} +

# Setup the project environment by:
# - Run pipenv shell to start the virtual env
# - Make pipenv use python defined by conda
# - Active housing_env with conda
env:
	pipenv shell
	pipenv --python=$(conda run which python) --site-packages
	conda activate housing_env

# Install all libraries of package
install-all:
	pipenv install --system --dev

# Install a package 
install:
	pipenv install $(pkg)

# Install a package in dev mode
install-dev:
	pipenv install --dev $(pkg)

# Run the model
model:
	pipenv run python src/main.py

# Run the model and predict a random value from our dataset.
predict:
	pipenv run python src/predict.py

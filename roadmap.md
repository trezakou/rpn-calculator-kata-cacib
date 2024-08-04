# Roadmap:

## Technical side:

- Add `pyproject.toml` file
- Implement Poetry for Python package and environment management
- Implement Linting with Ruff, flake8 & Black for example
- Implement pre-commit for auto linting and automated code correction and review before commits
- Implement docker (also useful in order to use PostgreSQL in a container)
- Improve logging, with loguru for example
- Implement CI/CD pipeline if the project is meant to be deployed in a production environment
- Add Authentification


## Operational side:

- Add tests
- add user-based access to the stacks, this allows users to use the tool without risking to touch other users calculations
- Add stack memory, to allow rollback of operations
- and other mathematical operations (square root, exponential, etc)
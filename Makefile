lint:
	@black --line-length 79 --target-version py39 dags plugins
	@isort --profile black --wrap-length 200 --line-length 200 dags plugins
	@autoflake --in-place --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --recursive dags plugins

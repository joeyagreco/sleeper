@echo off

IF "%1"=="fmt" (
    :: Format the code using Black and Autoflake
    black --config=pyproject.toml .
    autoflake --config=pyproject.toml .
) ELSE IF "%1" == "test" (
    :: Run tests using pytest
    cd test
    pytest
    cd ..
) ELSE IF "%1"=="cov" (
    :: Generate code coverage
    cd test
    coverage run -m pytest
    coverage xml -o coverage.xml
    coverage html
    cd ..
) ELSE (
    echo Invalid flag. Please specify a valid flag.
)

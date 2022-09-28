from functools import lru_cache

import inflection


@lru_cache
def to_cameCase(value: str) -> str:
    """Convert a string to camelCase"""
    return inflection.camelize(value, uppercase_first_letter=False)


@lru_cache
def to_snake_case(value: str) -> str:
    """Convert a string to snake_case"""
    return inflection.underscore(value)

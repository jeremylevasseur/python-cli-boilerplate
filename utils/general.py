from typing import Any


def build_payload(**kwargs: Any) -> dict[str, Any]:
    """
    Builds a dictionary payload for HTTP requests, excluding keys with None values.

    Args:
        **kwargs: Arbitrary keyword arguments representing the payload data.

    Returns:
        dict[str, Any]: The payload dictionary with keys that have non-None values.
    """
    return {key: value for key, value in kwargs.items() if value is not None}

def greet(name):
    """Build a greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        The greeting string ``"Hello, <name>!"``.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("world"))

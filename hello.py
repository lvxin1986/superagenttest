def greet(name):
    """Build a greeting for the given name.

    Args:
        name: The name to greet.

    Returns:
        The greeting string ``"Hello, <name>!"``.
    """
    return f"Hello, {name}!"


def square(number):
    """Compute the square of the given number.

    Args:
        number: The number to square.

    Returns:
        The product ``number * number``.
    """
    return number * number


if __name__ == "__main__":
    print(greet("world"))
    print(square(4))

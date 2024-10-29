# ID успешной посылки: 122873851.

def decoded_instructions(compressed_message: str) -> str:
    """Функция, которая расшифровывает сжатые сообщения
    и возвращает строку с командами.
    """
    commands: str = ''
    multiplier: str = ''
    stack: list[tuple[str, str]] = []

    for symbol in compressed_message:

        if symbol.isdigit():
            multiplier += symbol
        elif symbol == '[':
            stack.append((commands, multiplier))
            commands, multiplier = '', ''
        elif symbol == ']':
            symbol, multiplier = stack.pop()
            commands *= int(multiplier)
            commands = symbol + commands
            multiplier = ''
        else:
            commands += symbol

    return commands


if __name__ == '__main__':
    compressed_message = [str(symbol) for symbol in input()]
    print(decoded_instructions(compressed_message))

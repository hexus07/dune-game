from colorama import Fore

def colored(color: str, message: str) -> str:
    return f"{getattr(Fore, color.upper())}{message}{Fore.RESET}"

def bright(message: str) -> str:
    return colored('LIGHTWHITE_EX', message)

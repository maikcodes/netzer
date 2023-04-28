from colorama import Back, Fore, init, Style
import pprint

init(autoreset=True)


def print_process(message):
    print(
        f'\n{Style.BRIGHT}{Back.LIGHTYELLOW_EX}{Fore.BLACK}{message} 🔃...'
    )


def print_result(message):
    print(f'\n{Style.BRIGHT}{Fore.CYAN}{message}')


def print_array_result(message):
    print(f'\n{Style.BRIGHT}{Fore.GREEN}Array result:')
    print(f'{message}\n\n')

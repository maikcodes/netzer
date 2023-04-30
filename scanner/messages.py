from colorama import Back, Fore, init, Style

init(autoreset=True)


def print_process(message):
    print(
        f'\n{Style.BRIGHT}{Back.LIGHTYELLOW_EX}{Fore.BLACK}{message} 🔃...'
    )


def print_processing(message):
    print(f'\n{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{message}\n')


def print_blue_result(message, result):
    print(f'\n{Style.BRIGHT}{Fore.CYAN}{message}:')
    print(f'{result}')


def print_green_result(message, result):
    print(f'\n{Style.BRIGHT}{Fore.GREEN}{message}:')
    print(f'{result}')

def print_end_process():
    print(f'\n{Style.BRIGHT}{Fore.YELLOW}End process')

"""make_steam_link.py creates hyperlinks for use in steam messages."""
#!python3

import sys
from colorama import Fore

##### START CONFIGURATION #####
# Configure your URL to generate here
SUBDOMAIN = "oo."
DOMAIN = "ok"
SUBDOMAIN_COUNT = 1
# If you want to turn a Steam message into a hyperlink mess,
# This is your place. Configure your message to linkify here:
MSG_TO_LINKIFY = "This message will have been linkified"
# You can just run the script now from here :)
###### END CONFIGURATION ######

##### START CONSTRAINTS #####
STEAM_MAX_SUBDOMAIN_NAME_CHARS = 63
# The max amount of subdomains seems to vary depending on the length of the subdomain
# All of the below have been witnessed
# STEAM_MAX_SUBDOMAINS = 15
# STEAM_MAX_SUBDOMAINS = 126
# Regardless, these numbers are off, and right now you actually have 30 subdomains and a domain
# We will call it 31 until a refactor
STEAM_MAX_SUBDOMAINS = 31
STEAM_MAX_MESSAGE_CHARS = 5000
# The overall maximum amount of subdomains allowed in a URL
MAXIMUM_SUBDOMAINS = 500
##### END CONSTRAINTS #####


def make_steam_hyperlink(
    subdomain=SUBDOMAIN, subdomain_count=SUBDOMAIN_COUNT, domain=DOMAIN, truncate=False
):
    """Makes a steam hyperlink to be inserted into a steam message"""

    if subdomain_count == 0:
        message = f"{domain}"
        return message
    if subdomain_count > STEAM_MAX_SUBDOMAINS:
        print("Too many subdomains.")
        print(
            f"Subdomain count: {Fore.RED}{subdomain_count}{Fore.RESET} / {STEAM_MAX_SUBDOMAINS}"
        )
        sys.exit()
    overage = len(subdomain) - 1
    if overage > STEAM_MAX_SUBDOMAIN_NAME_CHARS:
        print(f"Subdomain: '{subdomain}' is too long.")
        print(
            f"Characters: {Fore.RED}{overage}{Fore.RESET} / {STEAM_MAX_SUBDOMAIN_NAME_CHARS}"
        )
        sys.exit()

    # Make a message
    message = f"{subdomain_count * subdomain}{domain}"
    # print(f"Message: \n{message}")

    # Check the length of the message
    message_length = len(message)
    if message_length > STEAM_MAX_MESSAGE_CHARS:
        if truncate:
            message = truncate_message(message, top_level_domain=domain)
        else:
            print(f"Message is too long. Max is {STEAM_MAX_MESSAGE_CHARS}")
            print(f"Length: {len(message)}")
            sys.exit()

    if subdomain_count > 1:
        print(f"Subdomain: {Fore.GREEN}{subdomain}{Fore.RESET}")
        print(
            f"Subdomain count: {Fore.GREEN}{len(message.split('.'))-2}{Fore.RESET} / {STEAM_MAX_SUBDOMAINS}"
        )
        print(f"Domains: {Fore.GREEN}1{Fore.RESET}")
    else:
        print(f"Domain: {Fore.GREEN}{subdomain}{Fore.RESET}")

    print(f"Top Level Domain: {Fore.GREEN}{domain}{Fore.RESET}")
    print(
        f"Total Message Length: {Fore.GREEN}{len(message)}{Fore.RESET} / {STEAM_MAX_MESSAGE_CHARS}"
    )

    return message


def truncate_message(
    message, max_chars=STEAM_MAX_MESSAGE_CHARS, top_level_domain=DOMAIN
):
    """Truncates a message to 5000 characters and adds a top level domain"""

    if len(message) > max_chars:
        print("Message is too long but will be truncated.")
        print(f"Message length: {len(message)} will be cut down to {max_chars}")
    # Truncate enough to add the top level domain without going over 5000
    message = message[: max_chars - (len(top_level_domain) + 1)]
    # check if the last character is a period
    if message[-1] == ".":
        message = f"{message}{top_level_domain}"
    else:
        # add the top level domain
        message = f"{message}.{top_level_domain}"

    print("[!] Truncated message.)")
    return message


def linkify(message=MSG_TO_LINKIFY):
    """Linkifies your message"""

    # Split the message into words
    words = message.split(" ")
    # Make a new list to hold the linkified words
    linkified_words = []
    # Iterate over the words
    for word in words:
        if len(word) > 3:
            # If the word is longer than 3 characters, put a period before the last 2 characters
            linkified_word = f"{word[:-2]}.{word[-2:]}"
            # Add the linkified word to the list
            linkified_words.append(linkified_word)
        else:
            # Add the word to the list
            linkified_words.append(word)

    # Join the words back together
    linkified_message = " ".join(linkified_words)
    return linkified_message


if __name__ == "__main__":
    # Make the hyperlink
    steam_message = make_steam_hyperlink()

    # Print the hyperlink
    print(
        f"{Fore.CYAN}\n [*] Copy the Steam hyperlink below:{Fore.RESET}")
    print(f"\n{steam_message}\n")

    # Print a linkified message
    print(f"{Fore.MAGENTA}\n [*] Linkified message:{Fore.RESET}")
    print(f"\n{linkify()}\n")

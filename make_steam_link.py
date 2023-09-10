"""
Name: make_steam_hyperlink.py
Author: Allen Montgomery, IO Security
Version: 0.0.3
Purpose: Creates hyperlinks for use in Steam chat messages.
"""

import sys
from colorama import Fore

# Configure your URI to generate here
# Change Host, Subdomains and Domain (TLD) to make a FQDN
HOST = "i1li1li1l."
SUBDOMAIN = "li1li1li1."
SUBDOMAIN_COUNT = 1
# Top Level Domain
DOMAIN = "il"

# Enter a string to transform into a 'linkified' Steam chat message
# TODO: Handle special characters :)
MSG_TO_LINKIFY = "Please download this cool link thanks much"

# You can just run the script now from here, unless you want to test constraints below

# CONSTRAINTS
STEAM_MAX_SUBDOMAIN_NAME_CHARS = 63
# TODO: Find out how these numbers are doubled/halved in Steam messages. Interesting coincidence.
# STEAM_MAX_SUBDOMAINS = [15, 31, 126]
STEAM_MAX_SUBDOMAINS = 31
STEAM_MAX_MESSAGE_CHARS = 5000


def make_steam_hyperlink(
    host=HOST,
    subdomain=SUBDOMAIN,
    subdomain_count=SUBDOMAIN_COUNT,
    domain=DOMAIN,
    truncate=False,
):
    """Makes a steam hyperlink to be inserted into a Steam chat message"""

    # Handle if you dont pass in any host or subdomain
    if host == "" and subdomain == "":
        print("No host or subdomain specified. Exiting.")
        sys.exit(1)

    # If you dont have a host but you defined a subdomain, use the subdomain as the host
    if host == "" and subdomain != "":
        host = subdomain
        subdomain_count += 1

    # If you don't have a count, just return the domain name
    if subdomain_count == 0:
        return f"{host}{domain}"

    # Check the quantity of subdomains against max limit
    if subdomain_count > STEAM_MAX_SUBDOMAINS:
        print("Too many subdomains.")
        print(
            f"Subdomain count: {Fore.RED}{subdomain_count}{Fore.RESET} / {STEAM_MAX_SUBDOMAINS}"
        )
        sys.exit(1)

    # Check the amount of characters in your subdomain against max limit
    overage = len(subdomain) - 1
    if overage > STEAM_MAX_SUBDOMAIN_NAME_CHARS:
        print(f"Subdomain: '{subdomain}' is too long.")
        print(
            f"Characters: {Fore.RED}{overage}{Fore.RESET} / {STEAM_MAX_SUBDOMAIN_NAME_CHARS}"
        )
        sys.exit(1)

    # Put together the URI for a hyperlink
    hyperlink = f"{subdomain_count * subdomain}{host}{domain}"

    # Check the overall length of the message
    message_length = len(hyperlink)
    # Choose between killing the program or truncating the message
    if message_length > STEAM_MAX_MESSAGE_CHARS:
        # If would set truncate to True, truncate the message
        if truncate:
            message = truncate_message(message, tld=domain)
        else:
            print(f"Message is too long. Max is {STEAM_MAX_MESSAGE_CHARS}")
            print(f"Length: {len(hyperlink)}")
            sys.exit(1)

    print(f"Host: {Fore.GREEN}{host}{Fore.RESET}")
    print(f"Subdomain: {Fore.GREEN}{subdomain}{Fore.RESET}")
    # We are subtracting 2 here for both the top level domain and the hostname
    print(
        f"Subdomain count: {Fore.GREEN}{len(hyperlink.split('.'))-2}{Fore.RESET} / {STEAM_MAX_SUBDOMAINS} and {Fore.GREEN}1{Fore.RESET} domain"
    )
    print(f"Top Level Domain: {Fore.GREEN}{domain}{Fore.RESET}")
    print(
        f"Total Message Length: {Fore.GREEN}{len(hyperlink)}{Fore.RESET} / {STEAM_MAX_MESSAGE_CHARS}"
    )

    return hyperlink


def truncate_message(message, max_chars=STEAM_MAX_MESSAGE_CHARS, tld=DOMAIN):
    """Truncates a message to 5000 characters and adds a top level domain"""

    if len(message) > max_chars:
        print("Message is too long but will be truncated.")
        print(f"Message length: {len(message)} will be cut down to {max_chars}")
    # Truncate enough to add the top level domain without going over 5000
    message = message[: max_chars - (len(tld) + 1)]
    # check if the last character is a period
    if message[-1] == ".":
        message = f"{message}{tld}"
    else:
        # add the top level domain
        message = f"{message}.{tld}"

    print("[!] Truncated message.)")
    return message


def linkify(message=MSG_TO_LINKIFY, truncate=False):
    """Converts a string of text, a message, into a hyperlinked version"""

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
    # Check the length of the message
    if len(linkified_message) > STEAM_MAX_MESSAGE_CHARS:
        if truncate:
            linkified_message = linkified_message[:STEAM_MAX_MESSAGE_CHARS]
        else:
            print("Message is too long. Max is 5000")
            print(f"Length: {len(linkified_message)}")
            sys.exit(1)

    return linkified_message


if __name__ == "__main__":
    print(
        f"{Fore.LIGHTGREEN_EX}->{Fore.RESET} {Fore.LIGHTBLUE_EX}ma.ke_ste.am_hyperli.nk.py{Fore.RESET} {Fore.LIGHTGREEN_EX}<-{Fore.RESET}"
    )
    print(f"{Fore.LIGHTGREEN_EX}Version: {Fore.RESET}0.0.3")
    print(f"{Fore.LIGHTGREEN_EX}WHY? {Fore.RESET}No reason. Just for the lulz.")
    print()
    # Make the hyperlink
    steam_message = make_steam_hyperlink()

    # Print the hyperlink
    print(f"{Fore.CYAN}\n [*] Copy the Steam hyperlink below:{Fore.RESET}")
    print(f"\n{steam_message}\n")

    # Print a linkified message
    print(f"{Fore.MAGENTA}\n [*] Copy the Steam Linkified message:{Fore.RESET}")
    print(f"\n{linkify()}\n")

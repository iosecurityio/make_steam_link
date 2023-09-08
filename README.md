# make_steam_link.py

Steam will automatically create a hyperlink in a message if it detects a valid URL scheme. This has gotten a little lenient and now doesn't even require the `https://` protocol. This scheme is just 2 characters, a period, and 2 more characters (ie. a small hostname and a small Top Level Domain). These are also inherently given an `http://` protocol, but thats a different story.

This script creates tests for hyperlinks in a Steam chat message. Change the configuration settings at the top of the script for testing.

## Usage

1. Edit the file `make_steam_link.py`

1. Run the file `python3 make_steam_link.py`

## Example Output
The largest available hyperlink I've been able to make is 1986 characters with the following output:

```shell
Subdomain: abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.
Subdomain count: 31 / 31
Top Level Domain: ab
Total Message Length: 1986 / 5000

[*] Copy the Steam hyperlink below:

abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.ab
```

Likewise, the smallest is something like this:

```shell
Domain: oo.
Top Level Domain: ok
Total Message Length: 5 / 5000

[*] Copy the Steam hyperlink below:

oo.ok
```

and finally, linkified text will turn every word that is >= 4 characters long into a hyperlink. For example:

```shell
[*] Linkified message:

Th.is messa.ge wi.ll ha.ve be.en linkifi.ed
```

## Observations

The constraints seem to vary. What seems to be true is you need 5 total characters to create a link. You need two characters for the hostname and two characters for the Top Level Domain. The period is the 5th character.

I need to fix some vernacular for referring to the parts of a URL. I'm using "Subdomain" to refer to the hostname, but that's not correct. The hostname is the entire thing. The subdomain is the part before the hostname. The Top Level Domain is the part after the hostname. Some counts might be off because of this, but it's arbitrary.

## Valid Links

![Hyperlinks](./static/example_links.png)

![Linkified](./static/linkified_message.png)

![Linkified](./static/big_link.png)

- `ha.ha`

- `co.co`

- `mo.us`

- `jo.in`

- `co.ol`

- `co.de`

- `abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabc.ab`

- ... and nearly all of your favorite 4 letter words that end in `ck`, `nt`, `ss`, etc.

- The possibilities are endless!

### Constraints

- The Subdomain can not be longer than 63 characters long

- The amount of subdomains is limited to 31

  - I have notes of 126 maximum characters, but I can't seem to reproduce that.

  - I also have notes of only being allowed 15 subdomains

  - The maximum amount of subdomains possible is capped at 500. Steam doesn't come close to that.

- The Top Level Domain has to be valid, or on an allow list of sorts.

- Steams character count for a message is 5000 characters.

### Final Notes

- Update: You can now Linkify your Steam messages. Example output above.

- TODO: Add more tests and more research into what I'm doing with my life.

- TODO: Clean up vernacular around subdomain/domain/hostname.

- TODO: Refactor into a class and add more functionality.
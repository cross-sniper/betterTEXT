__version__ = "betterTEXT v1"
from termcolor import colored
import webbrowser

def color_text(text, color):
    """
    Returns colored text using the specified color.
    """
    return colored(text, color)

def println(text, color=None):
    """
    Prints formatted text to the console with optional color.
    """
    if color:
        text = colored(text, color)
    print(text)

def request(prompt, color=None):
    """
    Prompts the user for input with optional color and returns the input value.
    """
    if color:
        prompt = colored(prompt, color)
    return input(prompt)


def multicolor_text(text, colors=None):
    """
    Returns the specified text with different colors.
    """
    if colors:
        parts = text.split(" ")
        colored_parts = [colored(part, colors[i % len(colors)]) for i, part in enumerate(parts)]
        return " ".join(colored_parts)
    else:
        return text

def multicolor_input(prompt, colors=None):
    """
    Prompts the user for input with the specified prompt and colors.
    """
    if colors:
        prompt = multicolor_text(prompt, colors)
    return input(prompt)



def search_online(query):
    """
    Searches for the specified query online using the default web browser.
    """
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

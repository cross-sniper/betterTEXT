
# betterTEXT

betterTEXT is a Python module that provides some enhanced text-related functionalities. It includes the following functions:

## `color_text(text, color)`

Returns colored text using the specified color.

### Parameters:

- `text` (str): The text to color.
- `color` (str): The color to use for the text. Must be one of the supported colors by the `termcolor` package (e.g., 'red', 'green', 'yellow', 'blue', etc.).

### Returns:

- A colored version of the input text.

## `println(text, color=None)`

Prints formatted text to the console with optional color.

### Parameters:

- `text` (str): The text to print.
- `color` (str, optional): The color to use for the text. Must be one of the supported colors by the `termcolor` package (e.g., 'red', 'green', 'yellow', 'blue', etc.). Default is `None`.

### Returns:

- None.

## `request(prompt, color=None)`

Prompts the user for input with optional color and returns the input value.

### Parameters:

- `prompt` (str): The prompt to display to the user.
- `color` (str, optional): The color to use for the prompt. Must be one of the supported colors by the `termcolor` package (e.g., 'red', 'green', 'yellow', 'blue', etc.). Default is `None`.

### Returns:

- The user input value.

## `search_online(query)`

Searches for the specified query online using the default web browser.

### Parameters:

- `query` (str): The query to search online.

### Returns:

- None.

## `multicolor_text(text, color=None)`

Returns a string with each character in a different color.

### Parameters:

- text (str): The text to color.
- color (str, optional): The color to use for the text. Must be one of the supported colors by the termcolor package (e.g., 'red', 'green', 'yellow', 'blue', etc.). Default is None.
### Returns:
- A string with each character in a different color.

## `multicolor_input(prompt, color=None)`

Prompts the user for input with each character in a different color.

### Parameters:
- prompt (str): The prompt to display to the user.
- color (str, optional): The color to use for the prompt. Must be one of the supported colors by the termcolor package (e.g., 'red', 'green', 'yellow', 'blue', etc.). Default is None.

### Returns:
- The user input value.


To use the `betterTEXT` module, you need to import it into your Python scripts:

```python
import betterTEXT
```

Then, you can use the module's functions as follows:

```python
# Colored text
print(betterTEXT.color_text("Hello, world!", "red"))

# Formatted print
betterTEXT.println("This is a formatted message", "green")

# User input
name = betterTEXT.request("What is your name? ")
betterTEXT.println(f"Hello, {name}!", "blue")

# Online search
betterTEXT.search_online("Python documentation")

# Multicolor text
print(betterTEXT.multicolor_text("Multicolor text!", "magenta"))

# Multicolor input
answer = betterTEXT.multicolor_input("Type something here: ", "yellow")
print(f"You typed: {answer}")
```
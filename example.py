#example.py
import betterTEXT


print(betterTEXT.color_text("Hello, world!", "red"))

# Formatted print
betterTEXT.println("This is a formatted message", "green")

# User input
name = betterTEXT.request("What is your name? ")
betterTEXT.println(f"Hello, {name}!", "blue")

# Online search
#betterTEXT.search_online("Python documentation")

# Multicolor text
betterTEXT.multicolor_text("Multicolor text!", ["blue","yellow"])

# Multicolor input
answer = betterTEXT.multicolor_input("Type something here: ", ["blue","red"])
print(f"You typed: {answer}")
import matplotlib.pyplot as plt

# Mapping characters to unique RGBA colors
character_colors = {
    'a': (0, 0, 1, 1),             # Blue
    'b': (0, 0, 0, 1),             # Black
    'c': (0.2, 0.2, 0.2, 1),       # Dark gray
    'd': (0.4, 0.4, 0.4, 1),       # Gray
    'e': (0.6, 0.6, 0.6, 1),       # Light gray
    'f': (0.8, 0.8, 0.8, 1),       # Very light gray
    'g': (1, 0, 0, 0.5),           # Semi-transparent red
    'h': (0, 1, 0, 0.5),           # Semi-transparent green
    'i': (0, 0, 1, 0.5),           # Semi-transparent blue
    'j': (1, 0, 1, 0.5),           # Semi-transparent magenta
    'k': (0, 1, 1, 0.5),           # Semi-transparent cyan
    'l': (1, 1, 0, 0.5),           # Semi-transparent yellow
    'm': (0.5, 0, 0.5, 0.5),       # Semi-transparent purple
    'n': (0.5, 0.5, 0, 0.5),       # Semi-transparent olive
    'o': (0, 0.5, 0.5, 0.5),       # Semi-transparent teal
    'p': (0.5, 0, 0, 0.5),         # Semi-transparent maroon
    'q': (0.5, 0.5, 0.5, 0.5),     # Semi-transparent silver
    'r': (0, 0, 0.5, 0.5),         # Semi-transparent navy
    's': (0, 0.5, 0, 0.5),         # Semi-transparent green
    't': (0.5, 0, 0, 0.5),         # Semi-transparent olive
    'u': (0.5, 0, 0.5, 0.5),       # Semi-transparent purple
    'v': (0, 0.5, 0.5, 0.5),       # Semi-transparent teal
    'w': (0.5, 0.5, 0, 0.5),       # Semi-transparent olive
    'x': (0.5, 0.5, 0.5, 0.5),     # Semi-transparent silver
    'y': (0.5, 0.5, 0, 0.5),       # Semi-transparent olive
    'z': (0, 0.5, 0, 0.5),         # Semi-transparent green
    'A': (1, 0, 0, 1),             # Red
    'B': (0, 1, 0, 1),             # Green
    'C': (0, 0, 1, 1),             # Blue
    'D': (1, 0, 1, 1),             # Magenta
    'E': (0, 1, 1, 1),             # Cyan
    'F': (1, 1, 0, 1),             # Yellow
    'G': (0.5, 0, 0.5, 1),         # Purple
    'H': (0.5, 0.5, 0, 1),         # Olive
    'I': (0, 0.5, 0.5, 1),         # Teal
    'J': (0.5, 0, 0, 1),           # Maroon
    'K': (0.5, 0.5, 0.5, 1),       # Silver
    'L': (0, 0, 0.5, 1),           # Navy
    'M': (0, 0.5, 0, 1),           # Lime
    'N': (0, 0, 0, 1),             # Black
    'O': (1, 1, 1, 1),             # White
    'P': (0.5, 0.5, 0.5, 1),       # Gray
    'Q': (1, 0.5, 0, 1),           # Orange
    'R': (0.5, 0, 0, 1),           # Maroon
    'S': (0, 0.5, 0, 1),           # Lime
    'T': (0, 0, 0.5, 1),           # Navy
    'U': (0.5, 0, 0.5, 1),         # Purple
    'V': (0, 0.5, 0.5, 1),         # Teal
    'W': (0.5, 0.5, 0, 1),         # Olive
    'X': (0.5, 0.5, 0.5, 1),       # Silver
    'Y': (1, 0.5, 0, 1),           # Orange
    'Z': (0, 0.5, 0.5, 1),         # Teal

    # Numeric Characters (0-9)
    '1': (0, 0.6, 0, 1),   # Light Green
    '2': (0, 0.6, 0.6, 1),   # Light Cyan
    '3': (0, 0, 0.6, 1),   # Dark Blue
    '4': (0.6, 0, 0.6, 1),   # Dark Purple
    '5': (0.6, 0.6, 0, 1),   # Dark Yellow
    '6': (0, 0, 0, 1),   # Black
    '7': (1, 1, 1, 1),   # White
    '8': (0.6, 0.6, 0.6, 1),   # Light Gray
    '9': (1, 0.6, 0, 1),   # Light Orange
    '0': (0.6, 0, 0, 1),   # Dark Red

    # Symbols and Punctuation
    '!': (1, 0.7, 0, 1),   # Orange
    ',': (1, 0.8, 0, 1),   # Light Orange
    '.': (1, 0.9, 0, 1),   # Very Light Orange
    '?': (1, 1, 0, 1),   # Yellow
    ':': (0, 0.6, 0.6, 1),   # Cyan
    ';': (0, 0.7, 0.7, 1),   # Light Cyan
    "'": (0, 0.8, 0.8, 1),   # Very Light Cyan
    '"': (0, 0.9, 0.9, 1),   # Extremely Light Cyan
    '-': (0, 1, 1, 1),   # Cyan
    '+': (0.6, 0, 0.6, 1),   # Purple
    '*': (0.6, 0.6, 0, 1),   # Olive
    '/': (0, 0.6, 0.6, 1),   # Teal
    '=': (0.6, 0, 0.6, 1),   # Purple
    '<': (0.6, 0.6, 0, 1),   # Olive
    '>': (0, 0.6, 0, 1),   # Green
    '$': (0, 0.7, 0.7, 1),   # Light Cyan
    '€': (0, 0.8, 0.8, 1),   # Very Light Cyan
    '£': (0, 0.9, 0.9, 1),   # Extremely Light Cyan
    '¥': (0, 1, 1, 1),   # Cyan
    '@': (0.6, 0, 0.6, 1),   # Purple
    '#': (0.6, 0.6, 0, 1),   # Olive
    '%': (0, 0.6, 0.6, 1),   # Teal
    '&': (0.6, 0, 0.6, 1),   # Purple
    '^': (0, 0.6, 0.6, 1),   # Teal
    '(': (0.6, 0, 0, 1),   # Dark Red
    ')': (0.6, 0.6, 0.6, 1),   # Silver
    '[': (0, 0.6, 0, 1),   # Green
    ']': (0, 0.6, 0.6, 1),   # Teal
    '{': (0, 0.6, 0, 1),   # Green
    '}': (0, 0.6, 0.6, 1),   # Teal
    '|': (0, 0.6, 0, 1),   # Green
    '`': (0, 0.6, 0.6, 1),   # Teal
    '~': (0, 0.6, 0, 1),   # Green

     # Whitespace Characters
    'space': (0.5, 0.5, 0.5, 1),   # Gray
    'tab': (0.8, 0.8, 0.8, 1),     # Light Gray
    'newline': (0.7, 0.7, 0.7, 1),  # Gray

    # Special Characters
    '\n': (0.7, 0, 0, 1),
    '\t': (0.7, 0, 0, 1), 
    '\r': (0.7, 0, 0, 1),    # Dark Red
}

def iterate_through_characters(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            
            for char in text:
                print(char)
    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")

# Example usage:
filename = "example.txt"
iterate_through_characters(filename)

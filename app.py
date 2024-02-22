from PIL import Image
import cv2
import os
import numpy as np

# Dictionary containing color codes for each character
character_colors = {
    'a': (0, 0, 255, 255),           # Blue
    'b': (0, 0, 0, 255),             # Black
    'c': (51, 51, 51, 255),          # Dark gray
    'd': (102, 102, 102, 255),       # Gray
    'e': (153, 153, 153, 255),       # Light gray
    'f': (204, 204, 204, 255),       # Very light gray
    'g': (255, 0, 0, 127),           # Semi-transparent red
    'h': (0, 255, 0, 127),           # Semi-transparent green
    'i': (0, 0, 255, 127),           # Semi-transparent blue
    'j': (255, 0, 255, 127),         # Semi-transparent magenta
    'k': (0, 255, 255, 127),         # Semi-transparent cyan
    'l': (255, 255, 0, 127),         # Semi-transparent yellow
    'm': (127, 0, 127, 127),         # Semi-transparent purple
    'n': (127, 127, 0, 127),         # Semi-transparent olive
    'o': (0, 127, 127, 127),         # Semi-transparent teal
    'p': (127, 0, 0, 127),           # Semi-transparent maroon
    'q': (127, 127, 127, 127),       # Semi-transparent silver
    'r': (0, 0, 127, 127),           # Semi-transparent navy
    's': (0, 127, 0, 127),           # Semi-transparent green
    't': (127, 0, 0, 127),           # Semi-transparent olive
    'u': (127, 0, 127, 127),         # Semi-transparent purple
    'v': (0, 127, 127, 127),         # Semi-transparent teal
    'w': (127, 127, 0, 127),         # Semi-transparent olive
    'x': (127, 127, 127, 127),       # Semi-transparent silver
    'y': (127, 127, 0, 127),         # Semi-transparent olive
    'z': (0, 127, 0, 127),           # Semi-transparent green
    'A': (255, 0, 0, 255),           # Red
    'B': (0, 255, 0, 255),           # Green
    'C': (0, 0, 255, 255),           # Blue
    'D': (255, 0, 255, 255),         # Magenta
    'E': (0, 255, 255, 255),         # Cyan
    'F': (255, 255, 0, 255),         # Yellow
    'G': (127, 0, 127, 255),         # Purple
    'H': (127, 127, 0, 255),         # Olive
    'I': (0, 127, 127, 255),         # Teal
    'J': (127, 0, 0, 255),           # Maroon
    'K': (127, 127, 127, 255),       # Silver
    'L': (0, 0, 127, 255),           # Navy
    'M': (0, 127, 0, 255),           # Lime
    'N': (0, 0, 0, 255),             # Black
    'O': (255, 255, 255, 255),       # White
    'P': (127, 127, 127, 255),       # Gray
    'Q': (255, 127, 0, 255),         # Orange
    'R': (127, 0, 0, 255),           # Maroon
    'S': (0, 127, 0, 255),           # Lime
    'T': (0, 0, 127, 255),           # Navy
    'U': (127, 0, 127, 255),         # Purple
    'V': (0, 127, 127, 255),         # Teal
    'W': (127, 127, 0, 255),         # Olive
    'X': (127, 127, 127, 255),       # Silver
    'Y': (255, 127, 0, 255),         # Orange
    'Z': (0, 127, 127, 255),         # Teal
}

reverse_character_colors = {
    (0, 0, 255): 'a', 
    (0, 0, 0): 'b', 
    (51, 51, 51): 'c', 
    (102, 102, 102): 'd', 
    (153, 153, 153): 'e', 
    (204, 204, 204): 'f', 
    (255, 0, 0, 127): 'g', 
    (0, 255, 0, 127): 'h', 
    (0, 0, 255, 127): 'i', 
    (255, 0, 255, 127): 'j', 
    (0, 255, 255, 127): 'k', 
    (255, 255, 0, 127): 'l', 
    (127, 0, 127, 127): 'm', 
                            (127, 127, 0, 127): 'n', 
                            (0, 127, 127, 127): 'o', 
                            (127, 0, 0, 127): 'p', 
                            (127, 127, 127, 127): 'q', 
                            (0, 0, 127, 127): 'r', 
                            (0, 127, 0, 127): 's', 
                            (127, 0, 0, 127): 't', 
                            (127, 0, 127, 127): 'u', 
                            (0, 127, 127, 127): 'v', 
                            (127, 127, 0, 127): 'w', 
                            (127, 127, 127, 127): 'x', 
                            (127, 127, 0, 127): 'y', 
                            (0, 127, 0, 127): 'z', 
                            (255, 0, 0): 'A', 
                            (0, 255, 0): 'B', 
                            (0, 0, 255): 'C', 
                            (255, 0, 255): 'D', 
                            (0, 255, 255): 'E', 
                            (255, 255, 0): 'F', 
                            (127, 0, 127): 'G', 
                            (127, 127, 0): 'H', 
                            (0, 127, 127): 'I', 
                            (127, 0, 0): 'J', 
                            (127, 127, 127): 'K', 
                            (0, 0, 127): 'L', 
                            (0, 127, 0): 'M', 
                            (0, 0, 0): 'N', 
                            (255, 255, 255): 'O', 
                            (127, 127, 127): 'P', 
                            (255, 127, 0): 'Q', 
                            (127, 0, 0): 'R', 
                            (0, 127, 0): 'S', 
                            (0, 0, 127): 'T', 
                            (127, 0, 127): 'U', 
                            (0, 127, 127): 'V', 
                            (127, 127, 0): 'W', 
                            (127, 127, 127): 'X', 
    (255, 127, 0): 'Y', 
    (0, 127, 127): 'Z'
}

def generate_character_video(filename, video_name='output_video.mp4', fps=120):
    try:
        with open(filename, 'r') as file:
            text = file.read()

            images = []

            for char in text:
                color_code = character_colors.get(char, (255, 255, 255, 255))
                image = Image.new("RGBA", (50, 50), color_code)
                images.append(np.array(image))

            height, width, _ = images[0].shape
            height, width = width, height

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_writer = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

            for img in images:
                bgr_img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
                video_writer.write(bgr_img)

            video_writer.release()

    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")

def convert_video_to_text(video_name, output_text_file):
    try:
        video = cv2.VideoCapture(video_name)

        text = ""

        while True:
            ret, frame = video.read()
            if not ret:
                break

            avg_bgr_color = np.mean(frame, axis=(0, 1))

            min_distance = float('inf')
            closest_color_char = ''
            for color, char in reverse_character_colors.items():
                distance = np.linalg.norm(np.array(color) - avg_bgr_color)
                if distance < min_distance:
                    min_distance = distance
                    closest_color_char = char
                    print(char)


            text += closest_color_char

        video.release()

        with open(output_text_file, 'w') as file:
            file.write(text)

    except Exception as e:
        print("An error occurred:", str(e))




# Example usage:
video_name = 'output_video.mp4'
output_text_file = 'output_text.txt'
convert_video_to_text(video_name, output_text_file)


# Example usage:
# filename = "example.txt"
# video_name = "output_video.mp4"
# generate_character_video(filename, video_name)

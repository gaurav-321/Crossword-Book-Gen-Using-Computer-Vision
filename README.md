# Crossword Book Gen Using Computer Vision
This is a Flask server that generates crossword puzzle books based on input. It uses cv2 for image processing and random for generating random file names for uploaded files.

## Features
- User can upload a CSV file containing the crossword puzzle clues and solutions
- User can select a font for the crossword puzzle book
- User can specify whether the header should be bold or not
- User can specify the size of the header
- User can specify the color of the header
- User can enable pagination for the crossword puzzle book
- User can specify the size of the words in the crossword puzzle
- User can specify whether the words in the crossword puzzle should be bold or not
- User can upload multiple images to be used as the background for the crossword puzzle book
## Requirements
- Python 3
- Flask
- cv2
- random
## Usage
To run the server, use the command python app.py. Then, go to http://localhost:80 in your web browser to access the crossword puzzle generator. Follow the prompts on the webpage to generate the crossword puzzle book.

## File Structure
Copy code
.
- ├── app.py
- ├── main.py
- ├── static
 -│   ├── back
 - │   ├── files
 - │   ├── fonts 
 - │   ├── output
 - │   ├── templates

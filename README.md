# Crossword Book Generator

Crossword Book Generator is a Python program that leverages Flask, OpenCV (cv2), and random to create custom crossword puzzle books. It provides an interactive web interface for users to upload CSV files and media, process the data, and generate output in PDF format.

## Features

- **Flask Web Interface**: Provides a user-friendly interface for uploading CSV files and media.
- **Image Processing**: Utilizes OpenCV to handle background selection and font styling.
- **CSV Parsing**: Extracts crossword clues and solutions from uploaded CSV files.
- **Dynamic PDF Generation**: Generates custom crossword puzzle books in PDF format based on user input.

## Installation

To install the dependencies, run:

```bash
pip install Flask cv2 random
```

## Usage

### Running the Application

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the application using:

```bash
python app.py
```

4. Open your web browser and go to `http://127.0.0.1:5000/` to access the interface.

### Uploading Files

- **CSV File**: Upload a CSV file containing crossword clues and solutions.
- **Media File**: Upload media files (images, fonts) for background selection and styling.

### Generating Output

After uploading the necessary files, click on the "Generate" button. The program will process the data and generate an output PDF file named `output.pdf`.

## Configuration

No additional configuration is required beyond installing dependencies and running the application.

## Tests

This project does not include automated tests at this time.

## Project Structure

```
CrosswordBookGenerator/
├── app.py
├── main.py
├── CrosswordBookGenerator/
│   ├── __init__.py
│   ├── CrosswordBookGenerator.py
│   ├── ImageProcessor.py
│   ├── CSVParser.py
│   └── HTMLTemplates.py
├── templates/
│   └── index.html
└── static/
    └── styles.css
```

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

1. Fork the project on GitHub.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this README to better fit your specific needs or add more sections as required!
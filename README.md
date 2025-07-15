# Nirnay: Career Advisor for Engineering Students

Nirnay is a machine learning–powered application that provides personalized career advice for engineering and technology students. Based on a student's academic profile, skills, goals, and financial background, the tool offers suggestions tailored to help them make more informed decisions about their professional future.

This application uses a fine-tuned, quantized language model and is deployed using Gradio for a simple and accessible user interface.

## Features

- Personalized career recommendations based on:
  - Academic degree and discipline
  - CGPA and work experience
  - Technical skills and interest areas
  - Financial constraints and long-term goals
- Built with a lightweight, quantized large language model
- Accessible via a browser interface using Gradio
- Easily customizable and extendable for additional use cases

## Project Structure
```
Nirnay/
├── app.py                 # Gradio app interface
├── utils.py               # Model loading and prompt generation
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
├── .gitignore             # Files/folders to ignore in version control
├── data/
│   ├── career_data.csv
│   ├── cleaned_data.csv
│   └── fine_tune_data.jsonl
├── notebooks/
│   ├── cleaning.ipynb
│   └── modeling.ipynb
├── quantized_model/       # (excluded from Git) contains model weights
├── assets/                # Screenshots and supporting images 
└── README.md              # Project description and setup guide
```


## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/Nirnay.git
cd Nirnay
pip install -r requirements.txt


### Running the App

Start the Gradio interface:


Then open your browser and go to `http://localhost:7860`.

## Model Details

The quantized model used for inference is excluded from version control (via `.gitignore`). To use the application:

- Place the quantized model files inside a folder named `quantized_model/`
- Or modify the `load_model()` function in `utils.py` to point to your model path or loading logic

## Screenshots

Screenshots demonstrating the interface and sample outputs are in the `assets/` folder.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

Nirnay was developed to support engineering students in making informed career decisions using modern language models and open-source tools such as Gradio and Hugging Face Transformers.

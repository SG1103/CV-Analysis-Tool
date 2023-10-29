# CV Analysis Tool

An automated tool designed to analyze CVs (resumes) and identify the best-fit candidate for a specific role using the power of OpenAI.

## Description

The CV Analysis Tool offers a streamlined way of assessing multiple CVs to determine which candidate is the most suitable for a particular position. By leveraging OpenAI's GPT models, this tool provides both a score for each CV and reasoning for the top pick, making the hiring process more efficient.

## Installation

1. Clone the repository.
2. Ensure you have the required libraries installed (`PyPDF2`, `openai`, `easygui`).
3. Set up the OpenAI API key in the `Hub` module (as referenced in the script).

## Usage

1. Place the CVs you want to analyze in the `CVs/` directory in PDF format.
2. Run the `main.py` script.
3. When prompted, input the desired role you're hiring for.
4. The tool will evaluate the CVs and present you with the best-fit candidate, their score, and the reasoning behind the choice.

## Note

Ensure that the OpenAI API key is correctly set up in the `Hub` module for the tool to function properly. The API key is used to communicate with OpenAI's GPT models for CV analysis.

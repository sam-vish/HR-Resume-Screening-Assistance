# HR Resume Screening Assistance

This application assists HR professionals in screening resumes efficiently using NLP, OpenAI and vector databases.

[Video Introduction](https://drive.google.com/file/d/VIDEO_ID_HERE/view?usp=sharing)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Overview

The HR Resume Screening Assistance application leverages Streamlit, OpenAI, Pinecone, and other libraries to streamline the process of analyzing resumes against job descriptions. It uses NLP models to extract relevant information and vector databases for efficient similarity searches.

## Features

- **Job Description Input:** Allows users to input job descriptions.
- **Resume Upload:** Enables users to upload multiple resumes in PDF format.
- **Automated Analysis:** Performs automated analysis of resumes based on job descriptions.
- **Summarization:** Provides summaries of relevant resumes.
- **Customizable:** Users can set the number of resumes to return in the analysis.

## Setup

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up environment variables by creating an `.env` file based on `env.example`.
4. Run the `app.py` file using Python.

## Usage

1. Run the application using `streamlit run app.py`.
2. Input the job description and the number of resumes to return.
3. Upload resumes in PDF format.
4. Click the "Help me with the analysis" button to initiate the analysis process.
5. View the results including relevant documents and their summaries.

## File Structure

- `app.py`: Main application file with the Streamlit interface.
- `utils.py`: Utility functions for handling PDFs, embeddings, Pinecone, and summarization.
- `env.example`: Example environment variable configuration file.
- `requirements.txt`: List of required Python packages.

## Dependencies

- `langchain`
- `streamlit`
- `openai`
- `python-dotenv`
- `pinecone-client`
- `pypdf`
- `sentence-transformers`

## Contributing

Contributions are welcome! Fork the repository, make your changes, and create a pull request. Ensure adherence to the code of conduct.

## License

This project is licensed under the [MIT License](LICENSE).

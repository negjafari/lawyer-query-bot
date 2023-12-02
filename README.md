# lawyer-query-bot
A lawyer chatbot using ChatGPT and BERT for answering Persian legal questions.

## Overview

Lawyer Query Bot is a project that implements a lawyer chatbot for answering Persian legal questions. The chatbot utilizes the powerful ChatGPT language model along with BERT for similarity checking between query and and questions in dataset.

## Features

- **ChatGPT Integration:** uses ChatGPT for generating responses to queries.
- **BERT for Similarity:** Employs BERT as a cross Encoder to check similarity in questions.
- **Model Used:** Utilizes the 'pedramyazdipoor/persian_xlm_roberta_large' model from Hugging Face.
- **Data Preprocessing:** Concatenates and preprocesses datasets, including data reduction, text cleaning, and stop word removal.
- **Top Similar Answers:** Returns the top 10 most similar answers based on user questions.

## Datasets

Datasets are available in the `dataset/` directory.

## Usage

1. Concatenate all datasets and create a unified dataset.
2. Apply data preprocessing, including data reduction, text cleaning, and stop word removal.
3. Utilize the 'pedramyazdipoor/persian_xlm_roberta_large' model for similarity checking.
4. Ask ChatGPT a valid question using the specified format in the documentation.

### Asking ChatGPT

```plaintext
Pre_message: "Please use the following top answers to assist in answering the question. If no relevant answer is found, output the phrase: 'No relevant answer found.'"

User_question: [User's actual question goes here]

Top 10 relevant answers extracted from dataset


## Google Colab

This project is implemented in Google Colab
Open the notebook in Google Colab by clicking on the following link: https://colab.research.google.com/drive/1vjlAnCui98oYATfag56QpaeoJQ5XEtYS

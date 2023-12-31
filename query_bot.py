# -*- coding: utf-8 -*-
"""query_bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vjlAnCui98oYATfag56QpaeoJQ5XEtYS

**preparing dataset**
"""

!gdown 1Mu8xm04jhgIBVGWrSmGZoBHoUwIfPUdt

!unzip vokala_data.zip -d 'sample_data/datasets/'

import pandas as pd
import glob

input_path = 'sample_data/datasets/'
output_path = 'sample_data/datasets/vokala_data.csv'

datasets = glob.glob(input_path + '*.csv')

data_frames = []

for dataset in datasets:
    data_frames.append(pd.read_csv(dataset))

merged = pd.concat(data_frames)

merged.to_csv(output_path, index=False)

df = pd.read_csv(output_path, encoding='utf-8') #(32889,6)

import matplotlib.pyplot as plt


missing_values = df.isnull().sum()
fig, ax = plt.subplots(figsize=(15, 6))
missing_values.plot.bar(ax=ax)

for i, val in enumerate(missing_values):
    ax.text(i, val + 10, str(val), ha='center', fontweight='bold')

plt.show()

"""**Import essential libraries**"""

import pandas as pd
import glob
import json
import numpy as np
import openai

"""**Preprocessing**"""

columns = ['_id', 'link','category', 'title']
df = df.drop(columns, axis=1)

df['answers'] = df['answers'].str.replace("'", '\"')

merged_texts = []
for x in df['answers']:
    try:
        texts = [entry['text'] for entry in json.loads(x)]
        merged_texts.append('\n'.join(texts))
    except Exception as e:
        merged_texts.append(x)

df['cleaned_answers'] = merged_texts

df = df.drop('answers', axis=1)

"""**Embedding**"""

!pip install sentence-transformers

from sentence_transformers import CrossEncoder

model1 = CrossEncoder('cross-encoder/stsb-roberta-base')

model2 = CrossEncoder('pedramyazdipoor/persian_xlm_roberta_large')

question = 'بعد از فوت یکی از والدین اموال چگونه تقسیم می شود؟'

sentence_pairs = []
for sentence1, sentence2 in zip(question, df['question']):
    sentence_pairs.append([sentence1, sentence2])

df['q-similatiry'] = model2.predict(sentence_pairs, show_progress_bar=True)

sorted_df = df.sort_values(by='q-similatiry', ascending=False)

top_10_questions = sorted_df.head(10)['question']
top_10_answers = sorted_df.head(10)['cleaned_answers']

"""**Ask ChatGPT**"""

API_KEY = 'REPLACE IT WITH YOUR OWN API KEY'
MODEL = 'gpt-3.5-turbo'

question = 'بعد از فوت یکی از والدین اموال چگونه تقسیم می شود؟'

answers_to_string = top_10_answers.to_string(index=False)

pre_message = "Use the content below to answer the following question and if you don't find a relevant answer, reply : پاسخ مرتبطی پیدا نشد!."
user_question = f"\nQuestion : {question}"
relevant_answers = f"\ncontent : {answers_to_string}"

query = pre_message + user_question + relevant_answers

def ask_question(question):
    openai.api_key = API_KEY

    messages = [
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['message']['content']
    else:
        print('Error:', response)
        return None

response = ask_question(query)
print(response)
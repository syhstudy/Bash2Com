import openai
import pandas as pd
from tqdm import tqdm
import random
import time
import math

random.seed(1234)
openai.api_base = 'xxxx'
openai.api_key = 'sk-xxxxx'

def comment(code):
    prompt = '#example code 1: find Path -name Regex -print' \
             '\n#example summarization 1: find all file and directori name _REGEX in entir filesystem' \
             '\n#a bash code:' + code + \
             '\n#Generated summarization(The length should not exceed 15 words):\n'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "To generate a short summarization in one sentence for bash code.To alleviate the difficulty of this task, I will give you one examples.Please learn from them."},
            {"role": "user", "content": prompt},
        ],
        temperature=0
    )
    return response['choices'][0]['message']['content']


if __name__ == '__main__':
    df = pd.read_csv('yiheng/test-1.csv',encoding='ISO-8859-1')
    source_codes = df['code'].tolist()

    num_batches = math.ceil(len(source_codes) / 100)
    for batch_index in range(num_batches):
        start_index = batch_index * 100
        end_index = min(start_index + 100, len(source_codes))

        source_batch = source_codes[start_index:end_index]

        python_codes = []
        for i in tqdm(range(len(source_batch))):
            python_codes.append(
                comment(source_batch[i]))
            time.sleep(1)

        df = pd.DataFrame(python_codes)
        if batch_index == 0:
            df.to_csv('yiheng/sml-one1.csv', index=False, header=None, line_terminator='\n')
        else:
            with open('yiheng/sml-one1.csv', 'a') as f:
                df.to_csv(f, index=False, header=None, line_terminator='\n')
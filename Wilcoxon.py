from scipy.stats import wilcoxon
from nlgeval import compute_individual_metrics
import pandas as pd
import numpy as np

hyp = pd.read_csv('./result/test_hyp.csv')
ref = pd.read_csv('./result/test_ref.csv')

hyp_data = np.array(hyp)
hyp_list=hyp_data.tolist()
ref_data = np.array(ref)
ref_list=ref_data.tolist()

data1_bleu1 = []
data1_bleu2 = []
data1_bleu3 = []
data1_bleu4 = []
data1_meteor = []
data1_rougel = []

for i in range(len(hyp)):
    metrics_dict = compute_individual_metrics(ref_list[i][0], hyp_list[i][0], no_skipthoughts=True, no_glove=True)
    data1_bleu1.append(metrics_dict['Bleu_1'])
    data1_bleu2.append(metrics_dict['Bleu_2'])
    data1_bleu3.append(metrics_dict['Bleu_3'])
    data1_bleu4.append(metrics_dict['Bleu_4'])
    data1_meteor.append(metrics_dict['METEOR'])
    data1_rougel.append(metrics_dict['ROUGE_L'])
    # print(data1_bleu1)

hyp = pd.read_csv('./result/test_hyp1.csv')
ref = pd.read_csv('./result/test_ref1.csv')

hyp_data = np.array(hyp)
hyp_list=hyp_data.tolist()
ref_data = np.array(ref)
ref_list=ref_data.tolist()

data2_bleu1 = []
data2_bleu2 = []
data2_bleu3 = []
data2_bleu4 = []
data2_meteor = []
data2_rougel = []

for i in range(len(hyp)):
    metrics_dict = compute_individual_metrics(ref_list[i][0], hyp_list[i][0], no_skipthoughts=True, no_glove=True)
    data2_bleu1.append(metrics_dict['Bleu_1'])
    data2_bleu2.append(metrics_dict['Bleu_2'])
    data2_bleu3.append(metrics_dict['Bleu_3'])
    data2_bleu4.append(metrics_dict['Bleu_4'])
    data2_meteor.append(metrics_dict['METEOR'])
    data2_rougel.append(metrics_dict['ROUGE_L'])
    # print(data1_bleu1)


stat, p = wilcoxon(data1_bleu1, data2_bleu1)
print('BLEU-1:')
print(p)
print('-----------------------')

stat, p = wilcoxon(data1_bleu2, data2_bleu2)
print('BLEU-2:')
print(p)
print('-----------------------')

stat, p = wilcoxon(data1_bleu3, data2_bleu3)
print('BLEU-3:')
print(p)
print('-----------------------')

stat, p = wilcoxon(data1_bleu4, data2_bleu4)
print('BLEU-4:')
print(p)
print('-----------------------')

stat, p = wilcoxon(data1_meteor, data2_meteor)
print('METEOR:')
print(p)
print('-----------------------')

stat, p = wilcoxon(data1_rougel, data2_rougel)
print('ROUGE-L:')
print(p)

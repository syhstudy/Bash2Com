I. Comparison results
==========================================
We randomly split our datasets three times with different random seeds. The detailed comparison result are shown as follows and the comparison results confirm the effectiveness of our proposed method.

Comparison result with the first data split(recorded in the paper):
![image](https://user-images.githubusercontent.com/93321396/218019291-af236217-215a-46a1-ae34-73484908ab64.png)

Comparison result with the second data split:
![image](https://user-images.githubusercontent.com/93321396/218021307-e30927dd-b223-4ad5-8ece-ad8ef7be26d6.png)

Comparison result with the third data split:
![image](https://user-images.githubusercontent.com/93321396/218024395-dbc4d5be-4138-4e67-9800-b4f405064a98.png)

II. L1 regularization in data augmentation
==========================================
Carl-Johann et al. established the connection between adversarial training and regularization, more details can be found in the catalogue "Theory.pdf".

The experimental results in this paper can verify the feasibility of NP-GD:
<img src="https://user-images.githubusercontent.com/93321396/218145656-62b81025-63a9-4641-b336-98f08c9cb397.png" width = "700" />

where 'with PGD' is $L2$ regularization, 'Bash2Com' is $L1$ and $L2$ regularization.

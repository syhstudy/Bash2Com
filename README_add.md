I. Comparison results
==========================================
We randomly split our datasets three times with different random seeds. The detailed comparison result are shown as follows and the comparison results confirm the effectiveness of our proposed method.

Comparison result with the first data split(recorded in the paper):
![image](https://user-images.githubusercontent.com/93321396/221564727-e27048ff-06aa-469f-9b7f-69176a5aa386.png)

Comparison result with the second data split:
![image](https://user-images.githubusercontent.com/93321396/221564639-b9468492-dff1-42f0-a03a-a54d0dc56554.png)

Comparison result with the third data split:
![image](https://user-images.githubusercontent.com/93321396/221564805-e89a1569-39ea-4835-a501-3f6e71ee293e.png)

II. L1 regularization in data augmentation
==========================================
Carl-Johann et al. established the connection between adversarial training and regularization, more details can be found in the catalogue "Theory.pdf".

The experimental results in this paper can verify the feasibility of NP-GD:
<img src="https://user-images.githubusercontent.com/93321396/218145656-62b81025-63a9-4641-b336-98f08c9cb397.png" width = "700" />

where 'with PGD' is $L2$ regularization, 'Bash2Com' is $L1$ and $L2$ regularization.

Comparison results (cross-validation)
==========================================
We randomly split our datasets three times with different random seeds. The detailed comparison result are shown as follows and the comparison results confirm the effectiveness of our proposed method.

Comparison result with the first data split(recorded in the paper):
![image](https://user-images.githubusercontent.com/93321396/218019291-af236217-215a-46a1-ae34-73484908ab64.png)

Comparison result with the second data split:
![image](https://user-images.githubusercontent.com/93321396/218021307-e30927dd-b223-4ad5-8ece-ad8ef7be26d6.png)

Comparison result with the third data split:
![image](https://user-images.githubusercontent.com/93321396/218024395-dbc4d5be-4138-4e67-9800-b4f405064a98.png)

Regularization in data augmentation
==========================================
The actual updated loss function of NP-GD can be expressed as follows (Aleksander Madry et al.[<sup>1</sup>](#refer-id) proposed that PGD confrontation training does not use normal samples, but TRADES and others pointed out that using normal samples can increase the accuracy of the model. Here adopts the loss function of adding normal samples):
$$\\tilde{L} (x,y):=\\frac{1}{2} (L(x,y)+L(x+\\delta ,y))$$


References
==========================================
<div id="refer-id"></div>
[1] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, “Towards deep learning models resistant to adversarial attacks,” 6th International Conference on Learning Representations, ICLR 2018 - Conference Track Proceedings, 2018.

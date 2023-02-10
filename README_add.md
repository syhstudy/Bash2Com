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
The actual updated loss function of adversarial training can be expressed as follows (Aleksander Madry et al.[<sup>1</sup>](#refer-id) proposed that PGD method does not use normal example, but TRADES et al.[<sup>2</sup>](#refer-id) pointed out that using normal example can increase the accuracy of the model. Here adopts the loss function of adding normal example):
$$\\tilde{L} (x,y):=\\frac{1}{2} (L(x,y)+L(x+\\delta ,y))$$

where $L(x,y)$ represents the loss function of the training process. $\delta$ represents the perturbation superimposed on the input. $y$ is the label of the example.
If the perturbation is relatively small (most of the perturbations used in adversarial training are relatively small at present), the first-order Taylor expansion[<sup>3</sup>](#refer-id) can be used to approximate it:
$$\\tilde{L} (x,y)\\approx \\frac{1}{2} (L(x,y)+L(x,y)+\\delta \\cdot \\partial _{x}L(x,y))=L(x,y)+\\frac{1}{2} \\delta \\cdot \\partial _{x}L(x,y)$$

where the second term is the change of loss function caused by perturbation:
$$\\delta \\cdot \\partial _{x}L(x,y)=\\underset{\\delta :\\left \\| \\delta  \\right \\| _{p}\\le \\epsilon }{max} \\left | L(x+\\delta ,y)-L(x,y) \\right | \\approx \\underset{\\delta :\\left \\| \\delta  \\right \\| _{p}\\le \\epsilon }{max}\\left | \\partial _{x}L\\cdot \\delta   \\right | =\\epsilon \\left \\| \\partial _{x}L \\right \\| _{q}$$

where $\left \| \cdot  \right \| _{q}$ is the dual norm of $\left \| \cdot  \right \| _{p}$ , defined as:
$$\\left \\| \\mathbf{z}   \\right \\| _{q}=sup \\{\\mathbf{z}^{\\top } \\mathbf{x}\\mid \\left \\| \\mathbf{x}   \\right \\| _{p}\\le 1\\}$$

when $p=1$ is $q=\infty $, there is usually $\\frac{1}{p}+ \\frac{1}{q}= 1$.
Substitute the result in Formula 3 into Formula 2:
$$\\tilde{L}(x,y) \\approx L(x,y)+\\frac{\\epsilon }{2} \\left \\| \\partial _{x}L  \\right \\| _{q}$$

Adversarial training becomes adding a special regularization term to the loss function, which is also proved by the method of enhancing the robustness of the model based on local linear regularization (Local Linear Regularization[<sup>1</sup>](#refer-id), Curvature Regularization[<sup>1</sup>](#refer-id)).

References
==========================================
<div id="refer-id"></div>
[1] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, “Towards deep learning models resistant to adversarial attacks,” 6th International Conference on Learning Representations, ICLR 2018 - Conference Track Proceedings, 2018.

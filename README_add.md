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
The actual updated loss function of NP-GD can be expressed as follows (Aleksander Madry and others proposed that PGD confrontation training does not use normal samples, but TRADES and others pointed out that using normal samples can increase the accuracy of the model. Here adopts the loss function of adding normal samples):
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow><mover><mi>L</mi><mo stretchy="false">~</mo></mover></mrow><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo stretchy="false">)</mo><mo>:=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mo stretchy="false">(</mo><mi>L</mi><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo stretchy="false">)</mo><mo>+</mo><mi>L</mi><mo stretchy="false">(</mo><mi>x</mi><mo>+</mo><mi>δ</mi><mo>,</mo><mi>y</mi><mo stretchy="false">)</mo><mo stretchy="false">)</mo></math>

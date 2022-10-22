# CSE4185 Assignment04: Neural Network with Pytorch

## 0. Implements
Deep Learning Framework인 pytorch를 활용해 간단한 Neural Network 구현

## 1. Requirements
jupyter notebook or colab, pytorch 1.6+

## 2. Problems
   - DataSet: CIFAR 10
   1. Implement Flatten Function (Flatten Layer)
   <img width="326" alt="1" src="https://user-images.githubusercontent.com/91405382/197314763-eae3c27b-cbed-479c-9c3f-7b3da99dd1fa.png">

   2. Implement Multi-Layer Perception(MLP)

   3. INPUT(32X32X3) -> CONV1(30X30X12) -> CONV2(28X28X12) -> POOL1(14X14X12) -> CONV3(12X12X24) -> CONV4(10X10X24) -> POOL2(5X5X24) -> FC -> ... -> FC (class num)를 따르는 CNN Model을 구현 

## Result

### Activation Function = Sigmoid
<img width="165" alt="Sigmoid" src="https://user-images.githubusercontent.com/91405382/197314854-ccd43291-b00e-49c5-8cb8-2a7bd5eb26e0.png">

### Activation Function = TanH
<img width="182" alt="TanH" src="https://user-images.githubusercontent.com/91405382/197314867-ab6df04b-8eb4-42eb-abe7-879d846853e3.png">

### Activation Function = ReLu
<img width="165" alt="ReLu" src="https://user-images.githubusercontent.com/91405382/197314889-d2fae651-36bc-413d-83a0-95dbbee900ae.png">

### Activation Function = LeakyReLu
<img width="165" alt="LeakyReLu" src="https://user-images.githubusercontent.com/91405382/197314917-f44ccda4-9398-4bbc-8efd-fcf7d3f03474.png">
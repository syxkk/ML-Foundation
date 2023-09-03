# ML-Foundation
机器学习基础

# - classifation
# - regression
# Training
## Function with unknow
Function_aim = comstant + hard sigmoid  
- $y=b+wx$  
$y=c\frac{1}{1+e^{-(w+b{x_1})}}=cSigmoid(b+w{x_1})$  
更改w--> 坡度 更改 b-->更改转折点，即坡度左右距离  更改c-->更改高度  
得到不同的$pieceswise function$ $$y=b+\sum_{i}{c_i}Sigmoid({b_i}+{w_i}{x_1})$$

  [为啥是一堆sigmoid相加呢Link](https://www.bilibili.com/video/BV1Q5411u7n9?vd_source=768ef0b6c1470b68659147dbd2450358)

- $y=b+\sum_{j}{w_j}{x_j}$  
  $\mbox{就用}\ y=b+\sum_{i}{c_i}sigmoid(b_i+\sum_{j}{w_{ij}}{x_j})$
  
  $i=1,2,3 j=1,2,3$  
  |$r_1$|  |$b_1$|
  |---|     |---|
  |$r_2$|$=$ |$b_2$|
  |$r_3$|  |$b_3$|
## Loss
${y_i}\mbox{ 表示真实值},\hat{y_i}\mbox{ 表示预测值}$  
${e_i}=\left|{y_i}-\hat{y_i}\right|\ L \mbox{ 是 mean absolute erro(MAE)}$

${e_i}=({y_i}-\hat{y_i})^2\ L \mbox{\ 是 mean square erro(MSE)}$

$$Loss: L=\frac{1}{N}\left|\sum_{i=1}^{n} e_i\right|$$
## Optimization
梯度下降  考虑一个parameter w
${w_0}\ \mbox{是随机的, }\eta\mbox{ 是learning rate, }{w_1}={w_0}-\eta\frac{\partial{L}}{\partial{W}}$  
$\mbox{当 }{\frac{\partial{L}}{\partial{w_0}}=0 \mbox{时，w不再更新，导致了local min 而不是 global min}}$  
考虑两个parameter  
${w_1}={w_0}-\eta\frac{\partial{L}}{\partial{w}}|_{w={w_0},b={b_0}}$  

${b_1}={b_0}-\eta\frac{\partial{L}}{\partial{w}}|_{w={w_0},b={b_0}}$  
updata b w inter

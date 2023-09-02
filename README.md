# ML-Foundation
机器学习基础

# - classifation
# - regression
# Training
## Function with unknow

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

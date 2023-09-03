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
得到不同的 $pieceswise function$  
$$y=b+\sum_{i}{c_i}Sigmoid({b_i}+{w_i}{x_1})$$

  [为啥是一堆sigmoid相加呢Link](https://www.bilibili.com/video/BV1Q5411u7n9?vd_source=768ef0b6c1470b68659147dbd2450358)

- $y=b+\sum_{j}{w_j}{x_j}$  
  $\mbox{就用}\ y=b+\sum_{i}{c_i}sigmoid(b_i+\sum_{j}{w_{ij}}{x_j})$
  
  $i=1,2,3\  j=1,2,3\  i\mbox{的个数是你decide  是个超参数越多 越能拟合越复杂piecewise function}$  
  $r=[r_1,r_2,r_3]^T$
  $b=[b_1,b_2,b_3]^T$  
  **w**
  |$w_{11}$|$w_{12}$|$w_{13}$|
  |-|-|-|
  |$w_{21}$|$w_{22}$|$w_{23}$|
  |$w_{31}$|$w_{32}$|$w_{33}$|
  
  $x=[x_1,x_2,x_3]^T$  
  ## **$$r=b+wx$$**
  $a_1=c_1sigmiod(r_1)$  
  $a=[a_1,a_2,a_3]^T$  
  $y=b+a_1+a_2+a_3$
  ### Relu
  $y=b+\sum_{2i}c_imax(0,b_i+\sum_{j}w_{ij}x_j)$
## Loss
${y_i}\mbox{ 表示真实值},\hat{y_i}\mbox{ 表示预测值}$  
${e_i}=\left|{y_i}-\hat{y_i}\right|\ L \mbox{ 是 mean absolute erro(MAE)}$

${e_i}=({y_i}-\hat{y_i})^2\ L \mbox{\ 是 mean square erro(MSE)}$

$$Loss: L=\frac{1}{N}\left|\sum_{i=1}^{n} e_i\right|$$
## Optimization
梯度下降  
- 考虑一个parameter w
${w_0}\ \mbox{是随机的, }\eta\mbox{ 是learning rate,是一个hyper peremeter }{w_1}={w_0}-\eta\frac{\partial{L}}{\partial{W}}$  
$\mbox{当 }{\frac{\partial{L}}{\partial{w_0}}=0 \mbox{时，w不再更新，导致了local min 而不是 global min}}$  
- 考虑两个parameter  
  ${w_1}={w_0}-\eta\frac{\partial{L}}{\partial{w}}|_{w={w_0},b={b_0}}$  

  ${b_1}={b_0}-\eta\frac{\partial{L}}{\partial{w}}|_{w={w_0},b={b_0}}$  
  updata b w inter
 - 考虑sigmoid拟合曲线  
    $\theta=flatten(all parameter)$
    **$\theta$**
    |$\theta_1$|
    |-|
    |$\theta_2$|
    |...|
    |$\theta_n$|
    
    $\mbox{random pick}\ \theta^0$  
    **$g\ \mbox{gradient} g=\nabla{L}({\theta^0}) $**  (这里github我还不知道为啥把梯度分量写进一个列向量里面就会报错 但是在stackedit里面就可以正常显示)  
    $\frac{\partial{L}}{\partial\theta_1}|_{\theta=\theta^0}$  

    $\frac{\partial{L}}{\partial\theta_2}|_{\theta=\theta^0}$  
    
    $\frac{\partial{L}}{\partial\theta_n}|_{\theta=\theta^0}$  
   $\theta^1=\theta^0-\eta{g}$
    (常用的更新参数方法 并不是把所有样本计算出总的Loss 而是一个batch)  
   |$L^1$|batch|
   |-|-|
   |$L^2$|batch|
   |$L^3$|batch|
   |...|...|
   
   randomly pick $\theta^0$  
   compute gradient $g^1=\nabla{L^1({\theta^0})}$  
   **update** $\theta^1=\theta^0-\eta{g^1}$  
   compute gradient $g^2=\nabla{L^2({\theta^1})}$  
   **update** $\theta^2=\theta^1-\eta{g^2}$   
    1 **epoch**=see all the batches once

### overfitting good at training,but worse at unseen data

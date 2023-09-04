## what is Pytorch ?
- An **machine learning framework** in Python.
- Two main features:
  - N-dimensional **Tensor** computation (like NumPy) on **GPUS**
  - **Automatic differentiation** for training deep neural networks
## How can I load my data into code ?
- dataset=MyDataset(file)
- dataloader=DataLoader(**dataset**,batch_size,shuffle=True)  (when Training: True,when Testing:False)
  ```Python
  from torch.utils.data import Dataset,DataLoader
  ## overwrite Dataset
  class MyDataset(Dataset):
	  def __init__(self,file):
		  self.data=...
	  ## read data
	  def __getitem__(self,index):
		  return self.data[index]
	  ## return one sample at a time
	  def __len__(self):
		  return len(self.data)
	  ##return the size of dataset
     ```
     ![Dataloader 的作用](/imgs/2023-09-04/n0Nl3mYoB7BqX4eG.png)
DataLoader 具体作用如上

## Tensors -Gradient Calculation
```Python
x=torch.tensor([[1.,0],[-1,1]],requires_grad=True)
z=x.pow(2).sum()
z=backward()
x.grad
##tensor([[2.,0],[-2,2]])
```
$x=\left[\begin{matrix} 
1&0\\
-1&1\\
\end{matrix}\right]\ z=\sum_{i}\sum_{j}{x_{ij}^2}$
$\frac{\partial{z}}{\partial{x_{ij}}}=2x_{ij}\ \frac{\partial{z}}{\partial{x}}=\left[\begin{matrix}
2&0\\
-2&2
\end{matrix}\right]$
## torch.nn
```Python
layer=torch.nn.Linear(32,64)
layer.weight.shape
## torch.Size([64,32])
layer.bias.shape
##torch.Size([64])
```
![Linear 说明](/imgs/2023-09-04/LLPI6Y3hw1MfhZkt.png)
## Loss Function
- Mean Squared Error (for regression tasks)
```Python
criterion=nn.MSELoss()
```
- Cross Entropy(for classification tasks)
```Python
criterion=nn.CrossEntropyLoss()
```

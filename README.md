# ds-ldl
《动手学深度学习》AI公益学习

## 环境安装过程遇到的问题
环境：
window10  
py3.7.4  

#### 问题1.由于之前配置tensorflow安装了cudn等等配件，直接无脑 pip install torch   
ModuleNotFoundError: No module named 'tools.nnwrap'  
原因：版本不匹配，直接pip无法正确安装  
解决方法：上官网匹配正确的版本，网址：https://download.pytorch.org/whl/torch_stable.html , 例如我自己就下载这个torch-1.1.0-cp37-cp37m-win_amd64.whl，接着pip安装这个就可以了。  

验证安装
`import torch`
`x = torch.rand(5, 3)`
`print(x)`
`torch.cuda.is_available()`

 
 
 
 
 
 



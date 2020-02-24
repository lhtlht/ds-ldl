# ds-ldl
《动手学深度学习》AI公益学习

## TASK OVERVIEW  

Task01：线性回归；Softmax与分类模型、多层感知机  
Task02：文本预处理；语言模型；循环神经网络基础  
Task03：过拟合、欠拟合及其解决方案；梯度消失、梯度爆炸；循环神经网络进阶（\*暂未理解）  
Task04：机器翻译及相关技术；注意力机制与Seq2seq模型；Transformer  
Task05：卷积神经网络基础；leNet；卷积神经网络进阶  
Task06：批量归一化和残差网络；凸优化；梯度下降  
Task07：优化算法进阶；word2vec；词嵌入进阶  
Task08：文本分类；数据增强；模型微调  
Task09：目标检测基础；图像风格迁移；图像分类案例1  
Task10：图像分类案例2；GAN；DCGAN  

## 环境安装过程遇到的问题
环境：  
window10  
py3.7.4  

#### 问题1.由于之前配置tensorflow安装了cudn等等配件，直接无脑 pip install torch   
ModuleNotFoundError: No module named 'tools.nnwrap'  
原因：版本不匹配，直接pip无法正确安装  
解决方法：上官网匹配正确的版本，网址：https://download.pytorch.org/whl/torch_stable.html , 例如我自己就下载这个torch-1.1.0-cp37-cp37m-win_amd64.whl，接着pip安装这个就可以了。  

验证安装 
```
import torch   
x = torch.rand(5, 3)  
print(x)  
torch.cuda.is_available()  
```

 #### 问题2.github网页加载ipynb文件失败
 解决方法：  
 1.复制你要查看的文件的URL，打开该网站：https://nbviewer.jupyter.org/ ，把你的URL复制到文本框，最后回车。  
 2.clone下来在本地查看  
 
 #### 问题3.spacy load问题   Can't find model 'en_core_web_sm'  
 解决方法：
 python -m spacy download en  或者  py -3 -m spacy download en  
 
 
 #### 问题4.nltk 安装完出现LookupError问题    
 解决方法：
 ```
import nltk     
nltk.download('punkt')   
```
 
 
 ## 自己照着代码运行，可能代码中穿插一些遇到的问题
 
 
 
 



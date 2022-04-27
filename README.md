
 

<div align="center">
<a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/built%20with-Python2.7-blue.svg" alt="built with Python2.7"/>
</a>
<a href="https://www.tensorflow.org/">
    <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="built with Tensorflow"/>
  </a>
</div>


# Supervised-Formality-Style-Transfer with Reinforcement Learning Framework - Mona Ebrahimi's Thesis
Formality style transfer is the task of modifying the formality of a given sentence without changing its content. Its challenge is the lack of large-scale sentence-aligned parallel data. In this paper, we propose a Reinforcement Learning Framework that takes psedo-parallel data and transfer the informal sentence to a formal style by appllying a dual training approach.

<div align="center">
 
| Formal Sentence |  Informal Sentence |
|:---:|:---:|
| اگر تمایل داشته باشید می توانید در جلسه شرکت کنید.  | اگه دوست داشتین میتونین بیایین تو جلسه |

</div>

## Training Data

- **Pseudo-parallel data:**
Digikala's Comments dataset is our dataset, the pseudo-parallel data created by a rulebased informal to formal model, data is created from two part; one is a parallel dataset which contain two aligned files(informal and formal). another one is the tsf folder which has both informal >>>>> formal and formal >>>>> informal in each file for training the dual training in each direction.

- **Evaluation Dataset:**
Our evaluation dataset(Shekasteh Dataset) is recently published and its sentences has various topics.

## Quick Start

**In order to help you quickly reproduce the existing works of text style transfer, we release the outputs of the models and the corresponding classifier result.**

## Output

Generated results (outputs) of our model are in the `outputs/` directory.


## Requirements
```
python==2.7
tensorflow==1.13.1
OpenNMT-tf==1.15.0 
```

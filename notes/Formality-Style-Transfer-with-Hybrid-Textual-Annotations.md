# Formality Style Transfer with Hybrid Textual Annotations

## 1.What is the problem

The problem is modifying or converting the informality of a given sentence to formality without changing its content.

## 2.What is the novelty of the article.
propose a novel formality transfer model that is able to incorporate hybrid types of loss functions to improve the quality of the transfered sentences
## 3.How is this solved?
approach involves a sequence-to-sequence (seq2seq) encoder-decoder model for style transformation and a style classification model. The proposed seq2seq model simultaneously handles the bidirectional transformation of formality between informal and formal, which enables various reconstruction losses to help model training; while the classification model fully utilizes the less expensive formality- classified annotation to compute a classifier-guided loss as ad- ditional feedback to the seq2seq model.

## 4.The advantages and disadvantages of the experiment
the first advantage is it can be easily adapted to other text style transfer tasks with competitive performance. Experiments on multiple benchmark datasets demonstrate that their approach achieves the best performance on formality style transfer by having both limited parallel data and larger unpaired data.

## 5.The problem that could be addressed in the future.
-Incomplete transfer and neglect of informal words
-failure to handle named entities.

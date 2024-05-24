# Rethinking Guidance Information to Utilize Unlabeled Samples: A Label-Encoding Perspective (ICML'24)

Official PyTorch implementation of Rethinking Guidance Information to Utilize Unlabeled Samples: A Label-Encoding Perspective.

Yulong Zhang, Yuan Yao, Shuhao Chen, Pengrong Jin, Yu Zhang, Jian Jin, Jiangang Lu.


## Abatract
Empirical Risk Minimization (ERM) has achieved great success in scenarios with sufficient labeled samples. However, many practical scenarios suffer from insufficient labeled samples. Under those scenarios, the ERM does not yield good performance as it cannot unleash the potential of unlabeled samples. In this paper, we rethink the guidance information to utilize unlabeled samples for handling those scenarios. By analyzing the learning objective of the ERM, we find that the guidance information for the labeled samples in a specific category is the corresponding label encoding. Inspired by this finding, we propose a Label-Encoding Risk Minimization (LERM) to mine the potential of unlabeled samples. It first estimates the label encodings through prediction means of unlabeled samples and then aligns them with their corresponding ground-truth label encodings. As a result, the LERM ensures both prediction discriminability and diversity and can be integrated into existing methods as a plugin. Theoretically, we analyze the relationship between the LERM and ERM. Empirically, we verify the superiority of the LERM under several label insufficient scenarios, including semi-supervised learning, unsupervised domain adaptation, and semi-supervised heterogeneous domain adaptation. 

## Installation

##### Install from Source Code

```shell
python setup.py install
pip install -r requirements.txt
```

## Usage
You can find scripts in the directory `SSL`, `UDA`, and `HDA`.

## Contact
If you have any problem with our code or have some suggestions, including the future feature, feel free to contact 
- Yulong Zhang (zhangylcse@zju.edu.cn)

or describe it in Issues.


## Acknowledgement

Our implementation is based on the [Transfer Learning Library](https://github.com/thuml/Transfer-Learning-Library), [BNM](https://github.com/cuishuhao/BNM), [SDAT](https://github.com/val-iisc/SDAT).

## Citation
If you find our paper or codebase useful, please consider citing us as:
```latex
@InProceedings{zhang2024rethinking,
  title={Rethinking Guidance Information to Utilize Unlabeled Samples: A Label-Encoding Perspective},
  author={Zhang, Yulong and Yao, Yuan and Chen, Shuhao and Jin, Pengrong and Jin, Jian and Lu Jiangang},
  booktitle={Proceedings of the 41th International Conference on Machine Learning},
  year={2024}
}
"""
@author: Baixu Chen
@contact: cbx_99_hasta@outlook.com
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class BatchNuclearNormMaximization(nn.Module):
    """
    Consistency loss between strong and weak augmented samples from `Unsupervised Data Augmentation for
    Consistency Training (NIPS 2020) <https://arxiv.org/pdf/1904.12848v4.pdf>`_.

    Args:
        threshold (float): Confidence threshold.
        temperature (float): Temperature.

    Inputs:
        - y_strong: unnormalized classifier predictions on strong augmented samples.
        - y: unnormalized classifier predictions on weak augmented samples.

    Shape:
        - y, y_strong: :math:`(minibatch, C)` where C means the number of classes.
        - Output: scalar.

    """

    def __init__(self,):
        super(BatchNuclearNormMaximization, self).__init__()


    def forward(self, y_strong, y):

        softmax_tgt = nn.Softmax(dim=1)(y_strong)
        _, s_tgt, _ = torch.svd(softmax_tgt)
        transfer_loss_1 = -torch.mean(s_tgt)

        softmax_tgt = nn.Softmax(dim=1)(y)
        _, s_tgt, _ = torch.svd(softmax_tgt)
        transfer_loss_2 = -torch.mean(s_tgt)
        
        transfer_loss = 0.1*transfer_loss_1 + transfer_loss_2

        return transfer_loss

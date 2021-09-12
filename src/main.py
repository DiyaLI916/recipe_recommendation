import argparse
import numpy as np
from time import time
from data_loader import load_data
from train import train

np.random.seed(555)

parser = argparse.ArgumentParser()

# recipe
parser.add_argument('--dataset', type=str, default='recipe', help='which dataset to use')
parser.add_argument('--n_epochs', type=int, default=1, help='the number of epochs')
parser.add_argument('--neighbor_sample_size', type=int, default=5, help='the number of neighbors to be sampled')
parser.add_argument('--dim', type=int, default=128, help='dimension of user and entity embeddings')
parser.add_argument('--n_iter', type=int, default=2, help='number of iterations when computing entity representation')
parser.add_argument('--batch_size', type=int, default=1024, help='batch size')
parser.add_argument('--l2_weight', type=float, default=1e-7, help='weight of l2 regularization')
parser.add_argument('--ls_weight', type=float, default=0.5, help='weight of LS regularization')
parser.add_argument('--lr', type=float, default=2e-2, help='learning rate')

show_loss = True
show_time = False
show_topk = False

t = time()

args = parser.parse_args()
data = load_data(args)

for item in data:
    print("------***-------")
    print(item)

train(args, data, show_loss, show_topk)

if show_time:
    print('time used: %d s' % (time() - t))

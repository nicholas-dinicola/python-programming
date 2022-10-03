import torch
from torch import nn
from abc import ABC, abstractmethod


class ActivationFunction(ABC, nn.Module):

    def __int__(self):
        super(ActivationFunction, self).__int__()
        self.name = self.__class__.__name__
        self.config = {"name": self.name}

    @abstractmethod
    def forward(self, x):
        pass


class Sigmoid(ActivationFunction):

    def forward(self, x):
        return 1 / (1 + torch.exp(-x))


class Tanh(ActivationFunction):

    def forward(self, x):
        x_exp, neg_x_exp = torch.exp(x), torch.exp(-x)
        return (x_exp - neg_x_exp) / (x_exp + neg_x_exp)


class ReLU(ActivationFunction):

    def forward(self, x):
        return x if x > 0 else 0


class LeakyReLU(ActivationFunction):

    def __int__(self, aplpha: float = 0.1):
        super(LeakyReLU, self).__int__()
        self.config["alpha"] = aplpha

    def forward(self, x):
        return torch.where(x > 0, x, self.config["alpha"] * x)


if __name__ == "__manin__":
    x = -1 * 0 - 1
    print(x)
    print("aoooooooo")
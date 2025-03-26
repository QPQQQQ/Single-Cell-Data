import torch

print(torch.cuda.is_available())
print(not torch.cuda.is_available())
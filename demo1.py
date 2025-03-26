import torch

# 检查 CUDA 是否可用
if torch.cuda.is_available():
    device = torch.device("cuda")  # 使用 GPU
    print("CUDA 可用，使用 GPU 加速")
else:
    device = torch.device("cpu")    # 使用 CPU
    print("CUDA 不可用，使用 CPU")

import torch

print("GPU Available:", torch.cuda.is_available())
print("Device Name:", torch.cuda.get_device_name(0))

with open("hello.txt", "wt") as fout:
    fout.write("Hello, World!\n")

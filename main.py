#!/usr/bin/env python3

import os

import torch

from colorama import Fore, init

init(autoreset=True)


def get_torch_device_list() -> list[torch.device]:
    torch_devices = []

    if torch.cuda.is_available():
        # Rocm uses the CUDA API
        # https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html
        print("Found Nvidia (Or maybe even AMD rocm) CUDA acceleration")
        print(f"  CUDA version     : {torch.version.cuda}")
        print(f"  CUDA acceleration: {torch.cuda.is_available()}")
        print(f"  CUDA device count: {torch.cuda.device_count()}")
        print(f"  Current device   : {torch.cuda.current_device()}")
        print("  Device List      :")

        for i in range(torch.cuda.device_count()):
            print(f"    CUDA device: {i}")
            print(f"      {torch.cuda.get_device_name(i)}")
            torch_devices.append(torch.device(f"cuda:{i}"))

    if torch.backends.mps.is_available():
        print("Found MPS (Apple Metal Performance Shaders) acceleration")
        torch_devices.append(torch.device("mps"))

    try:  # I don't think this ever fails
        torch_devices.append(torch.device("cpu"))
        print("Found CPU acceleration")
    except RuntimeError as err:
        print("Failed to find CPU acceleration")
        print(err)

    print()
    return torch_devices


def main():
    print(f"Torch: {torch.__version__}")
    print(f"Python: {os.sys.version}")
    print(f"OS: {os.uname().sysname} {os.uname().release} {os.uname().machine}")
    print()

    torch_devices = get_torch_device_list()

    print("Generating tensor to send to the devices...")
    x = torch.randn(3, 3)

    for torch_device in torch_devices:
        print(f"Torch device: {torch_device}")
        try:
            _ = x.to(torch_device)
            print(f"{Fore.GREEN}    Success!")
        except Exception as err:  # noqa: BLE001 # This is test code
            print(f"{Fore.RED}    Error\n{err}")


if __name__ == "__main__":
    main()

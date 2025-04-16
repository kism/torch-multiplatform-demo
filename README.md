# torch-multiplatform-demo

Demo of a torch project that runs with acceleration on Linux w/Nvidia and MacOS w/MPS.

The packages are defined in pyproject.toml, there are rules to install the correct packages for each platform.

## Setup

Install uv, this is my preferred tool to manage Python environments and packages.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create venv and install requirements.

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Run

Source the virtual environment if it's not already activated.

```bash
source .venv/bin/activate
```

Run the demo.

```bash
python3 main.py
```

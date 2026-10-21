# MiniHelper (Python Edition, CLI)
**An open-source CLI tool designed to solve minor inconveniences. It is simple and practical: just run the minihelper command followed by an operation and the required data from any terminal location. Installation and usage instructions are provided below.**

### Installation
To install MiniHelper locally in editable mode, run:
```bash
pip install -e .
```

### Usage
Once installed, you can use the tool from anywhere in your terminal:
```bash
minihelper plus 5 3
# Output: 8
```

### Architecture

```text
MiniHelper/
├── main.py                  ← Entry point (argparse + dispatch)
├── pyproject.toml           ← pip configuration (allows `minihelper` command)
├── README.md                ← Project documentation
├── requirements.txt         ← External dependencies
│
├── data/                    ← Data & registries (non-code)
│   ├── __init__.py          ← Package initializer
│   └── commands.py          ← COMMANDS dictionary mapping keys to core functions
│
└── core/                    ← Core logic
    ├── __init__.py          ← Facade (aggregates operations via `__all__`)
    ├── dispatcher.py        ← Routes command name to the correct function
    └── operations/          ← Actual operation functions
        ├── __init__.py      ← Exposes subdirectories (arithmetic, etc.)
        │
        ├── arithmetic/      ← Math operations
        │   ├── __init__.py  ← Exposes functions via `__all__`
        │   ├── plus.py      ← def plus(a, b): return a + b
        │   ├── minus.py     ← def minus(a, b): return a - b
        │   ├── multiply.py  ← def multiply(a, b): return a * b
        │   └── divide.py    ← def divide(a, b): return a / b
        │
        └── string_ops/      ← String operations (reserved for future)
            └── __init__.py
```
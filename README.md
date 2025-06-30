# N-Body Simulation with Python Wrapper

This project integrates a C-based N-body simulation with a Python wrapper, enabling users to interact with the simulation using Python. It is useful for astrophysical simulations, particle systems, or educational purposes.

## 📁 Project Structure

```
nbody-wrapper/                  
│   ├── nbody.c, nbody_comp.c, power1.c, etc. # C source code
│   ├── makefile           # Build instructions               
│   ├── nbody_wrapper.py   # Python interface to the compiled C code
│   ├── test.py            # Test script to run the simulation                  
│   ├── input.nbody_comp   # Input file
│   ├── output.nbody_8.000 # Output file                 
│   └── libnbody.so         # Shared library (after compilation)
```
## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yashdodiya9/python.git
cd python
```

### 2. Compile the C code

```bash
make
```

This generates a shared library (`libnbody.so` or similar) used by the Python wrapper.

### 3. Run the Python interface

```bash
python nbody_wrapper.py
```

You can also run `test.py` to verify functionality.

## Features

- Python wrapper for ease of use and integration
- Modular code with separate input/output handling
- Ready for integration into larger Python-based simulation frameworks

## Notes

- Make sure the compiled `.so` file path is correctly referenced in your Python wrapper.
- The `input.nbody_comp` file contains initial simulation parameters.

## Author

**Yash Dodiya**  
Feel free to contribute or raise issues!

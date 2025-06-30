import ctypes
import os

lib = ctypes.CDLL("./libnbody.so")
lib.run_nbody_simulation.argtypes = [ctypes.c_char_p]
lib.run_nbody_simulation.restype = None  #return type

def run_simulation(input_file):
    if not os.path.isfile(input_file):    #Ensures the input file exists before proceeding
        raise FileNotFoundError(f"{input_file} not found.")
    lib.run_nbody_simulation(input_file.encode('utf-8')) # Calls the actual C function from Python. 

#Running nbody_simulations, we can also run it here also
#run_simulation("input.nbody_comp")


#(I) UNDERSTANDING C CODES:
#1.Find a file (like nbody_comp.c) that seemed to be the main file.
#2.Find core functional files containing core & supporting functions (like nbody_funcs.c, powerspec.c, tf_fit.c, allottarrays.c    etc.)
#3.Look for header files that declared function interfaces, structures, and global variables (like nbody.h, etc.)
#4.Identify how the code is compiled(here using makefile), and what libraries it depends on(here FFTW for Fourier transforms &    OpenMP)

#(II) DECIDE WHAT IS NEEDED TO BE WRAPPED:
# We only need to expose main file(nbody_comp.c) other helping .c & .h files will be linked internally.

#(III) CREATING A SHARED LIBRARY:
#1.Identigy all C files & then write a makefile run like;
#gcc -fPIC -shared -o libnbody.so nbody_funcs.c allottarrays.c powerspec.c tf_fit.c nbody_wrapper_interface.c -I./fftw-3.3.10/fftw-install/include -L./fftw-3.3.10/fftw-install/lib -lfftw3f -lm -fopenmp
#2.This will make a file named "libnbody.so" which can be loaded in python via "ctypes".

#(IV) MAKING PYTHON WRAPPER (nbody_wrapper.py[this file only]):
#1.Load the shared library(libnbody.so) using ctypes.
#2.Declare function signature.
#3.Wrap it in a python function.

#(V) TEST IT.

#NOTE: 
#1."./libnbody.so" is a shared library(called dynamic library) that contains compiled machine code from your C source files.      It’s what enables Python to call your C functions without re-compiling them every time.
#2.All the ".c" files we compiled (like nbody_comp_final.c, nbody_funcs.c, etc.) are converted to binary code & bundled in this    ".so" file.
#3.But is doesn't include external libraries like(FFTW or OpenMP)but it knows how to find & link them at runtime by using         'lfftw3f -lfftw3f_threads -lm -fopenmp' while compiling/making .so file.
#4.Avoid using "printf" for i/p or o/p in function & try to use "void, int, float, double, etc." for funcion signature.

#SUMMARY OF PATH:
# your_code.c => your_code.h(optional) => libyourcode.so(compiled with gcc) => wrapper.py(calls C functions via ctypes).
# Basic comman for compilation "gcc -fPIC -shared -o lib<name>.so <your_sources>.c".
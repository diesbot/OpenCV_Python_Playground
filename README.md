# OpenCV_Python_Playground
In this repository I mess around with OpenCV in Python 3.

## Installing OpenCV for Python
The necessary packages will be installed using conda (Anaconda) for Python 3.  
Use ```conda update conda``` in preparation!

Steps:  
1. ```conda update --all```
2. ```conda create -n opencv numpy scipy scikit-learn matplotlib python=3```
3. ```source activate opencv``` (Linux, OSX),  
   ```activate opencv``` (Windows)
4. ```conda install -c menpo opencv3=3.1.0``` (look up current version on <http://binstar.org/>)

Check in python command line if the installation was successful.

```
import cv2
print(cv2.__version__)
```

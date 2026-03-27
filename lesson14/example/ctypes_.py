# использование посторонних  dll на "С"

import ctypes


# dll_path = os.path.join(os.path.dirname(__file__), "mylib.dll")
# lib = ctypes.WinDLL(dll_path)  # stdcall

user32 = ctypes.windll.user32  # Windows DLL!



GetSystemMetrics = user32.GetSystemMetrics
GetSystemMetrics.argtypes = [ctypes.c_int]
GetSystemMetrics.restype = ctypes.c_int

print("Ширина экрана:", GetSystemMetrics(0))    # SM_CXSCREEN
print("Высота экрана:", GetSystemMetrics(1))   # SM_CYSCREEN
print("Глубина цвета:", GetSystemMetrics(115)) # SM_CXBITS



kernel32 = ctypes.windll.kernel32
GetComputerNameA = kernel32.GetComputerNameA
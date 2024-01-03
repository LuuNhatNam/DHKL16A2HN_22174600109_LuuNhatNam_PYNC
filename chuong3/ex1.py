import numpy as np
numpy_version = np.__version__
print(f"Phiên bản NumPy hiện tại: {numpy_version}")
print("Cấu hình xây dựng của NumPy:")
for key, value in np.show_config().items():
    print(f"{key}: {value}")

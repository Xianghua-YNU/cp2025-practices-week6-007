import numpy as np
import matplotlib.pyplot as plt

def setup_parameters():
    """
    设置模拟牛顿环所需的参数
    
    返回:
    tuple: 包含激光波长(lambda_light,单位m)、透镜曲率半径(R_lens,单位m)的元组
    """
    lambda_light = 632.8e-9  # 氦氖激光波长 (m)
    R_lens = 0.1             # 透镜曲率半径 (m)
    return lambda_light, R_lens

def generate_grid():
    """
    生成模拟所需的网格坐标
    
    返回:
    tuple: 包含网格坐标X、Y以及径向距离r的元组
    """
    # 调整范围至±1mm，确保r的最大值远小于R_lens
    x = np.linspace(-0.001, 0.001, 1000)
    y = np.linspace(-0.001, 0.001, 1000)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2)
    return X, Y, r

def calculate_intensity(r, lambda_light, R_lens):
    """
    计算干涉强度分布
    
    参数:
    r (np.ndarray): 径向距离数组
    lambda_light (float): 激光波长(m)
    R_lens (float): 透镜曲率半径(m)
    
    返回:
    np.ndarray: 干涉强度分布数组
    """
    # 直接计算薄膜厚度d（由于r远小于R_lens，无需处理虚数）
    d = R_lens - np.sqrt(R_lens**2 - r**2)
    # 计算光强（公式与实验原理一致）
    intensity = 4 * (np.sin(2 * np.pi * d / lambda_light))**2
    return intensity

def plot_newton_rings(intensity):
    """
    绘制牛顿环干涉条纹图像
    
    参数:
    intensity (np.ndarray): 干涉强度分布数组
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(
        intensity, 
        cmap='gray', 
        extent=(-0.001, 0.001, -0.001, 0.001),  # 调整显示范围
        vmin=0,                                  # 设置颜色范围下限
        vmax=4,                                 # 设置颜色范围上限
        origin='lower'
    )
    plt.colorbar(label='Intensity')
    plt.title("Newton's Rings (Analytical Solution)")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.show()

if __name__ == "__main__":
    lambda_light, R_lens = setup_parameters()
    X, Y, r = generate_grid()
    intensity = calculate_intensity(r, lambda_light, R_lens)
    plot_newton_rings(intensity)

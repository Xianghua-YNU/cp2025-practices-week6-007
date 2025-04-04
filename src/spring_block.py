import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def solve_ode_euler(step_num):
    """
    使用欧拉法求解弹簧 - 质点系统的常微分方程。

    参数:
    step_num (int): 模拟的步数

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # 创建存储位置和速度的数组
    position = np.zeros(step_num + 1)
    velocity = np.zeros(step_num + 1)

    # 计算时间步长
    time_step = 2 * np.pi / step_num

    # 设置初始位置和速度
    position[0] = 0
    velocity[0] = 1

    # 使用欧拉法迭代求解微分方程
    for i in range(step_num):
        position[i + 1] = position[i] + velocity[i] * time_step
        velocity[i + 1] = velocity[i] - position[i] * time_step

    # 生成时间数组
    time_points = np.arange(step_num + 1) * time_step

    return time_points, position, velocity


def spring_mass_ode_func(state, time):
    """
    定义弹簧 - 质点系统的常微分方程。

    参数:
    state (list): 包含位置和速度的列表
    time (float): 时间

    返回:
    list: 包含位置和速度的导数的列表
    """
    x, v = state
    dxdt = v
    dvdt = -x  # 假设 k = m = 1
    return [dxdt, dvdt]


def solve_ode_odeint(step_num):
    """
    使用 odeint 求解弹簧 - 质点系统的常微分方程。

    参数:
    step_num (int): 模拟的步数

    返回:
    tuple: 包含时间数组、位置数组和速度数组的元组
    """
    # 设置初始条件
    initial_state = [0, 1]
    
    # 创建时间点数组
    time_points = np.linspace(0, 2 * np.pi, step_num + 1)
    
    # 使用 odeint 求解微分方程
    solution = odeint(spring_mass_ode_func, initial_state, time_points)
    
    # 从解中提取位置和速度
    position = solution[:, 0]
    velocity = solution[:, 1]
    
    return time_points, position, velocity


def plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint):
    """
    绘制欧拉法和 odeint 求解的位置和速度随时间变化的图像。
    """
    plt.figure(figsize=(10, 6))
    
    # 绘制位置对比图
    plt.subplot(2, 1, 1)
    plt.plot(time_euler, position_euler, 'b-', label='Euler Method')
    plt.plot(time_odeint, position_odeint, 'r--', label='odeint')
    plt.ylabel('Position')
    plt.title('Comparison of Solutions')
    plt.legend()
    
    # 绘制速度对比图
    plt.subplot(2, 1, 2)
    plt.plot(time_euler, velocity_euler, 'b-', label='Euler Method')
    plt.plot(time_odeint, velocity_odeint, 'r--', label='odeint')
    plt.ylabel('Velocity')
    plt.xlabel('Time')
    plt.legend()
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    step_count = 100
    # 使用欧拉法求解
    time_euler, position_euler, velocity_euler = solve_ode_euler(step_count)
    # 使用 odeint 求解
    time_odeint, position_odeint, velocity_odeint = solve_ode_odeint(step_count)
    # 绘制对比结果
    plot_ode_solutions(time_euler, position_euler, velocity_euler, time_odeint, position_odeint, velocity_odeint)

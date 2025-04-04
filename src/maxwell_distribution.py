import numpy as np
from scipy.integrate import quad
import time

# 最概然速率 (m/s)
vp = 1578  

def maxwell_distribution(v, vp):
    """
    计算麦克斯韦速率分布函数值
    
    参数：
    v : 分子速率 (m/s)
    vp : 最概然速率 (m/s)
    
    返回：
    分布函数f(v)的值
    """
    # 在此实现麦克斯韦分布函数
    f_v_ = 4/np.sqrt(np.pi)*(v**2/vp**3)*np.e**(-(v**2)/(vp**2))    #计算麦克斯韦速率分布函数值
    return f_v_

def percentage_0_to_vp(vp0):
    """
    计算速率在0到vp间隔内的分子数占总分子数的百分比
    
    参数：
    vp : 最概然速率 (m/s)
    
    返回：
    百分比值
    """
    # 在此实现0到vp的积分计算
    percent,error = quad(maxwell_distribution,0,vp0,args=(vp))  #使用quad函数进行积分
    return percent*100  #返回百分比值

def percentage_0_to_3_3vp(vp):
    """
    计算速率在0到3.3vp间隔内的分子数占总分子数的百分比
    
    参数：
    vp : 最概然速率 (m/s)
    
    返回：
    百分比值
    """
    # 在此实现0到3.3vp的积分计算
    return percentage_0_to_vp(3.3*vp) #在0到3.3vp区间积分

def percentage_3e4_to_3e8(vp):
    """
    计算速率在3×10^4到3×10^8 m/s间隔内的分子数占总分子数的百分比
    
    参数：
    vp : 最概然速率 (m/s)
    
    返回：
    百分比值
    """
    # 在此实现3×10^4到3×10^8的积分计算
    percent,error = quad(maxwell_distribution,3e4,3e8,args=(vp),epsabs=1e-100,epsrel=1e-100)
    return percent

def trapezoidal_rule(f, a, b, n):
    """
    使用梯形法则计算函数f在区间[a,b]上的定积分
    
    参数:
    f -- 被积函数
    a -- 积分下限
    b -- 积分上限
    n -- 区间划分数
    
    返回:
    积分近似值
    """
    # 在此实现梯形积分法则
    x = np.linspace(a,b,n)
    sumf = 0
    for i in x[1:-2]:
        sumf += f(i,vp)
    definite_integration = ((b-a)/(2*n))*(f(a,vp) + f(b,vp) + 2*sumf)
    return definite_integration

def compare_methods(task_name, quad_func, trap_func, vp, n_values=[10, 100, 1000]):
    """比较quad和梯形积分法的结果和性能"""
    print(f"\n{task_name}的方法对比:")
    
    # 使用quad计算（作为参考值）
    start_time = time.time()
    quad_result = quad_func(vp)
    quad_time = time.time() - start_time
    print(f"quad方法: {quad_result:.6f}%, 耗时: {quad_time:.6f}秒")
    
    # 使用不同区间划分数的梯形法则
    print("\n梯形积分法结果:")
    print(f"{'区间划分数':<12}{'结果 (%)':<15}{'相对误差 (%)':<15}{'计算时间 (秒)':<15}")
    
    for n in n_values:
        start_time = time.time()
        trap_result = trap_func(vp, n)
        trap_time = time.time() - start_time
        rel_error = abs(trap_result - quad_result) / quad_result * 100
        
        print(f"{n:<12}{trap_result:<15.6f}{rel_error:<15.6f}{trap_time:<15.6f}")

if __name__ == "__main__":
    # 测试代码
    print("=== 使用quad方法的结果 ===")
    print("0 到 vp 间概率百分比:", percentage_0_to_vp(vp), "%")
    print("0 到 3.3vp 间概率百分比:", percentage_0_to_3_3vp(vp), "%")
    print("3×10^4 到 3×10^8 间概率百分比:", percentage_3e4_to_3e8(vp), "%")
    
    print("\n=== quad方法与梯形积分法对比 ===")
    compare_methods("任务1: 0到vp", percentage_0_to_vp, percentage_0_to_vp_trap, vp)

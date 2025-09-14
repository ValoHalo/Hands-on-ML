import math
import csv
import random

def generate_sin_data_with_noise(length, step, noise_std=0.01, seed=42):
    """
    生成函数：sin(x / 180 * π) + x / 10000
    共 length 个数据点，步长为 step，
    添加高斯随机噪声（标准差=0.01），结果四舍五入到小数点后4位。
    使用固定种子保证结果可复现。
    """
    # 设置随机种子以确保可复现性
    random.seed(seed)
    
    data = []
    for i in range(length):
        x = i * step
        # 新函数：sin(x / 180 * π) + x / 10000
        y_clean = math.sin(x / 180 * math.pi) + x / 10000
        # 添加高斯噪声：均值为0，标准差为0.01
        noise = random.gauss(0, noise_std)
        y_noisy = y_clean + noise
        # 四舍五入到小数点后4位
        y_rounded = round(y_noisy, 4)
        data.append(y_rounded)
    return data

def save_to_csv(data, length, filename_prefix="sin_data_noisy"):
    """
    将数据保存为CSV文件，文件名包含长度信息，如：sin_data_noisy_300.csv
    """
    filename = f"{filename_prefix}_{length}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for value in data:
            writer.writerow([value])
    return filename

def main():
    try:
        length = int(input("请输入要生成的数据点数量 (length): "))
        if length <= 0:
            print("错误：length 必须是正整数。")
            return
        
        step = float(input("请输入步长 (step, 如 0.01): "))
        if step <= 0:
            print("错误：step 必须是正数。")
            return

        print(f"正在生成 {length} 个数据点，步长为 {step}，"
              f"函数为 sin(x/180 * π) + x/10000，噪声标准差=0.01，种子=42...")
        data = generate_sin_data_with_noise(length, step)
        
        filename = save_to_csv(data, length)
        print(f"数据已成功保存到 {filename}")
        print(f"前10个数据示例: {data[:10]}")

    except ValueError:
        print("错误：请输入有效的数字。")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
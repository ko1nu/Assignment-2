from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 保持与 input.py 一致的路径定义
DEFAULT_CSV_PATH = Path("data") / "expenses.csv"

def set_chinese_font():
    """
    设置中文字体，防止绘图时乱码
    """
    # 常见的系统字体尝试
    fonts = ['SimHei', 'Arial Unicode MS', 'PingFang SC', 'Microsoft YaHei']
    for font in fonts:
        plt.rcParams['font.sans-serif'] = [font]
        try:
            plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题
            return
        except:
            continue

def generate_expense_pie_chart(csv_path: Path):
    """
    读取 CSV 并生成饼图
    """
    if not csv_path.exists():
        print(f"❌ 错误: 找不到文件 {csv_path}。请先运行 input.py 添加数据。")
        return

    # 1. 读取数据
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return

    if df.empty:
        print("⚠️ CSV 文件内容为空，无法生成图表。")
        return

    # 2. 数据处理：按类别汇总金额
    # 确保 amount 列是数值类型
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    summary = df.groupby("category")["amount"].sum()

    # 3. 设置字体
    set_chinese_font()

    # 4. 绘图
    plt.figure(figsize=(10, 7))
    
    # 绘制饼图
    # autopct='%1.1f%%' 显示百分比，startangle=140 让图表更美观
    wedges, texts, autotexts = plt.pie(
        summary, 
        labels=summary.index, 
        autopct='%1.1f%%', 
        startangle=140,
        shadow=True,
        colors=plt.cm.Pastel1.colors
    )

    # 修饰图表
    plt.title(f"支出分类占比统计\n(总计: {summary.sum():.2f})", fontsize=14)
    plt.axis('equal')  # 保证是正圆

    # 5. 保存并展示
    output_img = Path("data") / "expenses_chart.png"
    plt.savefig(output_img)
    print(f"✅ 饼图已生成并保存至: {output_img}")
    
    print("📊 正在打开图表预览...")
    plt.show()

def main():
    print("=== Expense Visualizer (Member B) ===")
    generate_expense_pie_chart(DEFAULT_CSV_PATH)

if __name__ == "__main__":
    main()
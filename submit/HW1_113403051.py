# -*- coding: utf-8 -*-
import os
import pandas as pd

def load_and_explore_data(file_path):
    """任務一：讀取 CSV 並初步探索資料"""
    df = pd.read_csv(file_path, encoding='utf-8-sig')  # ← 請勿修改此行

    # TODO 1.1: 顯示前 5 筆資料
    print("=== 前 5 筆資料 ===")
    print(df.head())


    # TODO 1.2: 查看資料結構（欄位、型態、缺失值）
    print("\n=== 資料結構 ===")
    df.info()


    return df  # ← 請勿修改 return


def feature_engineering(df):
    """任務二：計算總分、平均分數與是否及格"""

    # 💡 記得將這裡的欄位名稱替換成你實際 CSV 裡的名稱
    subjects = ['國文', '英文', '數學', '自然', '社會']

    # TODO 2.1: 計算總分（五科加總）
    # sum(axis=1) 的意思是「橫向」相加，也就是把同一個學生的五科成績加起來
    df['總分'] = df[subjects].sum(axis=1)

    # TODO 2.2: 計算平均分數
    # 直接用剛剛算出來的總分除以 5 即可
    df['平均'] = df['總分'] / 5

    # TODO 2.3: 新增是否及格欄位（平均 >= 60 為及格）
    # 這行程式碼會自動判斷，如果 >= 60 就會填入 True，反之填入 False
    df['是否及格'] = df['平均'] >= 60

    return df  # ← 請勿修改 return


def filter_and_analyze_data(df):
    """任務三與五：篩選資料與統計"""

    # TODO 3.1: 找出數學成績 < 60 的學生
    math_failed = df[df['數學'] < 60]

    # TODO 3.2: 找出班級為 'A' 且英文 > 90 的學生
    # 注意：多個條件時，每個條件都要用括號包起來，並且用 & 代表「且」
    high_A = df[(df['班級'] == 'A') & (df['英文'] > 90)]

    # TODO 5.1: 顯示所有科目及平均分數的統計摘要
    # describe() 會自動計算數值欄位的平均數、標準差、最大最小值等統計數據
    summary = df.describe()

    # TODO 5.2: 找出總分最高的學生
    # Hint: 可以先找到總分最高分，再篩選對應學生
    max_total = df['總分'].max()
    top_student = df[df['總分'] == max_total]

    return {  # ← 請勿修改 return 結構（key 名稱不可變動）
        "processed_df": df,
        "math_failed": math_failed,
        "high_A": high_A,
        "summary": summary,
        "top_student": top_student
    }


def group_statistics(df):
    """任務四：使用 groupby 進行分組統計"""

    # TODO 4.1: 計算各班級的平均總分
    # 先根據 '班級' 分組，取出 '總分' 欄位，最後計算平均值
    class_avg_total = df.groupby('班級')['總分'].mean()

    # TODO 4.2: 計算各性別的及格率
    # 在 Python 中，True 代表 1，False 代表 0
    # 所以對布林值（是否及格）取平均，剛好就會得到「及格人數 / 總人數」的比例（及格率）
    gender_pass_rate = df.groupby('性別')['是否及格'].mean()

    return {  # ← 請勿修改 return 結構（key 名稱不可變動）
        "class_avg_total": class_avg_total,
        "gender_pass_rate": gender_pass_rate
    }


def save_results(df, output_file_path):
    """任務六：儲存為 CSV"""

    # TODO 6.1: 儲存 CSV，避免中文亂碼
    # index=False 是為了不要把左邊那排 0, 1, 2, 3... 的索引序號也存進去
    df.to_csv(output_file_path, index=False, encoding='utf-8-sig')



if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_CSV = os.path.join(BASE_DIR, '..', 'grades.csv')
    OUTPUT_CSV = os.path.join(BASE_DIR, 'grades_analyzed.csv')

    df = load_and_explore_data(INPUT_CSV)
    df = feature_engineering(df)
    result = filter_and_analyze_data(df)
    group_result = group_statistics(result["processed_df"])
    save_results(result["processed_df"], OUTPUT_CSV)

    print("完成所有分析任務")

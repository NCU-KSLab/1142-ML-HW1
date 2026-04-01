import sys
import subprocess

def ensure_pandas():
    try:
        # 嘗試導入 pandas
        import pandas
        print("Pandas 已經安裝，無需重複安裝。")
    except ImportError:
        # 如果導入失敗，執行安裝指令
        print("偵測到環境中缺少 pandas，正在嘗試自動安裝...")
        try:
            # sys.executable 確保安裝在目前使用的 Python 環境中
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
            print("Pandas 安裝成功！")
        except Exception as e:
            print(f"安裝失敗，請手動執行 'pip install pandas'。錯誤訊息: {e}")

# 在程式開始處執行檢查
ensure_pandas()

# 接下來就可以正常 import 了
import pandas as pd
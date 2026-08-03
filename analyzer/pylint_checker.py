# =========================================
# pylint代码检查模块
# Day2最终版
#
# 功能：
# 接收Python代码
# 调用pylint检查
# 返回检查报告
# =========================================

import sys

# 文件路径处理
import os


# 调用系统命令
import subprocess



# 定义代码检查函数
def check_python_code(code):


    # 创建临时代码文件
    file_path = "temp_code.py"



    # 写入用户代码
    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(code)



    # 调用pylint
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pylint",
            file_path
        ],

        # 获取输出
        capture_output=True,

        # 转换文本
        text=True
    )


    # 删除临时文件
    os.remove(file_path)


    # 返回检查结果
    return result.stdout + result.stderr
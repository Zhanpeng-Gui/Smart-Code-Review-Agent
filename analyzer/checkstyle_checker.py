# =========================================
# Java代码检查模块
# Day3
#
# 功能：
# 接收Java代码
# 调用Checkstyle
# 返回检查结果
# =========================================


# 文件操作
import os


# 调用外部程序
import subprocess



def check_java_code(code):


    # 临时Java文件

    file_path = "Temp.java"



    # 写入代码

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(code)



    # Checkstyle路径

    checkstyle_path = (
        "tools/checkstyle-13.9.0-all.jar"
    )


    # 规则文件

    config_path = (
        "rules/checkstyle.xml"
    )



    # 调用Checkstyle

    result = subprocess.run(
        [
            "java",
            "-jar",
            checkstyle_path,
            "-c",
            config_path,
            file_path
        ],

        capture_output=True
    )



    # 删除临时文件

    os.remove(file_path)



    # 返回结果

    # Java输出可能是不同编码
    # 这里强制转换成字符串
    
    output = (
        result.stdout.decode(
            "utf-8",
            errors="ignore"
        )
        +
        result.stderr.decode(
            "utf-8",
            errors="ignore"
        )
    )
    
    
    return output
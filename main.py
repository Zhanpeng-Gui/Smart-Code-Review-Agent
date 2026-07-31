# ======================================
# 智能代码评审Agent
# Day2版本
#
# 功能：
# 1. 接收用户代码
# 2. 调用pylint检查
# 3. 输出代码问题
# ======================================


# 导入我们的检查模块
from analyzer.pylint_checker import check_python_code



# 接收用户代码
def receive_code():

    print("请输入你的代码")
    print("输入 END 表示结束")


    code_lines = []


    while True:

        line = input()


        if line == "END":

            break


        code_lines.append(line)


    code = "\n".join(code_lines)


    return code



# 程序入口
if __name__ == "__main__":


    # 获取用户代码
    user_code = receive_code()


    print("\n========== 开始代码检查 ==========\n")


    # 调用pylint
    result = check_python_code(user_code)


    print(result)


    print("\n========== 检查结束 ==========")
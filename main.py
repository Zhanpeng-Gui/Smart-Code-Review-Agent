#=======================================
#智能代码评审Agent
#Day 1
#
#功能：
#1. 接受用户输入代码
#2. 保存代码内容
#3. 输出收到的代码
#=======================================


#定义一个函数
#作用：接收用户输入的代码
def receive_code():
    #提示用户输入代码
    print("请输入代码（输入 'END' 结束）：")
    code_lines = []
    while True:
        line = input()
        if line == "END":
            break
        code_lines.append(line)
    code = "\n".join(code_lines)
    return code

#Python程序入口
if __name__ == "__main__":
    #调用函数接收代码
    user_code = receive_code()
    #输出收到的代码
    print("\n========= Agent收到的代码 =========\n")
    print(user_code)
    print("\n========= 分析结束 =========\n")
    
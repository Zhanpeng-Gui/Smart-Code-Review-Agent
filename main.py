"""
智能代码评审Agent入口程序

功能：
1. 接收用户输入代码
2. 调用CodeReviewAgent
3. 生成Markdown报告
"""


# 导入Agent核心类
from agent.code_review_agent import CodeReviewAgent


# 导入报告生成模块
from agent.report_generator import generate_report



def get_user_code():
    """
    获取用户输入的代码

    用户输入END表示结束

    返回完整代码字符串
    """


    print("请输入你的代码")
    print("输入 END 表示结束")


    # 保存每一行代码

    lines = []


    while True:


        # 读取一行

        line = input()


        # 如果输入END，结束

        if line == "END":

            break


        # 保存代码

        lines.append(line)



    # 拼接成完整代码

    return "\n".join(lines)




def main():


    # 获取用户代码

    code = get_user_code()



    # 创建Agent

    agent = CodeReviewAgent()



    # 开始评审

    result = agent.review(code)



    # 生成报告

    report = generate_report(result)



    print("\n==========评审完成==========")

    print(
        f"报告位置：{report}"
    )




# 程序入口

if __name__ == "__main__":

    main()
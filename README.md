# Smart-Code-Review-Agent

一个基于大语言模型（LLM）的智能代码审查 Agent。

该项目模拟企业级 Code Review 流程，通过 **静态分析工具 + 大语言模型 + Agent 调度机制**，实现对 Python / Java 代码的自动化审查，并生成结构化审查结果和 Markdown 修复报告。


# 一、项目简介

在传统软件开发流程中，代码 Review 通常依赖人工完成，存在：

- 审查效率低
- 容易遗漏潜在风险
- 重复性规范检查耗费时间

本项目设计并实现一个智能代码审查 Agent：

用户提交代码后，Agent 自动完成：

1. 代码语言识别
2. Agent任务规划
3. 工具选择与调用
4. 静态代码分析
5. LLM智能分析
6. 风险等级评估
7. 问题统计
8. 自动生成修复建议
9. 输出结构化审查报告


整体流程：

```
              用户代码
                  |
                  v
        Code Review Agent
                  |
          Tool Planner
                  |
        +---------+---------+
        |                   |
        v                   v
  静态分析工具             LLM分析
        |                   |
        +---------+---------+
                  |
                  v
          风险分析模块
                  |
                  v
       Markdown Review Report
```



# 二、项目功能


## 1. 多语言代码检测

目前支持：

- Python
- Java


通过规则自动识别代码语言。

后续可扩展：

- C/C++
- JavaScript
- Go


---


## 2. Agent工具调度机制

项目引入简单 Agent Planner。

根据代码语言自动决定调用工具：

Python:

```
python_checker
llm_checker
```


Java:

```
java_checker
llm_checker
```


示例：

```python
['python_checker', 'llm_checker']
```

Agent 不再固定执行所有工具，而是根据任务选择合适工具。



---


## 3. Python静态代码检查


使用：

- pylint


检测：

- 未定义变量
- 缩进错误
- 缺少文档字符串
- 代码规范问题


示例：

```
temp_code.py:2:10: E0602: Undefined variable 'a'
```



---


## 4. Java代码静态检查


使用：

- Checkstyle


检测：

- Java代码格式问题
- 命名规范问题
- 编码规范问题



---


## 5. LLM智能代码分析


接入：

- 阿里云 DashScope
- Qwen大语言模型


用于分析静态工具无法发现的问题：

- SQL注入风险
- 空指针风险
- 资源泄露
- 事务问题
- 代码设计问题


输出结构化 JSON：

```json
{
    "issues":[
        {
            "type":"undefined-variable",
            "level":"critical",
            "location":"test.py:2",
            "reason":"变量未定义",
            "suggestion":"定义变量后再使用"
        }
    ]
}
```



---


## 6. 风险等级评估


根据：

- 静态检查结果
- LLM分析结果


综合判断代码风险：


|等级|说明|
|-|-|
|High|存在严重代码问题|
|Medium|存在潜在风险|
|Low|未发现明显风险|



---


## 7. 自动生成代码修复建议


针对发现的问题生成：

- 问题原因
- 修改方案
- 修复后的代码


示例：

```python
def test():
    """
    测试函数
    """
    a = 10
    print(a)
```



---


## 8. Markdown报告生成


自动生成：

```
review_report.md
```


报告包含：

- 风险等级
- 问题统计
- AI分析结果
- 静态检查结果
- 修复建议



---


## 9. FastAPI接口服务


提供 HTTP API：

接口：

```
POST /review
```


请求：

```json
{
    "code":"def test():\n    print(a)",
    "language":"python"
}
```


返回：

```json
{
    "success":true,
    "message":"代码审查完成",
    "data":{
        "language":"python",
        "risk":"High"
    }
}
```


支持：

- 请求参数校验
- 空代码拦截
- 异常处理
- Swagger接口测试



# 三、项目架构


```
Smart-Code-Review-Agent

│
├── agent
│   ├── code_review_agent.py
│   ├── risk_analyzer.py
│   ├── issue_analyzer.py
│   ├── report_generator.py
│   ├── report_formatter.py
│   └── fix_generator.py
│
├── analyzer
│   ├── pylint_checker.py
│   ├── checkstyle_checker.py
│   └── llm_checker.py
│
├── api
│   └── server.py
│
├── utils
│   ├── json_parser.py
│   └── logger.py
│
├── config
│   ├── __init__.py
│   └── settings.py
│
├── tools
│   └── checkstyle-13.9.0-all.jar
│
├── rules
│   └── checkstyle.xml
│
├── test_tools.py
├── test_llm.py
├── main.py
├── requirements.txt
└── README.md
```



# 四、技术栈


## 后端

- Python
- FastAPI
- Uvicorn


## AI

- LLM API
- Prompt Engineering
- JSON结构化输出


## Agent

- Tool Planning
- Agent Workflow设计
- 多工具协调调用


## 静态分析

- pylint
- Checkstyle


## 工程工具

- Git
- GitHub
- VSCode



# 五、运行方式


## 1. 克隆项目

```bash
git clone https://github.com/yourname/Smart-Code-Review-Agent.git
```


## 2. 创建虚拟环境

```bash
python -m venv venv
```


启动：

Windows:

```bash
venv\Scripts\activate
```


## 3. 安装依赖


```bash
pip install -r requirements.txt
```



## 4. 配置API Key


创建：

```
.env
```


填写：

```
DASHSCOPE_API_KEY=your_api_key
```



## 5. 启动服务


```bash
uvicorn api.server:app --reload
```


访问：

```
http://127.0.0.1:8000/docs
```


进入 FastAPI Swagger 页面测试接口。



# 六、项目开发过程


## Day1

完成：

- 项目初始化
- Git环境配置
- 基础代码输入模块


## Day2

完成：

- pylint静态分析
- Python代码检查模块


## Day3

完成：

- Java环境配置
- Checkstyle接入


## Day4

完成：

- LLM API接入
- Prompt设计


## Day5

完成：

- AI结果解析
- JSON处理


## Day6

完成：

- 风险等级分析
- 问题统计


## Day7

完成：

- Markdown报告生成
- 修复建议生成


## Day8

完成：

- FastAPI后端服务
- HTTP API接口
- Swagger接口测试
- 请求参数校验
- 空代码输入拦截
- API统一响应格式


## Day9

完成：

- Agent工具规划模块
- Tool Registry设计
- 根据代码类型动态选择工具
- Python / Java工具链调度
- Agent执行流程优化

- 引入 Planner-Executor 架构
- 实现任务规划模块 Planner
- 根据代码语言自动生成执行计划
- 引入 Tool Registry 工具注册机制
- 将静态检查和 LLM 分析封装为独立 Tool
- 实现 Agent 动态调用不同工具完成代码审查流程


当前 Agent 执行流程：

用户代码

↓

CodeReviewAgent

↓

Planner生成任务计划

↓

Tool Registry选择工具

↓

执行代码分析

↓

风险评估与报告生成

# 七、未来优化方向


后续计划：

- 增加 Web 前端页面
- 支持代码文件上传
- GitHub Pull Request自动Review
- 支持更多编程语言
- 引入RAG增强代码理解
- 接入代码仓库级分析
- 增加用户权限管理



# 八、项目总结


本项目实现了一个完整的智能代码审查 Agent。

相比传统静态检查工具：

- 静态工具负责发现确定性问题
- LLM负责理解代码逻辑和业务风险
- Agent负责规划任务并协调多个工具完成审查流程


通过项目实践：

- 掌握LLM API调用
- 理解Agent工作机制
- 学习Prompt Engineering
- 完成AI应用工程开发流程
- 掌握FastAPI后端接口开发



# API接口


启动：

```bash
uvicorn api.server:app --reload
```


访问：

```
http://127.0.0.1:8000/docs
```


接口：

```
POST /review
```


功能：

- Python代码审查
- Java代码审查
- pylint/checkstyle静态分析
- LLM智能分析
- Agent工具调度
- 自动生成修复建议
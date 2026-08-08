# Smart-Code-Review-Agent


一个基于 **LLM + Agent 架构** 的智能代码审查系统。


该项目模拟企业级 Code Review 流程，通过：

- 静态分析工具
- 大语言模型
- Agent任务规划
- 工具调度机制
- 历史记忆模块

实现对 Python / Java 代码的自动化审查，并生成结构化审查结果和 Markdown 修复报告。


---

# 一、项目简介


在传统软件开发流程中，代码 Review 通常依赖人工完成，存在：

- 审查效率低
- 容易遗漏潜在风险
- 重复性规范检查耗费时间


本项目设计并实现一个智能代码审查 Agent。


用户提交代码后，Agent 自动完成：


1. 代码语言识别
2. 历史审查记录读取
3. Agent任务规划
4. 工具选择与调用
5. 静态代码分析
6. LLM智能分析
7. 风险等级评估
8. 问题统计
9. 自动生成修复建议
10. Markdown审查报告生成


整体流程：


```
                 用户代码
                    |
                    v

          Code Review Agent

                    |
                    v

              Memory模块
          (历史审查记录)

                    |
                    v

              Planner规划

                    |
          +---------+---------+
          |                   |
          v                   v

   Static Tools             LLM Tool

(pylint/checkstyle)       智能分析

          |                   |

          +---------+---------+

                    |
                    v

             Risk Analyzer

                    |
                    v

          Fix Generator

                    |
                    v

          Markdown Report
```


---

# 二、项目功能


## 1. 多语言代码检测


目前支持：

- Python
- Java


通过代码特征自动识别语言。


后续可扩展：

- C/C++
- JavaScript
- Go



---


## 2. Agent任务规划机制


项目引入 Planner 模块。


Planner 根据：

- 当前代码语言
- 历史审查记录


自动决定需要调用的工具。


例如：


Python代码：

```
python_checker
llm_checker
```


Java代码：

```
java_checker
llm_checker
```


Agent 不再固定执行所有流程，而是根据任务动态规划执行步骤。


---


## 3. Tool Registry工具管理机制


项目采用工具注册机制管理不同分析能力。


当前支持：


```
python_checker

java_checker

llm_checker
```


每个工具独立封装：

- 输入代码
- 执行分析
- 返回结果


后续可以扩展：

```
security_checker

performance_checker

database_checker
```


---


## 4. Memory历史记忆模块


Agent支持历史审查记录保存。


记录内容包括：

- 审查时间
- 风险等级
- 问题统计
- 主要问题


历史信息会传递给 Planner，辅助后续任务规划。


---


## 5. Python静态代码检查


使用：

- pylint


检测：

- 未定义变量
- 语法错误
- 缩进错误
- 代码规范问题


示例：

```
temp_code.py:2:10:
E0602 Undefined variable 'a'
```


---


## 6. Java代码静态检查


使用：

- Checkstyle


检测：

- Java代码格式问题
- 命名规范问题
- 编码规范问题


---


## 7. LLM智能代码分析


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


## 8. 风险等级评估


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


## 9. 自动生成代码修复建议


针对发现的问题生成：

- 问题原因
- 修改方案
- 修复后的代码


示例：

```python
def test():

    a = 10

    print(a)
```


---


## 10. Markdown报告生成


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


## 11. Web可视化界面


基于：

- HTML
- CSS
- JavaScript


实现：

- 文件上传
- 代码审查
- 风险展示
- 问题列表展示
- Markdown格式修复建议渲染
- 报告下载


用户无需调用API即可完成代码审查。


---


# 三、项目架构


```
Smart-Code-Review-Agent

│
├── agent
│   ├── code_review_agent.py
│   ├── planner.py
│   ├── memory_manager.py
│   ├── risk_analyzer.py
│   ├── issue_analyzer.py
│   ├── report_generator.py
│   ├── report_formatter.py
│   └── fix_generator.py
│
├── tools
│   ├── tool_manager.py
│   ├── python_checker.py
│   ├── java_checker.py
│   └── llm_checker.py
│
├── api
│   └── server.py
│
├── frontend
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── utils
│   ├── json_parser.py
│   └── logger.py
│
├── config
│   ├── settings.py
│   └── __init__.py
│
├── rules
│   └── checkstyle.xml
│
├── requirements.txt
│
├── main.py
│
└── README.md
```


---


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

- Planner任务规划
- Tool Registry
- Memory机制
- Agent Workflow设计


## 静态分析

- pylint
- Checkstyle


## 前端

- HTML
- CSS
- JavaScript
- marked.js


## 工程工具

- Git
- GitHub
- VSCode


---


# 五、运行方式


## 1. 创建虚拟环境


```bash
python -m venv venv
```


启动：

Windows：

```bash
venv\Scripts\activate
```


---


## 2. 安装依赖


```bash
pip install -r requirements.txt
```


---


## 3. 配置API Key


创建：

```
.env
```


填写：

```
DASHSCOPE_API_KEY=your_api_key
```


---


## 4. 启动服务


```bash
uvicorn api.server:app --reload
```


访问：

```
http://127.0.0.1:8000
```


Swagger：

```
http://127.0.0.1:8000/docs
```


---


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
- JSON结构化处理


## Day6

完成：

- 风险等级分析
- 问题统计模块


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
- 异常处理


## Day9

完成：

- Agent Planner模块
- Tool Registry设计
- 动态工具调用
- Agent执行流程优化
- Web前端页面
- 文件上传代码审查


## Day10

完成：

- 前端UI优化
- Markdown网页渲染
- Agent Memory模块
- Planner结合历史记录
- Agent Workflow完善


---


# 七、未来优化方向


后续计划：

- 多Agent协作
- 自动修复代码并生成Patch
- GitHub Pull Request自动Review
- RAG代码知识库
- 支持代码仓库级分析
- 增加安全漏洞扫描
- 支持更多编程语言


---


# 八、项目总结


本项目实现了一个完整的智能代码审查 Agent。


相比传统静态检查工具：

- 静态工具负责发现确定性问题
- LLM负责理解代码逻辑和业务风险
- Agent负责任务规划和工具协调
- Memory负责保存历史上下文


通过项目实践：

- 掌握LLM API调用
- 理解Agent工作机制
- 学习Prompt Engineering
- 完成AI应用工程开发流程
- 掌握FastAPI后端开发
- 理解Agent系统设计


---


# API接口


启动：

```bash
uvicorn api.server:app --reload
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
- Agent任务规划
- Memory历史记录
- 自动生成修复建议
- Markdown报告生成
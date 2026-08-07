# Smart-Code-Review-Agent

一个基于大语言模型（LLM）的智能代码审查 Agent。

该项目模拟企业代码 Review 流程，通过静态分析工具 + 大模型分析，对 Python / Java 代码进行自动化检查，并生成 Markdown 格式审查报告。


## 一、项目简介

在传统软件开发流程中，代码 Review 通常依赖人工完成，存在：

- 审查效率低
- 容易遗漏潜在问题
- 规范检查重复工作量大

本项目设计并实现一个智能代码审查 Agent：

用户提交代码后，Agent 自动完成：

1. 代码语言识别
2. 静态代码检查
3. LLM 智能分析
4. 风险等级评估
5. 问题统计
6. 自动生成修复建议


整体流程：

```
        用户代码
            |
            v
    Code Review Agent
            |
    +-------+--------+
    |                |
    v                v
静态分析工具        LLM分析
    |                |
    +-------+--------+
            |
            v
     风险评估模块
            |
            v
    Markdown审查报告
```


## 二、项目功能


### 1. 多语言代码检测

目前支持：

- Python
- Java


通过简单规则自动识别代码语言。


---

### 2. Python静态代码检查


使用：

- pylint


检测：

- 未定义变量
- 缩进错误
- 缺少文档字符串
- 代码规范问题


示例：

```
temp_code.py:2:7: E0602: Undefined variable 'a'
```


---

### 3. Java代码静态检查


使用：

- Checkstyle


检测：

- Java代码规范问题
- 格式问题
- 命名规范问题


---

### 4. LLM智能代码分析


接入：

- 阿里云 DashScope
- Qwen 大语言模型


用于分析静态工具无法发现的问题：

- SQL注入风险
- 空指针风险
- 资源泄露
- 事务问题
- 代码设计问题


输出 JSON 格式：

```json
{
    "issues":[
        {
            "type":"Undefined variable",
            "level":"critical",
            "location":"test.py:2",
            "reason":"变量未定义",
            "suggestion":"定义变量后再使用"
        }
    ]
}
```


---

### 5. 风险等级评估


根据：

- LLM分析结果
- 静态检查结果


综合判断代码风险：

|等级|说明|
|-|-|
|High|存在严重代码问题|
|Medium|存在潜在风险|
|Low|未发现明显风险|


---

### 6. 自动生成代码修复建议


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

### 7. Markdown报告生成


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



## 三、项目架构


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
├── utils
│   ├── json_parser.py
│   └── logger.py
│
├── api
│   └── server.py
│
├── tools
│   └── checkstyle.jar
│
├── rules
│   └── checkstyle.xml
│
├── config
│   ├── __init__.py
│   └── settings.py
│
├── main.py
├── requirements.txt
└── README.md
```


## 四、技术栈


### 后端

- Python
- FastAPI


### AI

- LLM API
- Prompt Engineering
- JSON结构化输出


### 静态分析

- pylint
- Checkstyle


### 工程工具

- Git
- GitHub
- VSCode


## 五、运行方式


### 1. 克隆项目

```bash
git clone https://github.com/yourname/Smart-Code-Review-Agent.git
```


### 2. 创建虚拟环境


```bash
python -m venv venv
```


启动：

Windows:

```bash
venv\Scripts\activate
```


---

### 3. 安装依赖


```bash
pip install -r requirements.txt
```


---

### 4. 配置API Key


创建：

```
.env
```


填写：

```
DASHSCOPE_API_KEY=your_api_key
```


---

### 5. 启动项目


```bash
python main.py
```


访问：

```
http://127.0.0.1:8000/docs
```


使用 FastAPI Swagger 页面测试接口。


## 六、项目实现过程


### Day1

完成：

- 项目初始化
- Git环境配置
- 基础代码输入模块


### Day2

完成：

- pylint静态分析
- Python代码检查模块


### Day3

完成：

- Java环境配置
- Checkstyle接入


### Day4

完成：

- LLM API接入
- Prompt设计


### Day5

完成：

- AI结果解析
- JSON处理


### Day6

完成：

- 风险等级分析
- 问题统计


### Day7

完成：

- Markdown报告生成
- 修复建议生成

### Day8
- 引入 FastAPI 后端服务
- 提供 HTTP API 接口
- 支持 Swagger 在线接口测试
- 增加请求参数校验
- 实现空代码输入拦截

## 七、未来优化方向


后续计划：

- 增加 Web 前端页面
- 支持代码文件上传
- 增加 GitHub Pull Request 自动 Review
- 支持更多语言
- 引入 RAG 技术增强代码理解


## 八、项目总结


本项目实现了一个完整的智能代码审查 Agent。

相比传统静态检查工具：

- 静态工具负责发现确定性问题
- LLM负责理解代码逻辑和业务风险
- Agent负责协调多个工具完成自动化审查流程


通过该项目实践：

- 掌握 LLM API 调用
- 理解 Agent 工作流程
- 学习 Prompt Engineering
- 完成 AI 应用工程开发流程


## API接口

启动：

uvicorn api.server:app --reload


访问：

http://127.0.0.1:8000/docs


接口：

POST /review


功能：

- Python代码审查
- Java代码审查
- pylint/checkstyle静态分析
- LLM智能分析
- 自动生成修复建议
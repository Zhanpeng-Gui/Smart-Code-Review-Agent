from analyzer.llm_checker import check_by_llm


code = """
def test():
    print(a)
"""


static_result = """
E0602: Undefined variable 'a'
"""


result = check_by_llm(
    code,
    static_result
)


print(result)
from analyzer.llm_checker import check_by_llm



code = """

def login(username):

    sql = "select * from user where name='" + username + "'"

    return sql

"""



result = check_by_llm(code)


print(result)
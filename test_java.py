from analyzer.checkstyle_checker import check_java_code



code = """

public class Test {

public static void main(String[] args){

System.out.println("hello");

}

}

"""


result = check_java_code(code)


print(result)
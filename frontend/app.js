function cleanMarkdown(text){


    // 去除最外层 ```markdown 包裹

    text = text.replace(
        /^```markdown\s*/,
        ""
    );


    text = text.replace(
        /\s*```$/,
        ""
    );


    return text;

}





async function reviewCode(){

    document.getElementById(
        "result"
    ).innerHTML =
    `
    <h3>
    ⏳ 正在分析代码，请稍候...
    </h3>
    `;


    let file =
    document.getElementById(
        "fileInput"
    ).files[0];



    if(!file){

        alert(
            "请选择代码文件"
        );

        return;

    }



    let code =
    await file.text();



    document.getElementById(
        "fileInfo"
    ).innerHTML =
`
<h3>
文件信息
</h3>

<p>
文件名:
${file.name}
</p>

<p>
代码长度:
${code.length}
字符
</p>

<p>
语言:
${file.name.endsWith(".java") ? "Java" : "Python"}
</p>

`;



    let response =
    await fetch(
        "/review",
        {

            method:"POST",


            headers:{

                "Content-Type":
                "application/json"

            },


            body:
            JSON.stringify({

                code:code,

                language:
                file.name.endsWith(".java")
                ?
                "java"
                :
                "python"

            })

        }
    );



    let result =
    await response.json();



    if(!result.success){


        document.getElementById(
            "result"
        ).innerHTML =
        result.message;


        return;

    }



    let data =
    result.data;



    let issuesHTML = "";



    try {


        let ai =
        JSON.parse(
            data.ai_review
        );


        if(ai.issues.length > 0){


            issuesHTML = `

<table class="issue-table">

<tr>

<th>
类型
</th>

<th>
等级
</th>

<th>
位置
</th>

<th>
原因
</th>

</tr>


${
ai.issues.map(
issue =>

`

<tr>

<td>
${issue.type}
</td>


<td>
${issue.level}
</td>


<td>
${issue.location}
</td>


<td>
${issue.reason}
</td>


</tr>

`

).join("")

}


</table>

`;

        }


        else{


            issuesHTML =
            "<p>未发现代码问题</p>";


        }


    }
    catch(e){


        issuesHTML =
        "<p>问题解析失败</p>";


    }




    let riskColor="";



    if(data.risk==="High"){

        riskColor="red";

    }
    else if(data.risk==="Medium"){

        riskColor="orange";

    }
    else{

        riskColor="green";

    }




    // Markdown清洗

    let markdownFix =
    cleanMarkdown(
        data.fix
    );





    document.getElementById(
    "result"
    ).innerHTML = `


<h2>
审查结果
</h2>



<div class="risk-card"
style="border-left:8px solid ${riskColor};">



<h3>
风险等级
</h3>


<h2>

${
data.risk==="High"
?
"🔴"
:
data.risk==="Medium"
?
"🟠"
:
"🟢"
}


${data.risk}


</h2>



<p>
${data.risk_description}
</p>


</div>




<h3>
问题统计
</h3>


<p>
严重:
${data.issue_summary.high}
</p>



<p>
中等:
${data.issue_summary.medium}
</p>



<p>
低风险:
${data.issue_summary.low}
</p>




<h3>
问题列表
</h3>


${issuesHTML}





<h3>
静态检查结果
</h3>


<pre>

${data.static_check}

</pre>





<h3>
修复建议
</h3>


<div class="markdown-body">

${marked.parse(markdownFix)}

</div>


`;

}





// 下载报告

function downloadReport(){

    window.location.href =
    "/download/report";

}
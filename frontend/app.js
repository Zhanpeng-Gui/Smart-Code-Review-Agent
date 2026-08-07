async function reviewCode(){


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



    document.getElementById(
    "result"
    ).innerHTML = `


<h2>
审查结果
</h2>


<h3>
代码语言
</h3>

<p>
${data.language}
</p>


<h3>
风险等级
</h3>

<p>
${data.risk}
</p>


<h3>
问题统计
</h3>

<ul>

<li>
严重:
${data.issue_summary.high}
</li>

<li>
中等:
${data.issue_summary.medium}
</li>

<li>
低:
${data.issue_summary.low}
</li>

</ul>


<h3>
AI分析
</h3>

<pre>
${data.ai_review}
</pre>


<h3>
静态检查
</h3>

<pre>
${data.static_check}
</pre>


<h3>
修复建议
</h3>

<pre>
${data.fix}
</pre>


`;

}



// 下载报告

function downloadReport(){

    window.location.href =
    "/download/report"

}
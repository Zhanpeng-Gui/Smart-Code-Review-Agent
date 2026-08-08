import json
import os

from datetime import datetime



HISTORY_FILE = "memory/review_history.json"



def save_review(result):


    history = load_history()



    try:

        ai_result = json.loads(
            result["ai_review"]
        )


        issues = ai_result.get(
            "issues",
            []
        )


    except:

        issues = []



    history.append({

        "time":
        str(datetime.now()),


        "risk":
        result.get(
            "risk"
        ),


        "summary":
        result.get(
            "issue_summary"
        ),


        "issues":
        issues,


        "fix":
        result.get(
            "fix",
            ""
        )

    })



    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(

            history,

            f,

            ensure_ascii=False,

            indent=4

        )




def load_history():


    if not os.path.exists(
        HISTORY_FILE
    ):

        return []



    with open(

        HISTORY_FILE,

        "r",

        encoding="utf-8"

    ) as f:


        return json.load(f)

def get_recent_reviews(limit=5):


    history = load_history()


    return history[-limit:]
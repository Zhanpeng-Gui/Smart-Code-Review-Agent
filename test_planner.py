from agent.planner import Planner


planner = Planner()


print(
    planner.create_plan(
        "python"
    )
)


print(
    planner.create_plan(
        "java"
    )
)
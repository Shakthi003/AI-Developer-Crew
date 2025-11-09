from langgraph.graph import StateGraph
from pydantic import BaseModel
from typing import Optional
from crew_setup import create_dev_crew

class DevCrewState(BaseModel):
    task: str
    plan: Optional[str] = None
    code: Optional[str] = None
    review: Optional[str] = None
    fix_needed: Optional[bool] = False
    tests: Optional[str] = None

def build_dev_graph():
    planner, coder, reviewer, tester = create_dev_crew()

    g = StateGraph(state_schema=DevCrewState)

    def planner_node(state: DevCrewState):
        response = planner.invoke({"task": state.task})
        return {"task": state.task, "plan": response.content}

    def coder_node(state: DevCrewState):
        response = coder.invoke({"plan": state.plan})
        return {"task": state.task, "plan": state.plan, "code": response.content}

    def reviewer_node(state: DevCrewState):
        response = reviewer.invoke({"code": state.code})
        review = response.content
        fix_needed = "issue" in review.lower() or "error" in review.lower()
        return {
            "task": state.task,
            "plan": state.plan,
            "code": state.code,
            "review": review,
            "fix_needed": fix_needed
        }

    def tester_node(state: DevCrewState):
        response = tester.invoke({"code": state.code})
        return {
            "task": state.task,
            "plan": state.plan,
            "code": state.code,
            "review": state.review,
            "tests": response.content
        }

    g.add_node("START", lambda state: state)
    g.add_node("planner", planner_node)
    g.add_node("coder", coder_node)
    g.add_node("reviewer", reviewer_node)
    g.add_node("tester", tester_node)
    g.add_node("END", lambda state: state)

    g.add_edge("START", "planner")
    g.add_edge("planner", "coder")
    g.add_edge("coder", "reviewer")
    g.add_conditional_edges("reviewer", lambda s: "coder" if s.fix_needed else "tester")
    g.add_edge("tester", "END")

    g.set_entry_point("START")

    return g.compile()
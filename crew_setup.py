from crewai import Crew, Agent
from agents.planner import create_planner
from agents.coder import create_coder
from agents.reviewer import create_reviewer
from agents.tester import create_tester
from langchain_community.chat_models import ChatOllama
# Planner Agent using Gemma2B locally
def create_dev_crew():
    planner = create_planner()
    coder = create_coder()
    reviewer = create_reviewer()
    tester = create_tester()
    return [planner, coder, reviewer, tester]


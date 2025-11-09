import streamlit as st
from langgraph_flow import build_dev_graph

st.set_page_config(page_title="AI Developer Team", layout="wide")
st.title("🤖 AI Developer Crew — LangGraph + LangChain")

user_task = st.text_area(
    "Describe your software requirement:",
    placeholder="e.g., Build a Python CLI app to manage tasks"
)

if st.button("Generate Project Plan & Code"):
    if not user_task.strip():
        st.warning("Please enter a requirement first.")
    else:
        st.info("🚀 Running AI Developer Crew...")
        try:
            graph = build_dev_graph()
            result = graph.invoke({"task": user_task})

            st.success("✅ Task Completed!")
            st.subheader("Output Summary")

            st.success("✅ Task Completed!")
            st.subheader("Output Summary")

            st.markdown(f"**Project Plan:**\n{result.get('plan', '')}")
            st.code(result.get('code', ''), language="python")
            st.markdown(f"**Review Feedback:**\n{result.get('review', '')}")
            st.code(result.get('tests', ''), language="python")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
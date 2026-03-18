import streamlit as st
from agents import planner_agent, search_agent, analysis_agent, writer_agent

st.set_page_config(layout="wide")

st.title("🤖 Autonomous AI Research Agent")

st.write("Multi-Agent AI system that researches topics automatically.")

query = st.text_input("Enter research topic")

if st.button("Start Research"):

    progress = st.progress(0)

    log_box = st.empty()

    col1, col2 = st.columns(2)

    planner_box = col1.empty()
    search_box = col1.empty()
    analysis_box = col2.empty()
    writer_box = col2.empty()

    # Planner
    log_box.write("Planner agent started...")
    planner_box.info("🧠 Planner Agent running...")

    plan = planner_agent(query)

    planner_box.success("Planner completed")

    with st.expander("Planner Output"):
        st.write(plan)

    progress.progress(25)

    # Search
    log_box.write("Search agent collecting web data...")
    search_box.info("🌐 Search Agent running...")

    results = search_agent(query)

    search_box.success("Search completed")

    with st.expander("Search Results"):
        st.write(results)

    progress.progress(50)

    # Analysis
    log_box.write("Analysis agent extracting insights...")
    analysis_box.info("📊 Analysis Agent running...")

    insights = analysis_agent(results)

    analysis_box.success("Analysis completed")

    with st.expander("Extracted Insights"):
        st.write(insights)

    progress.progress(75)

    # Writer
    log_box.write("Writer agent generating report...")
    writer_box.info("📝 Writer Agent running...")

    report = writer_agent(insights)

    writer_box.success("Report Generated")

    progress.progress(100)

    st.subheader("📄 Final Research Report")

    st.write(report)
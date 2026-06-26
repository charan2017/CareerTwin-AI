import streamlit as st


def priority_color(priority):

    if priority == "High":
        return "🔴"

    elif priority == "Medium":
        return "🟡"

    else:
        return "🟢"


def show_recommendations(data):

    st.divider()

    st.subheader("🤖 AI Resume Suggestions")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.metric(
            "Estimated ATS",
            f"{data['estimated_score']}%"
        )

        st.info(
            f"🚀 Recommended Project\n\n**{data['project']}**"
        )

    with col2:

        st.markdown("### 📋 Improvement Plan")

        for item in data["suggestions"]:

            icon = priority_color(item["priority"])

            with st.container():

                st.markdown(
                    f"""
### {icon} {item['title']}

**Priority:** {item['priority']}

{item['description']}
"""
                )
import streamlit as st


def show_roadmap(analysis):

    st.subheader("🗺 Personalized Learning Roadmap")

    missing = analysis["missing"]

    if len(missing) == 0:

        st.success(
            "🎉 Congratulations! You already have all the required skills for this role."
        )

        return

    total_weeks = len(missing)

    for week, skill in enumerate(missing, start=1):

        st.markdown(f"### 📅 Week {week}")

        st.write(f"🎯 **Learn:** {skill}")
        st.write("📚 Study the official documentation")
        st.write("💻 Build one mini project")
        st.write("📝 Add the skill to your resume after practice")

        progress = week / total_weeks
        st.progress(progress)

        st.divider()

    st.success("🚀 Complete this roadmap to become job-ready!")
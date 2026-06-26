import streamlit as st


def hero():

    st.markdown(
        """
<style>

.hero{
    padding:35px;
    border-radius:22px;

    background:linear-gradient(
        135deg,
        #312E81,
        #1E3A8A,
        #0F172A
    );

    color:white;

    border:1px solid #334155;

    margin-bottom:30px;

    box-shadow:0 10px 40px rgba(0,0,0,.35);
}

.hero h1{
    font-size:52px;
    margin-bottom:10px;
}

.hero h3{
    color:#CBD5E1;
    margin-bottom:25px;
}

.hero p{
    font-size:18px;
    color:#E2E8F0;
    line-height:1.8;
}

.badge{
    display:inline-block;

    background:#4F46E5;

    padding:8px 18px;

    border-radius:30px;

    font-size:14px;

    margin-top:20px;

    font-weight:bold;
}

</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="hero">

<h1>🤖 CareerTwin AI Pro</h1>

<h3>AI Career Intelligence Platform</h3>

<p>

Analyze resumes.

Measure ATS performance.

Identify skill gaps.

Receive AI-powered career recommendations.

Generate learning roadmaps.

Prepare for interviews.

Everything in one intelligent platform.

</p>

<div class="badge">

🚀 Version 2.0

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Supported Roles", "6+")

    with c2:
        st.metric("AI Features", "10+")

    with c3:
        st.metric("Reports", "PDF")

    with c4:
        st.metric("Status", "Active")
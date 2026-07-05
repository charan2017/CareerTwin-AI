import streamlit as st


def hero():

    st.markdown(
        """
<style>

.hero{
    padding:40px;
    border-radius:24px;
    background:linear-gradient(
        135deg,
        #1E3A8A 0%,
        #312E81 50%,
        #0F172A 100%
    );
    border:1px solid #334155;
    color:white;
    box-shadow:0 18px 45px rgba(0,0,0,.35);
    margin-bottom:30px;
}

.hero h1{
    font-size:48px;
    margin-bottom:10px;
    font-weight:700;
}

.hero h3{
    color:#CBD5E1;
    font-size:22px;
    margin-bottom:20px;
}

.hero p{
    color:#E2E8F0;
    font-size:18px;
    line-height:1.8;
}

.hero-features{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top:25px;
}

.feature{
    background:rgba(255,255,255,0.08);
    padding:10px 18px;
    border-radius:25px;
    font-size:14px;
    font-weight:600;
}

.version{
    margin-top:25px;
    display:inline-block;
    padding:10px 18px;
    background:#2563EB;
    border-radius:25px;
    font-weight:600;
}

</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="hero">

<h1>🤖 CareerTwin AI Pro</h1>

<h3>Your AI Career Intelligence Platform</h3>

<p>
Analyze resumes, evaluate ATS compatibility, identify skill gaps,
discover the best career roles, generate personalized learning roadmaps,
and prepare for interviews—all from one intelligent platform.
</p>

<div class="hero-features">
    <div class="feature">📄 Resume Analysis</div>
    <div class="feature">📊 ATS Score</div>
    <div class="feature">🎯 Job Match</div>
    <div class="feature">🚀 Career Readiness</div>
    <div class="feature">🤖 AI Coach</div>
    <div class="feature">🗺 Learning Roadmap</div>
</div>

<div class="version">
Version 3.0
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("### 📈 Platform Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Resume Score", "ATS")

    with c2:
        st.metric("AI Features", "10+")

    with c3:
        st.metric("Reports", "PDF")

    with c4:
        st.metric("Status", "🟢 Stable")
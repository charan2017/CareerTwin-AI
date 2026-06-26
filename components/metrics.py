import streamlit as st


def show_metrics(score, matched, missing, readiness):

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div style="
                background:#1E293B;
                padding:20px;
                border-radius:18px;
                border:1px solid #334155;
                text-align:center;
            ">
                <h4 style="color:#94A3B8;">Resume Score</h4>
                <h1 style="color:#60A5FA;">{score}%</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div style="
                background:#1E293B;
                padding:20px;
                border-radius:18px;
                border:1px solid #334155;
                text-align:center;
            ">
                <h4 style="color:#94A3B8;">Skills Found</h4>
                <h1 style="color:#22C55E;">{len(matched)}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div style="
                background:#1E293B;
                padding:20px;
                border-radius:18px;
                border:1px solid #334155;
                text-align:center;
            ">
                <h4 style="color:#94A3B8;">Missing Skills</h4>
                <h1 style="color:#EF4444;">{len(missing)}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        color = "#22C55E"

        if "Almost" in readiness:
            color = "#FACC15"

        elif "Need" in readiness:
            color = "#EF4444"

        st.markdown(
            f"""
            <div style="
                background:#1E293B;
                padding:20px;
                border-radius:18px;
                border:1px solid #334155;
                text-align:center;
            ">
                <h4 style="color:#94A3B8;">Career Status</h4>
                <h3 style="color:{color};">{readiness}</h3>
            </div>
            """,
            unsafe_allow_html=True,
        )
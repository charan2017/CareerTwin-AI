import streamlit as st


def card(title, value, color, subtitle):

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            border-radius:18px;
            padding:28px;
            border-top:6px solid {color};
            text-align:center;
            box-shadow:0 8px 20px rgba(0,0,0,.25);
            min-height:180px;
        ">

        <h3 style="
            color:#CBD5E1;
            margin-bottom:20px;
            font-size:26px;
        ">
            {title}
        </h3>

        <h1 style="
            color:{color};
            font-size:52px;
            margin:0;
        ">
            {value}
        </h1>

        <p style="
            color:#94A3B8;
            font-size:18px;
            margin-top:15px;
        ">
            {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


def show_metrics(score, matched, missing, readiness):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        if score >= 80:
            subtitle = "Excellent"
        elif score >= 60:
            subtitle = "Good Progress"
        else:
            subtitle = "Needs Work"

        card(
            "📊 Resume Score",
            f"{score}%",
            "#3B82F6",
            subtitle,
        )

    with c2:

        card(
            "✅ Skills",
            len(matched),
            "#22C55E",
            "Detected",
        )

    with c3:

        card(
            "⚠ Missing",
            len(missing),
            "#F59E0B",
            "To Learn",
        )

    with c4:

        if "Job Ready" in readiness:
            color = "#22C55E"
        elif "Almost" in readiness:
            color = "#F59E0B"
        else:
            color = "#EF4444"

        card(
            "🚀 Status",
            readiness,
            color,
            "Career Readiness",
        )
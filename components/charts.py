import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def show_skill_chart(analysis):

    matched = len(analysis["matched"])
    missing = len(analysis["missing"])

    labels = [
        "Matched Skills",
        "Missing Skills"
    ]

    values = [
        matched,
        missing
    ]

    colors = [
        "#22C55E",
        "#EF4444"
    ]

    fig = px.pie(
        names=labels,
        values=values,
        hole=0.65,
        color=labels,
        color_discrete_sequence=colors
    )

    fig.update_layout(

        title="Skill Distribution",

        paper_bgcolor="#0F172A",

        plot_bgcolor="#0F172A",

        font=dict(
            color="white",
            size=16
        ),

        legend=dict(
            orientation="h",
            y=-0.2
        ),

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        height=420
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


def show_bar_chart(analysis):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Matched", "Missing"],

            y=[
                len(analysis["matched"]),
                len(analysis["missing"])
            ],

            marker_color=[
                "#22C55E",
                "#EF4444"
            ]

        )

    )

    fig.update_layout(

        title="Skill Comparison",

        paper_bgcolor="#0F172A",

        plot_bgcolor="#0F172A",

        font=dict(color="white"),

        height=420
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )


def show_dashboard(analysis):

    left, right = st.columns(2)

    with left:

        show_skill_chart(analysis)

    with right:

        show_bar_chart(analysis)
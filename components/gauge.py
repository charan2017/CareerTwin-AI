import streamlit as st
import plotly.graph_objects as go


def show_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,

            title={
                "text": "<b>ATS Score</b>",
                "font": {
                    "size": 26
                }
            },

            number={
                "suffix": "%",
                "font": {
                    "size": 44
                }
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#4F46E5"
                },

                "bgcolor": "#0F172A",

                "borderwidth": 2,

                "bordercolor": "#334155",

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#DC2626"
                    },

                    {
                        "range": [40, 70],
                        "color": "#F59E0B"
                    },

                    {
                        "range": [70, 100],
                        "color": "#22C55E"
                    }

                ]
            }

        )
    )

    fig.update_layout(

        paper_bgcolor="#0F172A",

        font={
            "color": "white"
        },

        height=380,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    st.plotly_chart(
        fig,
        width="stretch"
    )
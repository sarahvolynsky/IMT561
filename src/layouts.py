import pandas as pd
import streamlit as st
import plotly.express as px

from src.charts import plot_response_hist, plot_borough_bar


def header_metrics(df: pd.DataFrame) -> None:
    """Rendering header metrics. Placeholder values are intentional."""
    c1, c2, c3 = st.columns(3)

    # TODO (IN-CLASS): Replace these placeholders with real metrics from df
    # Suggestions:
    # - Total complaints (len(df))
    # - Median response time
    # - % from Web vs Phone vs App (pick one)

    total = len(df)
    median_rt = df["response_time_days"].median() if total else 0
    most_common = (
        df["complaint_type"].mode().iloc[0]
        if total and not df["complaint_type"].dropna().empty
        else "—"
    )
    with c1:
        st.metric("Total complaints", f"{total:,}")

    with c2:
        st.metric("Median response (days)", f"{median_rt:.2f}")

    with c3:
        st.metric("Most common complaint", most_common)


def body_layout_tabs(df: pd.DataFrame) -> None:
    """Tabs layout with 3 default tabs."""
    t1, t2, t3 = st.tabs(["Distribution", "By Borough", "Table"])

    with t1:
        st.subheader("Response Time Distribution")
        plot_response_hist(df)
        st.caption(
            "Most requests are resolved within a few days, but there are occasional long-response outliers."
        )

        # TODO (IN-CLASS): Add a short interpretation sentence under the chart

    with t2:
        st.subheader("Median Response Time by Borough")
        plot_borough_bar(df)
        st.caption(
            "Median response time varies across boroughs, suggesting differences in workload or operational efficiency."
        )

        st.subheader("Number of Complaints by Borough")
        count_df = (
            df.groupby("borough")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
        )

        fig = px.bar(count_df, x="borough", y="count", title=None)
        st.plotly_chart(fig, use_container_width=True)

        st.caption(
            "Brooklyn and Queens tend to generate the highest volume of complaints in this sample."
        )

    with t3:
        st.subheader("Filtered Rows")
        st.dataframe(df, use_container_width=True, height=480)

        csv_bytes = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download filtered data as CSV",
            data=csv_bytes,
            file_name="filtered_311_data.csv",
            mime="text/csv",
        )
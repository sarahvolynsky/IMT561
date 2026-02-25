NYC 311 Mini Dashboard (IMT 561)
Overview

This Streamlit dashboard explores a sample NYC 311 dataset to analyze complaint patterns, response times, and borough-level trends. The app allows users to filter the data and interact with coordinated visualizations in real time.

Intended Audience

This dashboard is designed for:

City operations managers

Policy analysts

Data analysts

Students exploring public service datasets

The tool helps stakeholders quickly identify trends in complaint volume and response performance.

Key Tasks Users Can Perform

Users can:

Filter complaints by borough, channel, complaint type, and response time range

View distribution of response times

Compare median response times across boroughs

Analyze complaint volume by borough

Inspect filtered records in a table

Download filtered results as a CSV

Questions This Dashboard Helps Answer

Which boroughs have longer median response times?

What types of complaints are most common?

How does complaint volume vary across boroughs?

Are there extreme response time outliers?

How to Run Locally
pip install -r requirements.txt
streamlit run app.py****

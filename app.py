import streamlit as st
import os
import pandas as pd
import re
import plotly.express as px
from io import StringIO
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

engine_llm = LLM(
    model="groq/llama-3.3-70b-versatile", 
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1
)

st.set_page_config(page_title="Aegis BI | Elite Engine", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FDF5E6; }
    .main .block-container { padding-top: 0rem !important; margin-top: -65px !important; }
    h1 { color: #5D4037 !important; font-family: 'Segoe UI', sans-serif; font-weight: 800; font-size: 28px !important; }
    h2 { color: #8B4513 !important; font-family: 'Segoe UI', sans-serif; font-weight: 700; font-size: 22px !important; margin-bottom: 10px; }
    .insight-card { background-color: #FFF9F0; padding: 20px; border-left: 5px solid #D4AF37; border-top: 1px solid #E5D3B3; margin-bottom: 20px; font-weight: 500; font-size: 15px; color: #5D4037; line-height: 1.8; }
    .stButton>button { 
        background-color: #D4AF37 !important; 
        color: #FFFFFF !important; 
        font-weight: 700; 
        height: 48px; 
        border-radius: 6px; 
        border: none;
        transition: all 0.3s ease-in-out !important;
    }
    .stButton>button:hover { 
        background-color: #8B4513 !important; 
        color: #FDF5E6 !important;
        box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
        border: 1px solid #D4AF37 !important;
    }
    .sidebar-text { font-size: 14px; font-weight: 700; color: #8B4513; margin-top: 25px; margin-bottom: 10px; }
    hr { border: 0; height: 1px; background-image: linear-gradient(to right, rgba(212, 175, 55, 0), rgba(212, 175, 55, 0.75), rgba(212, 175, 55, 0)); margin: 20px 0; }
    .metric-box { background-color: #FFF9F0; padding: 15px; border-radius: 8px; border-left: 4px solid #D4AF37; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

if 'vault' not in st.session_state: st.session_state.vault = {}
if 'page' not in st.session_state: st.session_state.page = "MAIN"

with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #D4AF37;'>AEGIS ARCHITECT</h2>", unsafe_allow_html=True)
    if st.button("NEW ANALYSIS"): st.session_state.page = "MAIN"
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown('<p class="sidebar-text">PREVIOUS RESEARCH</p>', unsafe_allow_html=True)
    for key in list(st.session_state.vault.keys()):
        display_label = " ".join(key.split()[:2]) + " ...."
        if st.button(display_label, key=key): st.session_state.page = key

if st.session_state.page == "MAIN":
    st.markdown("<h1>AEGIS BI LIGHTNING ENGINE</h1>", unsafe_allow_html=True)
    query = st.text_input("TARGET DOMAIN (2026):", placeholder="e.g., AgriTech in Tamil Nadu")
    
    if st.button("EXECUTE FAST SYNTHESIS"):
        if query:
            with st.spinner("Synthesizing Content and Architecture..."):
                try:
                    master_agent = Agent(
                        role='Elite BI Data Architect',
                        goal=f'Provide 4 brief bullet points followed by a dense, un-truncated 40-row dataset for {query}.',
                        backstory='Senior Architect at Zoho. You are a master of raw data generation. You never use ellipses or truncate rows. You explicitly print all 40 unique data rows sequentially without adding icons or emojis.',
                        llm=engine_llm
                    )

                    t1 = Task(
                        description=f'''Mandatory Execution for {query}:
                        1. Provide exactly 4 concise, high-level business analytics observations without any special icons or emojis.
                        2. Print the exact separator token: ###DATA###
                        3. Generate exactly 40 distinct, comprehensive rows of valid CSV data. 
                        
                        Columns: Category, Entity_Name, Metric, Investment_Cr, Growth_Rate_%
                        Ensure Entity_Name contains 40 explicit, non-duplicated operational entries matching the geography or scope of {query}. Do not summarize or stop early.''',
                        expected_output='Brief observations followed by marker and a complete 40-row CSV table.',
                        agent=master_agent
                    )

                    crew = Crew(agents=[master_agent], tasks=[t1], process=Process.sequential)
                    result = crew.kickoff()

                    raw_output = str(result.raw)
                    if "###DATA###" in raw_output:
                        text_part, csv_part = raw_output.split("###DATA###")
                        insights = text_part.strip()
                        clean_csv = csv_part.replace('```csv', '').replace('```', '').strip()
                        
                        df = pd.read_csv(StringIO(clean_csv))
                        
                        if "Tamil Nadu" in query or "TN" in query:
                            df = df[~df['Entity_Name'].str.contains('Thiruvananthapuram|Kochi|Kerala|Bangalore|Hyderabad', case=False, na=False)]
                        
                        df['Investment_Cr'] = pd.to_numeric(df['Investment_Cr'], errors='coerce').abs().fillna(120)
                        df['Growth_Rate_%'] = pd.to_numeric(df['Growth_Rate_%'], errors='coerce').fillna(10.5)
                        df['Category'] = df['Category'].str.strip()
                        df = df.sort_values(by='Category', ascending=False)
                        
                        df['Performance_Index'] = df.groupby('Category')['Investment_Cr'].transform(
                            lambda x: (((x - x.min()) / (x.max() - x.min())) * 60 + 40).round(1) if (x.max() != x.min()) else 82.5
                        ).fillna(82.5)

                        st.session_state.vault[query] = {'insights': insights, 'df': df}
                        st.session_state.page = query
                        st.rerun()
                    else:
                        st.error("Sequence Marker Missing. Retrying pipeline...")
                except Exception as e:
                    st.error(f"Engine Log: {e}")
else:
    data = st.session_state.vault[st.session_state.page]
    st.markdown(f"<h2>REPORT: {st.session_state.page.upper()}</h2>", unsafe_allow_html=True)
    
    df = data['df']
    
    st.markdown("<h2 style='color: #8B4513;'>INTERACTIVE POWER DASHBOARD</h2>", unsafe_allow_html=True)
    
    c_layout1, c_layout2 = st.columns(2)
    with c_layout1:
        fig_bar = px.bar(
            df, x="Entity_Name", y="Investment_Cr",
            color="Category", title="Capital Architecture Deployment Map",
            color_discrete_sequence=px.colors.sequential.YlOrBr
        )
        fig_bar.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_bar, use_container_width=True)
        
        df_line = df.sort_values(by="Growth_Rate_%")
        fig_line = px.line(
            df_line, x="Entity_Name", y="Growth_Rate_%",
            title="Growth Velocity Horizon Trend Analysis",
            markers=True, color_discrete_sequence=["#8B4513"]
        )
        fig_line.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_line, use_container_width=True)
        
    with c_layout2:
        fig_pie = px.pie(
            df, names="Category", values="Investment_Cr",
            title="Resource Distribution Allocation Profile",
            hole=0.4, color_discrete_sequence=px.colors.sequential.YlOrRd
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
        fig_scatter = px.scatter(
            df, x="Investment_Cr", y="Growth_Rate_%",
            size="Performance_Index", color="Category",
            title="Capital vs Momentum Correlation Matrix",
            hover_name="Entity_Name", color_discrete_sequence=px.colors.sequential.YlOrBr[3:]
        )
        fig_scatter.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    st.markdown("<hr>", unsafe_allow_html=True)
    
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.markdown(f'<div class="metric-box"><span style="color: #8B4513; font-weight:700;">TOTAL ENTERPRISE ASSETS</span><br><h2 style="margin:5px 0;">{len(df)} Units</h2></div>', unsafe_allow_html=True)
    with m_col2:
        st.markdown(f'<div class="metric-box"><span style="color: #8B4513; font-weight:700;">AGGREGATE CAPITAL</span><br><h2 style="margin:5px 0;">An ₹ {df["Investment_Cr"].sum():,.1f} Cr</h2></div>', unsafe_allow_html=True)
    with m_col3:
        st.markdown(f'<div class="metric-box"><span style="color: #8B4513; font-weight:700;">PEAK MOMENTUM</span><br><h2 style="margin:5px 0;">{df["Growth_Rate_%"].max()}%</h2></div>', unsafe_allow_html=True)
    with m_col4:
        st.markdown(f'<div class="metric-box"><span style="color: #8B4513; font-weight:700;">MEAN PERFORMANCE</span><br><h2 style="margin:5px 0;">{df["Performance_Index"].mean():.1f}</h2></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    if data['insights']:
        st.markdown("<h3 style='color: #8B4513;'>STRATEGIC INSIGHTS</h3>", unsafe_allow_html=True)
        st.markdown('<div class="insight-card">' + data['insights'] + '</div>', unsafe_allow_html=True)
        
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #8B4513;'>MASTER ENTERPRISE DATASET</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button(label="DOWNLOAD LOAD-READY CSV", data=df.to_csv(index=False), file_name=f"aegis_master.csv", mime="text/csv")

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Global Tech Ecosystem Explorer",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        padding-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('global_tech_ecosystem_data.csv')
    return df

df = load_data()

# Header
st.markdown('<div class="main-header">🌍 Global Tech Ecosystem Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Interactive Visualization of Global Technology Ecosystems Based on Open Data</div>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Region filter
regions = ['All'] + sorted(df['Region'].unique().tolist())
selected_region = st.sidebar.multiselect(
    "Select Region(s)",
    options=regions[1:],
    default=regions[1:]
)

# Sector filter
sectors = ['All'] + sorted(df['Sector'].unique().tolist())
selected_sector = st.sidebar.multiselect(
    "Select Sector(s)",
    options=sectors[1:],
    default=sectors[1:]
)

# Ecosystem score range
min_score, max_score = st.sidebar.slider(
    "Ecosystem Score Range",
    min_value=int(df['Ecosystem_Score'].min()),
    max_value=int(df['Ecosystem_Score'].max()),
    value=(int(df['Ecosystem_Score'].min()), int(df['Ecosystem_Score'].max()))
)

# Apply filters
filtered_df = df.copy()
if selected_region:
    filtered_df = filtered_df[filtered_df['Region'].isin(selected_region)]
if selected_sector:
    filtered_df = filtered_df[filtered_df['Sector'].isin(selected_sector)]
filtered_df = filtered_df[
    (filtered_df['Ecosystem_Score'] >= min_score) & 
    (filtered_df['Ecosystem_Score'] <= max_score)
]

# Key metrics
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Dataset Overview")
st.sidebar.metric("Total Cities", len(filtered_df['City'].unique()))
st.sidebar.metric("Total Sectors", len(filtered_df['Sector'].unique()))
st.sidebar.metric("Total Records", len(filtered_df))

# Main content area
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Overview", 
    "📈 Ecosystem Rankings", 
    "💰 Funding Analysis",
    "🎯 Sector Distribution",
    "🔬 Advanced Analytics"
])

# TAB 1: Overview
with tab1:
    st.header("Ecosystem Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_startups = filtered_df['Number_of_Startups'].sum()
        st.metric("Total Startups", f"{total_startups:,.0f}")

    with col2:
        total_funding = filtered_df['Total_Funding_M_USD'].sum()
        st.metric("Total Funding", f"${total_funding:,.0f}M")

    with col3:
        avg_growth = filtered_df['YoY_Growth_Rate'].mean()
        st.metric("Avg Growth Rate", f"{avg_growth:.1%}")

    with col4:
        avg_ecosystem_score = filtered_df['Ecosystem_Score'].mean()
        st.metric("Avg Ecosystem Score", f"{avg_ecosystem_score:.1f}")

    st.markdown("---")

    # World map visualization
    st.subheader("🗺️ Global Distribution by Region")

    region_summary = filtered_df.groupby('Region').agg({
        'Number_of_Startups': 'sum',
        'Total_Funding_M_USD': 'sum',
        'Ecosystem_Score': 'mean'
    }).reset_index()

    fig_map = px.treemap(
        region_summary,
        path=['Region'],
        values='Number_of_Startups',
        color='Ecosystem_Score',
        color_continuous_scale='Viridis',
        title='Ecosystem Distribution by Region (Size = Number of Startups, Color = Ecosystem Score)'
    )
    fig_map.update_layout(height=500)
    st.plotly_chart(fig_map, use_container_width=True)

    # City comparison
    st.subheader("🏙️ Top 10 Cities by Ecosystem Score")

    city_scores = filtered_df.groupby('City')['Ecosystem_Score'].mean().sort_values(ascending=False).head(10)

    fig_cities = px.bar(
        x=city_scores.index,
        y=city_scores.values,
        labels={'x': 'City', 'y': 'Average Ecosystem Score'},
        title='Top Performing Cities',
        color=city_scores.values,
        color_continuous_scale='Blues'
    )
    fig_cities.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_cities, use_container_width=True)

# TAB 2: Ecosystem Rankings
with tab2:
    st.header("Ecosystem Rankings & Comparisons")

    # Multi-dimensional comparison
    st.subheader("📊 Multi-Dimensional Ecosystem Analysis")

    city_metrics = filtered_df.groupby('City').agg({
        'Ecosystem_Score': 'mean',
        'Talent_Pool_Score': 'mean',
        'Market_Reach_Score': 'mean',
        'Funding_Accessibility_Score': 'mean',
        'Number_of_Startups': 'sum'
    }).reset_index()

    fig_scatter = px.scatter(
        city_metrics,
        x='Talent_Pool_Score',
        y='Funding_Accessibility_Score',
        size='Number_of_Startups',
        color='Ecosystem_Score',
        hover_name='City',
        hover_data={
            'Talent_Pool_Score': ':.1f',
            'Funding_Accessibility_Score': ':.1f',
            'Ecosystem_Score': ':.1f',
            'Number_of_Startups': ':,.0f'
        },
        title='Talent Pool vs Funding Accessibility (Size = Number of Startups)',
        labels={
            'Talent_Pool_Score': 'Talent Pool Score',
            'Funding_Accessibility_Score': 'Funding Accessibility Score'
        },
        color_continuous_scale='Plasma'
    )
    fig_scatter.update_layout(height=500)
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Radar chart for selected city
    st.subheader("🎯 Detailed City Profile")

    selected_city = st.selectbox("Select a city for detailed analysis:", sorted(filtered_df['City'].unique()))

    city_data = filtered_df[filtered_df['City'] == selected_city].groupby('City').agg({
        'Ecosystem_Score': 'mean',
        'Talent_Pool_Score': 'mean',
        'Market_Reach_Score': 'mean',
        'Funding_Accessibility_Score': 'mean',
        'YoY_Growth_Rate': 'mean'
    }).reset_index()

    categories = ['Ecosystem Score', 'Talent Pool', 'Market Reach', 'Funding Access', 'Growth Rate (×100)']
    values = [
        city_data['Ecosystem_Score'].values[0],
        city_data['Talent_Pool_Score'].values[0],
        city_data['Market_Reach_Score'].values[0],
        city_data['Funding_Accessibility_Score'].values[0],
        city_data['YoY_Growth_Rate'].values[0] * 100
    ]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=selected_city
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        title=f'{selected_city} Ecosystem Profile',
        height=450
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# TAB 3: Funding Analysis
with tab3:
    st.header("Funding Analysis")

    col1, col2 = st.columns(2)

    with col1:
        # Funding by sector
        st.subheader("💵 Total Funding by Sector")
        sector_funding = filtered_df.groupby('Sector')['Total_Funding_M_USD'].sum().sort_values(ascending=False)

        fig_sector_funding = px.pie(
            values=sector_funding.values,
            names=sector_funding.index,
            title='Distribution of Total Funding Across Sectors',
            hole=0.4
        )
        fig_sector_funding.update_layout(height=400)
        st.plotly_chart(fig_sector_funding, use_container_width=True)

    with col2:
        # Average funding per startup
        st.subheader("📊 Avg Funding per Startup")
        avg_funding_sector = filtered_df.groupby('Sector')['Avg_Funding_Per_Startup_M'].mean().sort_values(ascending=False)

        fig_avg_funding = px.bar(
            x=avg_funding_sector.index,
            y=avg_funding_sector.values,
            labels={'x': 'Sector', 'y': 'Average Funding (M USD)'},
            title='Average Funding per Startup by Sector',
            color=avg_funding_sector.values,
            color_continuous_scale='Greens'
        )
        fig_avg_funding.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig_avg_funding, use_container_width=True)

    # Funding vs Growth
    st.subheader("📈 Funding vs Growth Rate Analysis")

    city_funding_growth = filtered_df.groupby('City').agg({
        'Total_Funding_M_USD': 'sum',
        'YoY_Growth_Rate': 'mean',
        'Region': 'first'
    }).reset_index()

    fig_funding_growth = px.scatter(
        city_funding_growth,
        x='Total_Funding_M_USD',
        y='YoY_Growth_Rate',
        color='Region',
        size='Total_Funding_M_USD',
        hover_name='City',
        title='Total Funding vs Growth Rate by City',
        labels={
            'Total_Funding_M_USD': 'Total Funding (M USD)',
            'YoY_Growth_Rate': 'Year-over-Year Growth Rate'
        }
    )
    fig_funding_growth.update_layout(height=500)
    st.plotly_chart(fig_funding_growth, use_container_width=True)

# TAB 4: Sector Distribution
with tab4:
    st.header("Sector Distribution Analysis")

    # Startup distribution by sector
    st.subheader("🏢 Number of Startups by Sector")

    sector_startups = filtered_df.groupby('Sector')['Number_of_Startups'].sum().sort_values(ascending=False)

    fig_sector_startups = px.bar(
        x=sector_startups.index,
        y=sector_startups.values,
        labels={'x': 'Sector', 'y': 'Number of Startups'},
        title='Total Startups Across Sectors',
        color=sector_startups.values,
        color_continuous_scale='Rainbow'
    )
    fig_sector_startups.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_sector_startups, use_container_width=True)

    # Heatmap: City vs Sector
    st.subheader("🔥 City-Sector Ecosystem Score Heatmap")

    heatmap_data = filtered_df.pivot_table(
        values='Ecosystem_Score',
        index='City',
        columns='Sector',
        aggfunc='mean'
    )

    fig_heatmap = px.imshow(
        heatmap_data,
        labels=dict(x="Sector", y="City", color="Ecosystem Score"),
        title="Ecosystem Scores Across Cities and Sectors",
        color_continuous_scale='RdYlGn',
        aspect="auto"
    )
    fig_heatmap.update_layout(height=600)
    st.plotly_chart(fig_heatmap, use_container_width=True)

# TAB 5: Advanced Analytics
with tab5:
    st.header("Advanced Analytics")

    # Correlation analysis
    st.subheader("🔗 Correlation Analysis")

    correlation_data = filtered_df[[
        'Ecosystem_Score', 'Talent_Pool_Score', 'Market_Reach_Score',
        'Funding_Accessibility_Score', 'YoY_Growth_Rate', 'Number_of_Startups'
    ]].corr()

    fig_corr = px.imshow(
        correlation_data,
        labels=dict(color="Correlation"),
        title="Correlation Matrix of Ecosystem Metrics",
        color_continuous_scale='RdBu_r',
        zmin=-1, zmax=1,
        text_auto='.2f'
    )
    fig_corr.update_layout(height=600)
    st.plotly_chart(fig_corr, use_container_width=True)

    # Regional comparison
    st.subheader("🌍 Regional Performance Comparison")

    regional_comparison = filtered_df.groupby('Region').agg({
        'Ecosystem_Score': 'mean',
        'Number_of_Startups': 'sum',
        'Total_Funding_M_USD': 'sum',
        'YoY_Growth_Rate': 'mean',
        'Talent_Pool_Score': 'mean'
    }).reset_index()

    fig_regional = go.Figure()

    metrics = ['Ecosystem_Score', 'Talent_Pool_Score', 'YoY_Growth_Rate']
    metric_names = ['Ecosystem Score', 'Talent Pool Score', 'Growth Rate (×100)']

    for i, (metric, name) in enumerate(zip(metrics, metric_names)):
        values = regional_comparison[metric].values
        if metric == 'YoY_Growth_Rate':
            values = values * 100

        fig_regional.add_trace(go.Bar(
            name=name,
            x=regional_comparison['Region'],
            y=values,
            text=np.round(values, 2),
            textposition='auto'
        ))

    fig_regional.update_layout(
        title='Regional Performance Metrics Comparison',
        barmode='group',
        height=500,
        xaxis_title='Region',
        yaxis_title='Score / Rate'
    )
    st.plotly_chart(fig_regional, use_container_width=True)

    # Data table
    st.subheader("📋 Filtered Data Table")
    st.dataframe(
        filtered_df.style.background_gradient(subset=['Ecosystem_Score'], cmap='Greens'),
        use_container_width=True,
        height=400
    )

    # Download option
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_ecosystem_data.csv',
        mime='text/csv',
    )

# Footer
st.markdown("---")
st.markdown("""
### About This Project
This Interactive Global Tech Ecosystem Explorer visualizes open entrepreneurial ecosystem data to help:
- **Founders** discover optimal locations and sectors for startup formation
- **Investors** identify high-potential markets and emerging trends
- **Policymakers** understand ecosystem strengths and improvement areas

**Data Transparency:** This visualization uses synthetic open data modeled after global ecosystem reports. 
All methodology, filtering logic, and visualization choices are documented in the open-source repository.

**Tech Stack:** Python • Streamlit • Plotly • Pandas • NumPy

**Creator:** Md. Sohan Mahmud | Duke Kunshan University | INFOSCI 301 Final Project

**License:** MIT Open Source
""")

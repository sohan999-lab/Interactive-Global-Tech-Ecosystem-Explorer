# 🚀 Quick Start Guide

## Running the Application Locally

### Option 1: Automated Setup (Recommended)

**For Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
streamlit run app.py
```

**For Windows:**
```bash
setup.bat
venv\Scripts\activate.bat
streamlit run app.py
```

### Option 2: Manual Setup

1. **Install Python dependencies**
```bash
pip install streamlit pandas plotly numpy
```

2. **Run the application**
```bash
streamlit run app.py
```

3. **Open your browser**
- Navigate to: http://localhost:8501
- The dashboard should load automatically

## 📱 Using the Dashboard

### Sidebar Filters
- **Region Filter:** Select one or more regions to focus on
- **Sector Filter:** Choose specific technology sectors
- **Ecosystem Score Range:** Set minimum/maximum thresholds

### Navigation Tabs

**🌍 Overview Tab**
- View global distribution treemap
- See top 10 cities by ecosystem score
- Check key aggregate metrics

**📈 Ecosystem Rankings Tab**
- Compare talent pool vs funding accessibility
- Analyze individual city profiles with radar charts
- Identify ecosystem strengths and weaknesses

**💰 Funding Analysis Tab**
- Explore sector-wise funding distribution
- Compare average funding per startup
- Analyze funding vs growth correlations

**🎯 Sector Distribution Tab**
- View startup counts across sectors
- Examine city-sector performance heatmaps
- Identify sector concentration patterns

**🔬 Advanced Analytics Tab**
- Study correlation matrices
- Compare regional performance metrics
- Download filtered data for further analysis

## 🎯 Common Use Cases

### Finding the Best City for Your Startup
1. Go to **Ecosystem Rankings** tab
2. Select your sector in the sidebar
3. Compare cities using the scatter plot
4. Check detailed profiles with radar charts

### Identifying Investment Opportunities
1. Go to **Funding Analysis** tab
2. Filter by high-growth regions
3. Look for sectors with high funding vs growth correlation
4. Cross-reference with talent pool availability

### Benchmarking Ecosystems
1. Go to **Advanced Analytics** tab
2. Select regions to compare
3. View regional performance comparison chart
4. Download data for deeper analysis

## ⚠️ Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found Errors
Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

### Browser Doesn't Open Automatically
Manually navigate to:
```
http://localhost:8501
```

## 📊 Data Notes

- Dataset contains **160 records** (20 cities × 8 sectors)
- Scores range from 0-100
- Funding amounts in millions USD
- Growth rates shown as decimals (0.15 = 15%)

## 🔄 Updating the Application

To pull the latest changes:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
streamlit run app.py
```

## 📧 Need Help?

If you encounter issues:
1. Check the main README.md for detailed documentation
2. Review error messages in the terminal
3. Ensure all dependencies are installed correctly
4. Contact the project maintainer

---

**Happy Exploring! 🌍**

# 🌍 Interactive Global Tech Ecosystem Explorer

An open-source interactive visualization tool for exploring global technology ecosystems, startup distributions, funding patterns, and entrepreneurial opportunities across cities, regions, and sectors.

## 🎯 Project Overview

This project addresses the critical need for transparent, accessible visualization of global entrepreneurial ecosystems. By providing interactive data exploration tools, it helps founders, investors, and policymakers make informed decisions about startup formation, investment strategies, and ecosystem development.

## ✨ Features

### 📊 Five Major Analysis Modules

1. **Ecosystem Overview**
   - Global distribution treemap by region
   - Top 10 cities by ecosystem score
   - Key metrics dashboard (total startups, funding, growth rate)

2. **Ecosystem Rankings**
   - Multi-dimensional scatter analysis (Talent Pool vs Funding Accessibility)
   - Radar chart profiles for detailed city analysis
   - Interactive city comparison tools

3. **Funding Analysis**
   - Sector-wise funding distribution (pie chart)
   - Average funding per startup by sector
   - Funding vs growth rate correlation analysis

4. **Sector Distribution**
   - Startup count across sectors
   - City-Sector ecosystem heatmap
   - Cross-sector performance comparison

5. **Advanced Analytics**
   - Correlation matrix of ecosystem metrics
   - Regional performance comparison
   - Filterable data table with download functionality

### 🔍 Interactive Filtering

- **Region Filter:** Select single or multiple regions
- **Sector Filter:** Focus on specific technology sectors
- **Ecosystem Score Range:** Filter by minimum quality threshold
- Real-time visualization updates

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd global-tech-ecosystem-explorer
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the dashboard**
Open your browser and navigate to:
```
http://localhost:8501
```

## 📁 Project Structure

```
global-tech-ecosystem-explorer/
│
├── app.py                              # Main Streamlit application
├── global_tech_ecosystem_data.csv      # Dataset (160 records)
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── Adjustments                         # Create your file/branch for contributions
```

## 📊 Dataset Description

**Source:** Synthetic open data modeled after Dealroom.co Global Tech Ecosystem Index structure

**Coverage:**
- **20 Cities** across 4 regions (North America, Europe, Asia, Middle East)
- **8 Technology Sectors** (Fintech, AI/ML, SaaS, E-commerce, HealthTech, CleanTech, EdTech, Blockchain)
- **160 Total Records** (City × Sector combinations)

**Metrics:**
- Ecosystem Score (0-100)
- Number of Startups
- Total Funding (M USD)
- Average Funding per Startup
- Year-over-Year Growth Rate
- Talent Pool Score
- Market Reach Score
- Funding Accessibility Score

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | Streamlit 1.29.0 |
| **Data Processing** | Pandas 2.1.3 |
| **Visualization** | Plotly 5.18.0 |
| **Numerical Computing** | NumPy 1.26.2 |
| **Language** | Python 3.8+ |

## 🎨 Visualization Types

- **Treemap:** Regional distribution overview
- **Bar Charts:** City rankings, sector comparisons
- **Scatter Plots:** Multi-dimensional correlations
- **Radar Charts:** Individual city profiles
- **Pie Charts:** Funding distribution
- **Heatmaps:** City-sector performance matrices
- **Correlation Matrix:** Metric relationships
- **Grouped Bar Charts:** Regional comparisons

## 🌟 Use Cases

### For Entrepreneurs
- Discover optimal cities for startup formation based on sector
- Compare ecosystem strengths across regions
- Identify funding accessibility patterns

### For Investors
- Spot high-potential markets with strong growth rates
- Analyze sector-specific investment trends
- Evaluate talent pool availability

### For Policymakers
- Benchmark local ecosystems against global leaders
- Identify areas for improvement (talent, funding, market reach)
- Track ecosystem development over time

### For Researchers
- Study correlations between ecosystem factors
- Analyze regional entrepreneurship patterns
- Generate insights for academic publications

## 🔬 Academic Context

**Course:** INFOSCI 301 - Information Visualization  
**Institution:** Duke Kunshan University  
**Semester:** Fall 2025  

**Learning Objectives Met:**
- Open-source project development
- Interactive data visualization design
- User-centered interface principles
- Transparent data governance practices
- Community-focused tool creation

## 📖 Data Governance & Ethics

**Transparency Principles:**
- All data sources documented
- Methodology clearly explained
- Filtering logic visible to users
- Synthetic data clearly labeled

**Accessibility:**
- Responsive design for all screen sizes
- Color-blind friendly palettes
- Clear labeling and legends
- Download functionality for further analysis

**Open Source:**
- MIT License
- Full code availability
- Community contributions welcome
- Educational use encouraged

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

**Areas for contribution:**
- Additional visualization types
- Enhanced filtering options
- Real-time data integration
- Mobile optimization
- Multi-language support

## 📧 Contact

**Creator:** Md. Sohan Mahmud  
**Institution:** Duke Kunshan University  
**Course:** INFOSCI 301 - Information Visualization  
**Email:** mdsohan.mahmud@duke.edu  
**GitHub:** https://github.com/sohan999-lab

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Md. Sohan Mahmud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- Inspired by Dealroom.co Global Tech Ecosystem Index
- Built as part of INFOSCI 301 curriculum
- Thanks to Professor Luyao Zhang for guidance
- Data visualization best practices from Edward Tufte and Ben Shneiderman

## 🔮 Future Enhancements

- [ ] Real-time data integration from public APIs
- [ ] Machine learning predictions for ecosystem trends
- [ ] Social network analysis of founder connections
- [ ] Temporal analysis (multi-year comparisons)
- [ ] Export visualizations as high-resolution images
- [ ] Collaborative annotation features
- [ ] API endpoint for programmatic access

---

**⭐ If you find this project useful, please consider starring the repository!**

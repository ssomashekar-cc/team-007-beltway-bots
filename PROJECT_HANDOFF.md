# Sea Turtle Impact Analysis Platform

## Project Handoff Document

## Project Overview

The Sea Turtle Impact Analysis Platform is a Streamlit-based web application designed to help communities, advocacy groups, local governments, and tourism stakeholders understand how local policies and regulations impact both sea turtle conservation efforts and local economic outcomes.

The platform will compare municipalities against a designated "gold standard" municipality, Melbourne Beach, Florida, and provide insights into policy differences, potential environmental impacts, and tourism-related economic implications.

> **Data scope note (per data team):** Target municipalities for comparison against the Melbourne Beach gold standard are limited to municipalities within **Broward County, Florida**.

## Problem Statement

Provide stakeholders with the ability to:

- Understand local laws and environmental conditions affecting sea turtles.
- Educate community members on the relationship between conservation policies, turtle populations, and tourism outcomes.
- Recommend policy changes by comparing a target municipality against a proven "gold standard" municipality.

The long-term vision includes allowing users to simulate policy changes and estimate potential impacts on both turtle conservation and local tourism.

## Stakeholders

### Primary Stakeholders

- Community members
- Sea turtle advocates
- Environmental organizations
- Chamber of Commerce
- Tourism boards
- Local businesses
- Residents concerned with local economic stability
- Ecotourism supporters

### Secondary Stakeholders

- Municipal governments
- City council members
- Policy makers
- Conservation funding organizations

## Application Goals

The application is organized around three major user journeys:

### 1. Understand

Help users understand the current state of a municipality.

**Data to Display**

*Legal Data*
- Wildlife protection laws
- Turtle protection ordinances
- Dark sky ordinances
- Lighting restrictions
- Noise ordinances
- Beach access regulations

*Community Data*
- Population
- Population growth
- Demographics
- Tourism statistics
- Conservation spending

*Environmental Data*
- Turtle nesting counts
- Historical turtle populations
- Beach characteristics
- Vehicle access policies
- Bicycle access policies
- Beach access hours

**Deliverable**

Generate an AI-created summary describing:

- The municipality
- Existing conservation laws
- Tourism environment
- Strengths and weaknesses

### 2. Educate

Help users visualize conservation and economic trends.

**Visualizations**

*Turtle Metrics*
- Nest count trends
- Population trends
- Historical activity

*Tourism Metrics*
- Visitor counts
- Tourism revenue
- Seasonal trends

*Community Metrics*
- Population growth
- Census trends

**Comparison View**

Display side-by-side comparisons between:

- Target Municipality
- vs Melbourne Beach, FL

### 3. Recommend

Help decision makers determine possible policy changes.

**Legal Comparison**

Compare:

- Target Municipality Laws
- vs Melbourne Beach Laws

Identify:

- Laws that match
- Laws that differ
- Missing protections
- Additional restrictions

**Recommendations**

Provide AI-generated recommendations explaining:

- Potential conservation benefits
- Possible tourism impacts
- Alignment with best practices

## MVP Scope

The MVP should focus on demonstrating the end-to-end workflow.

### Included

- ✅ Municipality selection
- ✅ Melbourne Beach comparison
- ✅ Dashboard visualizations
- ✅ AI-generated municipality summaries
- ✅ AI legal comparison
- ✅ Recommendation generation
- ✅ Mock policy simulation

### Excluded

- ❌ Forecasting models
- ❌ Detailed economic modeling
- ❌ Automated data pipelines
- ❌ Nationwide municipality comparisons
- ❌ GIS mapping
- ❌ Real-time data ingestion

## Technical Architecture

### Frontend

**Streamlit**

Provides:

- User interface
- Dashboard visualization
- Interactive controls
- Scenario simulation

### AI Layer

**Azure OpenAI**

Used for:

*Municipality Summaries*

Generate plain-English explanations of:

- Laws
- Environmental conditions
- Community characteristics

*Legal Comparison*

Compare ordinances and identify:

- Similarities
- Differences
- Missing protections

*Recommendations*

Generate policy recommendations and explain impacts.

### Data Storage

**Azure Database for PostgreSQL**

Structured data:

- Municipalities
- Census statistics
- Tourism metrics
- Turtle metrics
- Conservation spending

**Azure Blob Storage**

Document storage:

- Ordinances
- PDFs
- Council documents
- Conservation plans
- Reference materials

## Proposed Application Pages

### Home

Displays:

- Mission statement
- Problem statement
- Municipality selector
- Overview metrics

### Understand

Displays:

- Community profile
- Current legal environment
- Beach characteristics
- AI-generated summary

### Educate

Displays:

- Turtle charts
- Tourism charts
- Census charts
- Melbourne Beach comparison

### Recommend

Displays:

- Policy comparison
- Legal gap analysis
- AI recommendations
- Scenario simulator

## Expected Data Sources

### Legal Data

- Municipal ordinances
- County ordinances
- Local government websites

### Environmental Data

- NOAA turtle data
- Sea Turtle Conservancy
- SWOT sea turtle data

### Tourism Data

- Tourism boards
- State tourism organizations
- Economic development agencies

### Census Data

- U.S. Census Bureau

### Environmental Indicators

- NASA Black Marble light pollution datasets

## Initial Project Structure

```
team-007-beltway-bots/
│
├── main.py
│
├── pages/
│   ├── 1_Understand.py
│   ├── 2_Educate.py
│   └── 3_Recommend.py
│
├── components/
│
├── services/
│   ├── municipality_service.py
│   ├── tourism_service.py
│   ├── turtle_service.py
│   ├── law_service.py
│   └── ai_service.py
│
├── models/
│
├── data/
│
├── prompts/
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Development Standards

### Package Management

Use:

```
uv
```

Add dependencies using:

```
uv add <package>
```

After pulling:

```
uv sync
```

### Version Control

Use feature branches:

```
git checkout -b feature/my-feature
```

Create pull requests into:

```
main
```

Avoid direct commits to main.

## Immediate Next Steps

### Sprint 1: Scaffolding

- Create Streamlit navigation
- Build 3-page layout
- Create reusable components
- Add mock data
- Define data contracts
- Create placeholder AI services

### Sprint 2: Data Integration

- Connect actual datasets
- Implement Azure OpenAI integration
- Build ordinance comparison engine

### Sprint 3: Recommendations

- Policy simulator
- Recommendation engine
- Executive summary generation

## Success Criteria for MVP

A user can:

1. Select a municipality.
2. Understand the municipality's current state.
3. Compare it against Melbourne Beach.
4. View differences in environmental protections.
5. Receive recommendations for improvement.
6. Explore potential outcomes of policy changes.

This demonstrates the full Understand → Educate → Recommend workflow even before advanced modeling and automated data ingestion are implemented.

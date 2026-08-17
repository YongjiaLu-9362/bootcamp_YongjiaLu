
# Crypto Unlock Events and Price Impact

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Token unlock events may create short-term selling pressure in crypto markets because previously locked tokens become available for trading. If the unlocked supply is large relative to circulating supply or trading volume, the event may lead to temporary price declines. For investors, understanding this relationship can help with risk management, short-term trading decisions, and potential arbitrage strategies.

However, the price impact of unlock events may not be uniform. Different unlock types, release sizes, market conditions, and project maturity levels may lead to different outcomes. Small or scheduled unlocks may already be priced in by the market, while regular unlocks could also signal a more stable project development path. This project aims to test whether unlock events are associated with measurable changes in crypto asset prices and whether unlock-related features can be used to design predictive factors.

## Stakeholder & User

The primary stakeholder is an investor or crypto asset manager who needs to decide whether to adjust positions before and after token unlock events.

The output would be used in an investment research workflow, especially during pre-trade analysis, risk monitoring, or factor research. The user may review upcoming unlock events, evaluate expected price pressure, and decide whether to reduce exposure, hedge, or look for short-term trading opportunities.

## Useful Answer & Decision

This project is mainly predictive, with some descriptive analysis.

The useful answer is whether unlock event information can help predict short-term price movements after the event. The key decision is whether an investor should treat an upcoming unlock as a negative price signal, a neutral event, or potentially a positive signal depending on unlock characteristics.

Possible metrics include:

- Price return before and after unlock events, such as 1-day, 3-day, 7-day, and 14-day returns
- Unlock size as a percentage of circulating supply
- Unlock value relative to average daily trading volume
- Volatility before and after unlock events
- Difference in price response across unlock types

The expected deliverable is a research notebook and a small factor dataset that links unlock event features with post-event price performance.

## Assumptions & Constraints

- Unlock event data can be obtained from Tokenomist. I am currently applying for a free trial.
- Price and volume data can be collected from crypto market data APIs or public sources.
- Unlock events are publicly known before they occur, so some price effects may already be priced in.
- The project focuses on measurable association and predictive usefulness, not strict causal identification.
- Data quality may vary across tokens, especially for smaller or less liquid crypto assets.
- Market-wide conditions, Bitcoin price movement, and liquidity may affect individual token prices around unlock events.
- The analysis may require filtering out tokens with very low liquidity or incomplete unlock histories.

## Known Unknowns / Risks

- It is unclear whether different unlock types have different effects on price.
- It is unclear whether large unlock events consistently create negative returns, or whether the market prices them in before the event.
- The relationship may be unstable across market regimes, such as bull markets versus bear markets.
- The project cannot fully prove causality because I cannot control all other market variables.
- The analysis will need to estimate confidence by comparing price behavior around unlock events with normal periods or similar non-event periods.
- Tokenomist data access may be limited depending on the free trial coverage.

## Lifecycle Mapping

Goal → Stage → Deliverable

- Define the investment research question → Problem Framing & Scoping (Stage 01) → Project README
- Collect unlock event and market data → Data Acquisition & Ingestion → Raw unlock and price datasets
- Clean and align event data with market data → Data Cleaning & Preprocessing → Event-level analysis dataset
- Test price behavior around unlock events → Exploratory Data Analysis → Event study notebook
- Build unlock-related predictive factors → Feature Engineering / Modeling → Factor dataset and predictive analysis
- Evaluate investment usefulness → Reporting & Communication → Final research summary and recommendations

## Repo Plan

The repository will be organized as follows:

```text
data/
  raw/          # Raw Tokenomist unlock data and market price data
  processed/    # Cleaned event-level and token-level datasets

src/
  ingestion/    # Scripts for collecting unlock and price data
  cleaning/     # Scripts for cleaning and merging datasets
  features/     # Scripts for creating unlock-related factors

notebooks/
  01_data_exploration.ipynb
  02_event_study.ipynb
  03_factor_analysis.ipynb

docs/
  project_readme.md
  methodology_notes.md
  final_report.md

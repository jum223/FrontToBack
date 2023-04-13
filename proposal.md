# Research Proposal: Industry Returns Throughout the Russia-Ukraine War
### By Juan, Matthew, and Luca
## Research Question

### What do we want to know or what problems are we trying to solve? As in the midterm, you should list (1) the “bigger” question/debate/problem you’re interested in, and also (2) the specific research question(s) you’ll actually try to answer.
- To what extent are the following industries returns: Energy, Food, Transport, Metals, and Microchips, affected by the Russia-Ukraine war, in respect to historical moments during the war?
    - We will then take two different approaches to answer the question at hand. In the first place, we will be analyzing how punctual major events from the war affected the returns by displaying visualizations of cumulative excess returns by industry 20 days before the events and 20 days after it. Through the usage of natural language processing, we also wanted to investigate if the mentioning of the Russia-Ukraine conflict in the 10-K filings for the selected companies’ within the industries of interest, will affect returns at all. 

### If your project is about relationships, what are the hypotheses you’re testing?
- Given Russia’s dominance on natural gas and oil exports and the over-dependence from European countries on Russia’s raw materials, we are initially hypothesizing that the energy industry will be the most affected industry in terms of decreased returns. In the same manner we are also hypothesizing that firms which make a mention of the conflict will see decreased returns based on the assumption that investors could see it as a negative aspect for the financial well being of the company.

- In order to answer the question and prove or reject our initial hypothesis, we plan on using scatterplots, correlation matrices, and line graph visualizations (see the sketch of the dashboard below). We are also planning on developing regression models for the 10-K analysis, the y variable being a cumulative return measure and the x variable being the positive/negative sentiment score for the 10-Ks.  

## Necessary Data
### What does the final dataset need to look like (mostly dictated by the question and the availability of data)
- Our data covers firms in the following industries: Energy, Food, Transport, Metals, and Microchips
- Sample period: February 24, 2022 - Present Day
- Sample Conditions: Our timeline is listed above. We have 18 listed events based on historical data. We plan on using those dates to then identify industry returns, t=-20, and t=+20 days. 
- Necessary Variables: Dates of events, Ticker, Industry, Date, Return, Market Return on Date, Excess Return, and 10k files for sentiment analysis. We plan on merging multiple data sets based on necessary variables in order to congregate our data in one place.

### What data do we have and what data do we need?
- We have data on five chosen ETFs one for each industry. From those ETFs we will be able to identify the major firms needed to run our sentiment analysis on. The sentiment analysis will run based on mentioning of the Russia-Ukraine war and can help us understand those correlations

### How will we collect more data?
- We plan on pulling data from multiple sources to accumulate all our necessary variables. 

### What are the raw inputs and how will you store them (the folder structure(s) for each input type)?
- We will have one input folder that will contain three sub folders. Each subfolder will hold one of the following:  firm returns data, events data timeline, and 10k files. 

### Speculate at a high level (not specific code!) about how you’ll transform the raw data into the final form.
- Regarding the 10-K data, we will first need to clean the 10-K html file so that we are only left with text data. From the 10-K file we will also have to pull the filing date which will allow us to compare pre and post cumulative returns for the given companies and industries. Once this is done we will calculate t-10 and t+10 cumulative returns for the firms of interests by using the complimentary firms-date-return dataset, in which, after having matched the filing date.
- Regarding our analysis of how specific events will affect certain industries, we plan on calculating cumulative returns from t-20 to t+20 by using the event-date dataset  and matching the dates from this dataset to dates on the firms-date-return dataset, and using groupby() functions to create the cumulative returns variables.    


## Additional Links with Information:
CNN War Timeline - https://www.cnn.com/interactive/2023/02/europe/russia-ukraine-war-timeline/index.html
Global Conflict tracker - https://www.cfr.org/global-conflict-tracker/conflict/conflict-ukraine
Affected Industries - https://sourcemap.com/news/five-industries-certain-to-be-affected-by-the-russian-ukrainian-conflict
War Data - https://acleddata.com/ukraine-conflict-monitor/#data

## ETFs, list of companies we will use 
Energy ETF (VDE): https://investor.vanguard.com/investment-products/etfs/profile/vde#portfolio-composition
Link to list: https://advisors.vanguard.com/investments/products/vde/vanguard-energy-etf#portfolio 
Food ETF (FTXG):https://www.ftportfolios.com/Retail/Etf/EtfHoldings.aspx?Ticker=FTXG
Transport ETF (XTN): https://www.ssga.com/us/en/intermediary/etfs/funds/spdr-sp-transportation-etf-xtn
Metals ETF (Not an ETF but the largest companies by market cap in the steel/metal industry)https://companiesmarketcap.com/steel-industry/largest-companies-by-market-cap/
Microchips ETF (XSD): https://www.ssga.com/us/en/intermediary/etfs/funds/spdr-sp-semiconductor-etf-xsd
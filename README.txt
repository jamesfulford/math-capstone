README.txt
by James Fulford

Welcome to James Fulford's analysis of St. Elizabeth Seton's Confirmation Program!
This project was done in late 2016 by James Fulford as his Mathematics Capstone Project.

Please note that the actual data, which contains the names of students, has been excluded.  This is what the directory structure would have looked like including the data.

Layout:
    Original Documents/ Store raw data here. Do not perform any edits: make copies.
    Data/
        = Copies of original documents
        = JSON data
        = Extraction scripts
        = Inspection scripts and results
        + Perform edits here.
    Analysis/
        = Load Scripts
    Reports/
    Error Logs/ Errors generated categorized by any of the steps in the process (outlined below)



Process:
    1. Retrieval: Get/enter the raw data.
        a) Store separately from other documents.
    2. Extraction: Extract and save the data into readily available format (json)
        a) Create extraction scripts to get the data from raw documents.
        b) Build tools that allow for easy loading of data.
        c) Catch simple errors in data
    3. Inspection: Inspect the data
        a) Check for legitimacy:
              i) Values are within reasonable tolerances
             ii) Critical fields are not empty
            iii) Unique data (names) don't appear multiple times
             iv) etc.
        b) Observe the data:
              i) Visualize the data
             ii) Summary Statistics, counts, etc.
    4. Analysis: Analyze the data
        a) Construct hypotheses based on observations
        b) Identify tools for analysis
              i) Machine Learning
             ii) Classical Statistical Analyses
        c) Test hypotheses using tools
    5. Reporting: Report Findings
        a) Generate statistics
        b) Form conclusions about hypotheses
        c) Build visualizations, key statistics, etc.
        d) Craft recommendations

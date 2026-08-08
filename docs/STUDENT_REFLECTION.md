# CMP7005 Self Reflection

## Project Development Experience

This project developed from a set of separate city-level CSV files into a structured Python data analysis and application project. The work required data loading, inspection, preprocessing, exploratory data analysis, model building, Streamlit interface development, and GitHub version control. A key learning point was that the assessment was not only about air pollution, but about demonstrating a complete and reproducible programming workflow.

## Data Handling Challenges

One of the first challenges was combining 26 separate city datasets while keeping the original files unchanged. The files shared the same column structure, which made concatenation appropriate, but the combined dataset still needed validation. The project therefore checks expected columns, parses the Date column, confirms dimensions, and preserves both raw and processed data. This made the workflow easier to explain and reproduce.

## Data Quality Challenges

The dataset contains substantial missing data, especially for variables such as Xylene, PM10, NH3, Toluene, and AQI. This made it unsuitable to apply one simple missing-value treatment to every column. Missing target AQI values cannot be artificially filled for supervised learning because that would create unreliable labels. In contrast, missing predictor values can be handled inside the machine-learning pipeline using median imputation. This distinction improved my understanding of how data cleaning decisions depend on the purpose of the analysis.

## EDA Challenges

A major improvement in the project was moving from producing charts to interpreting what those charts show. The EDA had to consider pollutant distributions, AQI category counts, city-level differences, seasonal patterns, and pollutant relationships. A further challenge was unequal temporal coverage: some cities have data from 2015, while others enter much later. This means that overall annual AQI trends must be interpreted cautiously because changes may reflect changing city composition as well as pollution changes.

## Model Development Challenges

The modelling task required careful feature preparation. AQI_Bucket was excluded because it is derived from AQI and would create target leakage. The project compares Linear Regression, Decision Tree, Random Forest, and Gradient Boosting models using MAE, MSE, RMSE, and R squared. Random Forest performed best on the test set. Hyperparameter tuning was also tested using GridSearchCV, but the tuned model did not improve RMSE enough to replace the original Random Forest. This showed that optimisation should be judged by evidence rather than assumed to improve results.

## Application Development Challenges

The Streamlit application required the analysis to be presented in a usable graphical interface. The app includes Data Overview, EDA, and Prediction sections. During testing, the Data Overview page needed a repair because Streamlit metric components require display-friendly values, so dates were converted into formatted strings. The EDA page was also strengthened to handle empty filtered results and to show clearer evidence of missing data, temporal analysis, city comparison, pollutant relationships, and correlations.

## Version Control

GitHub was used to document the development stages. Commits were organised around project setup, data loading, reusable modules, modelling outputs, Streamlit application development, notebook completion, screenshot evidence, and final repairs. This helped create a clearer development history and supported the version-control learning outcome.

## Skills Developed

The project developed practical skills in pandas data handling, reusable Python modules, exploratory visualisation, missing-data reasoning, scikit-learn pipelines, model evaluation, hyperparameter tuning, feature importance interpretation, Streamlit application development, and GitHub version control. It also improved my ability to write cautious academic interpretations based on actual program outputs.

## Areas for Further Improvement

If the project were extended, I would carry out deeper sensitivity analysis around highly incomplete pollutants, add more formal statistical tests for selected comparisons, and perform broader model validation. I would also improve the application with more guided chart explanations and more systematic user testing. If specific previous assessment feedback is available, it should be added here by the student in their own words; no specific previous-feedback document was available in the repository during this repair work.

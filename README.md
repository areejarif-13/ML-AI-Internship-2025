 **ML-AI-Internship-2025
Tasks provided for DevelopersHub.**
 
Task 1: Exploring and Visualizing a Simple Dataset
Objective:
Learn how to load, inspect, and visualize a dataset to understand data trends and distributions.
Dataset:
Iris Dataset (CSV format, can be loaded via seaborn or downloaded) Instructions:
● Load the dataset using pandas.
● Print the shape, column names, and the first few rows using .head().
● Use .info() and .describe() for summary statistics.
● Visualize the dataset:
○ Create a scatter plot to show relationships between features.
○ Use histograms to show value distributions.
○ Use box plots to identify outliers.

● Use matplotlib and seaborn for plotting.

Skills:
● Data loading and inspection using pandas
● Descriptive statistics and data exploration
● Basic plotting and visualization with seaborn and matplotlib

Task 2: Predict Future Stock Prices (Short-Term)
Objective:
Use historical stock data to predict the next day's closing price.
Dataset:
Stock market data from Yahoo Finance (retrieved using the yfinance Python library)
Instructions:
● Select a stock (e.g., Apple, Tesla).
● Load historical data using the yfinance library.
● Use features like Open, High, Low, and Volume to predict the next Close price.
● Train a Linear Regression or Random Forest model.
● Plot actual vs predicted closing prices for comparison.

Skills:
● Time series data handling
● Regression modeling
● Data fetching using APIs (yfinance)
● Plotting predictions vs real data

Task 3: Heart Disease Prediction
Objective:
Build a model to predict whether a person is at risk of heart disease based on their health data.
Dataset:
Heart Disease UCI Dataset (available on Kaggle)
Instructions:
● Clean the dataset (handle missing values if any).
● Perform Exploratory Data Analysis (EDA) to understand trends.
● Train a classification model (Logistic Regression or Decision Tree).
● Evaluate using metrics: accuracy, ROC curve, and confusion matrix.
● Highlight important features affecting prediction.

Skills:
● Binary classification
● Medical data understanding and interpretation
● Model evaluation using ROC-AUC and confusion matrix
● Feature importance analysis

Task 4: General Health Query Chatbot (Prompt
Engineering Based)
Objective:

Create a chatbot that can answer general health-related questions using an LLM (Large
Language Model).
Tools:
OpenAI GPT-3.5 via API (or use a free open-source model like Mistral-7B-Instruct on Hugging
Face)
Instructions:
● Build a simple Python script or notebook that sends user queries to an LLM.
● Use prompt engineering to make the responses friendly and clear (e.g., "Act like a helpful
medical assistant").
● Add safety filters to avoid giving medical advice that could be harmful.
● Example queries:
○ "What causes a sore throat?"
○ "Is paracetamol safe for children?"

Skills:
● Prompt design and testing
● Using APIs for LLMs (e.g., OpenAI, Hugging Face)
● Safety handling in chatbot responses
● Building simple conversational agents

Task 5: Mental Health Support Chatbot (Fine-Tuned)
Objective:
Build a basic chatbot that provides supportive and empathetic responses for stress, anxiety,
and emotional wellness.
Model Base:
DistilGPT2, GPT-Neo, or Mistral (7B)
Dataset for Fine-Tuning:

EmpatheticDialogues (Facebook AI)
Instructions:
● Fine-tune a small LLM using Hugging Face’s Trainer API.
● Train it to respond empathetically using real human dialogues.
● Ensure the tone is gentle and emotionally supportive.
● Build a command-line or Streamlit-based interface to test it.

Skills:
● Model fine-tuning with Hugging Face Transformers
● Emotional tone design for safe chatbots
● Conversation modeling
● Deployment using CLI or simple web apps

Task 6: House Price Prediction
Objective:
Predict house prices using property features such as size, bedrooms, and location.
Dataset:
House Price Prediction Dataset (available on Kaggle)
Instructions:
● Perform preprocessing on features like square footage, number of bedrooms, and
location.
● Train a regression model (Linear Regression or Gradient Boosting).
● Visualize predicted prices compared to actual prices.
● Evaluate with Mean Absolute Error (MAE) and RMSE.

Skills:
● Regression modeling
● Feature scaling and selection
● Model evaluation (MAE, RMSE)
● Real estate data understanding
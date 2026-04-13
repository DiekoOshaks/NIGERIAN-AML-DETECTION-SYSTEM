 Nigerian Anti-Money Laundering (AML) Detection System

 Overview

This project is an AI-powered Anti-Money Laundering (AML) system designed to detect suspicious financial transactions within the Nigerian financial ecosystem.

It combines:

*  Rule-based fraud detection (industry standard)
*  Machine learning (anomaly detection)
*  Risk scoring engine
*  Interactive monitoring dashboard

The system simulates how financial institutions identify and flag suspicious activities in compliance with regulatory bodies such as the Central Bank of Nigeria (CBN) and anti-corruption enforcement frameworks.



 Objectives

* Detect suspicious transaction patterns (fraud & money laundering)
* Identify anomalies in user behavior
* Assign risk scores to transactions
* Provide a real-time monitoring dashboard
* Simulate a fintech-grade AML pipeline



 Key Concepts Implemented

 1. Rule-Based Detection

Predefined rules are used to flag known suspicious behaviors:

* High-value transactions
* Rapid transaction frequency (smurfing)
* Unusual transaction patterns



 2. Machine Learning (Anomaly Detection)

The system uses Isolation Forest to detect:

* Unusual transaction amounts
* Irregular transaction timing
* Behavioral deviations

Unlike rule-based systems, this approach identifies unknown fraud patterns.



3. Risk Scoring Engine

Each transaction is assigned a risk score based on:

* Rule-based flags
* Machine learning anomalies

This allows prioritization of high-risk activities instead of simple binary classification.


 4. Monitoring Dashboard

A Streamlit dashboard provides:

* Transaction overview
* Suspicious activity alerts
* Risk score visualization
* Filtering and search capabilities



 System Architecture


Data Generation → Rule Engine → ML Model → Risk Engine → Dashboard



 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn (Isolation Forest)
* Streamlit (Dashboard)
* Faker (Synthetic data generation)



 How to Run the Project

 1. Clone the Repository


git clone https://github.com/DiekoOshaks/NIGERIAN-AML-DETECTION-SYSTEM.git
cd NIGERIAN-AML-DETECTION-SYSTEM

2. Install Dependencies
pip install -r requirements.txt


3. Generate Dataset

python generate_data.py

4. Run Rule-Based Detection

python rules_engine.py

5. Run Machine Learning Model

python ml_model.py

 6. Generate Risk Scores

python risk_engine.py

7. Launch Dashboard

cd apps
streamlit run app.py

 Sample Features

* Transaction amount analysis
* Time-based anomaly detection
* Location-based insights
* High-risk transaction alerts
* Fraud pattern simulation

 Nigerian Context & Relevance

This project is tailored to reflect financial risks common in Nigeria, including:

* Smurfing (multiple small transactions)
* Sudden large transfers
* Suspicious account activity
* Transaction spikes

It aligns with AML practices encouraged by:

* Central Bank of Nigeria (CBN)
* Economic and Financial Crimes Commission (EFCC)

 Compliance & Guidelines

This project follows general AML principles:

* KYC (Know Your Customer) simulation
* Transaction monitoring
* Suspicious Activity Reporting (SAR) logic
* Risk-based approach to fraud detection

 Note: This is a simulation project and not intended for real financial enforcement use.

 Use Cases

This system can be adapted for:

 Fintech Startups

* Fraud detection layer
* Transaction monitoring system

 Cybersecurity / Red Teaming

* Fraud simulation lab
* Behavioral anomaly detection

 Fraud Recovery Platforms

* Detect suspicious transactions early
* Alert victims in real-time

 Academic / Portfolio Use

* Demonstrates ML + cybersecurity + fintech integration
* Strong project for internships and job applications

 Future Improvements

* Real-time transaction streaming
* API integration (Flask/FastAPI)
* WhatsApp/Telegram alert system
* Network graph analysis (fraud rings)
* BVN/NIN identity verification simulation
* Deep learning models for fraud detection

 Contribution

Contributions are welcome!

Feel free to:

* Fork the repo
* Improve detection logic
* Add new features
* Submit pull requests

 License

This project is open-source and available under the MIT License.

 Author

Built by Diekololaoluwa Osakuade

 Final Note

This project demonstrates how Artificial Intelligence + Rule-Based Systems can be combined to build a real-world Anti-Money Laundering solution tailored for emerging markets like Nigeria.

If you found this useful, consider giving it a ⭐ on GitHub!

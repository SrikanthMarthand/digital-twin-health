
🧠 Digital Twin Health Assessment System

A clinical-grade soft computing project that creates a digital twin of human health using a hybrid fuzzy logic + neural network framework to support holistic health assessment.

🎯 Project Objective

The objective of this project is to design a Digital Twin–based Health Assessment System that evaluates overall human health using soft computing techniques, rather than predicting a specific disease.

The system provides interpretable decision support by combining numerical approximation with linguistic reasoning.

🧬 Core Concepts

Soft Computing

Fuzzy Logic (interpretability)

Artificial Neural Networks (approximation)

Digital Twin modeling

Clinical Decision Support Systems (CDSS)

🏗️ System Architecture
User Health Parameters
        ↓
Artificial Neural Network
(Numerical Health Score)
        ↓
Fuzzy Inference System
(Linguistic Risk Level)
        ↓
Digital Twin Visualization

⚙️ Technologies Used
Backend

Python

Flask

Flask-CORS

NumPy

Pandas

Scikit-learn

Frontend

React.js

SVG-based Digital Twin Visualization

Custom CSS (hospital-grade UI)

🩺 Key Features

Linguistic health risk classification
(Healthy / Moderate / High Risk)

Numerical health score estimation using ANN

Human body digital twin visualization

Organ-level stress interpretation

Explainable fuzzy rule-based reasoning

Clean, clinical-style web interface

🧠 Soft Computing Approach

This project follows a hybrid soft computing framework:

Artificial Neural Network estimates a continuous health score

Fuzzy Logic converts uncertain multi-parameter inputs into interpretable linguistic health states

The Digital Twin interface visually represents the inferred health condition

This approach balances accuracy and interpretability, which is a key principle of soft computing.

▶️ How to Run the Project
Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python api/app.py


Backend runs at:
http://127.0.0.1:5000

Frontend Setup
cd frontend
npm install
npm start


Frontend runs at:
http://localhost:3000

⚕️ Disclaimer

This system provides clinical decision support only and does not replace professional medical diagnosis or treatment.

👨‍🎓 Academic Context

This project was developed as part of a Soft Computing course and demonstrates the application of hybrid intelligent systems and digital twin concepts in healthcare decision support.
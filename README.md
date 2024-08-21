SmartMail Classifier
SmartMail Classifier is a full-stack application that fetches the latest emails from a user's inbox, classifies them into different categories using a machine learning model, and displays them accordingly. The classification categories include spam, social, promotional, marketing, and important.

Project Structure
The project is divided into three main components:

Frontend (React)
Backend (Node.js)
Text Classification (Machine Learning Model)
1. Frontend (React)
The frontend is built using React, providing a user-friendly interface for signing in via Google and viewing classified emails.

Installation
Navigate to the frontend directory:

bash
Copy code
cd frontend
Install the dependencies:

bash
Copy code
npm install
Run the application:

bash
Copy code
npm start
The frontend will be running on http://localhost:3000.

2. Backend (Node.js)
The backend is developed in Node.js, handling authentication, fetching emails, and serving data to the frontend.

Installation
Navigate to the backend directory:

bash
Copy code
cd backend
Install the dependencies:

bash
Copy code
npm install
Run the server:

bash
Copy code
node index.js
The backend will be running on http://localhost:5000.

3. Text Classification (Machine Learning Model)
The Text Classification component is a Python-based machine learning model that classifies emails into five categories: spam, social, promotional, marketing, and important.

Installation
Navigate to the Text_classification directory:

bash
Copy code
cd Text_classification
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
The model will be running on http://localhost:8000.

Usage
Sign in using your Google account.
Fetch the latest emails from your inbox.
View emails categorized into spam, social, promotional, marketing, and important.
Technologies Used
Frontend: React
Backend: Node.js, Express.js
Machine Learning: Python, Flask, Scikit-learn
License
This project is licensed under the MIT License.

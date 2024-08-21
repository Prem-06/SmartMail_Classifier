# 📧 SmartMail Classifier

SmartMail Classifier is a full-stack application that helps users organize their emails by categorizing them into different categories using a machine learning model. The categories include **spam**, **social**, **promotional**, **marketing**, and **important**. 

Users can sign in with their Google account, fetch their latest emails, and see them automatically classified.

## 📁 Project Structure

The project is divided into three main components:

- **Frontend**: Built with React.
- **Backend**: Built with Node.js and Express.js.
- **Text Classification**: A Machine Learning model built with Python and Flask.

```bash
📂 SmartMail_Classifier
│
├── 📁 frontend
├── 📁 backend
└── 📁 Text_classification

⚛️ Frontend (React)
The frontend provides the user interface for signing in through Google and displaying classified emails.

Installation and Setup
Navigate to the frontend directory:

bash
cd frontend
Install the dependencies:

bash
npm install
Start the development server:

bash
npm run dev


🌐 Backend (Node.js)
The backend handles user authentication, fetching emails, and serving data to the frontend.

Installation and Setup
Navigate to the backend directory:

bash
cd backend
Install the dependencies:

bash
npm install
Start the server:

bash
node index.js
The backend will be running at http://localhost:3000.


🧠 Text Classification (Machine Learning Model)
This component is responsible for classifying the fetched emails into the specified categories.

Installation and Setup
Navigate to the Text_classification directory:

bash
cd Text_classification
Install the required Python packages:

bash
pip install -r requirements.txt
Start the Flask application:

bash
python app.py
The machine learning model will be running at http://localhost:5000.


🚀 Usage
Sign In: Use your Google account to sign in.
Fetch Emails: Retrieve your latest emails with one click.
View Categories: See your emails categorized into spam, social, promotional, marketing, and important.

🛠️ Technologies Used
Frontend: React, JavaScript, HTML, CSS
Backend: Node.js, Express.js
Machine Learning: Python, Flask, Scikit-learn, Natural Language Processing (NLP)
Database: (Mention if you’re using any database, e.g., MongoDB)
Authentication: Google OAuth 2.0


# Sentiment Analyzer App

A web application that performs sentiment analysis on a given text. This app uses a backend API built with Python and Flask, which predicts whether the sentiment of a text is positive, negative, or neutral.

## Video Walkthrough
  link: https://drive.google.com/file/d/1Vseoo1IH5i4LBIgvJNXwRMiFyXgy2TbH/view?usp=sharing
## Features
- Input a sentence or paragraph.
- Get a sentiment prediction (positive, negative, or neutral).
- User-friendly interface built with React and styled with Tailwind CSS.

## Technologies Used
- **Frontend**: React, Tailwind CSS
- **Backend**: Python, Flask
- **NLP Model**: Any pre-trained sentiment analysis model (e.g., TextBlob, Hugging Face transformers)

## Prerequisites
Before running the project, make sure you have the following installed on your local machine:

- **Node.js**: [Download Node.js](https://nodejs.org/)
- **npm** (Node Package Manager): Comes with Node.js
- **Python**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/arunkabish1/sentiment-analyzer-App.git
cd sentiment-analyzer-App
```

### 2. Backend Setup
Navigate to the backend directory:
```bash
cd backend
```
Install the required Python dependencies:
```bash
pip install -r requirements.txt
```
Run the backend server:
```bash
python app.py
```
This will start the Flask server, usually running on `http://127.0.0.1:5000/`.


### 3. Frontend Setup
Navigate to the frontend directory:
```bash
cd frontend
```
Install the required npm dependencies:
```bash
npm install
```
Start the React development server:
```bash
npm start
```
This will start the frontend development server, usually running on `http://localhost:3000/`.


### 4. Running the App
Open your browser and go to `http://localhost:3000/`.

Enter any sentence in the text box and click **Analyze** to see the sentiment prediction.

## Project Structure

```plaintext
sentiment-analyzer-App/
├── backend/
│   ├── app.py                  # Flask server to handle sentiment analysis
│   ├── requirements.txt        # Python dependencies
|   ├── train_model.py          # For Train the model
|   ├── package_lock.json
├── frontend/
│   ├── public/                 # Public files 
│   |   ├──index.html
├── src/
│   │   ├── App.js              # Main React component
│   │   ├── index.js            # Entry point for React app
│   │   ├── index.css           # Tailwind CSS styles
│   ├── package.json            # npm configuration
|   ├── package_lock.json
|   ├── tailwind.config.js
├── .gitignore                  # Git ignore file
├── README.md                   # This README file
```

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

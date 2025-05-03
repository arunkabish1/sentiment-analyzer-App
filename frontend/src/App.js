import React, { useState } from 'react';
import axios from 'axios';
import "./index.css";

function App() {
  const [text, setText] = useState('');
  const [sentiment, setSentiment] = useState('');

  const handleSubmit = async () => {
    const res = await axios.post('http://127.0.0.1:5000/predict', { text });
    setSentiment(res.data.sentiment);
  };

  return (
    <div className="App flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-lg w-96">
        <h2 className="text-2xl font-bold text-center mb-4">Sentiment Analyzer</h2>
        <textarea
          className="w-full p-4 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={text}
          onChange={e => setText(e.target.value)}
          placeholder="Enter your sentence"
        />
        <br />
        <button
          onClick={handleSubmit}
          className="w-full mt-4 py-2 bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600 transition"
        >
          Analyze
        </button>
        <h3 className="mt-4 text-center text-xl">Prediction: {sentiment}</h3>
      </div>
    </div>
  );
}

export default App;

import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import React, { useState } from 'react';

function App() {
  const [string1, setString1] = useState('');
  const [string2, setString2] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/concatenate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ string1, string2 }),
        mode: 'cors', // Ensure 'cors' mode is set
      });
      if (response.ok) {
        const data = await response.json();
        setResult(data.result);
        console.log(data);
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Flask Test Server</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="string1">Name:</label>
          <input
            type="text"
            id="string1"
            value={string1}
            onChange={(e) => setString1(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="string2">Prescription:</label>
          <input
            type="text"
            id="string2"
            value={string2}
            onChange={(e) => setString2(e.target.value)}
          />
        </div>
        <button type="submit">Concatenate</button>
      </form>
      {result && (
        <div>
          <h2>Result:</h2>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default App;


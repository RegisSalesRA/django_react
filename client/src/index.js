import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Header from './components/header';

ReactDOM.render(
  <React.StrictMode>
    <Header/>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
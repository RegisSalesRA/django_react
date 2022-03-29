import React from 'react';
import ReactDOM from 'react-dom';
import reportWebVitals from './reportWebVitals';
import LoginComponent from './components/LoginComponent/LoginComponent';
import './style/global.css';

ReactDOM.render(
  <React.StrictMode>
    <LoginComponent />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
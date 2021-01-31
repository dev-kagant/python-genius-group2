import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import { ModalProvider } from "./components/Modal/Modal";
import configureStore from "./store/index";

const store = configureStore();

ReactDOM.render(
  <React.StrictMode>
    <ModalProvider>
        <Provider store = {store}>
          <App />
        </Provider>
    </ModalProvider>
  </React.StrictMode>,
  document.getElementById('root')
); 

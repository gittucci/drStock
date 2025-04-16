// Import necessary modules
import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import page from './app/products';
import page from './app/entries';
import page from './app/exits';
import page from './app/suppliers';
import page from './app/customers';
import page from './app/register';
import login-page from './app';
// Import other pages as needed


// Render the main application component with routing
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <Router>
            <Switch>
                <Route path="/" exact component={page} />
                <Route path="/products" component={page} />
                <Route path="/entries" component={page} />
                <Route path="/exits" component={page} />
                <Route path="/suppliers" component={page} />
                <Route path="/customers" component={page} />
                <Route path="/login" component={login-page} />
                {/* Add more routes as needed */}
            </Switch>
        </Router>
    </React.StrictMode>
);
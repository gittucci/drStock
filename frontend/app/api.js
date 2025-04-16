// frontend/app/api.js

const BASE_URL = "http://localhost:8000"; // Adjust if necessary

export const fetchProducts = async () => {
    const response = await fetch(`${BASE_URL}/products/`);
    return response.json();
};

export const addProduct = async (product) => {
    const response = await fetch(`${BASE_URL}/products/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(product),
    });
    return response.json();
};

// Similar functions for entries, exits, suppliers, and customers
export const fetchEntries = async () => {
    const response = await fetch(`${BASE_URL}/entries/`);
    return response.json();
};

export const addEntry = async (entry) => {
    const response = await fetch(`${BASE_URL}/entries/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(entry),
    });
    return response.json();
};

// Repeat for exits, suppliers, and customers
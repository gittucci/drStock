// frontend/app/products/ProductList.js

import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../api';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const getProducts = async () => {
            const data = await fetchProducts();
            setProducts(data);
        };
        getProducts();
    }, []);

    return (
        <div>
            <h1>Product List</h1>
            <ul>
                {products.map(product => (
                    <li key={product.product_id}>{product.description}</li>
                ))}
            </ul>
        </div>
    );
};

export default ProductList;
"use client"
import Link from 'next/link';
import React from 'react';

const ProductRegistrationPage: React.FC = () => {
    const productsData = [
        // Example product data
        {
            code: 'AB01',
            barcode: '123123123123',
            description: 'Produto a ser estocado',
            supplier: 'Fornecedor de Produtos do Brasil',
            restockPoint: 5,
            restockCost: 1.25,
            stockPrice: 2.50,
            unit: 'Peça',
            stockLocation: 'ABCD0001', 
        },
        // Add more product as needed
    ];

    const handleAddProduct = () => {
        // Logic to add a new product
        console.log("Add Product");
    };

    const handleEditProduct = (code: string) => {
        // Logic to edit an product based on the code
        console.log("Edit Customer", code);
    };

    const handleDeleteProduct = (code: string) => {
        // Logic to delete an product based on the code
        console.log("Delete Customer", code);
    };

    return (
        <div className="flex">
            <aside className="w-1/12 bg-blue-800 text-white p-4">
                <h2 className="text-center text-lg font-bold mb-4">Cadastro de Clientes</h2>
                <Link href="/products" className="block mb-3 text-center">Controle de Estoque</Link>
                <Link href="/entries" className="block mb-3 text-center">Entradas de Estoque</Link>
                <Link href="/exits" className="block mb-3 text-center">Saídas de Estoque</Link>
                <Link href="/customers" className="block mb-3 text-center">Cadastro de Clientes</Link>                
                <Link href="/suppliers" className="block mb-3 text-center">Cadastro de Fornecedores</Link>
                <Link href="/generate-inventory" className="block mb-3 text-center">Gerar Inventário</Link>
                <Link href="/export-report" className="block mb-3 text-center">Exportar Relatório</Link>
            </aside>
            <main className="flex-1 p-4">
                <h1 className="text-3xl font-bold mb-6">Localização de Produtos</h1>

                <div className="mb-4">
                    <button type="button" onClick={handleAddProduct} className="bg-blue-500 text-white px-4 py-2 rounded mr-2">Adicionar Produto</button>
                    <button type="button" onClick={() => handleEditProduct('AB01')} className="bg-yellow-500 text-white px-4 py-2 rounded mr-2">Editar Produto</button>
                    <button type="button" onClick={() => handleDeleteProduct('AB01')} className="bg-red-500 text-white px-4 py-2 rounded">Excluir Produto</button>
                </div>

                <div className="grid grid-cols-1 gap-4">
                    <div className="flex flex-col">
                        <label className="mb-1">Código do Produto</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="AB01" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Barcode do Produto</label>
                        <input type="email" className="border border-gray-300 p-2" placeholder="123123123123" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Descrição</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Produto a ser estocado" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Fornecedor</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Fornecedor de Produtos do Brasil" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Ponto de Reposição</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="5" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Custo de Reposição</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="1.25" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Preço de Estoque</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="2.50" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Unidade</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Peça" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Local de Estoque</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="ABCD0001" />
                    </div>
                </div>                    
            </main>
        </div>
    );
};

export default ProductRegistrationPage;
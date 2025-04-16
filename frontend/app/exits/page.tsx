"use client"
import Link from 'next/link';
import React from 'react';

const ExitsPage: React.FC = () => {
    const exitsData = [
        { code: 'AB01', barcode: '123123123123', description: 'ABJNDKSMMOIJOIIONIPPDOPJ', customer: 'John Johan Sebastian', exitDate: '01/01/25', quantity: 10, unit: 'Peça', stockPrice: 2.50, stockLocation: 'ABCD0001' },
        // Add more exits as needed
    ];

    const handleAddExit = () => {
        // Logic to add a new exit
        console.log("Add Exit");
    };

    const handleEditExit = (code: string) => {
        // Logic to edit an exit based on the code
        console.log("Edit Exit", code);
    };

    const handleDeleteExit = (code: string) => {
        // Logic to delete an exit based on the code
        console.log("Delete Exit", code);
    };

    return (
        <div className="flex">
            <aside className="w-1/12 bg-blue-800 text-white p-4">
                <h2 className="text-center text-lg font-bold mb-4">Saídas de Estoque</h2>
                <Link href="/products" className="block mb-3 text-center">Controle de Estoque</Link>
                <Link href="/entries" className="block mb-3 text-center">Entradas de Estoque</Link>
                <Link href="/register" className="block mb-3 text-center">Cadastro de Produtos</Link>
                <Link href="/suppliers" className="block mb-3 text-center">Cadastro de Fornecedores</Link>
                <Link href="/customers" className="block mb-3 text-center">Cadastro de Clientes</Link>
                <Link href="/generate-inventory" className="block mb-3 text-center">Gerar Inventário</Link>
                <Link href="/export-report" className="block mb-3 text-center">Exportar Relatório</Link>
            </aside>
            <main className="flex-1 p-4">
                <h1 className="text-3xl font-bold mb-6">Saídas de Estoque</h1>
                
                <div className="mb-4">
                    <button type="button" onClick={handleAddExit} className="bg-blue-500 text-white px-4 py-2 rounded mr-2">Adicionar Saída</button>
                    <button type="button" onClick={() => handleEditExit('AB01')} className="bg-yellow-500 text-white px-4 py-2 rounded mr-2">Editar Saída</button>
                    <button type="button" onClick={() => handleDeleteExit('AB01')} className="bg-red-500 text-white px-4 py-2 rounded">Excluir Saída</button>
                </div>

                <table className="min-w-full border-collapse border border-gray-300">
                    <thead>
                        <tr className="bg-gray-200">
                            <th className="border border-gray-300 p-2">Código do Produto</th>
                            <th className="border border-gray-300 p-2">Barcode do Produto</th>
                            <th className="border border-gray-300 p-2">Descrição</th>
                            <th className="border border-gray-300 p-2">Cliente</th>
                            <th className="border border-gray-300 p-2">Data de Saída</th>
                            <th className="border border-gray-300 p-2">Qtd. Saída</th>
                            <th className="border border-gray-300 p-2">Unidade</th>
                            <th className="border border-gray-300 p-2">Preço de Estoque</th>
                            <th className="border border-gray-300 p-2">Local de Estoque</th>
                        </tr>
                    </thead>
                    <tbody>
                        {exitsData.map((exit, index) => (
                            <tr key={index}>
                                <td className="border border-gray-300 p-2">{exit.code}</td>
                                <td className="border border-gray-300 p-2">{exit.barcode}</td>
                                <td className="border border-gray-300 p-2">{exit.description}</td>
                                <td className="border border-gray-300 p-2">{exit.customer}</td>
                                <td className="border border-gray-300 p-2">{exit.exitDate}</td>
                                <td className="border border-gray-300 p-2">{exit.quantity}</td>
                                <td className="border border-gray-300 p-2">{exit.unit}</td>
                                <td className="border border-gray-300 p-2">{exit.stockPrice}</td>
                                <td className="border border-gray-300 p-2">{exit.stockLocation}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </main>
        </div>
    );
};

export default ExitsPage;
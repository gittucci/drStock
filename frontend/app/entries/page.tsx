"use client"
import Link from 'next/link';
import React from 'react';

const EntriesPage: React.FC = () => {
    const entriesData = [
        { code: 'AB01', barcode: '123123123123', description: 'ABJNDKSMMOIJOIIONIPPDOPJ', supplier: 'Fabricante de Peças BEST', restockPoint: 5, restockCost: 1.25, entryDate: '01/01/25', quantity: 10, unit: 'Peça', stockPrice: 2.50, stockLocation: 'ABCD0001' },
        // Add more entries as needed
    ];

    const handleAddEntry = () => {
        // Logic to add a new entry
        console.log("Add Entry");
    };

    const handleEditEntry = (code: string) => {
        // Logic to edit an entry based on the code
        console.log("Edit Entry", code);
    };

    const handleDeleteEntry = (code: string) => {
        // Logic to delete an entry based on the code
        console.log("Delete Entry", code);
    };

    return (
        <div className="flex">
            <aside className="w-1/12 bg-blue-800 text-white p-4">
                <h2 className="text-center text-lg font-bold mb-4">Entradas de Estoque</h2>
                <Link href="/products" className="block mb-3 text-center">Controle de Estoque</Link>
                <Link href="/exits" className="block mb-3 text-center">Saídas de Estoque</Link>
                <Link href="/register" className="block mb-3 text-center">Cadastro de Produtos</Link>
                <Link href="/suppliers" className="block mb-3 text-center">Cadastro de Fornecedores</Link>
                <Link href="/customers" className="block mb-3 text-center">Cadastro de Clientes</Link>
                <Link href="/generate-inventory" className="block mb-3 text-center">Gerar Inventário</Link>
                <Link href="/export-report" className="block mb-3 text-center">Exportar Relatório</Link>
            </aside>
            <main className="flex-1 p-4">
                <h1 className="text-3xl font-bold mb-6">Entradas de Estoque</h1>
                
                <div className="mb-4">
                    <button type="button" onClick={handleAddEntry} className="bg-blue-500 text-white px-4 py-2 rounded mr-2">Adicionar Entrada</button>
                    <button type="button" onClick={() => handleEditEntry('AB01')} className="bg-yellow-500 text-white px-4 py-2 rounded mr-2">Editar Entrada</button>
                    <button type="button" onClick={() => handleDeleteEntry('AB01')} className="bg-red-500 text-white px-4 py-2 rounded">Excluir Entrada</button>
                </div>

                <table className="min-w-full border-collapse border border-gray-300">
                    <thead>
                        <tr className="bg-gray-200">
                            <th className="border border-gray-300 p-2">Código do Produto</th>
                            <th className="border border-gray-300 p-2">Barcode do Produto</th>
                            <th className="border border-gray-300 p-2">Descrição</th>
                            <th className="border border-gray-300 p-2">Fornecedor</th>
                            <th className="border border-gray-300 p-2">Ponto de Reposição</th>
                            <th className="border border-gray-300 p-2">Custo de Reposição</th>
                            <th className="border border-gray-300 p-2">Data de Entrada</th>
                            <th className="border border-gray-300 p-2">Qtd. Entrada</th>
                            <th className="border border-gray-300 p-2">Unidade</th>
                            <th className="border border-gray-300 p-2">Preço de Estoque</th>
                            <th className="border border-gray-300 p-2">Local de Estoque</th>
                        </tr>
                    </thead>
                    <tbody>
                        {entriesData.map((entry, index) => (
                            <tr key={index}>
                                <td className="border border-gray-300 p-2">{entry.code}</td>
                                <td className="border border-gray-300 p-2">{entry.barcode}</td>
                                <td className="border border-gray-300 p-2">{entry.description}</td>
                                <td className="border border-gray-300 p-2">{entry.supplier}</td>
                                <td className="border border-gray-300 p-2">{entry.restockPoint}</td>
                                <td className="border border-gray-300 p-2">{entry.restockCost}</td>
                                <td className="border border-gray-300 p-2">{entry.entryDate}</td>
                                <td className="border border-gray-300 p-2">{entry.quantity}</td>
                                <td className="border border-gray-300 p-2">{entry.unit}</td>
                                <td className="border border-gray-300 p-2">{entry.stockPrice}</td>
                                <td className="border border-gray-300 p-2">{entry.stockLocation}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </main>
        </div>
    );
};

export default EntriesPage;
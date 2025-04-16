"use client"
import Link from 'next/link';
import React from 'react';

const SupplierRegistrationPage: React.FC = () => {
    const suppliersData = [
        // Example supplier data
        {
            name: 'Fornecedor de Produtos do Brasil',
            email: 'emaildofornecedor@gmail.com',
            whatsapp: '(88) 88888-8888',
            cellphone: '(88) 88888-8888',
            telephone: '(88) 88888-8888',
            addressstreet: 'R. dos Fornecedores',
            addressnumber: '888',
            addresscomplement: 'Fábrica',
            addresscity: 'Fortaleza',
            addressstate: 'Ceará',
            addresscountry: 'Brasil',
            addresszipcode: '00000-000',
            cpf_cnpj: '88.888.888/0001-88'
        },
        // Add more supplier as needed
    ];

    const handleAddSupplier = () => {
        // Logic to add a new supplier
        console.log("Add Supplier");
    };

    const handleEditSupplier = (code: string) => {
        // Logic to edit an supplier based on the code
        console.log("Edit Supplier", code);
    };

    const handleDeleteSupplier = (code: string) => {
        // Logic to delete an supplier based on the code
        console.log("Delete Supplier", code);
    };

    return (
        <div className="flex">
            <aside className="w-1/12 bg-blue-800 text-white p-4">
                <h2 className="text-center text-lg font-bold mb-4">Cadastro de Fornecedores</h2>
                <Link href="/products" className="block mb-3 text-center">Controle de Estoque</Link>
                <Link href="/entries" className="block mb-3 text-center">Entradas de Estoque</Link>
                <Link href="/exits" className="block mb-3 text-center">Saídas de Estoque</Link>
                <Link href="/register" className="block mb-3 text-center">Cadastro de Produtos</Link>
                <Link href="/customers" className="block mb-3 text-center">Cadastro de Clientes</Link>
                <Link href="/generate-inventory" className="block mb-3 text-center">Gerar Inventário</Link>
                <Link href="/export-report" className="block mb-3 text-center">Exportar Relatório</Link>
            </aside>
            <main className="flex-1 p-4">
                <h1 className="text-3xl font-bold mb-6">Localização de Fornecedores</h1>

                <div className="mb-4">
                    <button type="button" onClick={handleAddSupplier} className="bg-blue-500 text-white px-4 py-2 rounded mr-2">Adicionar Fornecedor</button>
                    <button type="button" onClick={() => handleEditSupplier('AB01')} className="bg-yellow-500 text-white px-4 py-2 rounded mr-2">Editar Fornecedor</button>
                    <button type="button" onClick={() => handleDeleteSupplier('AB01')} className="bg-red-500 text-white px-4 py-2 rounded">Excluir Fornecedor</button>
                </div>

                <div className="grid grid-cols-1 gap-4">
                    <div className="flex flex-col">
                        <label className="mb-1">Nome do Fornecedor</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Fornecedor de Produtos do Brasil" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">e-mail</label>
                        <input type="email" className="border border-gray-300 p-2" placeholder="emaildofornecedor@gmail.com" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">WhatsApp</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="(88) 88888-8888" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Celular</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="(88) 88888-8888" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Fixo/Celular 2</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="(88) 88888-8888" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Endereço Rua</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="R. dos Fornecedores" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Endereço Número</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="888" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Complemento</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Fábrica" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Cidade</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Fortaleza" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Estado</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Ceará" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">País</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Brasil" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">CEP</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="00000-000" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">CNPJ/CPF</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="88.888.888/0001-88" />
                    </div>
                </div>                    
            </main>
        </div>
    );
};

export default SupplierRegistrationPage;
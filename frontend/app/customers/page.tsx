"use client"
import Link from 'next/link';
import React from 'react';

const CustomerRegistrationPage: React.FC = () => {
    const customersData = [
        // Example customer data
        {
            name: 'Cliente VIP Preferencial',
            email: 'emaildocliente@gmail.com',
            whatsapp: '(88) 88888-8888',
            cellphone: '(88) 88888-8888',
            telephone: '(88) 88888-8888',
            addressstreet: 'R. dos Clientes',
            addressnumber: '888',
            addresscomplement: 'Apto 88',
            addresscity: 'Cuiabá',
            addressstate: 'Mato Grosso',
            addresscountry: 'Brasil',
            addresszipcode: '00000-000',
            cpf_cnpj: '88.888.888/0001-88'
        },
        // Add more customer as needed
    ];

    const handleAddCustomer = () => {
        // Logic to add a new customer
        console.log("Add Customer");
    };

    const handleEditCustomer = (code: string) => {
        // Logic to edit an customer based on the code
        console.log("Edit Customer", code);
    };

    const handleDeleteCustomer = (code: string) => {
        // Logic to delete an customer based on the code
        console.log("Delete Customer", code);
    };

    return (
        <div className="flex">
            <aside className="w-1/12 bg-blue-800 text-white p-4">
                <h2 className="text-center text-lg font-bold mb-4">Cadastro de Clientes</h2>
                <Link href="/products" className="block mb-3 text-center">Controle de Estoque</Link>
                <Link href="/entries" className="block mb-3 text-center">Entradas de Estoque</Link>
                <Link href="/exits" className="block mb-3 text-center">Saídas de Estoque</Link>
                <Link href="/register" className="block mb-3 text-center">Cadastro de Produtos</Link>
                <Link href="/suppliers" className="block mb-3 text-center">Cadastro de Fornecedores</Link>
                <Link href="/generate-inventory" className="block mb-3 text-center">Gerar Inventário</Link>
                <Link href="/export-report" className="block mb-3 text-center">Exportar Relatório</Link>
            </aside>
            <main className="flex-1 p-4">
                <h1 className="text-3xl font-bold mb-6">Localização de Clientes</h1>

                <div className="mb-4">
                    <button type="button" onClick={handleAddCustomer} className="bg-blue-500 text-white px-4 py-2 rounded mr-2">Adicionar Cliente</button>
                    <button type="button" onClick={() => handleEditCustomer('AB01')} className="bg-yellow-500 text-white px-4 py-2 rounded mr-2">Editar Cliente</button>
                    <button type="button" onClick={() => handleDeleteCustomer('AB01')} className="bg-red-500 text-white px-4 py-2 rounded">Excluir Cliente</button>
                </div>

                <div className="grid grid-cols-1 gap-4">
                    <div className="flex flex-col">
                        <label className="mb-1">Nome do Cliente</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Cliente VIP Preferencial" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">e-mail</label>
                        <input type="email" className="border border-gray-300 p-2" placeholder="emaildocliente@gmail.com" />
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
                        <input type="text" className="border border-gray-300 p-2" placeholder="R. dos Clientes" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Endereço Número</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="888" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Complemento</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Apto 88" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Cidade</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Cuiabá" />
                    </div>
                    <div className="flex flex-col">
                        <label className="mb-1">Estado</label>
                        <input type="text" className="border border-gray-300 p-2" placeholder="Mato Grosso" />
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

export default CustomerRegistrationPage;
import Link from 'next/link';
import Image from 'next/image';

const products = [
    { id: 1, code: 'AB01', barcode: '123123123123', description: 'ABJNDKSMMOIJOIIONIPPDOPJOPJJ', restockPoint: 5, cost: 1.25, stock: 200, unit: 'Peça', location: 'ABCD0001' },
    { id: 2, code: 'AB02', barcode: '123123123123', description: 'DDFKLNDFINOPDFNIOSDNMMMMM', restockPoint: 7, cost: 1.25, stock: 200, unit: 'Peça', location: 'ABCD0002' },
    { id: 3, code: 'AB07', barcode: '123123123123', description: 'ABJNDKSMMOIJOIIONIPPDOPJOPJJ', restockPoint: 8, cost: 1.25, stock: 200, unit: 'Peça', location: 'ABCD0003' },
    // Add more products as needed
];

export default function Page() {
    return (
        <div className="flex">
            <aside className="w-1/12 bg-blue-800 text-white p-4">
                <h2 className="text-center text-lg font-bold mb-4">Controle de Estoque</h2>
                <Link href="/entries" className="block mb-3 text-center">Entradas de Estoque</Link>
                <Link href="/exits" className="block mb-3 text-center">Saídas de Estoque</Link>
                <Link href="/register" className="block mb-3 text-center">Cadastro de Produtos</Link>
                <Link href="/suppliers" className="block mb-3 text-center">Cadastro de Fornecedores</Link>
                <Link href="/customers" className="block mb-3 text-center">Cadastro de Clientes</Link>
                <Link href="/generate-inventory" className="block mb-3 text-center">Gerar Inventário</Link>
                <Link href="/export-report" className="block mb-3 text-center">Exportar Relatório</Link>
            </aside>
            <main className="flex-1 p-4">
                <h1 className="text-3xl font-bold mb-6">Localização de Produtos</h1>
                <table className="min-w-full border-collapse border border-gray-300">
                    <thead>
                        <tr className="bg-gray-200">
                            <th className="border border-gray-300 p-2">Código do Produto</th>
                            <th className="border border-gray-300 p-2">Barcode do Produto</th>
                            <th className="border border-gray-300 p-2">Descrição</th>
                            <th className="border border-gray-300 p-2">Ponto de Reposição</th>
                            <th className="border border-gray-300 p-2">Custo de Reposição</th>
                            <th className="border border-gray-300 p-2">Saldo Atualizado</th>
                            <th className="border border-gray-300 p-2">Unidade</th>
                            <th className="border border-gray-300 p-2">Local de Estoque</th>
                        </tr>
                    </thead>
                    <tbody>
                        {products.map(product => (
                            <tr key={product.id} className="hover:bg-gray-100">
                                <td className="border border-gray-300 p-2">{product.code}</td>
                                <td className="border border-gray-300 p-2">{product.barcode}</td>
                                <td className="border border-gray-300 p-2">{product.description}</td>
                                <td className="border border-gray-300 p-2">{product.restockPoint}</td>
                                <td className="border border-gray-300 p-2">{product.cost}</td>
                                <td className="border border-gray-300 p-2">{product.stock}</td>
                                <td className="border border-gray-300 p-2">{product.unit}</td>
                                <td className="border border-gray-300 p-2">{product.location}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </main>
        </div>
    );
} 
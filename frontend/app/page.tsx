import Link from 'next/link';

export default function Home() {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
            <h2 className="text-3xl font-bold text-center text-gray-800 mb-4">
                Bem-vindo ao DRS Stock Control Software
            </h2>
            <p className="text-lg text-center text-gray-600 mb-6">
                Gerencie seu estoque, entradas, saídas e fornecedores de forma eficiente.
            </p>
            <Link href="/products">
                <button className="bg-blue-500 text-white font-semibold py-2 px-4 rounded shadow hover:bg-blue-600 transition duration-200">
                    Acessar Estoque de Produtos
                </button>
            </Link>
        </div>
    );
}

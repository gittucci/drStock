import Link from 'next/link';

export default function LoginPage() {
    const handleLogin = () => {
        // Implement login logic here
        // After successful login, redirect to products page
        window.location.href = '/products-page';
    };

    return (
        <div>
            <h1>Login</h1>
            <button onClick={handleLogin}>Login</button>
            <Link href="/">Back to Home</Link>
        </div>
    );
} 
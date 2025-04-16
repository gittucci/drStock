import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";
import { NextResponse } from "next/server";

const isProtectedRoute = createRouteMatcher(['/']);

function redirectToSignIn(options?: SignInRedirectOptions): Promise<unknown>

export default clerkMiddleware(async (auth, req) => {
    const { userId, sessionClaims, redirectToSignIn } = await auth()

//   If the user isn't signed in and the route is private, redirect to sign-in

    if (!userId && isProtectedRoute(req)) {
        return redirectToSignIn({ returnBackUrl: req.url })
    }
//   If the user is logged and the route is protected, let then view
    if (userId && isProtectedRoute(req)) {
        return NextResponse.next();
    }

});

export const config = {
    matcher: ["/((?!.*\\..*|_next).*)", "/", "/(api|trpc)(.*)"]
};

export const routes = {
    products: '/products',
    entries: '/entries',
    exits: '/exits',
    suppliers: '/suppliers',   
    customers: '/customers',
};
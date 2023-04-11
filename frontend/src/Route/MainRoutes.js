import React from 'react';
import { Route, Routes } from "react-router-dom";
import HomePage from '../pages/HomePage';
import UserPage from '../pages/UserPage';
import Login from '../components/User/components/Login/Login';
import SignIn from '../components/User/components/SignIn/SignIn';
import CreateVideo from '../components/User/components/CreateVideo/CreateVideo';
const MainRoutes = () => {
    const PUBLIC_ROUTES = [
        {link: '/', element: <HomePage/>, id:1},
        {link: '/user', element: <UserPage/>, id:2},
        {link: '/user/login', element: <SignIn/>, id:3},
        {link: '/user/register', element: <Login/>, id:4},
        {link: '/user/create_video', element: <CreateVideo/>, id:5},
    ]
    return (
        <>
        <Routes>
            {PUBLIC_ROUTES.map((item) => (
            <Route path={item.link} element={item.element} key={item.id} />
            ))}
        </Routes>
        </>
    );
};

export default MainRoutes;
import React, { useState, useEffect } from 'react';
import { BrowserRouter, HashRouter } from 'react-router-dom';
import Helmet from 'react-helmet';
import { ToastContainer, Slide, toast } from 'react-toastify';

import Router from 'routes';

import { getUser, authorize } from 'services/api';


import favicon from './assets/images/aaklogo.ico';
import 'react-toastify/dist/ReactToastify.css';



const Layout = () => {
	return <>
		<Helmet>
			<title> Graphy </title>{' '}
			<link rel="icon" type="image/png" href={favicon} sizes="16x16" />
		</Helmet>
		<HashRouter>
			<Router> </Router>
		</HashRouter>
		<ToastContainer
			position="top-right"
			autoClose={2000}
			hideProgressBar={false}
			newestOnTop={false}
			closeOnClick
			rtl={false}
			pauseOnFocusLoss
			draggable
			pauseOnHover
			theme="light"
			transition={Slide}
		/>
	</>
}

const App = () => {
	return (
		<Layout />
	);
};

export default App;

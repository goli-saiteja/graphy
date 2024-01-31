import React, { useEffect } from 'react';
import { Routes } from 'react-router-dom';

//pages
import Metrics from 'pages/Metrics';
import Categories from 'pages/Categories';
import Events from 'pages/Events';
import Search from 'pages/Search';
import BulkProcess from 'pages/BulkProcess';
import PageNotFound from "pages/PageNotFound";

//layouts
import HeaderLayout from 'layouts/HeaderLayout';
import HeaderMenuLayout from 'layouts/HeaderMenuLayout';

import { getRoute } from './routers';

const pages = [
	{
		path: '/',
		element: <Metrics />,
		layout: HeaderMenuLayout,
	},
	{
		path: '/events/:page_type?/:select_type?/',
		element: <Events />,
		layout: HeaderMenuLayout,
	},
	{
		path: '/search/:select_type?/:page_type?/:filter_key?/:filter_value?/',
		element: <Search />,
		layout: HeaderMenuLayout,
	},
	{
		path: '/categories',
		element: <Categories />,
		layout: HeaderMenuLayout,
		redirect: "/",
	},
	{
		path: '/bulk-process',
		element: <BulkProcess />,
		layout: HeaderMenuLayout,
		redirect: "/"
	},
	{
		path: '*',
		element: <PageNotFound />,
		layout: HeaderLayout,
	},
	
];

function Router() {
	useEffect(() => {
		//console.log('router rendered');
	});

	return <Routes>{pages.map((page) => getRoute(page))}</Routes>;
}
export default Router;

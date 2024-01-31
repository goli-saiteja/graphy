import React, { useState } from 'react';
import { Outlet, NavLink } from 'react-router-dom';
import {
	SquaresFour,
	CalendarBlank,
	MagnifyingGlass,
	TreeStructure,
	Gear,
} from 'phosphor-react';
import './LeftMenu.scss';

const MenuItem = (props) => {
	const { title, icon: Icon, link } = props;

	return (
		<NavLink
			to={link}
			className={({ isActive }) => (isActive ? 'menu-item active' : 'menu-item')}
		>
			<div className="menu-icon">
				<Icon />
			</div>
			<div className="menu-title">{title}</div>
		</NavLink>
	);
};

function LeftMenu() {
	const menu =  [
		{ title: 'Metrics', icon: SquaresFour, link: '/', shouldDisplay: true },
		{ title: 'Events', icon: CalendarBlank, link: '/events', shouldDisplay: true },
		{ title: 'Search', icon: MagnifyingGlass, link: '/search', shouldDisplay: true },
		{ title: 'Categories', icon: TreeStructure, link: '/categories', shouldDisplay: true },
		{ title: 'Bulk Process', icon: Gear, link: '/bulk-process', shouldDisplay: true},
	];
	return (
		<div className="left-menu-container">
			{menu.filter(({ shouldDisplay }) => shouldDisplay).map(({ title, icon, link }, menuItemId) => (
				<MenuItem
					key={menuItemId}
					title={title}
					icon={icon}
					link={link}
				/>
			))}
		</div>
	);
}

export default LeftMenu;

import React, { useState, useEffect, useRef } from 'react';
import { Link } from 'react-router-dom';
import { CaretDown, SignOut } from 'phosphor-react';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import Grow from '@mui/material/Grow';
import Paper from '@mui/material/Paper';
import Popper from '@mui/material/Popper';
import MenuItem from '@mui/material/MenuItem';
import MenuList from '@mui/material/MenuList';


// import logo from 'assets/images/apple-vector-logo.svg';
import logo from 'assets/images/aaklogo.png';
import './Header.scss';

function Header() {
	const userName = `Saiteja Goli`;
	const [open, setOpen] = useState(false);
	const anchorRef = useRef(null);
	const handleToggle = () => {
		setOpen((prevOpen) => !prevOpen);
	};

	const handleClose = (event) => {
		if (anchorRef.current && anchorRef.current.contains(event.target)) {
			return;
		}

		setOpen(false);
	};

	const logout = () => {
		window.location = "/logout";
	}

	function handleListKeyDown(event) {
		if (event.key === 'Tab') {
			event.preventDefault();
			setOpen(false);
		} else if (event.key === 'Escape') {
			setOpen(false);
		}
	}

	// return focus to the button when we transitioned from !open -> open
	const prevOpen = React.useRef(open);
	React.useEffect(() => {
		if (prevOpen.current === true && open === false) {
			anchorRef.current.focus();
		}

		prevOpen.current = open;
	}, [open]);

	return (
		<div className="header-container">
			<Link to="/" >
				<div className="logo" >
					<img className="logo-img" src={logo} />
					{/* <div className="logo-title">Graphy</div> */}
				</div>
			</Link>
			<div className="username-block" onClick={handleToggle}>
				<div className="username">{userName}</div>
				<CaretDown size={13} weight="fill" ref={anchorRef} />
			</div>
			<Popper
				open={open}
				anchorEl={anchorRef.current}
				role={undefined}
				placement="bottom-end"
				transition
				disablePortal
			>
				{({ TransitionProps, placement }) => (
					<Grow
						{...TransitionProps}
						style={{
							transformOrigin:
								placement === 'bottom-start' ? 'left top' : 'left bottom',
						}}
					>
						<Paper>
							<ClickAwayListener onClickAway={handleClose}>
								<MenuList
									autoFocusItem={open}
									id="composition-menu"
									aria-labelledby="composition-button"
									onKeyDown={handleListKeyDown}
								>
									<MenuItem onClick={logout} className>
										<SignOut size={12} weight="bold" />
										Logout
									</MenuItem>
								</MenuList>
							</ClickAwayListener>
						</Paper>
					</Grow>
				)}
			</Popper>
		</div>
	);
}

export default Header;

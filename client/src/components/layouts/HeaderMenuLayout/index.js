import React from 'react';

import Header from 'base/Header';
import LeftMenu from 'base/LeftMenu';
import './HeaderMenuLayout.scss';

function HeaderMenuLayout(props) {
    return (
        <div className="header-menu-layout-container">
            <Header />
            <div className="main-container">
                <div className="aside-container">
                    <LeftMenu />
                </div>
                <div className="content-container">
                    {props?.children}
                </div>
            </div>
        </div>
    )
}

export default HeaderMenuLayout;
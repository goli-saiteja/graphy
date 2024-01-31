import React from 'react';

import Header from 'base/Header';
import './HeaderLayout.scss';

function HeaderLayout (props) {
    return (
        <div className="header-layout-container">
            <Header />
            <div className="main-container">
                {props?.children}
            </div>
        </div>
    )
}

export default HeaderLayout;
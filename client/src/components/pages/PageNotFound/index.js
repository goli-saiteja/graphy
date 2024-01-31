import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { CaretRight } from 'phosphor-react';
import './PageNotFound.scss';

function PageNotFound () {

    useEffect(() => {

    }, []);

    return (
        <div className='page-not-found-container'>
            <h1>The page you’re looking</h1>
            <h1>for can’t be found.</h1>
            <Link to={`/`}>Or go to Applications <CaretRight size={20} weight="light" /></Link>
        </div>
    )
}
export default PageNotFound;
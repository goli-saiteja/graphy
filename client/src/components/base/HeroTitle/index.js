import React from 'react';
import "./HeroTitle.scss";

function HeroTitle(props) {
	const { title, description } = props;
	return (
		<div className="hero-title-container">
			<div className="title">{title}</div>
			<div className="description">{description}</div>
		</div>
	);
}

export default HeroTitle;

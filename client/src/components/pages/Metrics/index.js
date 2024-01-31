import React, { useState, useEffect } from 'react';
import HeroTitle from 'base/HeroTitle';
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

import { getMetrics, getDepartments } from 'services/api';

import './Metrics.scss';

ChartJS.register(
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend
);

const options = {
	plugins: {
		title: {
			display: true,
			text: 'AAK TELE-SCIENCE - Total Employee Count',
			fullSize: true,
			font: {
				size: 18
			}
		},
	},
	maintainAspectRatio : false,
	scales: {
		x: {
			stacked: true,
			ticks: {
                font: {
					weight: "normal",
                    size: 12,
                }
            }
		},
		y: {
			stacked: true,
		},
	},
};

function Metrics() {
	const [data, setData] = useState({});
	const [labels, setLabels] = useState([]);
	const [chartData, setChartData] = useState({});
	let labelInfo = {
		"others": {
			color: "#B0B6C5",
			datasets: []
		},
		"operations": {
			color: "#F8A85E",
			datasets: []
		},
		"entrepreneurship": {
			color: "#6360AA",
			datasets: []
		},
		
		"arts_and_design": {
			color: "#FF8780",
			datasets: []
		},
		"consulting": {
			color: "#B30100",
			datasets: []
		},
		"education": {
			color: "#FFCD56",
			datasets: []
		},

		"marketing": {
			color: "#4AC0C0",
			datasets: []
		},
		"accounting": {
			color: "#82B67E",
			datasets: []
		},
		"data_science": {
			color: "#B7359F",
			datasets: []
		},
		"engineering": {
			color: "#627CE2",
			datasets: []
		}

	};

	const fetchData = async () => {
		let data = await getDepartments();
		const labels = data.reduce((acc, item) => {
			const fn = item.start_date;
			if (!acc.includes(fn)) {
				acc.push(fn)
			}
			return acc;
		}, []);

		setData(data);
		setLabels(labels);
		console.log("data", labels);
	};

	useEffect(() => {
		if (Object.keys(data).length) {
			labels.forEach(startDate => {
				Object.keys(labelInfo).forEach(fn => {
					// debugger;
					const fnObj = data.find(item => {
						const { start_date, functions } = item;
						return startDate === start_date && fn === functions
					});
					labelInfo[fn].datasets.push(fnObj?.retained || 0);
				})
			});
			let chartObj = {
				labels,
				datasets: Object.entries(labelInfo).map(department => {
					const [fn, departmentObj] = department;
					return {
						label: fn,
						data: departmentObj.datasets,
						backgroundColor: departmentObj.color,
					}
				})
			};
			console.log("chartObj", chartObj)
			setChartData(chartObj);
		}
	}, [data])

	useEffect(() => {
		fetchData();
	}, []);

	return (
		<div className="Metrics-container">
			<HeroTitle title="AAK TELE-SCIENCE" description="Employee details" />
			<div style={{maxWidth: "calc(100vw - 400px)", margin: "auto", minHeight: "calc(100vh - 200px)"}}>
				{
					!!Object.keys(chartData).length && <Bar options={options} data={chartData} />
				}
			</div>
		</div>
	);
}

export default Metrics;

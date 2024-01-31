const webpack = require('webpack');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

const webpackMockServer = require('webpack-mock-server');

const path = require('path');

const config = require('./src/config/development.json');

module.exports = merge(common, {
	mode: 'development',
	devServer: {
		port: '3020',
		static: {
			directory: path.join(__dirname, 'public'),
		},
		historyApiFallback: true,
		open: true,
		hot: true,
		liveReload: true,
		
	},
	plugins: [
		new HtmlWebpackPlugin({
			template: path.resolve(__dirname, 'public', 'index.html'),
		}),
		new webpack.DefinePlugin({
			config: JSON.stringify(config),
			'__REACT_DEVTOOLS_GLOBAL_HOOK__': '({ isDisabled: true })'
		}),
	],
});

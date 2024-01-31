const webpack = require('webpack');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

const webpackMockServer = require('webpack-mock-server');

const path = require('path');

const config = require('./src/config/production.json');

module.exports = merge(common, {
	mode: 'production',
	output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].[hash:8].js',
        sourceMapFilename: '[name].[hash:8].map',
        chunkFilename: '[id].[hash:8].js'
    },
	plugins: [
		new HtmlWebpackPlugin({
			template: path.resolve(__dirname, 'public', 'index.html'),
		}),
		new webpack.DefinePlugin({
			config: JSON.stringify(config),
			'__REACT_DEVTOOLS_GLOBAL_HOOK__': '({ isDisabled: true })'
		}),
		new CopyWebpackPlugin({
			patterns: [
				{ from: path.resolve(__dirname, 'public', 'static')}
			]
		})
	],
});

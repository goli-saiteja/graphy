const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
module.exports = {
	entry: './src/index.js',
	output: {
		filename: '[name].[contenthash].js',
		path: path.resolve(__dirname, './dist'),
		clean: true,
	},
	optimization: {
		moduleIds: 'deterministic',
		runtimeChunk: 'single',
		splitChunks: {
			cacheGroups: {
				vendor: {
					test: /[\\/]node_modules[\\/]/,
					name: 'vendors',
					chunks: 'all',
				},
			},
		},
	},

	resolve: {
		extensions: ['.js', '.jsx', '.json'],
		alias: {
			api: path.resolve(__dirname, 'src/services/http/api'),
			assets: path.resolve(__dirname, 'src/assets/'),
			base: path.resolve(__dirname, 'src/components/base/'),
			components: path.resolve(__dirname, 'src/components/'),
			config: path.resolve(__dirname, 'src/config/'),
			constants: path.resolve(__dirname, 'src/constants/'),
			fonts: path.resolve(__dirname, 'src/assets/fonts/'),
			images: path.resolve(__dirname, 'src/assets/images/'),
			layouts: path.resolve(__dirname, 'src/components/layouts/'),
			pages: path.resolve(__dirname, 'src/components/pages/'),
			routes: path.resolve(__dirname, 'src/routes/'),
			services: path.resolve(__dirname, 'src/services/'),
			styles: path.resolve(__dirname, 'src/styles/'),
			global: path.resolve(__dirname, 'src/styles/_global.scss'),
		},
	},
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: 'babel-loader',
			},
			{
				//This rule converts all .scss files to the .css. This convertion is required because browers can only understand css so all the scss code must be converted to the browser understandble css code.
				test: /\.s?css$/,
				use: [
					{
						loader: 'style-loader', // creates style nodes from JS strings
					},
					{
						loader: 'css-loader', // translates CSS into CommonJS
					},
					{
						loader: 'sass-loader', // compiles Sass to CSS
					},
				],
			},
			{
				//This rule is used to import images and fonts in the .scss files
				test: /\.(svg|gif|jpe?g|png|ico|mov)$/,
				use: [{ loader: 'url-loader?limit=100000' }],
			},
			{
				test: /\.(woff|woff2|eot|ttf|otf)$/i,
				type: 'asset/resource',
			},
		],
	},
};

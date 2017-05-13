var path = require('path');
var webpack = require('webpack');

// we write in JSX, and this converts JSX to javascript
// this tells webpack where to get the scripts, and where to output the javascript
module.exports = { 

    entry: [path.resolve(__dirname, 'src') + '/app/index.js'], // get cwd + src + /app/index.js
    output: { // output the imports (require) in index.js
        path: path.resolve(__dirname, 'dist') + '/app', // create the transformed javascript here
        filename: 'bundle.js',
        publicPath: '/app/' // the path index.html script uses
    },
    module: {
        loaders: [
            {
                test: /\.js$/, // regex looking for .js to convert to javascript
                include: path.resolve(__dirname, 'src'),
                loader: 'babel-loader',
                query: {
                    presets: ['react', 'es2015', 'react-hmre']
                }
            },
            {
                test: /\.css$/, // converting css
                loader: 'style-loader!css-loader'
            }
        ]
    },
    devServer: {
        historyApiFallback: true // back button works properly
    }, 
    plugins: [
        new webpack.ProvidePlugin({ // lets u use jquery
            $: 'jquery', 
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        }),
    ]
};
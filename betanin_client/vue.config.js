const webpack = require('webpack');

module.exports = {
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        '__NODE_ENV__': JSON.stringify(process.env.NODE_ENV || '')
      })
    ]
  }
}

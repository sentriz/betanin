const webpack = require('webpack');

module.exports = {
  configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
        '__SOURCE_COMMIT__': JSON.stringify(process.env.SOURCE_COMMIT || '')
      })
    ]
  }
}

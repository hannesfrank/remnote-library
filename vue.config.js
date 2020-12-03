module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/remnote-library/" : "/",
  devServer: {
    host: "0.0.0.0",
    https: true,
    disableHostCheck: true,
    port: 8080,
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    useLocalIp: false,
  },
};

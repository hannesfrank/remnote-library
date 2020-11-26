module.exports = {
    devServer: {
        host: '0.0.0.0',
        https: true,
        disableHostCheck: true,
        port: 8080,
        headers: {
            'Access-Control-Allow-Origin': '*'
        },
        useLocalIp: false,
    }
}
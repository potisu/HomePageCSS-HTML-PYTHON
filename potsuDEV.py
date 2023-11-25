import http.server
import socketserver

port = 8000

custom_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>potsuDEV</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap">
    <style>
        body {
            height: 1vh;
            margin: 0;
            padding: 0;
            background: url('imagens/soma.jpg') no-repeat center center fixed;
            background-size: 119%;
            font-family: 'Roboto Mono', monospace;
            overflow: hidden;
            animation: slidein 20s infinite alternate;
        }

        @keyframes slidein {
            0%, 50% { background-position: top; }
            25%, 75% { background-position: -100px 0px; }
        }

        .centerBox {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 600px;
        }

        .categoryWrapper {
            height: 310px;
            width: 460px;
            background: url("http://ohlookawebsite.com/bathroomtestfull.jpg") no-repeat center center;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        .categoryWrapper:after {
            position: absolute;
            top:0;
            left: 0;
            right:0;
            bottom: 0;
            background: #a29ca9;
            content: '';
            opacity: 0;
            transition: opacity 0.9s ease 0s; 
        }

        .categoryWrapper:hover:after {
            opacity: 0.4;
        }

        .categoryWrapper h1 {
            color:white;
            font-size: 50px;
            letter-spacing: 2px;
            transition: all 0.15s ease 0s; 
            position: relative;
            z-index: 10;
        }

        .categoryWrapper:hover h1 {
            transform: translateY(-10px);
        }

        .categoryWrapper button {
            position: absolute;
            transform: translateY(60px);
            -webkit-appearance: none;
            border: none;
            background: none;
            color:white;
            width: 250px;
            height:50px;
            font-size: 20px;
            padding: 0;
            margin: 0;
            outline: none;
            z-index: 10;
        }

        .categoryWrapper button span {
            display: block;
            position: relative;
            line-height: 50px;
            height: 50px;
            cursor: pointer;
        }

        .categoryWrapper button > span:after {
            content:'';
            position: absolute;
            top:0;
            left: 50%;
            width: 20px;
            height: 0;

            border: 1px solid white;
            border-left: none;
            border-bottom: none;

            transition: height 0.15s ease-out, width 0.15s ease-out 0.15s;
        }

        .categoryWrapper:hover button > span:after {
            width: calc(50% - 1px);
            height: calc(100% - 2px);
            transition: width 0.15s ease-out, height 0.15s ease-out 0.15s;
        }

        .categoryWrapper button > span:before {
            content:'';
            position: absolute;
            top:0;
            right: 50%;
            width: 20px;
            height: 0;

            border: 1px solid white;
            border-right: none;
            border-bottom: none;

            transition: height 0.15s ease-out, width 0.15s ease-out 0.15s;
        }

        .categoryWrapper:hover button > span:before {
            width: calc(50% - 1px);
            height: calc(100% - 2px);
            transition: width 0.15s ease-out, height 0.15s ease-out 0.15s;
        }

        .categoryWrapper button > span > span:before {
            content:'';
            position: absolute;
            bottom:0;
            right: 0%;
            width: 1px;
            height: 1px;
            opacity: 0;
        }

        .categoryWrapper:hover button > span > span:before {
            opacity: 1;
            border-bottom: 1px solid white;
            width: calc(50%);
            height: 1px;
            transition: opacity 0s ease-out 0.29s, width 0.15s ease-out 0.3s;
        }

        .categoryWrapper button > span > span:after {
            content:'';
            position: absolute;
            bottom:0;
            left: 0%;
            width: 1px;
            height: 1px;
            opacity: 0;
        }

        .categoryWrapper:hover button > span > span:after {
            opacity: 1;
            border-bottom: 1px solid white;
            width: calc(50%);
            height: 1px;
            transition: opacity 0s ease-out 0.29s, width 0.15s ease-out 0.3s;
        }

        .categoryWrapper button > span > span > span {
            transition: color 0.15s ease-out 0.3s;
            color: transparent;
        }

        .categoryWrapper:hover button > span > span > span {
            color:white;
        }

        .categoryWrapper button > span > span > span:after {
            position: absolute;
            top:0;left:0;right:0;bottom:0;
            color:#1f2e4d;
            content: attr(data-attr-span);
            width: 0%;
            height: 100%;
            background:white;
            white-space: nowrap;
            text-align: center;
            margin: auto;
            overflow: hidden;
            display: flex;
            justify-content: center;
            transition: width 0.2s;
        }

        .categoryWrapper button:hover > span > span > span:after {
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="centerBox">
        <div class="categoryWrapper">
            <h1>My Store</h1>
            <button onclick="window.location.href='/products';">
                <span>
                    <span>
                        <span data-attr-span="Products">
                            Products
                        </span>
                    </span>
                </span>
            </button>
        </div>
    </div>
</body>
</html>

"""

with open("index.html", "w") as html_file:
    html_file.write(custom_html)

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Servindo na porta {port}")
    httpd.serve_forever()


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

        .seperator-wrapper {
            width: 100%;
            overflow: hidden;
        }

        .seperator {
            width: 3000px;
            height: 5px;
            background: rgb(48, 255, 144);
            background: -moz-linear-gradient(left, rgba(48, 255, 144, 1) 0%, rgba(237, 45, 237, 1) 25%, rgba(201, 152, 38, 1) 50%, rgba(48, 255, 230, 1) 75%, rgba(48, 255, 144, 1) 100%);
            background: -webkit-gradient(linear, left top, right top, color-stop(0%, rgba(48, 255, 144, 1)), color-stop(25%, rgba(237, 45, 237, 1)), color-stop(50%, rgba(201, 152, 38, 1)), color-stop(75%, rgba(48, 255, 230, 1)), color-stop(100%, rgba(48, 255, 144, 1)));
            background: -webkit-linear-gradient(left, rgba(48, 255, 144, 1) 0%, rgba(237, 45, 237, 1) 25%, rgba(201, 152, 38, 1) 50%, rgba(48, 255, 230, 1) 75%, rgba(48, 255, 144, 1) 100%);
            background: -o-linear-gradient(left, rgba(48, 255, 144, 1) 0%, rgba(237, 45, 237, 1) 25%, rgba(201, 152, 38, 1) 50%, rgba(48, 255, 230, 1) 75%, rgba(48, 255, 144, 1) 100%);
            background: -ms-linear-gradient(left, rgba(48, 255, 144, 1) 0%, rgba(237, 45, 237, 1) 25%, rgba(201, 152, 38, 1) 50%, rgba(48, 255, 230, 1) 75%, rgba(48, 255, 144, 1) 100%);
            background: linear-gradient(to right, rgba(48, 255, 144, 1) 0%, rgba(237, 45, 237, 1) 25%, rgba(201, 152, 38, 1) 50%, rgba(48, 255, 230, 1) 75%, rgba(48, 255, 144, 1) 100%);
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#30ff90', endColorstr='#30ff90', GradientType=1);
            animation: moveGradient 3s infinite linear;
        }

        @keyframes moveGradient {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(100%);
            }
        }

        .centerBox {
            display: flex;
            justify-content: flex-start;
            align-items: flex-start;
            height: 100vh;
        }

        .categoryWrapper {
            height: 150px;
            width: 200px;
            background: url("http://ohlookawebsite.com/bathroomtestfull.jpg") no-repeat center center;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            margin: 10px;
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
            font-size: 20px;
            letter-spacing: 2px;
            transition: all 0.15s ease 0s; 
            position: relative;
            z-index: 10;
        }

        .categoryWrapper:hover h1 {
            transform: translateY(-5px);
        }

        .categoryWrapper button {
            position: absolute;
            transform: translateY(30px);
            appearance: none;
            -webkit-appearance: none;
            border: none;
            background: none;
            color:white;
            width: 120px;
            height:30px;
            font-size: 12px;
            padding: 0;
            margin: 0;
            outline: none;
            z-index: 10;
        }

        .categoryWrapper button span {
            display: block;
            position: relative;
            line-height: 30px;
            height: 30px;
            cursor: pointer;
        }

        .categoryWrapper button > span:after {
            content:'';
            position: absolute;
            top:0;
            left: 50%;
            width: 10px;
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
            width: 10px;
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

        .categoryWrapper:hover button > span > span > span:after {
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="seperator-wrapper">
        <div class="seperator gradient"></div>
    </div>
    <div class="centerBox">
        <div class="categoryWrapper" style="position: absolute; top: 10px; left: 10px;">
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

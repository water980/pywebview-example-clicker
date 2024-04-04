import webview
from tkinter import messagebox

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .btn{
            display: flex;
            justify-content: center;
        }
        #btn{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        #btn1, #btn2, #btn3{
            display: inline-block;
            padding: 15px, 20px;
            font-size: 22px;
            font-weight: bold;
            text-transform: uppercase;
            text-decoration: none;
            border-radius: 50px;
            transition: background-color 0.3s, color 0.3s, transform 0.3s;
            border: none;
            cursor: pointer;
            background-color: rgb(255, 234, 44);
            color: white;
            box-shadow: 0px 8px 15px rgba(0,0,0,0.1);   
            width: 250px;
            height: 50px;

        }
        #btn1:hover, #btn2:hover, #btn3:hover{
            background-color: rgb(187, 255, 29);
            color: aliceblue;
            transform: translateY(-3px);
        }
        #btn1:active, #btn2:active, #btn3:active{
            transform: translateY(1px);
            box-shadow: none;
        }
        #lab{
            font-family: Verdana, Geneva, Tahoma, sans-serif;
        }
    </style>
</head>
<body style="background-color: rgb(4, 81, 197);">
    <h1 id = "lab", style = "text-align: center;">0</h1>
    <div id = "btn">
        <button id="btn1">+</button>
        <button id="btn2">0</button>
        <button id="btn3">-</button>
    </div>
    <script>
        const lab = document.getElementById("lab");
        const btn1 = document.getElementById("btn1");
        const btn2 = document.getElementById("btn2");
        const btn3 = document.getElementById("btn3");
        
        let count = 0;

        btn1.onclick = function(){
            count++;
            lab.textContent = count;
        }
        btn3.onclick = function(){
            count--;
            lab.textContent = count;
        }
        btn2.onclick = function(){
            count = 0;
            lab.textContent = count;
            pywebview.api.mss()
        }

        
    </script>
</body>
</html>
"""
class Api():
    def mss(self):
        messagebox.showinfo('Clicker', 'value = 0')


webview.create_window('clicker', html = html , js_api=Api())
webview.start()
const {app, BrowserWindow} = require('electron')
const {ipcMain} = require('electron')
const url = require('url')
const path = require('path')

const TcpServer = require("../GUI/Core/Network/TcpServer.js")


class Launcher {

    runMorizon(event, args)
    {
        console.log("morizon called");
    }
}

let win;
let server;
let launcher = new Launcher();

ipcMain.on('morizon', (event, args) => launcher.runMorizon(event, args))

function cmain()
{

    win = new BrowserWindow({width: 800, height: 600, webPreferences: { nodeIntegration: true, contextIsolation: false,}})
    win.webContents.openDevTools();
    win.loadURL(url.format ({ pathname: path.join(__dirname, 'Assets/HTML/index.html'),  protocol: 'file:',  slashes: true}))

    server = new TcpServer();
    server.start();
}


app.on('ready', cmain);
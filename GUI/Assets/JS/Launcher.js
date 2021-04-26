const {ipcRenderer} = require('electron');

class Launcher
{
    #start;
    #stop;
    #linksArea;

    #links = Array();

    constructor() {
        let self = this;

        this.#start = document.getElementById("start_btn");
        this.#stop = document.getElementById("stop_btn");
        this.#linksArea = document.getElementById("links_area");
        this.#start.addEventListener('click', function (evt){self.launch(self,evt);})
    }

    getSelectedVendor() {return document.querySelector('div[class *= "Vendor-checkbox-selected"]');}

    init_links() {
        if (this.#linksArea !== undefined)
        {
            const pastedLinks = this.#linksArea.value;
            if (pastedLinks.includes("\n"))
            {
                const links = pastedLinks.split("\n");
                if (links instanceof Array)
                {
                    links.forEach(function (link){
                        console.log(link);
                    })
                }
            }
        }
    }


    launch(parent, evt)
    {
        let selected = parent.getSelectedVendor();
        if (selected !== undefined)
        {
            const key = selected.getAttribute('key');
            if (key !== undefined)
            {
                parent.init_links();
                switch (key)
                {
                    case "morizon":

                        break;
                }
            }
        }
    }
    stop()
    {

    }
}


const launcher = new Launcher();
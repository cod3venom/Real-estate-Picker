class UI
{
    #root = document.getElementById("root");
    #vendor_checkbox;

    #vendorEnum = {
        checkbox_active: "Vendor-checkbox-selected",
    }
    constructor() {
        this.setVendorCheckBoxes(document.querySelectorAll('div[class="Vendor-checkbox centered"]'));
    }

    setVendorCheckBoxes(boxes) {this.#vendor_checkbox = boxes; }
    getVendorCheckBoxes() {return this.#vendor_checkbox;}


    async hook_elements()
    {
        let self = this;
        this.#vendor_checkbox.forEach(function (checkbox ){
            checkbox.addEventListener('click', async function (evt){
               self.handle_vendor_checkbox(self, evt).then();
            });
        });
    }

    async handle_vendor_checkbox(parent,evt)
    {
        document.querySelectorAll('div[class ^= "Vendor-checkbox centered Vendor-checkbox-selected"]')
            .forEach(e => e.classList.remove(parent.#vendorEnum.checkbox_active));

        const checkbox = evt.target;
        if (checkbox !== undefined){
            if (checkbox.tagName === "IMG"){
                checkbox.parentNode.classList.toggle(this.#vendorEnum.checkbox_active);
            }
            if (checkbox.tagName === "DIV"){
                checkbox.classList.toggle(this.#vendorEnum.checkbox_active);
            }
        }
    }

    async start()
    {
        this.hook_elements().then();
    }
}


const ui = new UI();
ui.start();
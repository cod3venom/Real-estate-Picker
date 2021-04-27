const carousel = document.querySelector("ul[class='list-unstyled list-inline imageBoxList']");
if (carousel !== undefined)
{
    const total_items = carousel.querySelectorAll("li").length;
    console.log(total_items);

    const next_button = document.querySelector("div[class^='controlsLeft imageBoxArrowLeft']");
    console.log(next_button);
    if (total_items !== undefined && next_button !== undefined)
    {
        for(let i=0; i < total_items; i++)
        {
            console.log(i);
            next_button.click();
        }
    }
}
if (!window.jQuery)
{
    let script = document.createElement("script");
    script.src = "https://code.jquery.com/jquery-3.6.0.slim.js";
    script.integrity = "sha256-HwWONEZrpuoh951cQD1ov2HUK5zA5DwJ1DNUXaM6FsY=";
    script.crossOrigin = "anonymous";
    script.id = "HUMANIZER_JQUERY";

    document.body.appendChild(script);
}


if (window.jQuery)
{
    function scrollToElement(element) {
        let target = $('SELECTOR;');
        if (target !== undefined && target !== null)
        {
            $('html, body').animate({ scrollTop: target.offset().top }, 1000);
        }
    }

    scrollToElement();
}
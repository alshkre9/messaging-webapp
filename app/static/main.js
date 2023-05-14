window.onload = function ()
{
    var pathname = window.location.pathname;
    if (pathname == "/sign-in" || pathname == "/sign-up")
    {
        document.getElementById("vh1").style.height = "100vh";
    }
    else if (pathname.includes("/search"))
    {
        document.getElementById("vh1").style.minHeight = "100vh";
    }
    else
    {
        document.getElementById("vh1").style.height = "auto";
        document.getElementById("vh2").style.height = "100vh";
    }
    // setTimeout(function(){document.body.style.opacity="100";},500);
}
let flag = 1
function change_width()
{
    if (flag == 1)
    {
        menu = document.getElementById("menu");
        document.getElementById("rotate").style.animation = "rotate-right 0.3s forwards";
        menu.style.width = "0%";
        menu.style.border = "none";
    }
    else
    {
        document.getElementById("rotate").style.animation = "rotate-left 0.3s forwards";
        document.getElementById("menu").style.width = null;
        menu.style.border = null;
    }
    flag *= -1
}
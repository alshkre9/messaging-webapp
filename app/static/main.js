window.onload = function ()
{
    var pathname = window.location.pathname;
    if (pathname === "/sign-in" || pathname === "/sign-up")
    {
        document.getElementById("vh1").style.height = "100vh";
    }
    else
    {
        document.getElementById("vh1").style.height = "auto";
        document.getElementById("vh2").style.height = "100vh"
    }
}
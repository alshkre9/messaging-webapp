window.onload = function ()
{
    document.querySelectorAll("#friends-groups li").forEach(
        function (item) {
            item.addEventListener("click", function ()
            {
                change_main_chat()
            }
            )
        }
    )

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
}

let flag = 1

function change_main_chat()
{
    menu = document.getElementById("menu");
    rotate = document.getElementById("rotate")
    content = document.getElementById("content")
    if (flag == 1)
    {
        rotate.style.animation = "rotate-right 0.3s forwards";
        menu.style.width = "0%";
        menu.style.border = "none";
        content.style.width = "100%";
    }
    else
    {
        if (content.offsetWidth == 0)
        {
            room = null;
        }
        menu.style.border = null;
        rotate.style.animation = "rotate-left 0.3s forwards";
        menu.style.width = null;
        content.style.width = null;
    }
    flag *= -1
}

function create_message(message_value, class_name)
{
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(message_value));
    li.classList.add("message", class_name);
    document.getElementById("messages").appendChild(li);
}
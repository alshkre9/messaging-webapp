window.onload = function ()
{
    document.querySelectorAll("#friends-groups li").forEach(
        function (item) {
            item.addEventListener("click", function ()
            {
                // 
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

function create_message(message_value, class_name)
{
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(message_value));
    li.classList.add("message", class_name);
    document.getElementById("messages").appendChild(li);
}
window.onload = function ()
{
    document.querySelectorAll("#friends-groups li").forEach(
        function (item) {
            item.addEventListener("click", function ()
            {
                if (item.id != room_id)
                {
                    room_id = item.id
                    socket.emit("join", room_id)
                }
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

    try
    {
        
        document.getElementById("note").innerText = parseInt(document.querySelectorAll("#sub-menu > li").length); 
        n = parseInt(document.getElementById("note").innerText); 
        if (n > 99)
        {
            document.getElementById("note").innerText = 99;
        }
        else if (n == 0 || isNaN(n))
        {
            document.getElementById("note").style.display = "none"
        }
        }
    catch(TypeError){}

}

function create_message(message_value, class_name)
{
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(message_value));
    li.classList.add("message", class_name);
    document.getElementById("messages").appendChild(li);
}

function valid_authentication()
{
    let pattren_username = /^(?:\d|\w){8,28}$/;
    let pattren_password = /^.{8,28}$/;
    username = document.getElementById("username").value;
    password = document.getElementById("password").value;
    confiramtion = null;
    submit_flag = false;
    try {
        confirmation = document.getElementById("confirmation").value
        if (toString(password) === toString(confiramtion))
        {
            if (pattren_username.test(username) && pattren_password.test(password))
            {
                submit_flag = true
            }
        }
    }
    catch(TypeError)
    {
        if (pattren_username.test(username) && pattren_password.test(password))
        {
            submit_flag = true
        }    
    }

    if (submit_flag)
    {
        document.getElementById("auth-form").submit()
    }
    else
    {
        document.getElementById("warning").style.display = "block"
    }
    return
}

notice_flag = 1
function show_notice()
{
    if (notice_flag == 1 && document.getElementById("note").innerText > 0)
    {
        document.getElementById("sub-menu").style.display = "flex";
        document.getElementById("sub-menu").style.animationName = "go-down";
        notice_flag *= -1
    }
    else
    {
        document.getElementById("sub-menu").style.display = null
        document.getElementById("sub-menu").style.animationName = "go-up";
        notice_flag *= -1
    }
    return
}
const mediaquery = window.matchMedia("(max-width: 576px)")
window.onload = function ()
{
    document.querySelectorAll("#friends-groups li").forEach(
        function (item) {
            item.addEventListener("click", function ()
            {
                if (item.id != room_id)
                {
                    document.getElementById("messages").innerHTML = "";
                    room_id = item.id;
                    socket.emit("join", room_id);
                    document.getElementById("active-chat").style.setProperty("display", "flex")
                    document.getElementById("friend-name").innerText = document.getElementById("friend-" + item.id).innerText;
                    document.getElementById("friend-picture").style.backgroundImage = document.getElementById("friend-" + item.id + "-picture").style.getPropertyValue("background-image");
                    if (mediaquery.matches)
                    {
                        document.getElementById("menu").setAttribute("style", "width: 0% ; min-width: 0%") 
                        document.getElementById("content").style.setProperty("width", "100%") 
                        document.getElementById("content").style.setProperty("display", "flex") 
                    }
                }
            }
            )
        }
        )   
        
        var pathname = window.location.pathname;
        if (pathname != "/sign-in" && pathname != "/sign-up")
        {
            document.getElementById("vh2").style.setProperty("height", "100vh");
        }
        
        try
        {
            
            document.getElementById("note").innerText = parseInt(document.querySelectorAll("#sub-menu > ul > li").length); 
            n = parseInt(document.getElementById("note").innerText); 
            if (n > 99)
            {
                document.getElementById("note").innerText = 99;
        }
        else if (n == 0 || isNaN(n))
        {
            document.getElementById("note").style.setProperty("display", "none", "important")
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
    confirmation = null;
    submit_flag = false;
    try {
        confirmation = document.getElementById("confirmation").value;
        if (password === confirmation)
        {
            if (pattren_username.test(username) && pattren_password.test(password))
            {
                submit_flag = true;
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
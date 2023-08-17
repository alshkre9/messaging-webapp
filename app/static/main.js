
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
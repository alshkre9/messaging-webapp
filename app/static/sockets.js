const socket = io();
let user_id = null;

// start connection by storing room_id
socket.on("user_id", function(id)
    {
        user_id = id;
    }
);

// receive_message from the server
socket.on("receive_message", function(message_value, from, date) {
    console.log([message_value, from, date])
        if (from === user_id)
        {
            // create message for the user
            create_message(message_value, "user-message", date);
        }
        else
        {
            // create message for a friend
            create_message(message_value, "friend-message", date);
        }
});

function send_message()
{
        message_value = document.getElementById("message").value;
        if (message_value)
        {
            document.getElementById("message").value = null;
            socket.emit('send_message', message_value);
        }
}

function create_message(message_value, class_name, date)
{
    const li = document.createElement("li");
    let p = document.createElement("p")
    let span = document.createElement("span");
    p.innerText = message_value
    p.classList += "message-value"
    span.innerText = date
    span.classList += "date"
    li.appendChild(p)
    li.appendChild(span)
    // li.classList.add("message", class_name);
    li.classList.add("message", class_name);
    document.getElementById("messages").appendChild(li);
}
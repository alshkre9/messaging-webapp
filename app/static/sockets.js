const socket = io();
let user_id = null;

// start connection by storing room_id
socket.on("user_id", function(id)
    {
        user_id = id;
    }
);

// receive_message from the server
socket.on("receive_message", function(message_value, from) {
        if (from == user_id)
        {
            // create message for the user
            create_message(message_value, "user-message");
        }
        else
        {
            // create message for a friend
            create_message(message_value, "friend-message");
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

function create_message(message_value, class_name)
{
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(message_value));
    li.classList.add("message", class_name);
    document.getElementById("messages").appendChild(li);
}
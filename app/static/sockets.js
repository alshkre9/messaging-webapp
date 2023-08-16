const socket = io();
let user_id = null;
let room_id = null

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
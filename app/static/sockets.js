const socket = io();
let user_id = null;

// start connection by storing user_id
socket.on("user_id", function(id)
    {
        user_id = id;
    }
);

// receive_message from the server
socket.on("receive_message", function(message_value, sender_id) {
    if (sender_id === user_id)
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
        document.getElementById("message").value = null;
        socket.emit('send_message', message_value, user_id);
}
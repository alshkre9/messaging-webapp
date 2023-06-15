const socket = io();
let user_room = null;
let to_room = null

// start connection by storing room_id
socket.on("user_room", function(id)
    {
        user_room = id;
    }
);


// receive_message from the server
socket.on("receive_message", function(message_value, from_room) {
    if (from_room === user_room)
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
            if (to_room)
            {
                document.getElementById("message").value = null;
                socket.emit('send_message', message_value, to_room);
            }
        }
}
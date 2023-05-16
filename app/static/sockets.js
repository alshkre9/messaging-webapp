const socket = io();
let room = null;

socket.on("receive_message", function(message_value) {
    if (message_value) {
        create_message(message_value, "friend-message");
    }
});

function message()
{
    message_value = document.getElementById("message").value;
    socket.emit('send_message', message_value, room);
    create_message(message_value, "user-message");
}
function join_room()
{
    socket.emit("join", "");
}

function create_message(message_value, class_name)
{
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(message_value));
    li.classList.add("message", class_name);
    document.getElementById("messages").appendChild(li);
}




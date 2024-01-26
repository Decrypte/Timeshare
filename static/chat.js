// chat.js
document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById('chat-form');
    var input = document.getElementById('chat-input');
    var chatContainer = document.getElementById('chat-container');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        if(input.value.trim() !== '') {
            addChatMessage(input.value, 'user');
            input.value = ''; // Clear the input box
            sendToServer(input.value);
        }
    });

    function addChatMessage(message, type) {
        var messageDiv = document.createElement('div');
        messageDiv.classList.add('chat-message', type === 'user' ? 'user-message' : 'bot-message');
        messageDiv.textContent = message;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function sendToServer(message) {
        // AJAX call to the server
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/ask", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                var response = JSON.parse(this.responseText);
                addChatMessage(response.answer, 'bot'); // Update chat with bot response
            }
        };
        xhr.send("question=" + encodeURIComponent(message));
    }
});

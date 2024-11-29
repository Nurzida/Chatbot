document.getElementById("send-btn").addEventListener("click", function () {
    let userInput = document.getElementById("user-input").value;

    if (userInput.trim() === "") {
        alert("Please enter a message.");
        return;
    }

    // Display user message
    displayMessage(userInput, "user");

    // Clear input field
    document.getElementById("user-input").value = "";

    // Send user input to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            userInput: userInput,
        }),
    })
    .then(response => response.json())
    .then(data => {
        // Display chatbot's response
        displayMessage(data.response, "bot");
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

document.getElementById("user-input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        document.getElementById("send-btn").click();
    }
});

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.classList.add(sender === "user" ? "user-message" : "bot-message");

    const icon = sender === "user"
        ? '<i class="fas fa-user-circle"></i>'  // Human icon
        : '<i class="fas fa-robot"></i>';       // Robot icon

    messageElement.innerHTML = `${icon} <span>${message}</span>`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
}

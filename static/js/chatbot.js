document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const suggestionButtons = document.querySelectorAll('.suggestion-btn');
    
    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = isUser ? 'user-message' : 'bot-message';
        
        if (isUser) {
            messageDiv.innerHTML = `<p><strong>You:</strong> ${message}</p>`;
        } else {
            // Format bot responses with better readability
            const formattedMessage = message
                .replace(/\n/g, '<br>')
                .replace(/(Section \d+)/g, '<strong>$1</strong>')
                .replace(/(\$\d+,?\d*)/g, '<strong>$1</strong>')
                .replace(/(Chapter \d+:\d+)/g, '<strong>$1</strong>');
                
            messageDiv.innerHTML = `<p><strong>Legal Assistant:</strong> ${formattedMessage}</p>`;
        }
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'bot-message error';
        errorDiv.innerHTML = `<p><strong>Legal Assistant:</strong> ${message}</p>`;
        chatMessages.appendChild(errorDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) {
            showError('Please enter a question.');
            return;
        }
        
        addMessage(message, true);
        userInput.value = '';
        sendButton.disabled = true;
        sendButton.textContent = 'Sending...';
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            
            if (data.status === 'success') {
                addMessage(data.response);
            } else {
                showError(data.response || 'Sorry, I encountered an error. Please try again.');
            }
            
        } catch (error) {
            console.error('Chat error:', error);
            showError('Sorry, I am currently unavailable. Please try again later or check our resource sections.');
        } finally {
            sendButton.disabled = false;
            sendButton.textContent = 'Send';
            userInput.focus();
        }
    }
    
    // Enhanced event listeners
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    suggestionButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const question = this.getAttribute('data-question');
            if (question) {
                userInput.value = question;
                sendMessage();
                
                // Add visual feedback
                this.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 150);
            }
        });
    });
    
    // Auto-focus on input
    setTimeout(() => {
        userInput.focus();
    }, 1000);
    
    // Clear initial categories when user starts typing
    userInput.addEventListener('input', function() {
        const initialCategories = document.querySelector('.quick-categories');
        if (initialCategories && this.value.length > 0) {
            initialCategories.style.opacity = '0.6';
        } else if (initialCategories) {
            initialCategories.style.opacity = '1';
        }
    });
});
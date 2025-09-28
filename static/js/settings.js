document.addEventListener('DOMContentLoaded', function() {
    // Preferences form submission
    const preferencesForm = document.getElementById('preferencesForm');
    preferencesForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = {
            theme: document.getElementById('theme').value,
            language: document.getElementById('language').value,
            notify_reports: document.getElementById('reportNotifications').checked,
            notify_messages: document.getElementById('messageNotifications').checked,
            notify_updates: document.getElementById('updateNotifications').checked
        };
        
        // Send to server
        fetch('/account/preferences', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('Preferences saved successfully', 'success');
            } else {
                showNotification(data.message || 'Failed to save preferences', 'error');
            }
        });
    });

    // Delete account confirmation
    const deleteAccountBtn = document.getElementById('deleteAccountBtn');
    deleteAccountBtn.addEventListener('click', function() {
        if (confirm('Are you sure you want to delete your account? This cannot be undone.')) {
            fetch('/account/delete', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/';
                } else {
                    showNotification(data.message || 'Failed to delete account', 'error');
                }
            });
        }
    });

    // Export data
    const exportDataBtn = document.getElementById('exportDataBtn');
    exportDataBtn.addEventListener('click', function() {
        fetch('/account/export')
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'connectaid-data-export.json';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        });
    });

    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span class="notification-message">${message}</span>
                <button class="notification-close" aria-label="Close notification">
                    <svg viewBox="0 0 24 24" width="16" height="16">
                        <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/>
                    </svg>
                </button>
            </div>
        `;
        document.querySelector('.notification-container').appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'fadeOut 0.3s forwards';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
        
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.style.animation = 'fadeOut 0.3s forwards';
            setTimeout(() => notification.remove(), 300);
        });
    }
});
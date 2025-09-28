document.addEventListener('DOMContentLoaded', function() {
    // Avatar upload functionality
    const avatarUpload = document.getElementById('avatarUpload');
    const avatarPreview = document.getElementById('avatarPreview');
    const changeAvatarBtn = document.getElementById('changeAvatarBtn');
    
    changeAvatarBtn.addEventListener('click', () => avatarUpload.click());
    
    avatarUpload.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(event) {
                avatarPreview.style.backgroundImage = `url(${event.target.result})`;
                // Here you would typically upload to server
                // uploadAvatar(file);
            };
            reader.readAsDataURL(file);
        }
    });

    // Password change modal
    const changePasswordBtn = document.getElementById('changePasswordBtn');
    changePasswordBtn.addEventListener('click', () => {
        // Implement password change modal
        alert('Password change functionality would open a modal here');
    });

    // Two-factor toggle
    const twoFactorToggle = document.getElementById('twoFactorToggle');
    twoFactorToggle.addEventListener('change', function() {
        const enabled = this.checked;
        // Send request to server to update 2FA status
        fetch('/account/two-factor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ enabled })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                this.checked = !enabled; // Revert if failed
                alert(data.message || 'Failed to update two-factor authentication');
            }
        });
    });

    // Profile form submission
    const profileForm = document.getElementById('profileForm');
    profileForm.addEventListener('submit', function(e) {
        e.preventDefault();
        // Add form validation and submission logic
        alert('Profile update functionality would save changes here');
    });
});
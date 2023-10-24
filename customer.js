<script>
    document.getElementById('customer-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const firstName = document.getElementById('first-name').value;
        const lastName = document.getElementById('last-name').value;
        const phoneNumber = document.getElementById('phone-number').value;

        const data = {
            first_name: firstName,
            last_name: lastName,
            phone_number: phoneNumber
        };

        fetch('/customers', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            alert(result.message);
            // Optionally, you can redirect to another page or update the UI.
        })
        .catch(error => {
            alert('An error occurred. Please try again later.');
        });
    });
</script>

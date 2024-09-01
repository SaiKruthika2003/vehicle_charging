function updateChargingStatus() {
    fetch('/charging-status')
        .then(response => response.json())
        .then(data => {
            const statusElement = document.getElementById('charging-status');
            if (data.charging) {
                statusElement.innerText = 'Charging';
                statusElement.style.color = 'green';
            } else {
                statusElement.innerText = 'Not Charging';
                statusElement.style.color = 'red';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

setInterval(updateChargingStatus, 5000); // Check every 5 seconds

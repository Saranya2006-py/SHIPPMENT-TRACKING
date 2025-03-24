function trackShipment() {
    let trackingId = document.getElementById("trackingInput").value;

    if (!trackingId) {
        alert("Please enter a tracking ID!");
        return;
    }

    fetch(`/track/${trackingId}/`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").innerHTML = `<p style="color: red;">${data.error}</p>`;
            } else {
                document.getElementById("result").innerHTML = `
                    <p><strong>Tracking ID:</strong> ${data.tracking_id}</p>
                    <p><strong>Status:</strong> ${data.status}</p>
                    <p><strong>Location:</strong> ${data.location.latitude}, ${data.location.longitude}</p>
                `;
            }
        })
        .catch(error => {
            console.error("Error fetching shipment data:", error);
            document.getElementById("result").innerHTML = `<p style="color: red;">Error fetching shipment details.</p>`;
        });
}

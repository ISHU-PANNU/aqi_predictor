document.getElementById('predictBtn').addEventListener('click', function() {
    var formData = new FormData(document.getElementById('airQualityForm'));

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.predicted_air_quality_index) {
            document.getElementById('result').innerText = 'Predicted AQI: ' + data.predicted_air_quality_index;
        } else if (data.error) {
            document.getElementById('result').innerText = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred.';
    });
});
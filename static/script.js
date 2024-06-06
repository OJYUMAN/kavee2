document.getElementById('myButton').addEventListener('click', function (event) {
    event.preventDefault();  // Prevent the form from submitting normally

    var word = document.getElementById('exampleInputEmail1').value;  // Get the word input value

    fetch('/api/button_click', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: word })  // Include the word in the request body
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = data.message;
        });
});
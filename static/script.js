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
            var word = data[1];
            var wordinfo = data[0];
            console.log(wordinfo)
            console.log(word)

            var responseElement = document.getElementById('response');  // Clear the previous content
            responseElement.innerHTML = '';

            var lengthPara = document.createElement('p');  // Create a paragraph element
            lengthPara.textContent = 'พบคําคล้องจองทั้งหมด ' + Object.keys(wordinfo).length + ' คํา';  // Set the text to the length of wordinfo
            responseElement.appendChild(lengthPara);  // Add the paragraph to the response element

            var table = document.createElement('table');  // Create a table element
            table.style.borderCollapse = 'collapse';
            table.style.width = '100%';
            table.style.border = '1px solid #ddd';  // Lighter border color
            table.style.marginTop = '20px';  // Add some space between the paragraph and the table

            var tbody = document.createElement('tbody');  // Add a body row
            // Assuming word is an object with key-value pairs
            // Assuming word is an object with key-value pairs
            Object.entries(word).forEach(([key, value]) => {
                var row = document.createElement('tr');

                var tdWord = document.createElement('td');
                tdWord.style.border = '1px solid #ddd';  // Lighter border color
                tdWord.style.padding = '8px';

                var valueSpan = document.createElement('span');
                valueSpan.style.color = 'blue';  // Change the text color to blue
                valueSpan.appendChild(document.createTextNode(value + ' : '));
                tdWord.appendChild(valueSpan);

                var infoSpan = document.createElement('span');
                infoSpan.style.color = 'black';  // Change the text color to black
                infoSpan.appendChild(document.createTextNode(wordinfo[key]));
                tdWord.appendChild(infoSpan);

                row.appendChild(tdWord);

                tbody.appendChild(row);
            });

            table.appendChild(tbody);

            responseElement.appendChild(table);  // Append the table to the response element
        });
});


document.getElementById('mean').addEventListener('click', function (event) {
    event.preventDefault();  // Prevent the form from submitting normally

    var word = document.getElementById('exampleInputEmail1').value;  // Get the word input value

    fetch('/api/button_click2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: word })  // Include the word in the request body
    })
        .then(response => response.json())
        .then(data => {
            var word = data[1];
            var wordinfo = data[0];


            var responseElement = document.getElementById('response');  // Clear the previous content
            responseElement.innerHTML = '';

            var lengthPara = document.createElement('p');  // Create a paragraph element
            lengthPara.textContent = 'พบความหมายทั้งหมด ' + Object.keys(wordinfo).length + ' ความหมาย';  // Set the text to the length of wordinfo
            responseElement.appendChild(lengthPara);  // Add the paragraph to the response element

            var table = document.createElement('table');  // Create a table element
            table.style.borderCollapse = 'collapse';
            table.style.width = '100%';
            table.style.border = '1px solid #ddd';  // Lighter border color
            table.style.marginTop = '20px';  // Add some space between the paragraph and the table

            var tbody = document.createElement('tbody');  // Add a body row
            // Assuming word is an object with key-value pairs
            // Assuming word is an object with key-value pairs
            Object.entries(word).forEach(([key, value]) => {
                var row = document.createElement('tr');

                var tdWord = document.createElement('td');
                tdWord.style.border = '1px solid #ddd';  // Lighter border color
                tdWord.style.padding = '8px';

                var valueSpan = document.createElement('span');
                valueSpan.style.color = 'blue';  // Change the text color to blue
                valueSpan.appendChild(document.createTextNode(value + ' : '));
                tdWord.appendChild(valueSpan);

                var infoSpan = document.createElement('span');
                infoSpan.style.color = 'black';  // Change the text color to black
                infoSpan.appendChild(document.createTextNode(wordinfo[key]));
                tdWord.appendChild(infoSpan);

                row.appendChild(tdWord);

                tbody.appendChild(row);
            });

            table.appendChild(tbody);

            responseElement.appendChild(table);  // Append the table to the response element
        });
});
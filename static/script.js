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
        .then(wordinfo => {
            var responseElement = document.getElementById('response');  // Clear the previous content
            responseElement.innerHTML = '';

            var lengthPara = document.createElement('p');  // Create a paragraph element
            lengthPara.textContent = 'พบคําคล้องจองทั้งหมด' + Object.keys(wordinfo).length + 'คํา';  // Set the text to the length of wordinfo
            responseElement.appendChild(lengthPara);  // Add the paragraph to the response element

            var table = document.createElement('table');  // Create a table element
            table.style.borderCollapse = 'collapse';
            table.style.width = '100%';
            table.style.border = '1px solid black';  // Add border to table

            var tbody = document.createElement('tbody');  // Add a body row

            // Assuming wordinfo is an object with key-value pairs
            Object.entries(wordinfo).forEach(([key, value]) => {
                var row = document.createElement('tr');

                var th = document.createElement('th');
                th.style.border = '1px solid black';
                th.style.padding = '8px';
                th.appendChild(document.createTextNode(key));
                row.appendChild(th);

                var td = document.createElement('td');
                td.style.border = '1px solid black';
                td.style.padding = '8px';
                td.appendChild(document.createTextNode(value));
                row.appendChild(td);

                tbody.appendChild(row);
            });

            table.appendChild(tbody);

            responseElement.appendChild(table);  // Append the table to the response element
        });
});
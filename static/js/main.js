document.getElementById('converterForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const jsonInput = document.getElementById('jsonInput').value;

    const response = await fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ jsonInput: jsonInput }),
    });

    const data = await response.json();

    if (response.ok) {
        document.getElementById('graphqlOutput').value = data.graphqlOutput;
    } else {
        document.getElementById('graphqlOutput').value = `Error: ${data.error}`;
    }
});

// JSON Beautifier
document.getElementById('beautifyJson').addEventListener('click', function() {
    const jsonInput = document.getElementById('jsonInput').value;
    try {
        const parsedJson = JSON.parse(jsonInput);
        const beautifiedJson = JSON.stringify(parsedJson, null, 2);
        document.getElementById('jsonInput').value = beautifiedJson;
    } catch (e) {
        alert('Invalid JSON: Please check your input.');
    }
});

// Copy to Clipboard
document.getElementById('copyButton').addEventListener('click', function() {
    const outputTextArea = document.getElementById('graphqlOutput');
    outputTextArea.select();
    document.execCommand('copy');
    alert('GraphQL output copied to clipboard!');
});

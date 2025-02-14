let expression = '';

function addToResult(value) {
    expression += value;
    document.getElementById('result').value = expression;
}

function clearResult() {
    expression = '';
    document.getElementById('result').value = '';
}

async function calculateResult() {
    const response = await fetch('/calculate/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ expression: expression })
    });

    const result = await response.json();
    document.getElementById('result').value = result.result;
    expression = result.result;  // Keep the result for further calculations
}

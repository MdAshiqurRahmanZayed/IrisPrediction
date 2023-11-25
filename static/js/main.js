function predictIris() {
     const sepalLength = parseFloat(document.getElementById('sepal_length').value);
     const sepalWidth = parseFloat(document.getElementById('sepal_width').value);
     const petalLength = parseFloat(document.getElementById('petal_length').value);
     const petalWidth = parseFloat(document.getElementById('petal_width').value);

     const url = 'predict/'; // Replace with your actual API endpoint
     const data = {
          sepal_length: sepalLength,
          sepal_width: sepalWidth,
          petal_length: petalLength,
          petal_width: petalWidth
     };
     console.log(JSON.stringify(data));
     fetch(url, {
               method: "POST",
               headers: {
                    "Content-Type": "application/json",
               },
               body: JSON.stringify(data),
          })
          .then(response => {
               return response.json();
          })
          .then(result => {
               console.log(result.result);
               let text  = document.createElement('h3');
               text.innerHTML = `Predicted Class: <b>${result.result}</b>`;
               console.log(text);
               document.getElementById('result').appendChild(text);
          })
          .catch(error => {
               console.error('Error:', error);
          });

}
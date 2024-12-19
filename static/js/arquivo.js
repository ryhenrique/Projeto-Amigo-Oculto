document.getElementById('sortButton').addEventListener('click', function() {
    let inputNames = document.getElementById('names').value.trim();

    // Validação: Verifica se o campo está vazio ou se possui menos de 2 nomes
    if (inputNames === "") {
        alert("Por favor, insira os nomes.");
        return;
    }

    let names = inputNames.split(',').map(name => name.trim()).filter(name => name.length > 0);
    
    if (names.length < 2) {
        alert("É necessário pelo menos duas pessoas para o sorteio.");
        return;
    }

    // Sortear os amigos ocultos
    let result = sortearAmigos(names);

    // Exibir os resultados
    let resultsList = document.getElementById('resultsList');
    resultsList.innerHTML = '';  // Limpar resultados anteriores

    result.forEach(pair => {
        let listItem = document.createElement('li');
        listItem.textContent = `${pair[0]} tirou ${pair[1]}`;
        resultsList.appendChild(listItem);
    });

    // Mostrar a seção de resultados
    document.getElementById('resultSection').style.display = 'block';
});

// Função para sortear os amigos ocultos
function sortearAmigos(names) {
    let shuffledNames = [...names];
    let result = [];
    
    // Embaralhar os nomes
    shuffledNames.sort(() => Math.random() - 0.5);

    // Garantir que ninguém tire a si mesmo
    for (let i = 0; i < names.length; i++) {
        let giver = names[i];
        let receiver = shuffledNames[i];

        // Se alguém tirar a si mesmo, embaralha novamente
        if (giver === receiver) {
            return sortearAmigos(names);
        }

        result.push([giver, receiver]);
    }

    return result;
}

var contadorInputs = 0;

function adicionarInput(){
    const inputsContainer = document.getElementById('inputs-container');

    const novoInput = document.createElement('div');
    novoInput.classList.add("row");
    novoInput.classList.add("mb-3");
    novoInput.setAttribute('id', `acomp_${contadorInputs}`);
    novoInput.innerHTML = `
        <div class="col">
            <label>Link:</label>
            <input type="text" class="form-control upper" tabindex="5" name="link_${contadorInputs}" id="link_${contadorInputs}" required>
        </div>
    `;

    inputsContainer.appendChild(novoInput);
    contadorInputs++;   

    const inputQtde = document.getElementById('qtdeLinks');
    inputQtde.value = contadorInputs;
}
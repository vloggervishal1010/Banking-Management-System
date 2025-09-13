const formContainer = document.getElementById("form-container");

function showCreateAccount() {
    formContainer.innerHTML = `
        <h2>Create Account</h2>
        <form onsubmit="return createAccount()">
            <label for="name">Name:</label>
            <input type="text" id="name" required>
            
            <label for="deposit">Initial Deposit:</label>
            <input type="number" id="deposit" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" required>
            
            <button type="submit">Create Account</button>
        </form>
    `;
}

function showLogin() {
    formContainer.innerHTML = `
        <h2>Login</h2>
        <form onsubmit="return loginAccount()">
            <label for="accNumber">Account Number:</label>
            <input type="text" id="accNumber" required>
            
            <label for="loginPassword">Password:</label>
            <input type="password" id="loginPassword" required>
            
            <button type="submit">Login</button>
        </form>
    `;
}

function createAccount() {
    const name = document.getElementById("name").value;
    const deposit = document.getElementById("deposit").value;
    const password = document.getElementById("password").value;

    alert(`Account created successfully!\nName: ${name}\nDeposit: ${deposit}\nPassword: ${password}`);
    formContainer.innerHTML = "";
    return false; // prevent form submission
}

function loginAccount() {
    const accNumber = document.getElementById("accNumber").value;
    const password = document.getElementById("loginPassword").value;

    alert(`Login successful!\nAccount Number: ${accNumber}\nPassword: ${password}`);
    formContainer.innerHTML = "";
    return false; // prevent form submission
}
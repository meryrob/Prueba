document.getElementById('registerButton').addEventListener('click', registerUser);
document.getElementById('loginButton').addEventListener('click', loginUser);

async function registerUser() {
    try {
        const response = await fetch('/register', {method: 'GET'});
        const data = await response.json();

        const credential = await navigator.credentials.create(data);
        const credentialData = {
            id: credential.id,
            rawId: Array.from(new Uint8Array(credential.rawId)),
            response: {
                attestationObject: Array.from(new Uint8Array(credential.response.attestationObject)),
                clientDataJSON: Array.from(new Uint8Array(credential.response.clientDataJSON))
            },
            type: credential.type
        };

        await fetch('/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(credentialData)
        });
        console.log('Usuario registrado');
    } catch (err) {
        console.error('Error en el registro:', err);
    }
}

async function loginUser() {
    try {
        const response = await fetch('/login', {method: 'GET'});
        const data = await response.json();

        const assertion = await navigator.credentials.get(data);
        const assertionData = {
            id: assertion.id,
            rawId: Array.from(new Uint8Array(assertion.rawId)),
            response: {
                authenticatorData: Array.from(new Uint8Array(assertion.response.authenticatorData)),
                clientDataJSON: Array.from(new Uint8Array(assertion.response.clientDataJSON)),
                signature: Array.from(new Uint8Array(assertion.response.signature)),
                userHandle: Array.from(new Uint8Array(assertion.response.userHandle || []))
            },
            type: assertion.type
        };

        await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(assertionData)
        });
        console.log('Inicio de sesión exitoso');
    } catch (err) {
        console.error('Error en el inicio de sesión:', err);
    }
}

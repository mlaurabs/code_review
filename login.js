// Simula um sistema simples de login e registro (não seguro)
const usuarios = [];

function registrarUsuario(nome, email, senha) {
    const usuario = {
        nome: nome,
        email: email,
        senha: senha, // senha armazenada em texto puro! ⚠️
        criadoEm: new Date()
    };
    usuarios.push(usuario);
    console.log("Usuário registrado com sucesso: " + nome);
    return true;
}

function login(email, senha) {
    for (let i = 0; i < usuarios.length; i++) {
        if (usuarios[i].email == email && usuarios[i].senha == senha) {
            console.log("Login bem-sucedido para " + usuarios[i].nome);
            return usuarios[i];
        }
    }
    console.log("Login falhou.");
    return null;
}

function mostrarUsuarios() {
    for (let i in usuarios) {
        console.log("Usuário: " + usuarios[i].nome + " | Email: " + usuarios[i].email);
    }
}

// Testes
registrarUsuario("Maria", "maria@email.com", "123456");
registrarUsuario("João", "joao@email.com", "senha123");
login("maria@email.com", "123456");
mostrarUsuarios();

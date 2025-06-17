// Simula um sistema simples de login e registro (ainda não seguro, mas melhorado)
const usuarios = [];

function registrarUsuario(nome, email, senha) {
    // Verifica se o email já está cadastrado
    const usuarioExistente = usuarios.find(usuario => usuario.email === email);
    if (usuarioExistente) {
        console.log("Erro: Email já cadastrado.");
        return false;
    }

    const usuario = {
        nome: nome,
        email: email,
        senha: senha, // ⚠️ Ainda não seguro (deveria ser hasheada)
        criadoEm: new Date()
    };
    usuarios.push(usuario);
    console.log(`Usuário registrado com sucesso: ${nome}`);
    return true;
}

function login(email, senha) {
    const usuario = usuarios.find(user => user.email === email && user.senha === senha);
    if (usuario) {
        console.log(`Login bem-sucedido para ${usuario.nome}`);
        return usuario;
    } else {
        console.log("Login falhou: Email ou senha incorretos.");
        return null;
    }
}

function mostrarUsuarios() {
    if (usuarios.length === 0) {
        console.log("Nenhum usuário cadastrado.");
        return;
    }
    console.log("=== Lista de Usuários ===");
    usuarios.forEach(usuario => {
        console.log(`Nome: ${usuario.nome} | Email: ${usuario.email}`);
    });
}

// Testes
registrarUsuario("Maria", "maria@email.com", "123456");
registrarUsuario("João", "joao@email.com", "senha123");
registrarUsuario("João", "joao@email.com", "senha123"); // Tentativa de email duplicado
login("maria@email.com", "123456");
login("email_inexistente@teste.com", "senha"); // Login falho
mostrarUsuarios();
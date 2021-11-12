export class Validacao {
    static validaNome(nome) {
        if (nome.length < 5 || nome.length > 100) {
            return false;
        }
        let regex = /^[A-Za-z ]*$/
        if (nome.match(regex)) {
            return true;
        }
        return false;
    }
    static validaCpf(cpf) {
        const regex = /^\d{3}\.\d{3}\.\d{3}\-\d{2}$/
        if (cpf.match(regex)) {
            return true;
        }
        return false;
    }
    static validaSenha(senha) {
        const regex = /\s/
        if (senha.match(regex) || senha.length < 8) {
            return false;
        }
        return true;
    }
}
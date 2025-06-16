// Calcula o total de itens em um carrinho
function totalCarrinho(itens) {
    let total = 0;
    for (let i = 0; i < itens.length; i++) {
        total = total + itens[i].preco * itens[i].quantidade
    }
    if (total > 100) {
        console.log("Frete grátis")
    } else {
        console.log("Frete: R$ 20")
    }
    return total
}

let carrinho = [
    { nome: "Teclado", preco: 50, quantidade: 1 },
    { nome: "Mouse", preco: 30, quantidade: 2 }
];

let resultado = totalCarrinho(carrinho)
console.log("Total:" + resultado)

const produto = document.querySelectorAll('.py');
const container = document.querySelector('#produtos');

const btnList = document.querySelector('.btnList');
const produtoList = document.querySelectorAll('.produtoLista');
const addBtn = document.querySelector('.add');

function handleClick(e) {
    e.preventDefault();
    produtoList.forEach((item) => (item.style.display = 'flex'));
    container.style.display = 'flex';
}

btnList.addEventListener('click', handleClick);

if (produto.length < 1) {
    container.style.display = 'none';
}

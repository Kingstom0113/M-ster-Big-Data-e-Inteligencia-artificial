// Función para crear el grafo ponderado no dirigido
function crearGrafoNoDirigido() {
    const numNodos = document.getElementById('nodosNoDirigido').value;
    const numAristas = document.getElementById('aristasNoDirigido').value;

    let nodos = [];
    for (let i = 1; i <= numNodos; i++) {
        nodos.push({ id: i, label: i.toString() });
    }

    let aristas = [];
    for (let i = 1; i <= numAristas; i++) {
        const from = Math.floor(Math.random() * numNodos) + 1;
        const to = Math.floor(Math.random() * numNodos) + 1;
        const peso = Math.floor(Math.random() * 10) + 1; // Peso aleatorio entre 1 y 10
        aristas.push({ from: from, to: to, label: peso.toString(), width: peso });
    }

    let contenedor = document.getElementById('network');
    let datos = { nodes: new vis.DataSet(nodos), edges: new vis.DataSet(aristas) };
    let opciones = {
        edges: { smooth: false }
    };

    new vis.Network(contenedor, datos, opciones);
}

// Función para crear el grafo ponderado dirigido
function crearGrafoDirigido() {
    const numNodos = document.getElementById('nodosDirigido').value;
    const numAristas = document.getElementById('aristasDirigido').value;
    const pesos = document.getElementById('pesosDirigido').value.split(',').map(Number);
    const direcciones = document.getElementById('direccionesDirigido').value.split(',');

    if (pesos.length !== parseInt(numAristas) || direcciones.length !== parseInt(numAristas)) {
        alert('El número de pesos y direcciones debe coincidir con el número de aristas.');
        return;
    }

    let nodos = [];
    for (let i = 1; i <= numNodos; i++) {
        nodos.push({ id: i, label: i.toString() });
    }

    let aristas = [];
    for (let i = 0; i < numAristas; i++) {
        const [from, to] = direcciones[i].split('-').map(Number);
        const peso = pesos[i];
        aristas.push({ from: from, to: to, label: peso.toString(), arrows: 'to', width: peso });
    }

    let contenedor = document.getElementById('network2');
    let datos = { nodes: new vis.DataSet(nodos), edges: new vis.DataSet(aristas) };
    let opciones = {
        edges: {
            arrows: { to: { enabled: true } },
            smooth: false
        }
    };

    new vis.Network(contenedor, datos, opciones);
}

// Llamamos a las funciones para cargar los grafos iniciales con valores por defecto
crearGrafoNoDirigido();
crearGrafoDirigido();


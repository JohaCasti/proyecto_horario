document.addEventListener('DOMContentLoaded', function() {
    const centroSelect = document.getElementById('centro');
    const fichasSelect = document.getElementById('fichas');
    const salonSelect = document.getElementById('salon');

    centroSelect.addEventListener('change', function() {
        const centro = centroSelect.value;
        fetch('/vista/fichas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ centro: centro })
        })
        .then(response => response.json())
        .then(data => {
            const fichas = data.fichas;
            const salones = data.salones;

            fichasSelect.innerHTML = fichas.map(ficha => `<option value="${ficha}">${ficha}</option>`).join('');
            salonSelect.innerHTML = salones.map(salon => `<option value="${salon}">${salon}</option>`).join('');
        });
    });

    // Trigger the change event to populate the initial values
    centroSelect.dispatchEvent(new Event('change'));
});

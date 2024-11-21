
    // Récupérer les éléments
    const prixInput = document.getElementById('prixInput');
    const avanceInput = document.getElementById('avanceInput');
    const soldeSection = document.getElementById('soldeSection');

    // Fonction pour vérifier si l'avance est égale au prix
    function checkSolde() {
        const prix = parseFloat(prixInput.value) || 0;
        const avance = parseFloat(avanceInput.value) || 0;

        if (avance === prix && prix > 0) {
            soldeSection.style.display = 'block'; // Afficher la section Soldé
        } else {
            soldeSection.style.display = 'none'; // Masquer la section Soldé
        }
    }

    // Ajouter des écouteurs d'événements pour surveiller les champs
    prixInput.addEventListener('input', checkSolde);
    avanceInput.addEventListener('input', checkSolde);

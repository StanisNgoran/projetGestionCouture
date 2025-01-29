
document.addEventListener("DOMContentLoaded", function() {
                  // Sélectionner le conteneur de message
                  const messageContainer = document.getElementById('message-container');
                  
                  if (messageContainer) {
                      // Cacher le message après 3 secondes
                      setTimeout(() => {
                          messageContainer.style.display = 'none';
                      }, 1000);  // 3000 ms = 3 secondes
                  }
              });
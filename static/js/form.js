function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


document.addEventListener("DOMContentLoaded", function () {
    console.log('skrypt się ładuje')
    const form = document.querySelector(".form");
    console.log(form);
    const added = document.querySelector(".added");
    


 
    form.addEventListener("submit", function(event) {
        event.preventDefault();
    
        const formData = new FormData(form);  // Tworzenie obiektu FormData z danymi formularza
   
        const eventUrl = form.getAttribute('action') || window.location.href;

        fetch(eventUrl, {
            method: "POST",
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const added = document.querySelector(".added");
            added.innerHTML = '<button class="btn btn-outline-primary zamknij">Zamknij</button>' + data.message_content;

            added.style.display = "block";

            const closeButton = document.querySelector(".zamknij");
            closeButton.addEventListener("click", function() {
                const added = document.querySelector(".added");
                added.style.display = "none";
                location.reload()
            });
            
            console.log('widzę added');
        })
        
        
        .catch(error => {
            console.log('There was a problem with the fetch operation:', error.message);
            added.innerHTML = "Wystąpił błąd podczas przesyłania formularza.";
            added.classList.add("error-messages");
        });
    });

    
});
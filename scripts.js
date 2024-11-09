document.getElementById('opportunity-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission to server

    // Get the form values
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const date = document.getElementById('date').value;
    const location = document.getElementById('location').value;

    // Create a new opportunity object
    const opportunity = {
        title: title,
        description: description,
        date: date,
        location: location
    };

    // Get the existing opportunities from localStorage, or initialize an empty array if none. Used https://www.youtube.com/watch?v=fYTTUBa-lPc as a tutorial and also https://www.youtube.com/watch?v=iiADhChRriM
    let h2.innerHTML = JSON.parse(localStorage.getItem('opportunities')) || [];

    // Add the new opportunity to the array
    h2.innerHTML.push(opportunity);

    // Save the updated array of opportunities back to localStorage
    function display() {
    localStorage.setItem('opportunities', JSON.stringify(opportunity));
    h2.innerHTML = localstorage.getItem("opportunities")
}

    // Clear the form fields after submission
    document.getElementById('opportunity-form').reset();
});


// Load and display opportunities when the page loads
document.addEventListener('DOMContentLoaded', function () {
    const opportunities = JSON.parse(localStorage.getItem('opportunities')) || [];
    displayOpportunities(opportunities);
});

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

    // Get the existing opportunities from localStorage, or initialize an empty array if none
    let opportunities = JSON.parse(localStorage.getItem('opportunities')) || [];

    // Add the new opportunity to the array
    opportunities.push(opportunity);

    // Save the updated array of opportunities back to localStorage
    localStorage.setItem('opportunities', JSON.stringify(opportunities));

    // Add the new opportunity to the page (for immediate display without reloading)
    displayOpportunities(opportunities);

    // Clear the form fields after submission
    document.getElementById('opportunity-form').reset();
});

// Function to display opportunities on the page
function displayOpportunities(opportunities) {
    const opportunityList = document.querySelector('.opportunities-list');
    opportunityList.innerHTML = ''; // Clear existing opportunities

    // Loop through the stored opportunities and display them
    opportunities.forEach(opportunity => {
        const opportunityItem = document.createElement('div');
        opportunityItem.classList.add('opportunity-item');

        opportunityItem.innerHTML = `
            <h3>${opportunity.title}</h3>
            <p><strong>Date:</strong> ${opportunity.date}</p>
            <p><strong>Location:</strong> ${opportunity.location}</p>
            <p>${opportunity.description}</p>
        `;

        opportunityList.appendChild(opportunityItem);
    });
}

// Load and display opportunities when the page loads
document.addEventListener('DOMContentLoaded', function () {
    const opportunities = JSON.parse(localStorage.getItem('opportunities')) || [];
    displayOpportunities(opportunities);
});

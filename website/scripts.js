document.getElementById('opportunity-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission to server

    // Get the form values
    const title = document.getElementById('title').value;
    const description = document.getElementById('description').value;
    const date = document.getElementById('date').value;
    const location = document.getElementById('location').value;

    // Basic validation to check if fields are filled
    if (!title || !description || !date || !location) {
        alert("Please fill in all fields.");
        return;
    }

    // Create a new opportunity object
    const opportunity = {
        title: title,
        description: description,
        date: date,
        location: location
    };

    // Get the existing opportunities from localStorage, or initialize an empty array if none
    let opportunities = [];
    try {
        opportunities = JSON.parse(localStorage.getItem('opportunities')) || [];
    } catch (error) {
        console.error("Error parsing opportunities from localStorage", error);
    }

    // Add the new opportunity to the array
    opportunities.push(opportunity);

    // Save the updated array of opportunities back to localStorage
    try {
        localStorage.setItem('opportunities', JSON.stringify(opportunities));
    } catch (error) {
        console.error("Error saving opportunities to localStorage", error);
    }

    // Add the new opportunity to the page (for immediate display without reloading)
    displayOpportunities(opportunities);

    // Clear the form fields after submission
    document.getElementById('opportunity-form').reset();
});

// Function to display opportunities on the page
function displayOpportunities(opportunities) {
    const opportunityList = document.querySelector('.opportunities-list');
    opportunityList.innerHTML = ''; // Clear existing opportunities

    if (opportunities.length === 0) {
        opportunityList.innerHTML = '<p>No opportunities available.</p>';
    }

    // Loop through the stored opportunities and display them
    opportunities.forEach((opportunity, index) => {
        const opportunityItem = document.createElement('div');
        opportunityItem.classList.add('opportunity-item');

        opportunityItem.innerHTML = `
            <h3>${opportunity.title}</h3>
            <p><strong>Date:</strong> ${opportunity.date}</p>
            <p><strong>Location:</strong> ${opportunity.location}</p>
            <p>${opportunity.description}</p>
            <button class="delete-btn" data-index="${index}">Delete</button>
        `;

        opportunityList.appendChild(opportunityItem);
    });

    // Add event listeners for the delete buttons
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const index = button.getAttribute('data-index');
            deleteOpportunity(index);
        });
    });
}

// Function to delete an opportunity
function deleteOpportunity(index) {
    let opportunities = [];
    try {
        opportunities = JSON.parse(localStorage.getItem('opportunities')) || [];
    } catch (error) {
        console.error("Error parsing opportunities from localStorage", error);
        return;
    }

    // Remove the opportunity at the specified index
    opportunities.splice(index, 1);

    // Save the updated array of opportunities back to localStorage
    try {
        localStorage.setItem('opportunities', JSON.stringify(opportunities));
    } catch (error) {
        console.error("Error saving opportunities to localStorage", error);
    }

    // Re-display the updated opportunities list
    displayOpportunities(opportunities);
}

// Load and display opportunities when the page loads
document.addEventListener('DOMContentLoaded', function () {
    const opportunities = JSON.parse(localStorage.getItem('opportunities')) || [];
    displayOpportunities(opportunities);
});

// tutorial used was https://www.youtube.com/watch?v=2hJ1rTANVnk

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

    // Save the opportunity to localStorage
    function opp() {
        if (localStorage.getItem('opportunities') == null) {
            localStorage.setItem('opportunities', '[]');
        }
        const old_opportunities = JSON.parse(localStorage.getItem('opportunities'));
        old_opportunities.push(opportunity);
        localStorage.setItem('opportunities', JSON.stringify(old_opportunities));
        return old_opportunities;
    }

    const updatedOpportunities = opp();

    // Add the new opportunity to the page (for immediate display without reloading)
    displayOpportunities(updatedOpportunities);

    // Clear the form fields after submission
    document.getElementById('opportunity-form').reset();
});

// Display opportunities on the page
function displayOpportunities(opportunities) {
    let output = '';
    opportunities.forEach(opportunity => {
        output += `<div>
            <h3>${opportunity.title}</h3>
            <p>${opportunity.description}</p>
            <p>${opportunity.date}</p>
            <p>${opportunity.location}</p>
        </div>`;
    });
    document.getElementById('output').innerHTML = output;
}

// Initial display of opportunities on page load
function display() {
    if (localStorage.getItem('opportunities') != null) {
        const opportunities = JSON.parse(localStorage.getItem('opportunities'));
        displayOpportunities(opportunities);
    }
}
display(); // Call on page load

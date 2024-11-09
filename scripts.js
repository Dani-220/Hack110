// Used https://www.youtube.com/watch?v=2hJ1rTANVnk as a tutorial for this code
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
    function opp(){
        if(localStorage.getItem('opportunity') == null){
            localStorage.setItem('opportunity', '[]');
                                 }
        var old_opportunities = JSON.parse(localStorage.getItem('opportunities'));
        old_opportunities.push(opportunity);
        localStorage.setItem('opportunities', JSON.stringify(old_opportunities));
    }
    const updatedOpportunities = opp();

    // Add the new opportunity to the page (for immediate display without reloading)
    displayOpportunities(old_opportunities);

    // Clear the form fields after submission
    document.getElementById('opportunity-form').reset();
});
function display() {
    if (localStorage.getItem('opportunities') != null) {
        const opportunities = JSON.parse(localStorage.getItem('opportunities'));
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
}
display();

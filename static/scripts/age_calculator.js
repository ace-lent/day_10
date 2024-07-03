function calculateAge() {
    var name = $('#name').val();
    var birthdate = $('#birthdate').val();
    var currentDate = new Date().toISOString().split('T')[0];

    if (birthdate > currentDate) {
        $('#modalBody').html('<p>Error: Birthdate cannot be in the future.</p>');
        $('#ageModal').modal('show');
        return;
    }

    $.ajax({
        url: '/calculate_age',
        method: 'POST',
        data: { name: name, birthdate: birthdate },
        success: function(response) {
            $('#modalBody').html(`<p>Hi ${response.name}, you are currently ${response.age} years old.</p>`);
            $('#ageModal').modal('show'); 
        },
        error: function(xhr, status, error) {
            $('#modalBody').html('<p>Error calculating age.</p>');
            $('#ageModal').modal('show');
            console.error(error);
        }
    });
}

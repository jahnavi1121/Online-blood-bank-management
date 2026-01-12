function registerDonor() {
    alert("Donor registered successfully!");
}

function searchDonor() {
    let bg = document.getElementById("bloodGroup").value;
    if (bg === "") {
        alert("Please select blood group");
    } else {
        document.getElementById("result").innerHTML =
            "Donors available for blood group: " + bg;
    }
}
// script.js
function submit() {
    var username = document.getElementById('username').value;
    var class1 = document.getElementById('class1').value;
    var password = document.getElementById('password').value;
  
    // Store user details in local storage
    localStorage.setItem('username', username);
    localStorage.setItem('class1', class1);
  
    // Redirect to My Account page
    window.location.href = 'myaccount1.html';
  }
  
  function displayAccountDetails() {
    var username = localStorage.getItem('username');
    var class1 = localStorage.getItem('email');
  
    if (username && email) {
      document.getElementById('accountDetails').innerHTML = `
        <p><strong>Username:</strong> ${username}</p>
        <p><strong>Email:</strong> ${class1} </p>
      `;
    } else {
      document.getElementById('accountDetails').innerHTML = '<p>No account details found.</p>';
    }
  }
  
  // Check if the current page is My Account page and display details
  if (window.location.href.includes('myaccount1.html')) {
    displayAccountDetails();
  }
// script.js

function updateCurrentDate() {
    const currentDateElement = document.getElementById('currentDate');
    const today = new Date();
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const currentDate = today.getDate();
    const currentMonth = months[today.getMonth()];
    const currentYear = today.getFullYear();
    currentDateElement.innerText = `Today (${currentDate} ${currentMonth} ${currentYear})`;
  }
  
  // Call the function to set the initial date
  updateCurrentDate();
  
  function updateDropdownDates() {
    const dropdownMenu = document.getElementById('dateDropdown');
    const today = new Date();
    const currentMonth = today.getMonth() + 1; // Adding 1 as getMonth() returns zero-indexed month
    const year = today.getFullYear();
    const dropdownItems = dropdownMenu.querySelectorAll('.dropdown-item');
  
    // Map each dropdown item to its corresponding date range
    const dateRanges = [
      'January - March',
      'March - June',
      'June - August',
      'August - November'
      // Add more date ranges as needed
    ];
  
    // Loop through each dropdown item and set its text content
    for (let i = 0; i < dropdownItems.length; i++) {
      dropdownItems[i].textContent = dateRanges[i];
    }
  }
  
  // Call the function to set the initial dropdown options
  updateDropdownDates();
  
  // Update dropdown options every minute (you can adjust the interval as needed)
  setInterval(updateDropdownDates, 60000);
  

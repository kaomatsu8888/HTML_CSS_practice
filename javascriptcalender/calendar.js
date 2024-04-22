const header = document.getElementById('month-year'); // <h1 id="month-year"></h1>
const datesGrid = document.getElementById('calendar-dates'); // <div id="calendar-dates"></div>

let currentDate = new Date(); // Current date

function renderCalendar() { // Render the calendar
  datesGrid.innerHTML = ''; // Clear previous dates
  const firstDay = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1); // First day of the month
  const lastDay = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0); // Last day of the month
  
  header.innerText = `${firstDay.toLocaleString('ja-JP', { month: 'long' })} ${firstDay.getFullYear()}`;

  // Fill the empty spaces for days of the week
  for (let i = 0; i < firstDay.getDay(); i++) {
    datesGrid.appendChild(document.createElement('div'));
  }

  // Fill the actual days
  for (let day = 1; day <= lastDay.getDate(); day++) {
    const dateElement = document.createElement('div');
    dateElement.innerText = day;
    datesGrid.appendChild(dateElement);
  }
}

function moveMonth(months) {
  currentDate.setMonth(currentDate.getMonth() + months);
  renderCalendar();
}

document.addEventListener('DOMContentLoaded', renderCalendar);

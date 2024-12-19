function getVisitCount() {
  return parseInt(localStorage.getItem('visitCount') || '0');
}

function incrementVisitCount() {
  let count = getVisitCount();
  count++;
  localStorage.setItem('visitCount', count);
  return count;
}

document.addEventListener('DOMContentLoaded', (event) => {
  const visitCountElement = document.getElementById('visitCount');
  const count = incrementVisitCount();
  visitCountElement.textContent = `Visits: ${count}`;
});





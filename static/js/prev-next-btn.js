var currentPage = 1;
var rowsPerPage = 10;
var table = document.querySelector('.table');
var totalEntries = table.rows.length - 1; 
var pageInfo = document.getElementById('pageInfo');

function showPage(page) {
    var start = (page - 1) * rowsPerPage + 1;
    var end = Math.min(start + rowsPerPage - 1, totalEntries);
    for (var i = 1; i <= totalEntries; i++) {
        if (i >= start && i <= end) {
            table.rows[i].style.display = 'table-row';
        } 
        else {
            table.rows[i].style.display = 'none';
        }
    }
    
    pageInfo.innerHTML = 'Menampilkan ' + start + ' sampai ' + end + ' dari ' + totalEntries + ' entri';
}

function nextPage() {
    if (currentPage < Math.ceil(totalEntries / rowsPerPage)) {
        currentPage++;
        showPage(currentPage);
    }
}

function previousPage() {
    if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
    }
}

showPage(currentPage);
function showBreakingNews(messages, index) {
    var container = document.getElementById('breaking-news-container');
    var strongElement = document.createElement('strong');
    strongElement.className = 'breaking-news-latest';
    strongElement.textContent = messages[index];
    container.innerHTML = '';
    container.appendChild(strongElement);

    setTimeout(function () {
        index = (index + 1) % messages.length;
        showBreakingNews(messages, index);
    }, 3000);
}

var announcements = [
    'Visi dan Misi PRODI TI UIM',
    'JADWAL PERKULIAHAN PROGRAM',
    'UIM Me-Reproduksi',
    'KALENDER AKADEMIK PRODI'
];

showBreakingNews(announcements, 0);
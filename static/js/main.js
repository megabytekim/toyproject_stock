document.getElementById('giftBox').addEventListener('click', async function() {
    try {
        const response = await fetch('/pick_gift');
        const data = await response.json();
        
        const result = document.getElementById('result');
        const stockName = document.getElementById('stockName');
        const stockImage = document.getElementById('stockImage');
        const message = document.getElementById('message');
        const searchLink = document.getElementById('searchLink');
        
        stockName.textContent = data.name;
        stockImage.src = `/static/images/${data.image}`;
        
        if (data.message) {
            message.textContent = data.message;
            searchLink.style.display = 'none';
        } else {
            message.textContent = '';
            searchLink.href = data.search_url;
            searchLink.style.display = 'inline-block';
        }
        
        result.style.display = 'block';
    } catch (error) {
        console.error('Error fetching gift:', error);
        alert('Oops! Something went wrong. Please try again!');
    }
}); 
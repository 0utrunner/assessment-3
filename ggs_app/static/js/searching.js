document.getElementById('search-bar').addEventListener('submit', (event)=>{
    event.preventDefault()
    const lookup = document.getElementById('item')
    axios.get('/result', {params:{query: lookup.value}}).then((response)=>{
        found = document.createElement('img')
        found.src = response.data.url
        out = document.createElement('h4')
        out.innerText = 'Out of stock'
        const node = document.createElement('li')
        node.appendChild(found)
        node.appendChild(out)
        document.getElementById('myList').appendChild(node)
    })
})
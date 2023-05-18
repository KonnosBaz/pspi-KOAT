const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE
    const searchButton = document.getElementById("searchButton");
    searchButton.onclick = searchButtonOnClick;

    const saveButton = document.getElementById("saveButton");
    saveButton.onclick = productFormOnSubmit;
    // END CODE HERE
}



searchButtonOnClick = () => {
    // BEGIN CODE HERE

    const name = document.getElementById("searchField");
    const table = document.getElementById("resultsTable");
    
    l = table.rows.length

    for (var i = 1 ; i<l ; i++){
        table.deleteRow(-1);
    }
    
    const res = new XMLHttpRequest();
    res.open("GET", `${api}/search?name=${name.value}`);
    res.onreadystatechange = () => {
        if (res.readyState == 4) {
            if (res.status == 200) {
                const results = JSON.parse(res.response);
                
                if (results.length >= 1) {
                    for (r in results){
                        makeRow(table,results[r]);
                    }
                }
                else {
                    makeEmptyRow(table);
                }
                
            }
        }
    };
    res.send();    
    // END CODE HERE
}



productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    
    

    const name= document.getElementById("NAME");
    const year= document.getElementById("YEAR");
    const price = document.getElementById("PRICE");
    const color = document.getElementById("COLOR");
    const size = document.getElementById("SIZE")


    const res = new XMLHttpRequest();
    res.open("POST", `${api}/add-product`);
    res.onreadystatechange = () => {
        if (res.readyState == 4) {
            if (res.status == 200) {
                alert(res.responseText);
            }
        }
    };
    
    res.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    

    res.send(JSON.stringify({
        "name": `${name.value}`,
        "production_year": Number(year.value),
        "price": Number(price.value),
        "color": Number(color.value),
        "size": Number(size.value)
    }));

    
    // END CODE HERE
}

makeRow = (table,x) => {
    row = table.insertRow();
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    cell.innerHTML = x.id;
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    cell.innerHTML = x.name;
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    cell.innerHTML = x.production_year;
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    cell.innerHTML = x.price;
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    cell.innerHTML = x.color;
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    cell.innerHTML = x.size;
}


makeEmptyRow = (table) => {
    row = table.insertRow();
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");

    cell = row.insertCell(-1);
    cell.classList.add("formThTd");

    cell = row.insertCell(-1);
    cell.classList.add("formThTd");

    cell = row.insertCell(-1);
    cell.classList.add("formThTd");

    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    
    cell = row.insertCell(-1);
    cell.classList.add("formThTd");
    
}
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
    // alert(getContinent.value);
    
    
    const res = new XMLHttpRequest();
    res.open("GET", `${api}/search?name=${name.value}`);
    res.onreadystatechange = () => {
        if (res.readyState == 4) {
            if (res.status == 200) {
                console.log(res.responseText);
            }
        }
    };
    res.send()
    
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
    // same for the project 
    res.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    // change input (inside the JSON stringify)for the project
    res.send(JSON.stringify({
        "id" : `Uhh... not sure`,
        "name": `${name.value}`,
        "production_year": Number(year.value),
        "price": Number(price.value),
        "color": Number(color.value),
        "size": Number(size.value)
     }));
    // END CODE HERE
}
